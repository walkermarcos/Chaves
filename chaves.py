#coding=utf-8
from PyQt4 import QtCore,QtGui
from PyQt4.Qt import QTimer
from login import Ui_MainWindow
from dialog import Ui_Dialog
from dialog2 import Ui_Dialog2
from dialog3 import Ui_Dialog_3
from nivel1 import Ui_Nivel1
from entregar import Ui_Mainentrega
from receber import Ui_receber
from conf import Ui_Conf
from nivel2 import Ui_nivel2
from cad_user import Ui_Cadast_user
from cad_login import Ui_Cad_Logins
from mhlib import isnumeric
import datetime
import psycopg2
import sys
import csv
import glob
    
def select_banco_str(sql):
    global hot
    global dat
    global ussr
    global paswd
    con = psycopg2.connect(host= hot,
                    database= dat,
                    user= ussr,
                    password= paswd) 
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    return recset
    con.close()    

def insert_banco(sql):                    
    global hot
    global dat
    global ussr
    global paswd
    con = psycopg2.connect(host= hot,
                    database= dat,
                    user= ussr,
                    password= paswd)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
     
class login(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global hot
        global dat
        global ussr
        global paswd
        hot = ''
        dat = ''
        ussr = ''
        paswd = ''
        confirma = glob.glob('config.csv')
        if len(confirma) > 0:
            conf = csv.reader(open('config.csv'))
            config = list(range(4))
            i = 0
            for x in conf:
                config[i] = str(x)
                i += 1
            for i in range(4):
                if i == 0:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            hot += config[i][j]
                if i == 1:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            dat += config[i][j]
                if i == 2:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            ussr += config[i][j]
                if i == 3:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            paswd += config[i][j]                              
        QtCore.QObject.connect(self.ui.but_sair,QtCore.SIGNAL('clicked()'),self.fecha)
        QtCore.QObject.connect(self.ui.but_ok,QtCore.SIGNAL('clicked()'),self.entra)
        QtCore.QObject.connect(self.ui.edit_senha,QtCore.SIGNAL('returnPressed()'),self.entra)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.conf)
        self.ui.edit_nome.setFocus()
        if len(hot) == 0:
            self.ui.but_ok.setEnabled(False)
        else:
            self.ui.but_ok.setEnabled(True)    
    def conf(self):
        c = conf(self)
        c.show()
        self.setVisible(False)
    def fecha(self):
        self.close()  
    def entra(self):
        global logs
        nome = self.ui.edit_nome.text()
        senha = self.ui.edit_senha.text()
        while len(nome) < 20:
            nome += " "
        while len(senha) < 20:
            senha += " "    
        sql = '''select l.nivel,l.id
            from logins l
            where l.login = '%s' and senha = '%s' ''' % (str(nome),str(senha))
        log = select_banco_str(sql)
        if len(log) > 0:
            logs = int(log[0][1])
            if log[0][0] == 1: # Nivel 1
                sql = 'update logins set ativo = True where id = %d' % logs
                insert_banco(sql)
                s = nivel1(self)
                s.show()
                self.setVisible(False)
            elif log[0][0] == 2: # Nivel 2
                s = nivel2(self)
                s.show()
                self.setVisible(False)    
        else:
            t = dialog(self)
            texto = "Usuário e/ou senha inválidos!"
            t.ui.label.setText(texto.decode('utf-8'))
            t.show()

class conf(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Conf()
        self.ui.setupUi(self)             
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha) 
        confirma = glob.glob('config.csv')
        if len(confirma) > 0:
            conf = csv.reader(open('config.csv'))
            config = list(range(4))
            hot = ''
            dat = ''
            ussr = ''
            paswd = ''
            i = 0
            for x in conf:
                config[i] = str(x)
                i += 1
            for i in range(4):
                if i == 0:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            hot += config[i][j]
                if i == 1:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            dat += config[i][j]
                if i == 2:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            ussr += config[i][j]
                if i == 3:
                    for j in range(len(config[i])):
                        if "'" != config[i][j] != ' ' and '[' != config[i][j] != ']':
                            paswd += config[i][j]
                self.ui.lineEdit.setText(hot)
                self.ui.lineEdit_2.setText(dat)
                self.ui.lineEdit_3.setText(ussr)
                self.ui.lineEdit_4.setText(paswd) 
    def closeEvent(self,event):
        s = login(self)
        s.setVisible(True)
        self.setVisible(False)
        event.ignore()
    def fecha(self):
        configs = (self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),
                   self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text())
        with open('config.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile,delimiter = ' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(configs)
        self.close()
                      
class dialog(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)             
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha) 
    def fecha(self):
        self.close()

class dialog2(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)             
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha) 
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.manda)
    def manda(self):
        item = self.ui.listWidget.currentItem()
        usr_select = QtGui.QListWidgetItem.text(item)
        nome = ''
        i = 0
        for i in range(len(usr_select)):
            if (usr_select[i] == ' ' and usr_select[i+1] != ' ') or usr_select[i] != ' ':
                nome += usr_select[i]    
            else :
                break
        self.close()
        e = entregar(self)
        e.ui.lineEdit.clear()
        e.ui.lineEdit.setText(nome)  
        e.procura_usr()  
        e.show()
    def fecha(self):
        self.close()
        e = entregar(self)
        e.show()
        
class dialog3(QtGui.QDialog):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog_3()
        self.ui.setupUi(self)   
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha)
    def fecha(self):
        self.close()

class nivel1(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Nivel1()
        self.ui.setupUi(self)
        self.showMaximized()
        QtCore.QObject.connect(self.ui.but_sair,QtCore.SIGNAL('clicked()'),self.fecha) 
        QtCore.QObject.connect(self.ui.but_entr,QtCore.SIGNAL('clicked()'),self.entrega)  
        QtCore.QObject.connect(self.ui.but_rec,QtCore.SIGNAL('clicked()'),self.receberc)   
        self.connect(self, QtCore.SIGNAL('triggered()'),self.fecha)
        self.ui.tableWidget.doubleClicked.connect(self.recebers)      
        self.preenche_lista()
        self.ui.lineEdit.textChanged.connect(self.preenche_lista)
    def closeEvent(self,event):
        global logs
        sql = 'update logins set ativo = False where id = %d' % logs
        insert_banco(sql)
        y = login(self)
        self.setVisible(False)
        y.show()
        event.ignore()
    def fecha(self):
        self.close() 
    def recebers(self):
        select = self.ui.tableWidget.selectedItems()
        items = []
        for sel in select:
            items.append(QtGui.QTableWidgetItem(sel).text())
        nomes = items[3]
        salas = items[1]
        nome = ''
        sala = ''
        for i in range(len(nomes)):
            if (nomes[i] == ' ' and nomes[i+1] != ' ') or nomes[i] != ' ':
                nome += nomes[i]    
            else :
                break
        for j in range(len(salas)):
            if (salas[j] == ' ' and salas[j+1] != ' ') or salas[j] != ' ':
                sala += salas[j]    
            else :
                break        
        r = receber(self)
        r.show()
        r.ui.combo_chav.clear()
        sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),s.predio_id
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where s.nome = '%s' and r.usuario_id = u.id and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.nome = '%s' and r.datahora_rec isnull''' % (sala,nome)
        ret = select_banco_str(sql)
        for x in ret:
            if x[6] == int(r.ui.combo_pred.itemText(r.ui.combo_pred.currentIndex())[:3]):
                texto = "%3d - %s - Cópia %d - %s - %s" % (x[0],x[4],x[3],x[1],x[5])
                r.ui.combo_chav.addItem(texto.decode('utf-8'))
                r.ui.lineEdit.setText('%s' % x[2][:4])
        self.setVisible(False)         
    def receberc(self):
        r = receber(self)
        r.show()
        self.setVisible(False)
    def entrega(self):
        ent = entregar(self)
        ent.show()    
        self.setVisible(False)
    def preenche_lista(self):
        colunas = ['Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
        self.ui.tableWidget.clear()
        if (self.ui.lineEdit.text()) == 0:
            sql = '''select l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull'''
        else :
            filtro = str(self.ui.lineEdit.text())
            sql = '''select l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull
                and (upper(u.nome) like '%s%%' or upper(s.nome) like '%s%%')''' % (filtro.upper(),filtro.upper())
        ret = select_banco_str(sql)
        self.ui.tableWidget.setRowCount(len(ret))
        self.ui.tableWidget.setColumnCount(5)
        for j in range(5):
            item2 = QtGui.QTableWidgetItem(colunas[j])
            self.ui.tableWidget.setHorizontalHeaderItem(j,item2)
            for i in range(len(ret)):
                texto = str(ret[i][j])
                item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                self.ui.tableWidget.setItem(i,j,item)
                
class entregar(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Mainentrega()
        self.ui.setupUi(self)
        self.preenche_pred()
        self.ui.lineEdit.setFocus()
        QtCore.QObject.connect(self.ui.but_canc,QtCore.SIGNAL('clicked()'),self.fecha)
        QtCore.QObject.connect(self.ui.but_proc,QtCore.SIGNAL('clicked()'),self.procura_usr)    
        QtCore.QObject.connect(self.ui.but_ent,QtCore.SIGNAL('clicked()'),self.ent_valores)
        QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL('returnPressed()'),self.procura_usr)
    def closeEvent(self,event):
        n = nivel1(self)
        n.setVisible(True)
        self.setVisible(False)
        event.ignore()
    def fecha(self):
        self.close()  
    def ent_valores(self):
        chave_id = self.ui.combo_sal.itemText(self.ui.combo_sal.currentIndex())[:3]
        sql = 'select chave_id from retiradas where datahora_rec isnull and chave_id = %d' % int(chave_id)
        testa = select_banco_str(sql)
        if len(testa) > 0:
            d = dialog(self)
            d.ui.label.setText("Chave em aberto!")
            d.show()
        else:    
            global logs
            usr_id = self.ui.lineEdit.text()[:3]
            sql = 'insert into retiradas(login_id,chave_id,usuario_id,datahora_ent) values(%d,%d,%d,now())' % (int(logs),
                                                                                            int(chave_id),int(usr_id))
            insert_banco(sql)
            self.close()
            s = nivel1(self)
            s.show()
    def preenche_pred(self):
        self.ui.combo_pred.clear()
        sql = 'select * from predios'
        pred = select_banco_str(sql)
        for p in pred:
            text = "%2d - %s" % p
            self.ui.combo_pred.addItem(text.decode('utf-8'))
    def procura_usr(self):
        self.ui.combo_sal.clear()
        predio_id = self.ui.combo_pred.itemText(self.ui.combo_pred.currentIndex())[:3]
        usr_cpf = ''
        cpf = ''
        user = '%s' % self.ui.lineEdit.text()
        for i in range(0,len(user)):
            if isnumeric(user[i]) or user[i] == '0':
                usr_cpf += str(user[i])   
        cpf = usr_cpf[:3] + '.' + usr_cpf[3:6] + '.' + usr_cpf[6:9] + '-' + usr_cpf[9:] + ' '    
        if len(user) > 0:
            sql = '''select u.id,u.nome,u.tipo
                from usuarios u
                where ((upper(remove_acento(u.nome)) like '%s%%' or upper(u.nome) like '%s%%') or u.cpf = '%s') ''' % (user.upper(),
                                                                                                              user.upper(),str(cpf))
            usr = select_banco_str(sql)
            if len(usr) == 1:
                texto = "%2d - %s" % (usr[0][0],usr[0][1])
                self.ui.lineEdit.setText(texto.decode('utf-8'))        
                if usr[0][2] == 'p':    
                    sql = ''' select c.id,s.nome,c.nro_copia
                            from chaves c,salas s,autos a
                where a.usuario_id = %d and a.sala_id = s.id and c.sala_id = s.id and s.predio_id = %d
                            union 
                        select c.id,s.nome,c.nro_copia
                        from chaves c,salas s,autos a    
                where c.sala_id = s.id and s.predio_id = %d and (s.direito = 'p' or s.direito = 'a') '''  % (usr[0][0],int(predio_id),int(predio_id))
                elif usr[0][2] == 'a':
                    sql = '''select c.id,s.nome,c.nro_copia
                            from chaves c,salas s,autos a
                where a.usuario_id = %d and a.sala_id = s.id and c.sala_id = s.id and s.predio_id = %d
                            union 
                        select c.id,s.nome,c.nro_copia
                        from chaves c,salas s,autos a    
                where c.sala_id = s.id and s.predio_id = %d and s.direito = 'a' ''' % (usr[0][0],int(predio_id),int(predio_id))
                chv = select_banco_str(sql)
                for c in chv:
                    text = "%2d - %s - Cópia %d" % c
                    self.ui.combo_sal.addItem(text.decode('utf-8'))
                QtCore.QObject.connect(self.ui.combo_pred,QtCore.SIGNAL('currentIndexChanged(const QString&)'),self.limpa)
            elif len(usr) > 1:
                d2 = dialog2(self)
                d2.ui.listWidget.clear()
                for u in usr:   
                    un = u[1].decode('utf-8') 
                    item = QtGui.QListWidgetItem(un)
                    d2.ui.listWidget.addItem(item)
                    d2.ui.listWidget.setCurrentRow(0)
                self.setVisible(False)    
                d2.show()  
            else:
                d = dialog(self)
                texto = "Usuário nao encontrado!"
                d.ui.label.setText(texto.decode('utf-8'))
                d.show()
        else:
            d = dialog(self)
            d.ui.label.setText("Precisa digitar algo!")
            d.show()      
    def limpa(self):
        self.ui.lineEdit.clear()
        self.ui.combo_sal.clear()          
                              
class receber(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_receber()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.but_canc,QtCore.SIGNAL('clicked()'),self.fecha)
        QtCore.QObject.connect(self.ui.but_rec,QtCore.SIGNAL('clicked()'),self.recebe_chaves)
        self.preenche_pred()
    def closeEvent(self,event):
        n = nivel1(self)
        n.setVisible(True)
        self.setVisible(False)
        event.ignore()
    def recebe_chaves(self): 
        retir_id = int(self.ui.combo_chav.itemText(self.ui.combo_chav.currentIndex())[:4])   
        sql = 'update retiradas set datahora_rec = now() where id = %d' % retir_id
        insert_banco(sql)
        self.preenche_combo()
        t = dialog(self)
        t.ui.label.setText("Chave recebida com sucesso!")
        t.show()
    def preenche_pred(self):
        self.ui.combo_pred.clear()
        sql = 'select * from predios'
        pred = select_banco_str(sql)
        for p in pred:
            text = "%2d - %s" % p
            self.ui.combo_pred.addItem(text.decode('utf-8'))
        QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL('returnPressed()'),self.preenche_combo)
        QtCore.QObject.connect(self.ui.combo_pred,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.preenche_combo)    
    def fecha(self):
        self.close()
    def preenche_combo(self):
        self.ui.combo_chav.clear()
        sala = str(self.ui.lineEdit.text())
        sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),s.predio_id
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where upper(s.nome) = '%s' and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = r.usuario_id and r.datahora_rec isnull''' % (sala.upper())
        ret = select_banco_str(sql)
        for r in ret:
            if r[6] == int(self.ui.combo_pred.itemText(self.ui.combo_pred.currentIndex())[:3]):
                texto = "%3d - %s - Cópia %d - %s - %s" % (r[0],r[4],r[3],r[1],r[5])
                self.ui.combo_chav.addItem(texto.decode('utf-8'))
                self.ui.lineEdit.setText('%s' % r[2][:4])

class nivel2(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_nivel2()
        self.ui.setupUi(self) 
        self.showMaximized()
        self.preenche_ano()
        self.preenche_mes()
        self.preenche_pred()
        self.tabela_retiradas()
        self.lista_logins()
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)
        self.preenche_usuarios()
        self.lista_usuarios()
        self.tabela_autos()
        self.tabela_salas()
        self.tabela_predios()
        self.tabela_logins()
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_12.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_14.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        timer = QTimer(self)
        timer2 = QTimer(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha)  
        QtCore.QObject.connect(self.ui.comboBox,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas) 
        QtCore.QObject.connect(self.ui.comboBox_2,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas) 
        QtCore.QObject.connect(self.ui.comboBox_3,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
        QtCore.QObject.connect(self.ui.comboBox_4,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
        QtCore.QObject.connect(self.ui.comboBox_5,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.preenche_sala)
        QtCore.QObject.connect(self.ui.comboBox_7,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_salas)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL('clicked()'),self.exclui_retiradas)  
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.exclui_usuarios)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.add_user)
        QtCore.QObject.connect(self.ui.pushButton_5,QtCore.SIGNAL("clicked()"),self.insert_autos)
        QtCore.QObject.connect(self.ui.pushButton_6,QtCore.SIGNAL("clicked()"),self.exclui_autos)
        QtCore.QObject.connect(self.ui.pushButton_8,QtCore.SIGNAL("clicked()"),self.insert_sala)
        QtCore.QObject.connect(self.ui.pushButton_7,QtCore.SIGNAL("clicked()"),self.exclui_sala)
        QtCore.QObject.connect(self.ui.pushButton_11,QtCore.SIGNAL("clicked()"),self.insert_copia)
        QtCore.QObject.connect(self.ui.pushButton_10,QtCore.SIGNAL("clicked()"),self.exclui_copia)
        QtCore.QObject.connect(self.ui.pushButton_12,QtCore.SIGNAL("clicked()"),self.exclui_predio)
        QtCore.QObject.connect(self.ui.pushButton_14,QtCore.SIGNAL("clicked()"),self.exclui_logins)
        QtCore.QObject.connect(self.ui.pushButton_9,QtCore.SIGNAL("clicked()"),self.add_predio)
        QtCore.QObject.connect(self.ui.pushButton_13,QtCore.SIGNAL("clicked()"),self.add_login)
        QtCore.QObject.connect(timer2,QtCore.SIGNAL("timeout()"),self.tabela_retiradas)
        QtCore.QObject.connect(timer,QtCore.SIGNAL("timeout()"),self.lista_logins)
        self.ui.lineEdit.textChanged.connect(self.preenche_usuarios)
        self.ui.lineEdit_2.textChanged.connect(self.tabela_retiradas)
        self.ui.lineEdit_7.textChanged.connect(self.abilita_add)
        self.ui.lineEdit_8.textChanged.connect(self.tabela_predios)
        self.ui.lineEdit_9.textChanged.connect(self.tabela_logins)
        self.ui.tableWidget_2.doubleClicked.connect(self.lista_user)
        self.ui.tableWidget_6.doubleClicked.connect(self.lista_login)
        self.ui.tableWidget_4.itemSelectionChanged.connect(self.lista_copias)
        self.ui.tableWidget_5.itemSelectionChanged.connect(self.abilita_exlusao)
        self.ui.tableWidget.itemSelectionChanged.connect(self.abilita_exlusao_ret)
        self.ui.tableWidget_2.itemSelectionChanged.connect(self.abilita_exlusao_usr)
        self.ui.listWidget_2.itemSelectionChanged.connect(self.abilita_add_aut)
        self.ui.tableWidget_3.itemSelectionChanged.connect(self.abilita_exlusao_aut)
        self.ui.tableWidget_6.itemSelectionChanged.connect(self.abilita_exclusao_log)
        self.ui.lineEdit_3.textChanged.connect(self.lista_usuarios)
        self.ui.lineEdit_4.textChanged.connect(self.tabela_autos)
        self.ui.lineEdit_6.textChanged.connect(self.tabela_salas)
        self.ui.lineEdit_5.textChanged.connect(self.abilita_add_sala)
        timer.start(5000)
        timer2.start(15000) 
    def closeEvent(self,event):
        s = login(self)
        s.setVisible(True)
        self.setVisible(False)
        event.ignore()
    def abilita_add_sala(self):
        tamanho = len(self.ui.lineEdit_5.text())
        if tamanho > 0:
            self.ui.pushButton_8.setEnabled(True)
        else:
            self.ui.pushButton_8.setEnabled(False)
    def abilita_exclusao_log(self):
        select = self.ui.tableWidget_6.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_14.setEnabled(True)
        else:
            self.ui.pushButton_14.setEnabled(False)
    def abilita_exlusao_aut(self):
        select = self.ui.tableWidget_3.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_6.setEnabled(True)
        else:
            self.ui.pushButton_6.setEnabled(False)    
    def abilita_add_aut(self):
        select = self.ui.listWidget_2.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_5.setEnabled(True)
        else:
            self.ui.pushButton_5.setEnabled(False)
    def abilita_exlusao_usr(self):
        select = self.ui.tableWidget_2.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_3.setEnabled(True)
        else:
            self.ui.pushButton_3.setEnabled(False)
    def abilita_exlusao_ret(self):
        select = self.ui.tableWidget.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_4.setEnabled(True)
        else:
            self.ui.pushButton_4.setEnabled(False)
    def abilita_add(self):
        if len(self.ui.lineEdit_7.text()) > 0:
            self.ui.pushButton_9.setEnabled(True)
        else:
            self.ui.pushButton_9.setEnabled(False)    
    def abilita_exlusao(self):
        select = self.ui.tableWidget_5.selectedItems()
        if len(select) > 0:
            self.ui.pushButton_12.setEnabled(True)
        else:
            self.ui.pushButton_12.setEnabled(False)    
    def excluil(self):
        global exclog
        for e in exclog:
            try:
                sql = ''' delete from logins where id = %d ''' % int(e)
                insert_banco(sql)
                self.tabela_logins()
            except psycopg2.IntegrityError:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possivel excluir login %d,contate administrador do sistema!" % e) 
                d.show()
    def exclui_logins(self):
        select = self.ui.tableWidget_6.selectedItems()
        items = []
        global exclog
        if len(select) > 0:
            for sel in select:
                items.append(QtGui.QTableWidgetItem(sel).text())   
            exclog = []
            i = 0    
            if len(items) > 3:    
                while i < len(items):
                    exclog.append(int(items[i]))
                    i += 3
            else:
                exclog.append(int(items[0]))        
            if len(exclog) >= 1:
                d = dialog3(self)
                d.ui.label.setText(u"A exclusão de Logins é permanente e não pode ser desfeita.")
                d.show()
                self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluil)
    def lista_login(self):
        select = self.ui.tableWidget_6.selectedItems()
        global log_id
        list_user = []
        for s in select:
            list_user.append(QtGui.QTableWidgetItem(s).text())
        log_id = list_user[0]
        sql = ''' select id,nome,nivel,login,senha from logins where id = %d ''' % int(log_id)
        logins = select_banco_str(sql)
        nome = logins[0][1]
        nivel = logins[0][2]
        login = logins[0][3]
        senha = str(logins[0][4])
        senhas = ''
        for s in senha:
            if s != ' ':
                senhas += s
        c = cad_login(self)
        c.limpa()
        c.ui.lineEdit.setText(str(nome).decode('utf-8'))
        c.ui.comboBox_2.setCurrentIndex((nivel - 1))
        c.ui.lineEdit_3.setText(login)
        c.ui.lineEdit_4.setText(senhas)
        c.show()
        self.setVisible(False)    
        self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.atualiza_login)
        c.ui.lineEdit.setFocus()
    def add_login(self):
        c = cad_login(self)
        self.setVisible(False)
        c.show()
        self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.add_login)
        c.ui.lineEdit.setFocus()
    def tabela_logins(self):
        self.ui.tableWidget_6.clear()
        if self.ui.lineEdit_9.text() > 0:
            nome = str(self.ui.lineEdit_9.text())
            sql = ''' select id,nome,nivel from logins where upper(nome) like '%s%%' order by nome''' % nome.upper()
        else:
            sql = ''' select id,nome,nivel from logins order by nome'''
        users = select_banco_str(sql) 
        colunas = [' ID ','Nome','Nivel']
        if len(users) > 0:
            self.ui.tableWidget_6.setRowCount(len(users))
            self.ui.tableWidget_6.setColumnCount(len(colunas))         
            for j in range(len(colunas)):
                item2 = QtGui.QTableWidgetItem(colunas[j])
                self.ui.tableWidget_6.setHorizontalHeaderItem(j,item2)
                maior = len(colunas[j])
                for i in range(len(users)):
                    texto = str(users[i][j])
                    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                    self.ui.tableWidget_6.setItem(i,j,item)
                    if len(texto) > maior: maior = len(texto)
                self.ui.tableWidget_6.setColumnWidth(j,(maior*8))  
        else: 
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)
    def add_predio(self):
        nome = self.ui.lineEdit_7.text()
        sql = '''select nome from predios
            where nome = '%s' ''' % nome
        verifica = select_banco_str(sql)
        if len(verifica) > 0:
            d = dialog(self)
            d.ui.label.setText(u"Prédio já cadastrado com esse nome!")
            d.show()
        else:
            sql = ''' insert into predios(nome) values('%s')''' % nome
            if len(nome) > 0:    
                try:
                    insert_banco(sql)
                    d = dialog(self)
                    d.ui.label.setText(u"Prédio incluido com sucesso!")
                    d.show()
                    self.tabela_predios()
                    self.preenche_pred()
                    self.ui.lineEdit_7.clear()
                except psycopg2.Error:
                    d = dialog(self)
                    d.ui.label.setText(u"Não foi possível incluir,contate administrador!")
                    d.show()            
    def exclui_predio(self):
        d = dialog3(self)
        d.ui.label.setText(u"A exclusão de prédios é permanente e não pode ser desfeita.")
        d.show()
        self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluip)
    def excluip(self):
        select = self.ui.tableWidget_5.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        i = 0
        excp = []
        if len(lista) > 3:
            while i < len(lista):
                excp.append(lista[i])
                i += 3
        elif len(lista) == 3: excp.append(lista[0])
        if len(excp) > 0:
            for e in excp:
                sql = ''' delete from predios where id = %d ''' % int(e)
                try:
                    insert_banco(sql)
                    d = dialog(self)
                    d.ui.label.setText(u"Prédio %d excluido!" % int(e))
                    d.show()
                    self.tabela_predios()
                    self.preenche_pred()
                except psycopg2.IntegrityError:
                    d = dialog(self)
                    d.ui.label.setText(u"Não foi possível excluir o prédio %s,existem salas cadastradas!" % int(e))
                    d.show()
    def tabela_predios(self):
        self.ui.tableWidget_5.clear()
        if len(self.ui.lineEdit_8.text()) > 0:
            filtro = str(self.ui.lineEdit_8.text())
            sql = ''' select id,nome from predios 
                where upper(nome) like '%s%%'
                order by nome''' % filtro.upper()
        else:
            sql = ''' select id,nome from predios
                    order by nome'''
        predios = select_banco_str(sql)
        colunas = [' ID ','Nome','Nro.Salas']
        if len(predios) > 0:
            self.ui.tableWidget_5.setRowCount(len(predios))
            self.ui.tableWidget_5.setColumnCount(len(colunas))         
            for j in range(len(colunas)):
                item2 = QtGui.QTableWidgetItem(colunas[j])
                self.ui.tableWidget_5.setHorizontalHeaderItem(j,item2)
                maior = len(colunas[j])
                for i in range(len(predios)):
                    sql = '''select nome from salas where predio_id = %d''' % predios[i][0]
                    salas = select_banco_str(sql)
                    nro_salas = len(salas)
                    if j == 2:
                        texto = str(nro_salas)
                    else:    texto = str(predios[i][j])
                    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                    self.ui.tableWidget_5.setItem(i,j,item)
                    if len(texto) > maior: maior = len(texto)
                self.ui.tableWidget_5.setColumnWidth(j,(maior*6))  
        else: 
            self.ui.tableWidget_5.clear()
            self.ui.tableWidget_5.setRowCount(0)
            self.ui.tableWidget_5.setColumnCount(0)
    def exclui_copia(self):
        d = dialog3(self)
        d.ui.label.setText(u"A exclusão de cópias é permanente e não pode ser desfeita.")
        d.show()
        self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluic)
    def excluic(self):
        select = self.ui.tableWidget_4.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        if len(lista) > 0:
            sala = int(lista[0])
            sql = ''' select id,nro_copia from chaves
            where sala_id = %d 
            order by nro_copia''' % sala
            chaves = select_banco_str(sql)
            maior = 0
            for ch in chaves:
                if maior < ch[1]:
                    maior = ch[1]
                    chave_id = ch[0]
            sql = ''' delete from chaves where id = %d''' % int(chave_id)
            try:
                insert_banco(sql)
                self.lista_copias()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possível excluir cópia,contate administrador do sistema!")
                d.show()
    def insert_copia(self):
        select = self.ui.tableWidget_4.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        if len(lista) > 0:
            sala = int(lista[0])
            sql = ''' select nro_copia from chaves
            where sala_id = %d 
            order by nro_copia''' % sala
            chaves = select_banco_str(sql)
            maior = 0
            if len(chaves) > 0:
                for ch in chaves:
                    if maior < ch[0]:
                        maior = ch[0]      
            else: maior = 0     
            sql = ''' insert into chaves(nro_copia,sala_id) values(%d,%d)''' % ((maior+1),sala)
            try:
                insert_banco(sql)
                self.lista_copias()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possível cadastrar cópia,contate administrador do sistema!")
                d.show()
    def lista_copias(self):
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.listWidget_3.clear()
        select = self.ui.tableWidget_4.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        if len(lista) > 0:
            sala = int(lista[0])
            sql = ''' select id,nro_copia from chaves
            where sala_id = %d 
            order by nro_copia''' % sala
            chaves = select_banco_str(sql)
            if len(chaves) > 0:
                for ch in chaves:
                    texto = '%2d - Cópia %d' % ch
                    item = QtGui.QListWidgetItem(texto.decode('utf-8'))
                    self.ui.listWidget_3.addItem(item)
                self.ui.pushButton_10.setEnabled(True)
            else:
                self.ui.pushButton_10.setEnabled(False)
                self.ui.lineEdit_3.clear()
    def exclui_sala(self):
        d = dialog3(self)
        d.ui.label.setText(u"A exclusão de salas é permanente e não pode ser desfeita.")
        d.show()
        self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluis)
    def excluis(self):
        select = self.ui.tableWidget_4.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        i = 0
        excs = []
        if len(lista) > 3:
            while i < len(lista):
                excs.append(lista[i])
                i += 3
        elif len(lista) == 3: excs.append(lista[0])
        for e in excs:    
            sala = int(e)
            sql = ''' delete from salas where id = %d ''' % sala
            try:
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Sala %d Excluida!" % sala)
                d.show()
                self.tabela_salas()
                self.tabela_predios()
                self.preenche_sala()
            except psycopg2.IntegrityError:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possível excluir a sala,existem cópias para ela!")
                d.show()
    def tabela_salas(self):
        self.ui.tableWidget_4.clear()
        predio = self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex())[:3]
        if len(self.ui.lineEdit_6.text()) > 0:
            filtro = str(self.ui.lineEdit_6.text())
            sql = ''' select id,nome,direito from salas
            where upper(nome) like '%s%%' and predio_id = %d
            order by nome ''' % (filtro.upper(),int(predio))
        else:
            try:
                sql = ''' select id,nome,direito from salas
                        where predio_id = %d
                        order by nome ''' % int(predio)
                salas = select_banco_str(sql)            
                colunas = [' ID ','Nome','Direito'] 
                if len(salas) > 0:
                    self.ui.tableWidget_4.setRowCount(len(salas))
                    self.ui.tableWidget_4.setColumnCount(len(colunas))         
                    for j in range(len(colunas)):
                        item2 = QtGui.QTableWidgetItem(colunas[j])
                        self.ui.tableWidget_4.setHorizontalHeaderItem(j,item2)
                        maior = len(colunas[j])
                        for i in range(len(salas)):
                            if salas[i][j] == 'p': texto = 'Todos Professores'
                            elif salas[i][j] == 'a': texto = 'Todos Alunos'
                            elif salas[i][j] == None: texto = ''
                            else:
                                texto = str(salas[i][j])
                            item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                            self.ui.tableWidget_4.setItem(i,j,item)
                            if len(texto) > maior: maior = len(texto)
                        self.ui.tableWidget_4.setColumnWidth(j,(maior*6))  
                else: 
                    self.ui.tableWidget_4.clear()
                    self.ui.tableWidget_4.setRowCount(0)
                    self.ui.tableWidget_4.setColumnCount(0) 
            except ValueError:
                pass 
    def insert_sala(self):
        nome = self.ui.lineEdit_5.text()
        predio = self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex())[:3]
        if self.ui.comboBox_8.currentIndex() == 2:
            direito = 'a'
        elif self.ui.comboBox_8.currentIndex() == 1:
            direito = 'p'
        else:
            direito = ''
        sql = ''' select nome from salas
                where upper(nome) = '%s' and predio_id = %d ''' % (str(nome).upper(),int(predio))
        verifica = select_banco_str(sql)
        if len(verifica) > 0:
            d = dialog(self)
            d.ui.label.setText(u"Sala %s já cadastrada" % verifica[0][0])
            d.show()
        else:
            sql = ''' insert into salas(nome,predio_id,direito) values('%s',%d,'%s')''' % (str(nome).upper(),int(predio),str(direito))  
            try:
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Sala Cadastrada com sucesso!")
                d.show()
                self.tabela_salas()
                self.ui.lineEdit_5.clear()
                self.ui.comboBox_8.setCurrentIndex(0)
                self.tabela_predios()
                self.preenche_sala()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Problema ao cadastrar a sala,contate administrador do sistema!")
                d.show()
    def exclui_autos(self):
        select = self.ui.tableWidget_3.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QTableWidgetItem(sel).text()
            lista.append(item)
        global exca
        exca = []
        i = 0    
        if len(lista) > 4:    
            while i < len(lista):
                exca.append(int(lista[i]))
                i += 4
        else:
            exca.append(int(lista[0]))
        if len(exca) > 0:
            d = dialog3(self)
            d.ui.label.setText(u"A exclusão de autorizações é permanente e não pode ser desfeita.")
            d.show()
            self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluia)
    def excluia(self):
        global exca
        for e in exca:
            try:
                sql = ''' delete from autos where id = %d ''' % e
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Autorização %d excluida!" % e) 
                d.show()
                self.tabela_autos()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possivel excluir autorização %d !" % e) 
                d.show() 
    def insert_autos(self):
        select = self.ui.listWidget_2.selectedItems()
        lista = []
        for sel in select:
            item = QtGui.QListWidgetItem(sel).text()
            lista.append(item[:4]) 
        sala = str(self.ui.comboBox_6.itemText(self.ui.comboBox_6.currentIndex()))[:4]
        global logs
        login = logs
        if len(lista) > 0:
            for li in lista:
                sql = ''' select sala_id,usuario_id from autos
                    where sala_id = %d and usuario_id = %d ''' % (int(sala),int(li))
                procura = select_banco_str(sql)
                if len(procura) > 0:
                    d = dialog(self)
                    d.ui.label.setText(u"Autorização já existente para usuário %d!" % int(li))
                    d.show()
                else:
                    sql = ''' insert into autos(sala_id,usuario_id,login_id) values(%d,%d,%d) ''' % (int(sala),int(li),int(login))
                    try:
                        insert_banco(sql)
                        d = dialog(self)
                        d.ui.label.setText(u"Autorização realizada com sucesso para usuário %d!" % int(li))
                        d.show()
                    except psycopg2.Error:
                        d = dialog(self)
                        d.ui.label.setText(u"Impossivel registrar autorização para %d!" % int(li))
                        d.show()  
            self.tabela_autos()      
    def tabela_autos(self):
        self.ui.tableWidget_3.clear()
        if len(self.ui.lineEdit_4.text()) > 0:
            filtro = str(self.ui.lineEdit_4.text())
            sql = ''' select a.id,s.nome,u.nome,l.nome
            from autos a,salas s,usuarios u,logins l
            where a.sala_id = s.id and a.usuario_id = u.id and a.login_id = l.id and (upper(u.nome) like '%s%%' or upper(s.nome) like '%s%%')
            order by s.nome ''' % (filtro.upper(),filtro.upper())
        else:
            sql = ''' select a.id,s.nome,u.nome,l.nome
                    from autos a,salas s,usuarios u,logins l
                    where a.sala_id = s.id and a.usuario_id = u.id and a.login_id = l.id
                    order by s.nome '''
        autos = select_banco_str(sql)
        colunas = [' ID ','Sala',u'Usuário','Login'] 
        if len(autos) > 0:
            self.ui.tableWidget_3.setRowCount(len(autos))
            self.ui.tableWidget_3.setColumnCount(len(colunas))         
            for j in range(len(colunas)):
                item2 = QtGui.QTableWidgetItem(colunas[j])
                self.ui.tableWidget_3.setHorizontalHeaderItem(j,item2)
                maior = len(colunas[j])
                for i in range(len(autos)):
                    texto = str(autos[i][j])
                    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                    self.ui.tableWidget_3.setItem(i,j,item)
                    if len(texto) > maior: maior = len(texto)
                self.ui.tableWidget_3.setColumnWidth(j,(maior*6))  
        else: 
            self.ui.tableWidget_3.clear()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.tableWidget_3.setColumnCount(0)   
    def lista_usuarios(self):
        self.ui.listWidget_2.clear()
        if len(self.ui.lineEdit_3.text()) > 0:
            nome = u"%s" % str(self.ui.lineEdit_3.text())
            sql = ''' select id,nome from usuarios where upper(nome) like '%s%%'
                    order by nome''' % nome.upper()
        else:
            sql = ''' select id,nome from usuarios order by nome '''
        usuarios = select_banco_str(sql)
        for usuario in usuarios:
            texto = "%3d - %s" % usuario
            item = QtGui.QListWidgetItem(texto.decode('utf-8'))
            self.ui.listWidget_2.addItem(item)
    def preenche_sala(self):
        try:
            self.ui.comboBox_6.clear()
            predio = int(self.ui.comboBox_5.itemText(self.ui.comboBox_5.currentIndex())[:3])
            sql = ''' select id,nome from salas where predio_id = %d order by nome''' % predio
            salas = select_banco_str(sql)
            for sala in salas:
                texto = "%3d - %s" % sala
                self.ui.comboBox_6.addItem(texto.decode('utf-8'))
        except ValueError:
            pass
    def add_user(self):
        c = cad_user(self)
        self.setVisible(False)
        c.show()
        self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.add_user)
        c.ui.lineEdit.setFocus()
    def lista_user(self):
        select = self.ui.tableWidget_2.selectedItems()
        global usr_id
        list_user = []
        for s in select:
            list_user.append(QtGui.QTableWidgetItem(s).text())
        usr_id = list_user[0]
        nome = list_user[1]
        if list_user[2] == 'None': cod = 0
        else:    cod = list_user[2]
        eml = list_user[3]
        cpf = list_user[4]
        tipo = list_user[5]
        c = cad_user(self)
        c.limpa()
        c.ui.lineEdit.setText(nome)
        c.ui.spinBox.setValue(int(cod))
        c.ui.lineEdit_3.setText(eml)
        c.ui.lineEdit_4.setText(cpf)
        if tipo == 'p':c.ui.comboBox.setCurrentIndex(0)
        else : c.ui.comboBox.setCurrentIndex(1)
        c.show()
        self.setVisible(False)    
        self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.atualiza_user)
        c.ui.lineEdit.setFocus()
    def exclui_retiradas(self):
        global exc
        select = self.ui.tableWidget.selectedItems()
        items = []   
        if len(select) > 0:    
            for sel in select:
                items.append(QtGui.QTableWidgetItem(sel).text())       
                exc = []
                i = 0
            if self.ui.comboBox_2.currentIndex() == 0 or self.ui.comboBox_2.currentIndex() == 2:
                num = 7
            else: num = 6 
            if len(items) > num:    
                while i < len(items):
                    exc.append(int(items[i]))
                    i += num
            else:
                exc.append(int(items[i]))
            if len(exc) >= 1:
                d = dialog3(self)
                d.ui.label.setText(u"A exclusão de retiradas é permanente e não pode ser desfeita.")
                d.show()
                self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluit)   
    def excluit(self):
        global exc
        for e in exc:
            try:
                sql = ''' delete from retiradas where id = %d ''' % e
                insert_banco(sql)
                self.tabela_retiradas()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possivel excluir retirada %d !" % e) 
                d.show()
    def excluiu(self):
        global excu
        for e in excu:
            try:
                sql = ''' delete from usuarios where id = %d ''' % e
                insert_banco(sql)
                self.tabela_retiradas()
            except psycopg2.IntegrityError:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possivel excluir usuário %d,existem retiradas ou autorizações para o mesmo!" % e) 
                d.show()
        self.preenche_usuarios()
    def exclui_usuarios(self):
        select = self.ui.tableWidget_2.selectedItems()
        items = []
        global excu
        if len(select) > 0:
            for sel in select:
                items.append(QtGui.QTableWidgetItem(sel).text())   
            excu = []
            i = 0    
            if len(items) > 6:    
                while i < len(items):
                    excu.append(int(items[i]))
                    i += 6
            else:
                excu.append(int(items[i]))        
            if len(excu) >= 1:
                d = dialog3(self)
                d.ui.label.setText(u"A exclusão de usuários é permanente e não pode ser desfeita.")
                d.show()
                self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluiu)    
    def preenche_usuarios(self):
        self.ui.tableWidget_2.clear()
        if self.ui.lineEdit.text() > 0:
            nome = str(self.ui.lineEdit.text())
            sql = ''' select * from usuarios where upper(nome) like '%s%%' order by nome''' % nome.upper()
        else:
            sql = ''' select * from usuarios'''
        users = select_banco_str(sql) 
        colunas = [' ID ','Nome','Cod.Barras','Email','Cpf','Tipo']
        if len(users) > 0:
            self.ui.tableWidget_2.setRowCount(len(users))
            self.ui.tableWidget_2.setColumnCount(len(colunas))         
            for j in range(len(colunas)):
                item2 = QtGui.QTableWidgetItem(colunas[j])
                self.ui.tableWidget_2.setHorizontalHeaderItem(j,item2)
                maior = len(colunas[j])
                for i in range(len(users)):
                    if j == 5:
                        if str(users[i][j]) == 'p':
                            texto = 'Professor'
                        elif str(users[i][j]) == 'a':
                            texto = 'Aluno'
                        else: texto = 'Servidor'
                    else:    
                        texto = str(users[i][j])
                    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                    self.ui.tableWidget_2.setItem(i,j,item)
                    if len(texto) > maior: maior = len(texto)
                self.ui.tableWidget_2.setColumnWidth(j,(maior*8))  
        else: 
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)
    def fecha(self):
        self.close() 
    def lista_logins(self):
        self.ui.listWidget.clear()
        sql = 'select nome from logins where ativo = True'
        ativos = select_banco_str(sql)
        if len(ativos) > 0:
            for a in ativos:
                texto = "%s" % a
                item = QtGui.QListWidgetItem(texto.decode('utf-8'))
                self.ui.listWidget.addItem(item) 
    def preenche_ano(self):
        self.ui.comboBox_4.clear()
        dt = datetime.date.today()
        ano = dt.year
        while ano >= (dt.year - 5):
            self.ui.comboBox_4.addItem(str(ano))
            ano -= 1
        self.ui.comboBox_4.setCurrentIndex(0)
    def preenche_mes(self):
        self.ui.comboBox_3.clear()
        dt = datetime.date.today()
        mes_atual = dt.month - 1
        meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']   
        for i in meses:
            texto = "%s" % i
            self.ui.comboBox_3.addItem(texto.decode('utf-8'))
        self.ui.comboBox_3.setCurrentIndex(mes_atual)
    def preenche_pred(self):
        self.ui.comboBox.clear()
        self.ui.comboBox_5.clear()
        self.ui.comboBox_7.clear()
        sql = 'select * from predios'
        pred = select_banco_str(sql)
        for p in pred:
            text = "%2d - %s" % p
            self.ui.comboBox.addItem(text.decode('utf-8'))
            self.ui.comboBox_5.addItem(text.decode('utf-8')) 
            self.ui.comboBox_7.addItem(text.decode('utf-8')) 
        self.preenche_sala()       
    def tabela_retiradas(self):
        try:
            self.ui.tableWidget.clear()
            if len(self.ui.lineEdit_2.text()) > 0:
                filtro = str(self.ui.lineEdit_2.text())
            else:
                filtro = ''    
            ano = self.ui.comboBox_4.itemText(self.ui.comboBox_4.currentIndex())
            predio = int(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())[:3])
            escolha = self.ui.comboBox_2.currentIndex()
            m = (int(self.ui.comboBox_3.currentIndex()) + 1)
            if m < 10: mes = ('0' + str(m) + '/' + str(ano))
            else: mes = (str(m) + '/' + str(ano))   
            if escolha == 0 : # Todas
                sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_rec desc''' % (predio,mes)
                colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
                if len(filtro) > 0:
                    sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where (upper(u.nome) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_rec desc''' % (filtro.upper(),filtro.upper(),predio,mes)    
            elif escolha == 1: # Em Aberto
                sql =  '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_ent desc'''   % (predio,mes)
                colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
                if len(filtro) > 0:
                    sql =  '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where (upper(u.nome) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_ent desc'''   % (filtro.upper(),filtro.upper(),predio,mes)
            else: # Fechadas
                sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and r.datahora_rec notnull and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_rec desc''' % (predio,mes)
                colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
                if len(filtro) > 0:
                    sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
                from logins l,retiradas r,salas s,usuarios u,chaves c
                where (upper(u.nome) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and r.datahora_rec notnull and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
                order by r.datahora_rec desc''' % (filtro.upper(),filtro.upper(),predio,mes)
            ret = select_banco_str(sql)
            if len(ret) > 0:
                self.ui.tableWidget.setRowCount(len(ret))
                self.ui.tableWidget.setColumnCount(len(colunas))         
                for j in range(len(colunas)):
                    item2 = QtGui.QTableWidgetItem(colunas[j])
                    self.ui.tableWidget.setHorizontalHeaderItem(j,item2)
                    maior = len(colunas[j])
                    for i in range(len(ret)):
                        texto = str(ret[i][j])
                        item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
                        self.ui.tableWidget.setItem(i,j,item)
                        if len(texto) > maior: maior = len(texto)
                    self.ui.tableWidget.setColumnWidth(j,(maior*8))  
            else: 
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.setColumnCount(0)  
        except ValueError:
            pass

class cad_login(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Cad_Logins()
        self.ui.setupUi(self)             
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha)
        self.limpa()
    def closeEvent(self,event):
        n = nivel2(self)
        n.setVisible(True)
        n.ui.toolBox.setCurrentIndex(1)
        n.ui.tabWidget.setCurrentIndex(4)
        self.setVisible(False)
        event.ignore()    
    def limpa(self):
        self.ui.lineEdit.clear()
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
    def add_login(self):
        lista = []
        lista.append(self.ui.lineEdit.text())
        lista.append((self.ui.comboBox_2.currentIndex()+1))
        lista.append(self.ui.lineEdit_3.text())
        lista.append(self.ui.lineEdit_4.text())
        sql = ''' select login from logins where login = '%s' ''' % lista[2]
        verifica = select_banco_str(sql)
        if len(verifica) == 0:
            sql = ''' insert into logins (nome,nivel,login,senha) values ('%s',%d,'%s','%s') ''' % (lista[0],int(lista[1]),lista[2],
                                                                                                     lista[3])
            try:
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Login cadastrado com sucesso!")
                d.show()
                self.limpa()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Ocorreu um erro,contate administrador do programa!")
                d.show()
        else:
            d = dialog(self)
            d.ui.label.setText(u"Login igual encontrado!")
            d.show()    
    def atualiza_login(self):
        global log_id
        lista = []
        lista.append(log_id)
        lista.append(self.ui.lineEdit.text())
        lista.append((self.ui.comboBox_2.currentIndex()+1))
        lista.append(self.ui.lineEdit_3.text())
        lista.append(self.ui.lineEdit_4.text())
        login_nome = str(lista[3])
        i = 0
        while len(login_nome) < 20:
            login_nome += ' '
            i += 1
        sql = ''' select id,login from logins where login = '%s' ''' % login_nome
        verifica = select_banco_str(sql)
        prosegue = False
        if len(verifica) > 0:
            for v in verifica:
                if v[0] != int(lista[0]) and v[1] == login_nome:
                    prosegue = False
                    break
                else: prosegue = True
        else: prosegue = True            
        if prosegue == True:            
            sql = ''' update logins set nome = '%s',nivel = %d,login = '%s',senha = '%s' where id = %d ''' % (lista[1],int(lista[2]),
                                                                                                            lista[3],lista[4],int(lista[0]))  
            try:
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Alteração feita com sucesso!")
                d.show()
                self.limpa()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Não foi possível realizar a alteração desejada.!")
                d.show()
        else:
            d = dialog(self)
            d.ui.label.setText(u"Login igual encontrado!")
            d.show() 
    def fecha(self):
        self.close()

class cad_user(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Cadast_user()
        self.ui.setupUi(self)             
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha)
        self.limpa()
    def closeEvent(self,event):
        n = nivel2(self)
        n.setVisible(True)
        n.ui.toolBox.setCurrentIndex(1)
        self.setVisible(False)
        event.ignore()
    def limpa(self):
        self.ui.lineEdit.clear()
        self.ui.spinBox.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.comboBox.setCurrentIndex(0) 
    def add_user(self):
        lista = []
        lista.append(self.ui.lineEdit.text())
        lista.append(self.ui.spinBox.value())
        lista.append(self.ui.lineEdit_3.text())
        lista.append(self.ui.lineEdit_4.text())
        if self.ui.comboBox.currentIndex() == 0: tipo = 'p'
        elif self.ui.comboBox.currentIndex() == 1: tipo = 'a'
        else: tipo = 's'
        lista.append(tipo)
        sql = ''' select nome from usuarios where nome = '%s' ''' % lista[0]
        verifica = select_banco_str(sql)
        if len(verifica) == 0:
            sql = ''' insert into usuarios (nome,cod_barra,email,cpf,tipo) values ('%s',%d,'%s','%s','%s') ''' % (lista[0],lista[1],lista[2],
                                                                                                                  lista[3],lista[4])
            try:
                insert_banco(sql)
                d = dialog(self)
                d.ui.label.setText(u"Usuário cadastrado com sucesso!")
                d.show()
            except psycopg2.Error:
                d = dialog(self)
                d.ui.label.setText(u"Ocorreu um erro,contate administrador do programa!")
            self.limpa()
        else:
            d = dialog(self)
            d.ui.label.setText(u"Usuário já cadastrado com esse nome!")
            d.show()     
    def atualiza_user(self):
        global usr_id
        lista = []
        lista.append(usr_id)
        lista.append(self.ui.lineEdit.text())
        lista.append(self.ui.spinBox.value())
        lista.append(self.ui.lineEdit_3.text())
        lista.append(self.ui.lineEdit_4.text())
        if self.ui.comboBox.currentIndex() == 0: tipo = 'p'
        elif self.ui.comboBox.currentIndex() == 1: tipo = 'a'
        else: tipo = 's'
        lista.append(tipo)  
        sql = ''' update usuarios set nome = '%s',cod_barra = %d,email = '%s',cpf = '%s',tipo = '%s' where id = %d ''' % (lista[1],lista[2],
                                                                        lista[3],lista[4],lista[5],int(lista[0]))  
        try:
            insert_banco(sql)
            d = dialog(self)
            d.ui.label.setText(u"Alteração feita com sucesso!")
            d.show()
        except psycopg2.Error:
            d = dialog(self)
            d.ui.label.setText(u"Não foi possível realizar a alteração desejada.!")
            d.show()
        self.limpa()
    def fecha(self):
        self.close()
             
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = login()
    myapp.show()
    sys.exit(app.exec_())    
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
    def fecha(self):
        configs = (self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),
                   self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text())
        with open('config.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile,delimiter = ' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(configs)
        self.close()
        l = login(self)
        l.show()
                      
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
        self.ui.tableWidget.doubleClicked.connect(self.recebers)      
        self.preenche_lista()
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
    def fecha(self):
        global logs
        sql = 'update logins set ativo = False where id = %d' % logs
        insert_banco(sql)
        y = login(self)
        self.close() 
        y.setVisible(True)
    def preenche_lista(self):
        colunas = ['Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
        self.ui.tableWidget.clear()
        sql = '''select l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull'''
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
    def fecha(self):
        self.close()
        s = nivel1(self)
        s.show()    
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
        s = nivel1(self)
        s.show() 
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
        timer = QTimer(self)
        timer2 = QTimer(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha)  
        QtCore.QObject.connect(self.ui.comboBox,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas) 
        QtCore.QObject.connect(self.ui.comboBox_2,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas) 
        QtCore.QObject.connect(self.ui.comboBox_3,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
        QtCore.QObject.connect(self.ui.comboBox_4,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL('clicked()'),self.exclui_retiradas)  
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.exclui_usuarios)
        QtCore.QObject.connect(timer2,QtCore.SIGNAL("timeout()"),self.tabela_retiradas)
        QtCore.QObject.connect(timer,QtCore.SIGNAL("timeout()"),self.lista_logins)
        self.ui.lineEdit.textChanged.connect(self.preenche_usuarios)
        timer.start(5000)
        timer2.start(15000)
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
            sql = ''' select * from usuarios where upper(nome) like '%s%%' ''' % nome.upper()
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
        y = login(self)
        self.close() 
        y.setVisible(True)
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
        sql = 'select * from predios'
        pred = select_banco_str(sql)
        for p in pred:
            text = "%2d - %s" % p
            self.ui.comboBox.addItem(text.decode('utf-8'))        
    def tabela_retiradas(self):
        self.ui.tableWidget.clear()
        ano = self.ui.comboBox_4.itemText(self.ui.comboBox_4.currentIndex())
        predio = int(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())[:3])
        escolha = self.ui.comboBox_2.currentIndex()
        m = (int(self.ui.comboBox_3.currentIndex()) + 1)
        if m < 10: mes = ('0' + str(m) + '/' + str(ano))
        else: mes = (str(m) + '/' + str(ano))   
        if escolha == 0: # Todas
            sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
            order by r.datahora_rec desc''' % (predio,mes)
            colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
        elif escolha == 1: # Em Aberto
            sql =  '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
            order by r.datahora_ent desc'''   % (predio,mes)
            colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
        else: # Fechadas
            sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
            from logins l,retiradas r,salas s,usuarios u,chaves c
            where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and r.datahora_rec notnull and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
            order by r.datahora_rec desc''' % (predio,mes)
            colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
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
             
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = login()
    myapp.show()
    sys.exit(app.exec_())    

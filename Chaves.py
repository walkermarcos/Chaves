#coding=UTF-8
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QTimer
from Tela_master import Ui_Projeto_Chaves
from dialog3 import Ui_Dialog_3
from conf import Ui_Conf
from entregar import Ui_Mainentrega
from receber import Ui_receber
from cad_user import Ui_Cadast_user
from cad_login import Ui_Cad_Logins
import datetime
import sys
import glob
import psycopg2
import ConfigParser
from mhlib import isnumeric
import md5


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


def verifica_cpf(cpf):
  numeros = ''
  for c in cpf:
    if isnumeric(c) or c == '0':
      numeros += c
  if len(numeros) > 0:
    total1 = 0
    i = 10
    for n in numeros[:9]:
      total1 += (int(n) * i)
      i -= 1
    total2 = 0
    i = 11
    for n in numeros[:10]:
      total2 += (int(n) * i)
      i -= 1
    resto1 = total1 % 11
    resto2 = total2 % 11
    if resto1 < 2: dig1 = 0
    else: dig1 = 11 - resto1
    if resto2 < 2: dig2 = 0
    else: dig2 = 11 - resto2
    if (dig1 == int(numeros[9])) and (dig2 == int(numeros[10])):
      return True
    else: return False
  else: return True


class Chaves(QtGui.QMainWindow):
  def __init__(self,parent = None):
    super(Chaves,self).__init__(parent)
    self.ui = Ui_Projeto_Chaves()
    self.ui.setupUi(self)
    #self.ui.login.setVisible(False)
    self.ui.nivel1.setVisible(False)
    self.ui.nivel2.setVisible(False)
    self.login()
    self.setWindowState(QtCore.Qt.WindowMaximized)
    global fecha
    fecha = False

  def closeEvent(self,event):
    try:
      global fecha
      if fecha == False:
	texto = "Utilize o botão Sair para fechar!"
	QtGui.QMessageBox.about(self,"Alerta!",texto.decode('UTF-8'))
	event.ignore()
      else: event.accept()
    except Error as error:
      erro = "%s" % error
      QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
      event.accept()
	      # ---- Nivel2 ---- #
  def nivel2(self):
    #self.ui.nivel2.setVisible(True)
    self.setCentralWidget(self.ui.nivel2)
    self.ui.nivel2.show()
    timer = QTimer(self)
    timer2 = QTimer(self)
    QtCore.QObject.connect(self.ui.but_sair_nivel2,QtCore.SIGNAL('clicked()'),self.fecha_nivel2)
    QtCore.QObject.connect(self.ui.comboBox,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
    QtCore.QObject.connect(self.ui.comboBox_2,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
    QtCore.QObject.connect(self.ui.comboBox_3,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
    QtCore.QObject.connect(self.ui.comboBox_4,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_retiradas)
    QtCore.QObject.connect(self.ui.comboBox_5,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.preenche_sala)
    QtCore.QObject.connect(self.ui.comboBox_7,QtCore.SIGNAL("currentIndexChanged(const QString&)"),self.tabela_salas)
    QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL('clicked()'),self.exclui_retiradas)
    QtCore.QObject.connect(self.ui.but_excluser,QtCore.SIGNAL("clicked()"),self.exclui_usuarios)
    QtCore.QObject.connect(self.ui.but_novouser,QtCore.SIGNAL("clicked()"),self.add_user)
    QtCore.QObject.connect(self.ui.but_addaut,QtCore.SIGNAL("clicked()"),self.insert_autos)
    QtCore.QObject.connect(self.ui.but_excaut,QtCore.SIGNAL("clicked()"),self.exclui_autos)
    QtCore.QObject.connect(self.ui.pushButton_8,QtCore.SIGNAL("clicked()"),self.insert_sala)
    QtCore.QObject.connect(self.ui.but_excsala,QtCore.SIGNAL("clicked()"),self.exclui_sala)
    QtCore.QObject.connect(self.ui.pushButton_11,QtCore.SIGNAL("clicked()"),self.insert_copia)
    QtCore.QObject.connect(self.ui.pushButton_10,QtCore.SIGNAL("clicked()"),self.exclui_copia)
    QtCore.QObject.connect(self.ui.pushButton_12,QtCore.SIGNAL("clicked()"),self.exclui_predio)
    QtCore.QObject.connect(self.ui.pushButton_14,QtCore.SIGNAL("clicked()"),self.exclui_logins)
    QtCore.QObject.connect(self.ui.but_addpredio,QtCore.SIGNAL("clicked()"),self.add_predio)
    QtCore.QObject.connect(self.ui.but_addlogin,QtCore.SIGNAL("clicked()"),self.add_login)
    QtCore.QObject.connect(timer2,QtCore.SIGNAL("timeout()"),self.tabela_retiradas)
    QtCore.QObject.connect(timer,QtCore.SIGNAL("timeout()"),self.lista_logins)
    self.ui.filtra_nome.textChanged.connect(self.preenche_usuarios)
    self.ui.lineEdit_2.textChanged.connect(self.tabela_retiradas)
    self.ui.nome_predio.textChanged.connect(self.abilita_add)
    self.ui.lineEdit_8.textChanged.connect(self.tabela_predios)
    self.ui.filtro_login.textChanged.connect(self.tabela_logins)
    self.ui.table_user.doubleClicked.connect(self.lista_user)
    self.ui.table_login.doubleClicked.connect(self.lista_login)
    self.ui.table_sala.itemSelectionChanged.connect(self.lista_copias)
    self.ui.table_predio.itemSelectionChanged.connect(self.abilita_exlusao)
    self.ui.table_retir.itemSelectionChanged.connect(self.abilita_exlusao_ret)
    self.ui.table_user.itemSelectionChanged.connect(self.abilita_exlusao_usr)
    self.ui.listWidget_2.itemSelectionChanged.connect(self.abilita_add_aut)
    self.ui.table_autos.itemSelectionChanged.connect(self.abilita_exlusao_aut)
    self.ui.table_login.itemSelectionChanged.connect(self.abilita_exclusao_log)
    self.ui.filtra_user.textChanged.connect(self.lista_usuarios)
    self.ui.filtra_auto.textChanged.connect(self.tabela_autos)
    self.ui.filtra_sala.textChanged.connect(self.tabela_salas)
    self.ui.line_sala.textChanged.connect(self.abilita_add_sala)
    timer.start(5000)
    timer2.start(15000)
    self.preenche_ano()
    self.preenche_mes()
    self.preenche_pred()
    self.tabela_retiradas()
    self.lista_logins()
    self.preenche_usuarios()
    self.tabela_autos()
    self.tabela_salas()
    self.tabela_predios()
    self.tabela_logins()
    self.ui.but_excsala.setEnabled(False)
    self.ui.pushButton_10.setEnabled(False)
    self.ui.pushButton_11.setEnabled(False)
    self.ui.but_addpredio.setEnabled(False)
    self.ui.pushButton_12.setEnabled(False)
    self.ui.pushButton_4.setEnabled(False)
    self.ui.but_addaut.setEnabled(False)
    self.ui.but_excaut.setEnabled(False)
    self.ui.but_excluser.setEnabled(False)
    self.ui.pushButton_14.setEnabled(False)
    self.ui.pushButton_8.setEnabled(False)
  def abilita_add_sala(self):
    tamanho = len(self.ui.line_sala.text())
    if tamanho > 0: self.ui.pushButton_8.setEnabled(True)
    else: self.ui.pushButton_8.setEnabled(False)
  def abilita_exclusao_log(self):
    select = self.ui.table_login.selectedItems()
    if len(select) > 0: self.ui.pushButton_14.setEnabled(True)
    else: self.ui.pushButton_14.setEnabled(False)
  def abilita_exlusao_aut(self):
    select = self.ui.table_autos.selectedItems()
    if len(select) > 0: self.ui.but_excaut.setEnabled(True)
    else: self.ui.but_excaut.setEnabled(False)
  def abilita_add_aut(self):
    select = self.ui.listWidget_2.selectedItems()
    if len(select) > 0: self.ui.but_addaut.setEnabled(True)
    else: self.ui.but_addaut.setEnabled(False)
  def abilita_exlusao_usr(self):
    select = self.ui.table_user.selectedItems()
    if len(select) > 0: self.ui.but_excluser.setEnabled(True)
    else: self.ui.but_excluser.setEnabled(False)
  def abilita_exlusao_ret(self):
    select = self.ui.table_retir.selectedItems()
    if len(select) > 0: self.ui.pushButton_4.setEnabled(True)
    else: self.ui.pushButton_4.setEnabled(False)
  def abilita_add(self):
    if len(self.ui.nome_predio.text()) > 0: self.ui.but_addpredio.setEnabled(True)
    else: self.ui.but_addpredio.setEnabled(False)
  def abilita_exlusao(self):
    select = self.ui.table_predio.selectedItems()
    if len(select) > 0: self.ui.pushButton_12.setEnabled(True)
    else: self.ui.pushButton_12.setEnabled(False)
  def excluil(self):
    global exclog
    for e in exclog:
      try:
	sql = ''' delete from logins where id = %d ''' % int(e)
	insert_banco(sql)
	self.tabela_logins()
      except psycopg2.IntegrityError as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
  def exclui_logins(self):
    select = self.ui.table_login.selectedItems()
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
      else: exclog.append(int(items[0]))
      if len(exclog) >= 1:
	d = dialog3(self)
	d.ui.label.setText(u"A exclusão de Logins é permanente e não pode ser desfeita.")
	d.show()
	self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluil)
  def lista_login(self):
    select = self.ui.table_login.selectedItems()
    global log_id
    list_user = []
    for s in select:
      list_user.append(QtGui.QTableWidgetItem(s).text())
    log_id = list_user[0]
    sql = ''' select id,nome,nivel,login from logins where id = %d ''' % int(log_id)
    logins = select_banco_str(sql)
    nome = logins[0][1]
    nivel = logins[0][2]
    login = logins[0][3]
    #senha = str(logins[0][4])
    #senhas = ''
    #for s in senha:
    #  if s != ' ': senhas += s
    c = cad_login(self)
    c.show()
    c.limpa()
    c.ui.lineEdit.setText(str(nome).decode('utf-8'))
    c.ui.comboBox_2.setCurrentIndex((nivel - 1))
    c.ui.lineEdit_3.setText(login)
    #c.ui.lineEdit_4.setText(senhas)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.atualiza_login)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),self.tabela_logins)
    c.ui.lineEdit.setFocus()
  def add_login(self):
    c = cad_login(self)
    c.show()
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.add_login)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),self.tabela_logins)
    c.ui.lineEdit.setFocus()
  def tabela_logins(self):
    self.ui.table_login.clear()
    if self.ui.filtro_login.text() > 0:
      nome = str(self.ui.filtro_login.text())
      sql = ''' select id,nome,nivel from logins where remove_acento(upper(nome)) like '%s%%' order by nome''' % nome.upper()
    else: sql = ''' select id,nome,nivel from logins order by nome'''
    users = select_banco_str(sql)
    colunas = [' ID ','Nome','Nivel']
    if len(users) > 0:
      self.ui.table_login.setRowCount(len(users))
      self.ui.table_login.setColumnCount(len(colunas))
      for j in range(len(colunas)):
	item2 = QtGui.QTableWidgetItem(colunas[j])
	self.ui.table_login.setHorizontalHeaderItem(j,item2)
	maior = len(colunas[j])
	for i in range(len(users)):
	  texto = str(users[i][j])
	  item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	  self.ui.table_login.setItem(i,j,item)
	  if len(texto) > maior: maior = len(texto)
	self.ui.table_login.setColumnWidth(j,(maior*8))
    else:
      self.ui.table_login.clear()
      self.ui.table_login.setRowCount(0)
      self.ui.table_login.setColumnCount(0)
  def add_predio(self):
    nome = self.ui.nome_predio.text()[:40]
    sql = '''select nome from predios
	where nome = '%s' ''' % nome
    verifica = select_banco_str(sql)
    if len(verifica) > 0:
      texto = "Prédio já cadastrado com esse nome!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    else:
      sql = ''' insert into predios(nome) values('%s')''' % nome
      if len(nome) > 0:
	try:
	  insert_banco(sql)
	  texto = "Prédio cadastrado com sucesso!"
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	  self.tabela_predios()
	  self.preenche_pred()
	  self.ui.nome_predio.clear()
	except psycopg2.Error as error:
	  erro = "%s" % error
	  QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	  pass
  def exclui_predio(self):
    d = dialog3(self)
    d.ui.label.setText(u"A exclusão de prédios é permanente e não pode ser desfeita.")
    d.show()
    self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluip)
  def excluip(self):
    select = self.ui.table_predio.selectedItems()
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
	  texto = "Prédio %d excluido!" % int(e)
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	  self.tabela_predios()
	  self.preenche_pred()
	except psycopg2.IntegrityError:
	  texto = "Não foi possível excluir o prédio %s,existem salas cadastradas!" % int(e)
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	  pass
  def tabela_predios(self):
    self.ui.table_predio.clear()
    if len(self.ui.lineEdit_8.text()) > 0:
      filtro = str(self.ui.lineEdit_8.text())
      sql = ''' select id,nome from predios
	  where remove_acento(upper(nome)) like '%s%%'
	  order by nome''' % filtro.upper()
    else:
      sql = ''' select id,nome from predios
	      order by nome'''
    predios = select_banco_str(sql)
    colunas = [' ID ','Nome','Nro.Salas']
    if len(predios) > 0:
      self.ui.table_predio.setRowCount(len(predios))
      self.ui.table_predio.setColumnCount(len(colunas))
      for j in range(len(colunas)):
	item2 = QtGui.QTableWidgetItem(colunas[j])
	self.ui.table_predio.setHorizontalHeaderItem(j,item2)
	maior = len(colunas[j])
	for i in range(len(predios)):
	  sql = '''select nome from salas where predio_id = %d''' % predios[i][0]
	  salas = select_banco_str(sql)
	  nro_salas = len(salas)
	  if j == 2: texto = str(nro_salas)
	  else: texto = str(predios[i][j])
	  item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	  self.ui.table_predio.setItem(i,j,item)
	  if len(texto) > maior: maior = len(texto)
	self.ui.table_predio.setColumnWidth(j,(maior*6))
    else:
      self.ui.table_predio.clear()
      self.ui.table_predio.setRowCount(0)
      self.ui.table_predio.setColumnCount(0)
  def exclui_copia(self):
    d = dialog3(self)
    d.ui.label.setText(u"A exclusão de cópias é permanente e não pode ser desfeita.")
    d.show()
    self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluic)
  def excluic(self):
    select = self.ui.table_sala.selectedItems()
    select2 = self.ui.listWidget_3.selectedItems()
    lista = []
    lista2 = []
    if len(select2) > 0:
      for sel in select2:
	item = QtGui.QListWidgetItem(sel).text()
	lista2.append(item)
    for sel in select:
      item = QtGui.QTableWidgetItem(sel).text()
      lista.append(item)
    if len(lista) > 0:
      if len(lista2) > 0: sql = ''' delete from chaves where id = %d ''' % int(lista2[0][:3])
      else:
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
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
  def insert_copia(self):
    select = self.ui.table_sala.selectedItems()
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
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
  def lista_copias(self):
    self.ui.but_excsala.setEnabled(True)
    self.ui.pushButton_11.setEnabled(True)
    self.ui.listWidget_3.clear()
    select = self.ui.table_sala.selectedItems()
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
	self.ui.filtra_user.clear()
  def exclui_sala(self):
    d = dialog3(self)
    d.ui.label.setText(u"A exclusão de salas é permanente e não pode ser desfeita.")
    d.show()
    self.connect(d.ui.pushButton,QtCore.SIGNAL('clicked()'),self.excluis)
  def excluis(self):
    select = self.ui.table_sala.selectedItems()
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
	texto = "Sala %d Excluida!" % sala
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	self.tabela_salas()
	self.tabela_predios()
	self.preenche_sala()
      except psycopg2.IntegrityError:
	texto = "Não foi possível excluir a sala,existem cópias para ela!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	pass
  def tabela_salas(self):
    self.ui.table_sala.clear()
    predio = self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex())[:3]
    try:
      if len(self.ui.filtra_sala.text()) > 0:
        filtro = str(self.ui.filtra_sala.text())
        sql = ''' select id,nome,direito,horario_min,horario_max from salas
        where upper(nome) like '%s%%' and predio_id = %d
        order by nome ''' % (filtro.upper(),int(predio))
      else:
        sql = ''' select id,nome,direito,horario_min,horario_max from salas
		where predio_id = %d
		order by nome ''' % int(predio)

      salas = select_banco_str(sql)
      colunas = [' ID ','Nome','Direito',u'Horário']
      if len(salas) > 0:
	self.ui.table_sala.setRowCount(len(salas))
	self.ui.table_sala.setColumnCount(len(colunas))
	for j in range(len(colunas)):
	  item2 = QtGui.QTableWidgetItem(colunas[j])
	  self.ui.table_sala.setHorizontalHeaderItem(j,item2)
	  maior = len(colunas[j])
	  for i in range(len(salas)):
	    if j == 3:
	      texto = '%s -- %s' % (salas[i][j],salas[i][j+1])
	    else:
	      if salas[i][j] == 'p': texto = 'Todos Professores'
	      elif salas[i][j] == 'a': texto = 'Todos Alunos'
	      elif salas[i][j] == None: texto = ''
	      else: texto = str(salas[i][j])
	    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	    self.ui.table_sala.setItem(i,j,item)
	    if len(texto) > maior: maior = len(texto)
	  self.ui.table_sala.setColumnWidth(i,(maior*6))
      else:
	self.ui.table_sala.clear()
	self.ui.table_sala.setRowCount(0)
	self.ui.table_sala.setColumnCount(0)
    except ValueError:
      pass
  def insert_sala(self):
    nome = self.ui.line_sala.text()[:10]
    predio = self.ui.comboBox_7.itemText(self.ui.comboBox_7.currentIndex())[:3]
    horario_max = str(self.ui.lineEdit_4.text())
    horario_min = str(self.ui.lineEdit_3.text())
    if self.ui.comboBox_8.currentIndex() == 2: direito = 'a'
    elif self.ui.comboBox_8.currentIndex() == 1: direito = 'p'
    else: direito = ''
    sql = ''' select nome from salas
	    where upper(nome) = '%s' and predio_id = %d ''' % (str(nome).upper(),int(predio))
    verifica = select_banco_str(sql)
    if len(verifica) > 0:
      texto = "Sala %s já cadastrada" % verifica[0][0]
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    else:
      sql = ''' insert into salas(nome,predio_id,direito,horario_min,horario_max) values('%s',%d,'%s','%s','%s')''' % (str(nome).upper(),int(predio),str(direito),horario_min,horario_max)
      try:
	insert_banco(sql)
	texto = "Sala Cadastrada com sucesso!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	self.tabela_salas()
	self.ui.line_sala.clear()
	self.ui.lineEdit_4.clear()
	self.ui.lineEdit_3.clear()
	self.ui.line_sala.setFocus()
	self.ui.comboBox_8.setCurrentIndex(0)
	self.tabela_predios()
	self.preenche_sala()
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
  def exclui_autos(self):
    select = self.ui.table_autos.selectedItems()
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
	texto = "Autorização %d excluida!" % e
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	self.tabela_autos()
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
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
	  texto = "Autorização já existente para usuário %d!" % int(li)
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	else:
	  sql = ''' insert into autos(sala_id,usuario_id,login_id) values(%d,%d,%d) ''' % (int(sala),int(li),int(login))
	  try:
	    insert_banco(sql)
	    texto = "Autorização realizada com sucesso para usuário %d!" % int(li)
	    QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	  except psycopg2.Error as error:
	    erro = "%s" % error
	    QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	    pass
      self.tabela_autos()
  def tabela_autos(self):
    self.ui.table_autos.clear()
    if len(self.ui.filtra_auto.text()) > 0:
      filtro = str(self.ui.filtra_auto.text())
      sql = ''' select a.id,s.nome,u.nome,l.nome
      from autos a,salas s,usuarios u,logins l
      where a.sala_id = s.id and a.usuario_id = u.id and a.login_id = l.id and (remove_acento(upper(u.nome)) like '%s%%' or upper(s.nome) like '%s%%')
      order by s.nome ''' % (filtro.upper(),filtro.upper())
    else:
      sql = ''' select a.id,s.nome,u.nome,l.nome
	      from autos a,salas s,usuarios u,logins l
	      where a.sala_id = s.id and a.usuario_id = u.id and a.login_id = l.id
	      order by s.nome '''
    autos = select_banco_str(sql)
    colunas = [' ID ','Sala',u'Usuário','Login']
    if len(autos) > 0:
      self.ui.table_autos.setRowCount(len(autos))
      self.ui.table_autos.setColumnCount(len(colunas))
      for j in range(len(colunas)):
	item2 = QtGui.QTableWidgetItem(colunas[j])
	self.ui.table_autos.setHorizontalHeaderItem(j,item2)
	maior = len(colunas[j])
	for i in range(len(autos)):
	  texto = str(autos[i][j])
	  item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	  self.ui.table_autos.setItem(i,j,item)
	  if len(texto) > maior: maior = len(texto)
	self.ui.table_autos.setColumnWidth(j,(maior*6))
    else:
      self.ui.table_autos.clear()
      self.ui.table_autos.setRowCount(0)
      self.ui.table_autos.setColumnCount(0)
  def lista_usuarios(self):
    self.ui.listWidget_2.clear()
    if len(self.ui.filtra_user.text()) > 0:
      nome = u"%s" % str(self.ui.filtra_user.text())
      sql = ''' select id,nome from usuarios where remove_acento(upper(nome)) like '%s%%'
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
    c.show()
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.add_user)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),self.preenche_usuarios)
    c.ui.lineEdit.setFocus()
  def lista_user(self):
    select = self.ui.table_user.selectedItems()
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
    c.show()
    c.limpa()
    c.ui.lineEdit.setText(nome)
    c.ui.spinBox.setValue(int(cod))
    c.ui.lineEdit_3.setText(eml)
    c.ui.lineEdit_4.setText(cpf)
    if tipo[:1] == 'P': c.ui.comboBox.setCurrentIndex(0)
    elif tipo[:1] == 'A' : c.ui.comboBox.setCurrentIndex(1)
    else: c.ui.comboBox.setCurrentIndex(2)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),c.atualiza_user)
    self.connect(c.ui.pushButton,QtCore.SIGNAL('clicked()'),self.preenche_usuarios)
    c.ui.lineEdit.setFocus()
  def exclui_retiradas(self):
    global exc
    select = self.ui.table_retir.selectedItems()
    items = []
    if len(select) > 0:
      for sel in select:
	items.append(QtGui.QTableWidgetItem(sel).text())
	exc = []
	i = 0
      if self.ui.comboBox_2.currentIndex() == 0 or self.ui.comboBox_2.currentIndex() == 2: num = 7
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
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
  def excluiu(self):
    global excu
    for e in excu:
      try:
	sql = ''' delete from usuarios where id = %d ''' % e
	insert_banco(sql)
	self.tabela_retiradas()
	self.lista_usuarios()
      except psycopg2.IntegrityError:
	texto = "Não foi possivel excluir usuário %d,existem retiradas ou autorizações para o mesmo!" % e
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	pass
    self.preenche_usuarios()
  def exclui_usuarios(self):
    select = self.ui.table_user.selectedItems()
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
    self.lista_usuarios()
    self.ui.table_user.clear()
    if self.ui.filtra_nome.text() > 0:
      nome = str(self.ui.filtra_nome.text())
      sql = ''' select * from usuarios where remove_acento(upper(nome)) like '%s%%' order by nome''' % nome.upper()
    else:
      sql = ''' select * from usuarios'''
    users = select_banco_str(sql)
    colunas = [' ID ','Nome','Cod.Barras','Email','Cpf','Tipo']
    if len(users) > 0:
      self.ui.table_user.setRowCount(len(users))
      self.ui.table_user.setColumnCount(len(colunas))
      for j in range(len(colunas)):
	item2 = QtGui.QTableWidgetItem(colunas[j])
	self.ui.table_user.setHorizontalHeaderItem(j,item2)
	maior = len(colunas[j])
	for i in range(len(users)):
	  if j == 5:
	    if str(users[i][j]) == 'p': texto = 'Professor'
	    elif str(users[i][j]) == 'a': texto = 'Aluno'
	    else: texto = 'Servidor'
	  else: texto = str(users[i][j])
	  item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	  self.ui.table_user.setItem(i,j,item)
	  if len(texto) > maior: maior = len(texto)
	self.ui.table_user.setColumnWidth(j,(maior*8))
    else:
      self.ui.table_user.clear()
      self.ui.table_user.setRowCount(0)
      self.ui.table_user.setColumnCount(0)
  def fecha_nivel2(self):
    global fecha
    fecha = True
    QtGui.QMessageBox.about(self,'Alerta!','O programa sera fechado!')
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
      self.ui.table_retir.clear()
      if len(self.ui.lineEdit_2.text()) > 0: filtro = str(self.ui.lineEdit_2.text())
      else: filtro = ''
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
	colunas = ['ID','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
	if len(filtro) > 0:
	    sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
	from logins l,retiradas r,salas s,usuarios u,chaves c
	where (remove_acento(upper(u.nome)) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
	order by r.datahora_rec desc''' % (filtro.upper(),filtro.upper(),predio,mes)
      elif escolha == 1: # Em Aberto
	sql =  '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
	from logins l,retiradas r,salas s,usuarios u,chaves c
	where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
	order by r.datahora_ent desc'''   % (predio,mes)
	colunas = ['ID','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
	if len(filtro) > 0:
	  sql =  '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
	from logins l,retiradas r,salas s,usuarios u,chaves c
	where (remove_acento(upper(u.nome)) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull and s.predio_id = %d and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
	order by r.datahora_ent desc'''   % (filtro.upper(),filtro.upper(),predio,mes)
      else: # Fechadas
	sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
	from logins l,retiradas r,salas s,usuarios u,chaves c
	where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and r.datahora_rec notnull and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
	order by r.datahora_rec desc''' % (predio,mes)
	colunas = ['ID','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega','Data/Hora Recebimento']
	if len(filtro) > 0:
	  sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),to_char(r.datahora_rec, 'DD/MM/YYYY hh24:mi')
	from logins l,retiradas r,salas s,usuarios u,chaves c
	where (remove_acento(upper(u.nome)) like '%s%%' or upper(s.nome) like '%s%%') and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and s.predio_id = %d and r.datahora_rec notnull and to_char(r.datahora_ent, 'MM/YYYY') = '%s'
	order by r.datahora_rec desc''' % (filtro.upper(),filtro.upper(),predio,mes)
      ret = select_banco_str(sql)
      if len(ret) > 0:
	self.ui.table_retir.setRowCount(len(ret))
	self.ui.table_retir.setColumnCount(len(colunas))
	for j in range(len(colunas)):
	  item2 = QtGui.QTableWidgetItem(colunas[j])
	  self.ui.table_retir.setHorizontalHeaderItem(j,item2)
	  maior = len(colunas[j])
	  for i in range(len(ret)):
	    texto = str(ret[i][j])
	    item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	    self.ui.table_retir.setItem(i,j,item)
	    if len(texto) > maior: maior = len(texto)
	  self.ui.table_retir.setColumnWidth(i,(maior * 4))
      else:
	self.ui.table_retir.clear()
	self.ui.table_retir.setRowCount(0)
	self.ui.table_retir.setColumnCount(0)
    except ValueError:
      pass
	      # ---- /Nivel2 ---- #
	      # ---- Nivel1 ---- #
  def nivel1(self):
    #self.ui.nivel1.setVisible(True)
    self.setCentralWidget(self.ui.nivel1)
    self.ui.nivel1.show()
    QtCore.QObject.connect(self.ui.but_sair_2,QtCore.SIGNAL('clicked()'),self.fecha_nivel1)
    QtCore.QObject.connect(self.ui.but_entr,QtCore.SIGNAL('clicked()'),self.entrega)
    QtCore.QObject.connect(self.ui.but_rec,QtCore.SIGNAL('clicked()'),self.receberc)
    self.ui.tableWidget.doubleClicked.connect(self.recebers)
    self.preenche_lista()
    self.ui.lineEdit.textChanged.connect(self.preenche_lista)
  def recebers(self):
    select = self.ui.tableWidget.selectedItems()
    items = []
    for sel in select:
      items.append(QtGui.QTableWidgetItem(sel).text())
    retir_id = items[0]
    r = receber(self)
    r.show()
    r.ui.combo_chav.clear()
    sql = '''select r.id,u.nome,s.nome,c.nro_copia,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi'),s.predio_id,p.nome
    from logins l,retiradas r,salas s,usuarios u,chaves c,predios p
    where r.id = %d and l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and r.usuario_id = u.id and s.predio_id = p.id''' % (int(retir_id))
    ret = select_banco_str(sql)
    r.ui.combo_pred.clear()
    texto = "%2d - %s" % (ret[0][5],ret[0][6])
    r.ui.combo_pred.addItem(texto)
    texto = "%3d - %s - %s - Cópia %d - %s" % (ret[0][0],ret[0][1],ret[0][2],ret[0][3],ret[0][4])
    r.ui.combo_chav.addItem(texto.decode('utf-8'))
    r.ui.lineEdit.setText('%s' % ret[0][2][:4])
    r.ui.but_canc.clicked.connect(self.preenche_lista)
  def receberc(self):
    r = receber(self)
    r.show()
    r.ui.but_canc.clicked.connect(self.preenche_lista)
  def entrega(self):
    e = entregar(self)
    e.show()
    e.ui.but_ent.clicked.connect(self.preenche_lista)
  def fecha_nivel1(self):
    global logs
    global fecha
    try:
      sql = ''' update logins set ativo = False where id = %d ''' % logs
      insert_banco(sql)
      fecha = True
      QtGui.QMessageBox.about(self,'Alerta!','O programa sera fechado!')
      self.close()
    except psycopg2.Error as error:
      erro = "%s" % error
      QtGui.QMessageBox.about(self,"Alerta!",erro.decode("UTF-8"))
  def preenche_lista(self):
    colunas = [' ID ','Login','Sala',u'Cópia',u'Usuário','Data/Hora Entrega']
    self.ui.tableWidget.clear()
    if (self.ui.lineEdit.text()) == 0:
      sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
      from logins l,retiradas r,salas s,usuarios u,chaves c
      where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull'''
    else :
      filtro = str(self.ui.lineEdit.text())
      sql = '''select r.id,l.nome,s.nome,c.nro_copia,u.nome,to_char(r.datahora_ent, 'DD/MM/YYYY hh24:mi')
      from logins l,retiradas r,salas s,usuarios u,chaves c
      where l.id = r.login_id and c.id = r.chave_id and c.sala_id = s.id and u.id = usuario_id and r.datahora_rec isnull
      and (remove_acento(upper(u.nome)) like '%s%%' or upper(s.nome) like '%s%%')''' % (filtro.upper(),filtro.upper())
    ret = select_banco_str(sql)
    self.ui.tableWidget.setRowCount(len(ret))
    self.ui.tableWidget.setColumnCount(len(colunas))
    for j in range(len(colunas)):
      item2 = QtGui.QTableWidgetItem(colunas[j])
      self.ui.tableWidget.setHorizontalHeaderItem(j,item2)
      for i in range(len(ret)):
	texto = str(ret[i][j])
	item = QtGui.QTableWidgetItem(texto.decode('utf-8'))
	self.ui.tableWidget.setItem(i,j,item)
				  # ---- /Nivel1 ---- #
				  # ---- Login ---- #
  def login(self):
    #self.ui.login.setVisible(True)
    self.confere_dados()
    self.limpa_login()
    QtCore.QObject.connect(self.ui.but_sair,QtCore.SIGNAL('clicked()'),self.fecha)
    QtCore.QObject.connect(self.ui.but_ok,QtCore.SIGNAL('clicked()'),self.entra)
    QtCore.QObject.connect(self.ui.edit_senha,QtCore.SIGNAL('returnPressed()'),self.entra)
    QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.conf)
    self.ui.edit_nome.setFocus()
    self.ui.login.setGeometry(160,60,323,379)
  def confere_dados(self):
    global hot
    global dat
    global ussr
    global paswd
    hot = ''
    dat = ''
    ussr = ''
    paswd = ''
    confirma = glob.glob('config.ini')
    if len(confirma) > 0:
      config = ConfigParser.RawConfigParser()
      config.read('config.ini')
      hot = config.get('Section1','hot')
      dat = config.get('Section1','dat')
      ussr = config.get('Section1','ussr')
      paswd = config.get('Section1','paswd')
    if len(hot) == 0: self.ui.but_ok.setEnabled(False)
    else: self.ui.but_ok.setEnabled(True)
  def limpa_login(self):
    self.ui.edit_nome.clear()
    self.ui.edit_senha.clear()
  def conf(self):
    c = conf(self)
    c.show()
    c.ui.pushButton.clicked.connect(self.confere_dados)
  def fecha(self):
    global fecha
    fecha = True
    self.close()
  def entra(self):
    global logs
    nome = self.ui.edit_nome.text()
    senha = md5.new(str(self.ui.edit_senha.text())).hexdigest()
    while len(nome) < 20:
      nome += " "
    #while len(senha) < 20:
    #  senha += " "
    sql = '''select l.nivel,l.id
	      from logins l
	      where l.login = '%s' and senha = '%s' ''' % (str(nome),senha)
    try:
      log = select_banco_str(sql)
      if len(log) > 0:
	logs = int(log[0][1])
	if log[0][0] == 1: # Nivel 1
	  sql = 'update logins set ativo = True where id = %d' % logs
	  insert_banco(sql)
	  self.nivel1()
	  #self.ui.login.setVisible(False)
	elif log[0][0] == 2: # Nivel 2
	  self.nivel2()
	  #self.ui.login.setVisible(False)
      else:
	texto = "Usuário e/ou senha inválidos!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    except psycopg2.Error as error:
      erro = "%s" % error
      QtGui.QMessageBox.about(self,"Problema","%s" % erro.decode("UTF-8"))
      pass
			      # ---- /Login ---- #
class conf(QtGui.QDialog):
  def __init__(self,parent = None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Conf()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.grava_dados)
    confirma = glob.glob('config.ini')
    if len(confirma) > 0:
      hot = ''
      dat = ''
      ussr = ''
      paswd = ''
      config = ConfigParser.RawConfigParser()
      config.read('config.ini')
      hot = config.get('Section1','hot')
      dat = config.get('Section1','dat')
      ussr = config.get('Section1','ussr')
      paswd = config.get('Section1','paswd')
      self.ui.lineEdit.setText(hot)
      self.ui.lineEdit_2.setText(dat)
      self.ui.lineEdit_3.setText(ussr)
      self.ui.lineEdit_4.setText(paswd)
  def closeEvent(self,event):
    self.grava_dados()
    event.accept()
  def grava_dados(self):
    config = ConfigParser.RawConfigParser()
    config.add_section('Section1')
    hot = str(self.ui.lineEdit.text())
    dat = str(self.ui.lineEdit_2.text())
    ussr = str(self.ui.lineEdit_3.text())
    paswd = str(self.ui.lineEdit_4.text())
    config.set('Section1','hot',hot)
    config.set('Section1','dat',dat)
    config.set('Section1','ussr',ussr)
    config.set('Section1','paswd',paswd)
    with open('config.ini', 'wb') as configfile:
      config.write(configfile)
      self.fecha_conf()
  def fecha_conf(self):
    self.close()

class dialog3(QtGui.QDialog):
  def __init__(self,parent = None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_Dialog_3()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha)
    QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.fecha)
  def fecha(self):
    self.close()

class receber(QtGui.QMainWindow):
  def __init__(self,parent = None):
    QtGui.QMainWindow.__init__(self, parent)
    self.ui = Ui_receber()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.but_canc,QtCore.SIGNAL('clicked()'),self.fecha)
    QtCore.QObject.connect(self.ui.but_rec,QtCore.SIGNAL('clicked()'),self.recebe_chaves)
    self.preenche_pred()
  def recebe_chaves(self):
    try:
      retir_id = int(self.ui.combo_chav.itemText(self.ui.combo_chav.currentIndex())[:4])
      sql = 'update retiradas set datahora_rec = now() where id = %d' % retir_id
      insert_banco(sql)
      self.preenche_combo()
      texto = "Chave recebida com sucesso!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    except ValueError as error:
      erro = "%s" % error
      QtGui.QMessageBox.about(self,"Alerta!",erro.decode('UTF-8'))
  def preenche_pred(self):
    self.ui.combo_pred.clear()
    sql = 'select * from predios'
    pred = select_banco_str(sql)
    for p in pred:
      text = "%2d - %s" % p
      self.ui.combo_pred.addItem(text.decode('utf-8'))
      QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL('returnPressed()'),self.preenche_combo)
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

class entregar(QtGui.QMainWindow):
  def __init__(self,parent = None):
    QtGui.QMainWindow.__init__(self, parent)
    self.ui = Ui_Mainentrega()
    self.ui.setupUi(self)
    self.ui.lista.setVisible(False)
    self.preenche_pred()
    self.ui.lineEdit.setFocus()
    QtCore.QObject.connect(self.ui.but_canc,QtCore.SIGNAL('clicked()'),self.fecha)
    QtCore.QObject.connect(self.ui.but_proc,QtCore.SIGNAL('clicked()'),self.procura_usr)
    QtCore.QObject.connect(self.ui.but_ent,QtCore.SIGNAL('clicked()'),self.ent_valores)
    QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL('returnPressed()'),self.procura_usr)
  def fecha(self):
    self.close()
  def ent_valores(self):
    date = datetime.datetime.now()
    hora = date.hour
    minuto = date.minute

    try:
      chave_id = self.ui.combo_sal.itemText(self.ui.combo_sal.currentIndex())[:3]
      sql = 'select chave_id from retiradas where datahora_rec isnull and chave_id = %d' % int(chave_id)
      testa = select_banco_str(sql)
      sql = 'select sala_id from chaves where id = %d' % int(chave_id)
      sala_id = select_banco_str(sql)
      sql = 'select horario_min,horario_max from salas where id = %d' % int(sala_id[0][0])
      verifica_horario = select_banco_str(sql)
      hora1 = ''
      hora2 = ''
      hora_min = str(verifica_horario[0][0])
      hora_max = str(verifica_horario[0][1])
      i = 0
      while i < len(hora_min):
        a = hora_min[i]
        if isnumeric(a):
          hora1 += str(a)
        i += 1
      i = 0
      while i < len(hora_max):
        a = hora_max[i]
        if isnumeric(a):
          hora2 += str(a)
        i += 1
      if (len(hora1) > 0) and (len(hora2) > 0):
	minimo = 0
	maximo = 0
	if (int(verifica_horario[0][0][:2]) == hora) and (int(verifica_horario[0][0][3:]) <= minuto):
	  minimo = 1
	elif (int(verifica_horario[0][0][:2]) < hora):
	  minimo = 1
	else: minimo = 0
	if(int(verifica_horario[0][1][:2]) == int(hora)) and (int(verifica_horario[0][1][3:]) >= int(minuto)):
	   maximo = 1
	elif (int(verifica_horario[0][1][:2]) > int(hora)):
	  maximo = 1
	else: maximo = 0
      else:
	maximo = 1
	minimo = 1
      if len(testa) > 0:
	texto = "Chave em aberto!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
      elif (maximo == 0) or (minimo == 0):
	texto = "Sala com restrição de horário,a chave não pode ser entregue."
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
      else:
	global logs
	usr_id = self.ui.lineEdit.text()[:3]
	sql = 'insert into retiradas(login_id,chave_id,usuario_id,datahora_ent) values(%d,%d,%d,now())' % (int(logs),
											      int(chave_id),int(usr_id))
	insert_banco(sql)
	self.fecha()
    except ValueError:
      QtGui.QMessageBox.about(self,"Alerta!","Aconteceu um erro!")
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
    usr_cpf = 'poipoipoipo'
    cpf = ''
    user = '%s' % self.ui.lineEdit.text()
    for a in user[:3]:
      if isnumeric(a):
	usr_cpf = ''
	break
    for i in range(0,len(user)):
      if isnumeric(user[i]) or user[i] == '0':
	usr_cpf += str(user[i])
    cpf = usr_cpf[:3] + '.' + usr_cpf[3:6] + '.' + usr_cpf[6:9] + '-' + usr_cpf[9:] + ' '
    if len(user) > 0:
      sql = '''select u.id,u.nome,u.tipo
                from usuarios u
                where (remove_acento(upper(u.nome)) like '%s%%' or upper(nome) like '%s%%')  or u.cpf = '%s' ''' % (user.upper(),
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
	else:
	  sql = '''select c.id,s.nome,c.nro_copia
                from chaves c,salas s,autos a
                where a.usuario_id = %d and a.sala_id = s.id and c.sala_id = s.id and s.predio_id = %d ''' % (usr[0][0],int(predio_id))
        chv = select_banco_str(sql)
        for c in chv:
	  text = "%2d - %s - Cópia %d" % c
          self.ui.combo_sal.addItem(text.decode('utf-8'))
          QtCore.QObject.connect(self.ui.combo_pred,QtCore.SIGNAL('currentIndexChanged(const QString&)'),self.limpa)
      elif len(usr) > 1:
        self.ui.listWidget.clear()
        for u in usr:
	  un = u[1].decode('utf-8')
          item = QtGui.QListWidgetItem(un)
          self.ui.listWidget.addItem(item)
          self.ui.listWidget.setCurrentRow(0)
        self.ui.lista.setVisible(True)
        self.ui.pushButton.clicked.connect(self.lista_users)
        self.ui.pushButton_2.clicked.connect(self.canc_lista)
      else:
        texto = "Usuário nao encontrado!"
        QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    else:
      texto = "Precisa digitar algo!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
  def canc_lista(self):
    self.ui.lista.setVisible(False)
  def lista_users(self):
    item = self.ui.listWidget.selectedItems()
    usr_select = ''
    for i in item:
      usr_select += i.text()
    mandanome = ''
    i = 0
    for i in range(len(usr_select)):
      if (usr_select[i] == ' ' and usr_select[i+1] != ' ') or usr_select[i] != ' ':
	mandanome += usr_select[i]
      else :
	break
    self.ui.lineEdit.clear()
    self.ui.lineEdit.setText(mandanome)
    self.ui.lista.setVisible(False)
    self.procura_usr()
  def limpa(self):
    self.ui.lineEdit.clear()
    self.ui.combo_sal.clear()

class cad_login(QtGui.QMainWindow):
  def __init__(self,parent = None):
    QtGui.QMainWindow.__init__(self, parent)
    self.ui = Ui_Cad_Logins()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha_cadlogin)
    self.limpa()
  def limpa(self):
    self.ui.lineEdit.clear()
    self.ui.comboBox_2.setCurrentIndex(0)
    self.ui.lineEdit_3.clear()
    self.ui.lineEdit_4.clear()
  def add_login(self):
    lista = []
    lista.append(self.ui.lineEdit.text()[:40])
    lista.append((self.ui.comboBox_2.currentIndex()+1))
    lista.append(self.ui.lineEdit_3.text()[:20])
    lista.append(md5.new(str(self.ui.lineEdit_4.text()[:20])).hexdigest())
    sql = ''' select login from logins where login = '%s' ''' % lista[2]
    verifica = select_banco_str(sql)
    if len(verifica) == 0:
      sql = ''' insert into logins (nome,nivel,login,senha) values ('%s',%d,'%s','%s') ''' % (lista[0],int(lista[1]),lista[2],
												lista[3])
      try:
	insert_banco(sql)
	texto = "Login cadastrado com sucesso!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	self.fecha_cadlogin()
      except psycopg2.Error:
	texto = "Ocorreu um erro,contate administrador do programa!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	pass
    else:
      texto = "Login igual encontrado!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
  def atualiza_login(self):
    global log_id
    lista = []
    lista.append(log_id)
    lista.append(self.ui.lineEdit.text()[:40])
    lista.append((self.ui.comboBox_2.currentIndex()+1))
    lista.append(self.ui.lineEdit_3.text()[:20])
    nova_senha = str(self.ui.lineEdit_4.text()[:20])
    if (len(nova_senha) > 0):
      lista.append(md5.new(nova_senha).hexdigest())
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
      if len(lista) > 4:
        sql = ''' update logins set nome = '%s',nivel = %d,login = '%s',senha = '%s' where id = %d ''' % (lista[1],int(lista[2]),
												      lista[3],lista[4],int(lista[0]))
      else:
        sql = '''update logins set nome = '%s',nivel = %d,login = '%s' where id = %d ''' % (lista[1],int(lista[2]),lista[3],int(lista[0]))
      try:
	insert_banco(sql)
	texto = "Alteração feita com sucesso!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	self.fecha_cadlogin()
      except psycopg2.Error as error:
	#texto = "Não foi possível realizar a alteração desejada.!"
	texto = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	pass
    else:
      texto = "Login igual encontrado!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
  def fecha_cadlogin(self):
    self.close()

class cad_user(QtGui.QMainWindow):
  def __init__(self,parent = None):
    QtGui.QMainWindow.__init__(self, parent)
    self.ui = Ui_Cadast_user()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.fecha_caduser)
    self.limpa()
  def limpa(self):
    self.ui.lineEdit.clear()
    self.ui.spinBox.clear()
    self.ui.lineEdit_3.clear()
    self.ui.lineEdit_4.clear()
    self.ui.comboBox.setCurrentIndex(0)
  def add_user(self):
    lista = []
    lista.append(self.ui.lineEdit.text()[:40])
    lista.append(self.ui.spinBox.value())
    lista.append(self.ui.lineEdit_3.text()[:60])
    lista.append(self.ui.lineEdit_4.text()[:15])
    if self.ui.comboBox.currentIndex() == 0: tipo = 'p'
    elif self.ui.comboBox.currentIndex() == 1: tipo = 'a'
    else: tipo = 's'
    lista.append(tipo)
    sql = ''' select nome from usuarios where nome = '%s' ''' % lista[0]
    verifica = select_banco_str(sql)
    verifica_c = verifica_cpf(lista[3])
    if len(verifica) == 0:
      if verifica_c == True:
	sql = ''' insert into usuarios (nome,cod_barra,email,cpf,tipo) values ('%s',%d,'%s','%s','%s') ''' % (lista[0],lista[1],lista[2],
													      lista[3],lista[4])
	try:
	  insert_banco(sql)
	  texto = "Usuário cadastrado com sucesso!"
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	except psycopg2.Error:
	  texto = "Ocorreu um erro,contate administrador do programa!"
	  QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
	  pass
	self.limpa()
      else:
	texto = "CPF inválido!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
    else:
      texto = "Usuário já cadastrado com esse nome!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
  def atualiza_user(self):
    global usr_id
    lista = []
    lista.append(usr_id)
    lista.append(self.ui.lineEdit.text()[:40])
    lista.append(self.ui.spinBox.value())
    lista.append(self.ui.lineEdit_3.text()[:60])
    lista.append(self.ui.lineEdit_4.text()[:15])
    if self.ui.comboBox.currentIndex() == 0: tipo = 'p'
    elif self.ui.comboBox.currentIndex() == 1: tipo = 'a'
    else: tipo = 's'
    lista.append(tipo)
    verifica_c = verifica_cpf(lista[4])
    if verifica_c == True:
      sql = ''' update usuarios set nome = '%s',cod_barra = %d,email = '%s',cpf = '%s',tipo = '%s' where id = %d ''' % (lista[1],lista[2],
								      lista[3],lista[4],lista[5],int(lista[0]))
      try:
	insert_banco(sql)
	texto = "Alteração feita com sucesso!"
	QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
      except psycopg2.Error as error:
	erro = "%s" % error
	QtGui.QMessageBox.about(self,'Alerta!',erro.decode("UTF-8"))
	pass
      self.limpa()
    else:
      texto = "CPF inválido!"
      QtGui.QMessageBox.about(self,'Alerta!',texto.decode('UTF-8'))
  def fecha_caduser(self):
    self.close()

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = Chaves()
  myapp.show()
  sys.exit(app.exec_())
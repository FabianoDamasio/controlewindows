from PyQt5 import uic,QtWidgets,QtGui
import os
import subprocess

def comando(cmd):
	os.system(cmd)

def cancelar():
	cmd = 'shutdown /a '
	comando(cmd)
	wincan.close()
	win1.show()


def desligar():
	if windes1.lineEdit == '' or windes1.lineEdit_2 == '':
		print ('alo')
	else:
		H = windes1.lineEdit.text()
		M = windes1.lineEdit_2.text()
		horasr = (int(H) * 3600)
		minr = (int(M) * 60)
		tempor = (horasr + minr)
		t = str(tempor)
		cmd = 'shutdown /s /t ' + (t)
		comando(cmd)
		windes1.close()
		wincan.show()



def reiniciar():
	if winres1.lineEdit == '' or winres1.lineEdit_2 == '':
		print ('alo')
	else:
		H = winres1.lineEdit.text()
		M = winres1.lineEdit_2.text()
		horasr = (int(H) * 3600)
		minr = (int(M) * 60)
		tempor = (horasr + minr)
		t = str(tempor)
		cmd = 'shutdown /r /t ' + (t)
		comando(cmd)
		winres1.close()
		wincan.show()



def janela_reiniciar():
	win1.close()
	winres1.show()

def janela_desligar():
	win1.close()
	windes1.show()

def fechar_janelas():
	win1.close()

def voltar1():
	win1.show()
	windes1.close()

def voltar2():
	win1.show()
	winres1.close()


app = QtWidgets.QApplication([])
win1 = uic.loadUi('win1.ui')
windes1 = uic.loadUi('windes.ui')
winres1 = uic.loadUi('winres.ui')
wincan = uic.loadUi('wincan.ui')
win1.show()
win1.pushButton_3.clicked.connect(fechar_janelas)
win1.pushButton.clicked.connect(janela_desligar)
win1.pushButton_2.clicked.connect(janela_reiniciar)
windes1.pushButton_3.clicked.connect(voltar1)
windes1.pushButton.clicked.connect(desligar)
winres1.pushButton.clicked.connect(reiniciar)
winres1.pushButton_3.clicked.connect(voltar2)
wincan.pushButton_3.clicked.connect(cancelar)


app.exec()

'''subprocess.call('comando')'''
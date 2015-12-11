# -*- mode: python -*-
a = Analysis(['chaves.py'],
             pathex=['PyQt4.QtCore,PyQt4.QtGui,SIP', '/home/marcos/workspace/Chaves'],
             hiddenimports=['login.py','nivel1.py','nivel2.py','entregar.py','receber.py','conf.py','dialog.py','dialog2.py','dialog3.py','cad_user.py','cad_login.py','logo_rc.py'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='chaves',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='chaves')

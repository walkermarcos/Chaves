from cx_Freeze import setup, Executable
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QTimer
import datetime
import sys
import glob
import psycopg2
import ConfigParser
from mhlib import isnumeric


# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['PyQt4.QtGui', 'PyQt4.QtCore',
     'PyQt4.Qt',
    'datetime', 'sys', 'glob', 'psycopg2',
    'ConfigParser', 'mhlib'], excludes = [])



setup(  name = "Projeto Chaves",
        version = "0.1",
        description = "Software simples para gerenciamento de chaves.",
        options = {"build_exe": buildOptions},
        executables = [Executable("Chaves.py")])
#-*- coding : utf-8 -*-

"""This module provides Contacts application."""

import sys
import os
from PyQt5.QtWidgets import QApplication


from .views import Window

def main():
    """Contacts main function"""
    #Create the application
    app = QApplication(sys.argv)
    #Create the main window
    win = Window()
    win.show()
    #Run the event loop
    sys.exit(app.exec())
    
    

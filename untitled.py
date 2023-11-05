import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.example)
        def example(self):
            signs=''
            if self.ui.checkBox.isChecked():
                signs='bhjfcv,hw ea.'
            if self.ui.checkBox-2.isChecked():
                signs='0123456789'
            result=''
            number=random.randint(5,10)
            for i in range(number):
                result+=random.choice(signs)
            self.ui.label_2.setText(result)
app=QApplication([])
ex=Widget()
ex.show()
app.exec_()


<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>MingLiU-ExtB</family>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="autoFillBackground">
   <bool>false</bool>
  </property>
  <property name="styleSheet">
   <string notr="true">color:green;background-color:lightblue;border:2px solid black; border-radius:5px;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QCheckBox" name="checkBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>300</y>
      <width>221</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Використовувати числа</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox_2">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>340</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Використовувати алфавіт</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>402</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Згенерувати</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>240</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Тут буде результат</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>110</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Генератор паролів</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>25</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

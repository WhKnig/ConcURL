from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import shutil
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import logging
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download("stopwords")
import pickle
#import bert

import metricks
import sqlite3
#from homepage2vec.model import WebsiteClassifier

'''  TO DO
homepage2vec
BERT
pyplot
documentation
'''

english_stopwords = stopwords.words("english")
out_dir = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1228, 815)
        MainWindow.setWindowIcon(QtGui.QIcon('image/icon_app.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(66, 37, 143);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1228, 815))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        # self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont('Raleway')
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.gl_men = QtWidgets.QWidget()
        self.gl_men.setObjectName("gl_men")
        self.fon_gl = QtWidgets.QLabel(self.gl_men)
        self.fon_gl.setGeometry(QtCore.QRect(0, 0, 1228, 815))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fon_gl.sizePolicy().hasHeightForWidth())
        self.fon_gl.setSizePolicy(sizePolicy)
        self.fon_gl.setStyleSheet("background-image: url(image/fon_11.png);")
        self.fon_gl.setText("")
        self.fon_gl.setObjectName("fon_gl")
        self.uk_metr = QtWidgets.QLabel(self.gl_men)
        self.uk_metr.setGeometry(QtCore.QRect(265, 110, 180, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.uk_metr.setFont(font)
        self.uk_metr.setObjectName("uk_metr")
        self.uk_metr.setStyleSheet("image: url(image/Metrics.png);\n"
"background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")
        self.uk_metr.setAlignment(Qt.AlignCenter)
        self.pres_metr = QtWidgets.QTextBrowser(self.gl_men)
        self.pres_metr.setGeometry(QtCore.QRect(40, 180, 621, 551))
        self.pres_metr.setStyleSheet("color: rgb(66, 37, 143);\n"
"background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.pres_metr.setObjectName("pres_metr")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Calibri")
        self.pres_metr.setFont(font)
        # self.line = QtWidgets.QFrame(self.gl_men)
        # self.line.setGeometry(QtCore.QRect(915, 320, 51, 5))
        # self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        # self.line_2 = QtWidgets.QFrame(self.gl_men)
        # self.line_2.setGeometry(QtCore.QRect(915, 520, 5, 100))
        # self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        # self.line_txt = QtWidgets.QFrame(self.gl_men)
        # self.line_txt.setGeometry(QtCore.QRect(915, 470, 61, 16))
        # self.line_txt.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_txt.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_txt.setObjectName("line_n")
        # self.line_csv = QtWidgets.QFrame(self.gl_men)
        # self.line_csv.setGeometry(QtCore.QRect(915, 470, 61, 16))
        # self.line_csv.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_csv.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_csv.setObjectName("line_v")
        # self.bd_ico = QtWidgets.QLabel(self.gl_men)
        # self.bd_ico.setGeometry(QtCore.QRect(760, 470, 150, 150))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # font.setBold(True)
        # font.setWeight(75)
        # self.bd_ico.setFont(font)
        # self.bd_ico.setObjectName("uk_metr")
        # self.bd_ico.setStyleSheet("image: url(image/db_icon.png);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.save_bd = QtWidgets.QPushButton(self.gl_men)
        self.save_bd.setGeometry(QtCore.QRect(770, 580, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_bd.setFont(font)
        self.save_bd.setStyleSheet("image: url(image/txt.png);" "background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")

        self.save_bd.setObjectName("save_bd")
        self.save_CSV = QtWidgets.QPushButton(self.gl_men)
        self.save_CSV.setGeometry(QtCore.QRect(950, 580, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_CSV.setFont(font)
        self.save_CSV.setStyleSheet("image: url(image/csv.png);" "background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")
        self.save_CSV.setObjectName("save_CSV")
        self.tabWidget.addTab(self.gl_men, "")
        self.one_site = QtWidgets.QWidget()
        self.one_site.setObjectName("one_site")
        self.fon_gl_2 = QtWidgets.QLabel(self.one_site)
        self.fon_gl_2.setGeometry(QtCore.QRect(0, 0, 1228, 815))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fon_gl_2.sizePolicy().hasHeightForWidth())
        self.fon_gl_2.setSizePolicy(sizePolicy)
        self.fon_gl_2.setStyleSheet("background-image: url(image/fon_22.png);")
        self.fon_gl_2.setText("")
        self.fon_gl_2.setObjectName("fon_gl_2")
        self.edit_link1 = QtWidgets.QLineEdit(self.one_site)
        self.edit_link1.setGeometry(QtCore.QRect(50, 130, 760, 45))
        self.edit_link1.setStyleSheet("color: rgb(66, 37, 143);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;" "padding: 0 0 0 10px;")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_link1.setFont(font)
        self.edit_link1.setObjectName("edit_link1")
        self.edit_link1.setPlaceholderText("Specify here link ")
        self.class_link1 = QtWidgets.QPushButton(self.one_site)
        self.class_link1.setGeometry(QtCore.QRect(840, 130, 180, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.class_link1.setFont(font)
        self.class_link1.setStyleSheet("image: url(image/classify.png);" "background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")
        self.class_link1.setObjectName("class_link1")
        self.result_class_link1 = QtWidgets.QLabel(self.one_site)
        self.result_class_link1.setGeometry(QtCore.QRect(50, 200, 610, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result_class_link1.setFont(font)
        self.result_class_link1.setStyleSheet("color: rgb(66, 37, 143);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.result_class_link1.setObjectName("result_class_link1")
        self.result_class_link1.setAlignment(Qt.AlignCenter)
        self.fon_vibr = QtWidgets.QLabel(self.one_site)
        self.fon_vibr.setGeometry(QtCore.QRect(690, 205, 470, 270))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fon_vibr.setFont(font)
        self.fon_vibr.setStyleSheet("color: rgb(66, 37, 143);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.fon_vibr.setText("")
        self.fon_vibr.setObjectName("fon_vibr")
        self.uk_1 = QtWidgets.QRadioButton(self.one_site)
        self.uk_1.setGeometry(QtCore.QRect(705, 215, 450, 31))
        self.uk_1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_1.setFont(font)
        self.uk_1.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_1.setObjectName("uk_1")
        self.uk_2 = QtWidgets.QRadioButton(self.one_site)
        self.uk_2.setGeometry(QtCore.QRect(705, 265, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_2.setFont(font)
        self.uk_2.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_2.setObjectName("uk_2")
        self.uk_3 = QtWidgets.QRadioButton(self.one_site)
        self.uk_3.setGeometry(QtCore.QRect(705, 315, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_3.setFont(font)
        self.uk_3.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_3.setObjectName("uk_3")
        self.uk_4 = QtWidgets.QRadioButton(self.one_site)
        self.uk_4.setGeometry(QtCore.QRect(705, 365, 450, 41))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_4.setFont(font)
        self.uk_4.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_4.setObjectName("uk_4")
        self.uk_4.setChecked(True)
        self.uk_5 = QtWidgets.QRadioButton(self.one_site)
        self.uk_5.setGeometry(QtCore.QRect(705, 415, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_5.setFont(font)
        self.uk_5.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_5.setObjectName("uk_5")
        self.tabWidget.addTab(self.one_site, "")
        self.many_site = QtWidgets.QWidget()
        self.many_site.setObjectName("many_site")
        self.fon_1 = QtWidgets.QLabel(self.many_site)
        self.fon_1.setGeometry(QtCore.QRect(0, 0, 1228, 815))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fon_1.sizePolicy().hasHeightForWidth())
        self.fon_1.setSizePolicy(sizePolicy)
        self.fon_1.setStyleSheet("background-image: url(image/fon_33.png);")
        self.fon_1.setText("")
        self.fon_1.setObjectName("fon_1")
        self.fon_pod_vbr = QtWidgets.QLabel(self.many_site)
        self.fon_pod_vbr.setGeometry(QtCore.QRect(710, 130, 470, 270))
        self.fon_pod_vbr.setStyleSheet("color: rgb(66, 37, 143);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.fon_pod_vbr.setText("")
        self.fon_pod_vbr.setObjectName("fon_pod_vbr")
        self.res_on_scr = QtWidgets.QTextBrowser(self.many_site)
        self.res_on_scr.setGeometry(QtCore.QRect(50, 130, 631, 600))
        self.res_on_scr.setStyleSheet("color: rgb(66, 37, 143);" "background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        self.res_on_scr.setObjectName("res_on_scr")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_on_scr.setFont(font)
        self.file_with_links = QtWidgets.QPushButton(self.many_site)
        self.file_with_links.setGeometry(QtCore.QRect(710, 675, 372, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.file_with_links.setFont(font)
        self.file_with_links.setStyleSheet(
            "image: url(image/classify_file.png);" "background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")
        self.file_with_links.setObjectName("file_with_links")
        self.dwn_res = QtWidgets.QPushButton(self.many_site)
        self.dwn_res.setGeometry(QtCore.QRect(621, 670, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dwn_res.setFont(font)
        self.dwn_res.setStyleSheet("image: url(image/down_icon2.png);" "background-color: rgb(216, 209, 241, 0);" "border-radius: 15px;")
        self.dwn_res.setObjectName("dwn_res")
        self.uk_11 = QtWidgets.QRadioButton(self.many_site)
        self.uk_11.setGeometry(QtCore.QRect(725, 140, 450, 31))
        self.uk_11.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_11.setFont(font)
        self.uk_11.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_11.setObjectName("uk_11")
        self.uk_22 = QtWidgets.QRadioButton(self.many_site)
        self.uk_22.setGeometry(QtCore.QRect(725, 190, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_22.setFont(font)
        self.uk_22.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_22.setObjectName("uk_22")
        self.uk_33 = QtWidgets.QRadioButton(self.many_site)
        self.uk_33.setGeometry(QtCore.QRect(725, 240, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_33.setFont(font)
        self.uk_33.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_33.setObjectName("uk_33")
        self.uk_44 = QtWidgets.QRadioButton(self.many_site)
        self.uk_44.setGeometry(QtCore.QRect(725, 290, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_44.setFont(font)
        self.uk_44.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_44.setObjectName("uk_44")
        self.uk_44.setChecked(True)
        self.uk_55 = QtWidgets.QRadioButton(self.many_site)
        self.uk_55.setGeometry(QtCore.QRect(725, 340, 450, 31))
        font = QtGui.QFont("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uk_55.setFont(font)
        self.uk_55.setStyleSheet("color: rgb(80, 37, 143);" "background-color: rgb(216, 209, 241, 0);")
        self.uk_55.setObjectName("uk_55")
        self.tabWidget.addTab(self.many_site, "")
        self.btns()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ConcURL"))
        self.uk_metr.setText(_translate("MainWindow", ""))
        #Здесь писать метрики
        self.pres_metr.setText(_translate("MainWindow", f'{metricks.dtc}\n\n{metricks.mnb}\n\n{metricks.sgd}\n\n{metricks.svc}'))
        self.save_bd.setText(_translate("MainWindow", ""))
        self.save_CSV.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gl_men), _translate("MainWindow", "Metrics"))
        self.class_link1.setText(_translate("MainWindow", ""))
        self.result_class_link1.setText(_translate("MainWindow", "Result of classify"))
        self.uk_1.setText(_translate("MainWindow", "DecisionTreeClassifier"))
        self.uk_2.setText(_translate("MainWindow", "MultinomialNB"))
        self.uk_3.setText(_translate("MainWindow", "SGDClassifier"))
        self.uk_4.setText(_translate("MainWindow", "SVC"))
        self.uk_5.setText(_translate("MainWindow", "Bert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.one_site), _translate("MainWindow", "One link"))
        self.file_with_links.setText(_translate("MainWindow", ""))
        self.dwn_res.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.many_site), _translate("MainWindow", "File with links"))
        self.uk_11.setText(_translate("MainWindow", "DecisionTreeClassifier"))
        self.uk_22.setText(_translate("MainWindow", "MultinomialNB"))
        self.uk_33.setText(_translate("MainWindow", "SGDClassifier"))
        self.uk_44.setText(_translate("MainWindow", "SVC"))
        self.uk_55.setText(_translate("MainWindow", "Bert"))

    def btns(self):
        self.save_bd.clicked.connect(lambda: self.scach())
        self.class_link1.clicked.connect(self.link_res)
        self.file_with_links.clicked.connect(lambda: self.br_file())
        self.dwn_res.clicked.connect(lambda: self.save_file())
        self.save_CSV.clicked.connect(lambda: self.scach2())

    def save_csv(self):
        df = pd.DataFrame(columns=['id', 'link', 'label'])
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        rows = sql.execute(f"""SELECT * FROM data""").fetchall()
        for row in rows:
            df.loc[len(df.index)] = [row[0], row[1], row[2]]
        df.to_csv('./output_csv.csv')

    def scach2(self):
        filepath_raw, filename_raw = os.path.split(str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow)))
        filepath_raw = filepath_raw.replace("('", "")
        filename = filename_raw.replace("', 'All Files (*)')", "")
        dir = (filepath_raw + "/" + filename)
        self.save_csv()
        shutil.copy('output_csv.csv', dir)

    def read_db(self):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        rows = sql.execute(f"""SELECT * FROM data""").fetchall()
        with open('output_db.txt', 'w') as f:
            for i in rows:
                f.write(str(i)[1:-1] + '\n')

    def scach(self):
        filepath_raw, filename_raw = os.path.split(str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow)))
        filepath_raw = filepath_raw.replace("('", "")
        filename = filename_raw.replace("', 'All Files (*)')", "")
        dir = (filepath_raw + "/" + filename)
        self.read_db()
        shutil.copy('output_db.txt', dir)

    # def hp2v(self, link):
    #     model = WebsiteClassifier()
    #     website = model.fetch_website(link)
    #     scores, embeddings = model.predict(website)
    #     print(scores)
    #     for k, v in scores.items():
    #         if v == max(scores.values()):
    #             return k

    def link_res(self):
        link = self.edit_link1.text()

        if self.uk_4.isChecked() == True:
            use_mod = 'Support Vector Classification.sav'
        elif self.uk_2.isChecked() == True:
            use_mod = 'MultinomialNB Sklearn.sav'
        elif self.uk_3.isChecked() == True:
            use_mod = 'SGDClassifier.sav'
        elif self.uk_1.isChecked() == True:
            use_mod = 'DecisionTreeClassifier.sav'
        elif self.uk_5.isChecked() == True:
            use_mod = 'bert.sav'

        def executePost(page):
            soup = bs(page.text, 'html.parser')
            # Получаем заголовок статьи
            title = soup.find('title')
            title = str(title.text)

            return title

        def get_post(postLink, newdf):
            currPostUrl = postLink
            try:
                response = requests.get(currPostUrl)
                #response.raise_for_status()
                response_title = executePost(response)
                dataList = [currPostUrl, response_title]
                newdf.loc[len(newdf)] = dataList
            except Exception as e:
                print(e)

        def remove_punct(text):
            # удаление пунктуации в тексте
            table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ',
                     40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ',
                     47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ',
                     64: ' ', 91: ' ', 92: ' ', 93: ' ', 94: ' ', 95: ' ', 96: ' ',
                     123: ' ', 124: ' ', 125: ' ', 126: ' '}
            return text.translate(table)

        def txt_prep(df):
            # функция приводит весь текст к нижнему регистру
            df['title без изменений'] = df['title']
            df['title'] = df['title'].str.lower()
            # удаляет пунктуацию
            df['title'] = df['title'].map(lambda x: remove_punct(x))
            # удаляет стоп слова
            df['title'] = df['title'].map(lambda x: x.split(' '))
            df['title'] = df['title'].map(lambda x: [token for token in x if token not in english_stopwords \
                                                     and token != " " \
                                                     and token.strip() not in punctuation])
            df['title'] = df['title'].map(lambda x: ' '.join(x))
            # удаление ковычек и цифр
            df['title'] = df['title'].str.replace('»', '')
            df['title'] = df['title'].str.replace('«', '')
            #df['title'] = df['title'].str.replace(r"\d+", '')
            return df

        def lemm(df):
            tfidf = pickle.load(open("vectorizer.pickle", 'rb'))
            wordnet_lemmatizer = WordNetLemmatizer()
            lemmatized_list = []
            text = df.title[0]
            text_words = nltk.word_tokenize(text)
            for word in text_words:
                word_norm = wordnet_lemmatizer.lemmatize(word, pos="v")
                lemmatized_list.append(word_norm)

            lemmatized_text = " ".join(lemmatized_list)  # early access review
            df['lemm'] = lemmatized_text
            x_test = tfidf.transform(df['lemm']).todense()
            return x_test

        def preprocessing(link):
            newdf = pd.DataFrame(columns=['link', 'title'])
            get_post(link, newdf)
            txt_prep(newdf)
            vectorized = lemm(newdf)
            loaded_model = pickle.load(open(use_mod, 'rb'))
            vectorized = np.asarray(vectorized)
            y_pred = loaded_model.predict(vectorized)
            return y_pred

        m_dict = {'0': 'Arts', '1': 'Business', '2': 'Computers', '3': 'Games', '4': 'Health', '5': 'Home', '6': 'Kids',
                  '7': 'News',
                  '8': 'Recreation', '9': 'Reference', '10': 'Science', '11': 'Shopping', '12': 'Society',
                  '13': 'Sports'}


        if use_mod == 'bert.sav':
            df = pd.DataFrame(columns=['link', 'label'])
            df.loc[len(df.index)] = [link, 'Arts']
            #df = bert.main(df)
            self.result_class_link1.setText(df.loc[len(df.index)-1, 1])
        else:
            res = str(preprocessing(link)[0])
            self.result_class_link1.setText(m_dict[res])



        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute(f"INSERT INTO data(link, label, model) VALUES (?, ?, ?)", (link, m_dict[res], use_mod[:-3]))
        db.commit()

    def br_file(self):
        filepath_raw, filename_raw = os.path.split(str(QtWidgets.QFileDialog.getOpenFileName(MainWindow)))
        filepath_raw = filepath_raw.replace("('", "")
        filename = filename_raw.replace("', 'All Files (*)')", "")
        filepath = (filepath_raw + "/" + filename)

        if filepath[-4:] == '.txt':
            f = open(filepath)
            ff = open('result.txt', 'w')
            ff.write(filepath + '\n')
        elif filepath[-4:] == '.csv':
            flag = 1
            f = pd.read_csv(filepath)
            ff = pd.read_csv('result.csv')


        self.res_on_scr.setText(filepath + '\n')

        if self.uk_44.isChecked() == True:
            use_mod = 'Support Vector Classification.sav'
        elif self.uk_22.isChecked() == True:
            use_mod = 'MultinomialNB Sklearn.sav'
        elif self.uk_33.isChecked() == True:
            use_mod = 'SGDClassifier.sav'
        elif self.uk_55.isChecked() == True:
            use_mod = 'bert.sav'
        elif self.uk_11.isChecked() == True:
            use_mod = 'DecisionTreeClassifier.sav'

        def executePost(page):
            soup = bs(page.text, 'html.parser')
            # Получаем заголовок статьи
            title = soup.find('title')
            title = str(title.text)

            return title

        def get_post(postLink, newdf):
            currPostUrl = postLink
            try:
                response = requests.get(currPostUrl)
                # response.raise_for_status()
                response_title = executePost(response)
                dataList = [currPostUrl, response_title]
                newdf.loc[len(newdf)] = dataList
            except Exception as e:
                print(e)

        def remove_punct(text):
            # удаление пунктуации в тексте
            table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ',
                     40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ',
                     47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ',
                     64: ' ', 91: ' ', 92: ' ', 93: ' ', 94: ' ', 95: ' ', 96: ' ',
                     123: ' ', 124: ' ', 125: ' ', 126: ' '}
            return text.translate(table)

        def txt_prep(df):
            # функция приводит весь текст к нижнему регистру
            df['title без изменений'] = df['title']
            df['title'] = df['title'].str.lower()
            # удаляет пунктуацию
            df['title'] = df['title'].map(lambda x: remove_punct(x))
            # удаляет стоп слова
            df['title'] = df['title'].map(lambda x: x.split(' '))
            df['title'] = df['title'].map(lambda x: [token for token in x if token not in english_stopwords \
                                                     and token != " " \
                                                     and token.strip() not in punctuation])
            df['title'] = df['title'].map(lambda x: ' '.join(x))
            # удаление ковычек и цифр
            df['title'] = df['title'].str.replace('»', '')
            df['title'] = df['title'].str.replace('«', '')
            # df['title'] = df['title'].str.replace(r"\d+", '')
            return df

        def lemm(df):
            tfidf = pickle.load(open("vectorizer.pickle", 'rb'))
            wordnet_lemmatizer = WordNetLemmatizer()
            lemmatized_list = []
            text = df.title[0]
            text_words = nltk.word_tokenize(text)
            for word in text_words:
                word_norm = wordnet_lemmatizer.lemmatize(word, pos="v")
                lemmatized_list.append(word_norm)

            lemmatized_text = " ".join(lemmatized_list)  # early access review
            df['lemm'] = lemmatized_text
            x_test = tfidf.transform(df['lemm']).todense()
            return x_test

        def preprocessing(link):
            newdf = pd.DataFrame(columns=['link', 'title'])
            get_post(link, newdf)
            txt_prep(newdf)
            vectorized = lemm(newdf)
            loaded_model = pickle.load(open(use_mod, 'rb'))
            vectorized = np.asarray(vectorized)
            y_pred = loaded_model.predict(vectorized)
            return y_pred

        if filepath[-4:] == '.txt':
            for i in f.readlines():
                link = i[:-1]
                res = str(preprocessing(link)[0])
                m_dict = {'0': 'Arts', '1': 'Business', '2': 'Computers', '3': 'Games', '4': 'Health', '5': 'Home',
                          '6': 'Kids', '7': 'News',
                          '8': 'Recreation', '9': 'Reference', '10': 'Science', '11': 'Shopping', '12': 'Society',
                          '13': 'Sports'}

                db = sqlite3.connect('data.db')
                sql = db.cursor()
                sql.execute(f"INSERT INTO data(link, label, model) VALUES (?, ?, ?)", (link, m_dict[res], use_mod[:-3]))
                db.commit()
                ff.write(link + ' : ' + m_dict[res] + '\n')

                self.res_on_scr.setText(self.res_on_scr.toPlainText() + link + ' : ' + m_dict[res] + '\n')
            ff.close()
        else:
            for index, row in f.iterrows():
                res = str(preprocessing(row.link)[0])
                m_dict = {'0': 'Arts', '1': 'Business', '2': 'Computers', '3': 'Games', '4': 'Health', '5': 'Home',
                          '6': 'Kids', '7': 'News',
                          '8': 'Recreation', '9': 'Reference', '10': 'Science', '11': 'Shopping', '12': 'Society',
                          '13': 'Sports'}

                db = sqlite3.connect('data.db')
                sql = db.cursor()
                sql.execute(f"INSERT INTO data(link, label, model) VALUES (?, ?, ?)", (row.link, m_dict[res], use_mod[:-3]))
                db.commit()

                ff.loc[len(ff.index)] = [row.link, res, use_mod[:-3]]
                self.res_on_scr.setText(self.res_on_scr.toPlainText() + row.link + ' : ' + m_dict[res] + '\n')


    def save_file(self):
        global flag
        filepath_raw, filename_raw = os.path.split(str(QtWidgets.QFileDialog.getExistingDirectory(MainWindow)))
        filepath_raw = filepath_raw.replace("('", "")
        filename = filename_raw.replace("', 'All Files (*)')", "")
        dir = (filepath_raw + "/" + filename)
        shutil.copy('result.txt', dir)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

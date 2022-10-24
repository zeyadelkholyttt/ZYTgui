from os import link
import os
from time import sleep
from re import search
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
import sys
import humanize
from ZYTD import Ui_MainWindow
from pytube.cli import on_progress
from pytube import YouTube
from pytube import Playlist


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('ZYTD.ui', self)
        
        self.pushButton.clicked.connect(self.download_button)
        self.pushButton_3.clicked.connect(self.git)
        self.pushButton_2.clicked.connect(self.browse)

    
    
        
    def browse(self):
        save_place = QFileDialog.getExistingDirectory(self, "downlaoding location")
        text = str(save_place)
        path = (text[2:].split(',')[0].replace("'",''))
        self.lineEdit_2.setText(path)
    def git(self):
        if self.mp4.isChecked() == True and self.video.isChecked() == True:
            self.comboBox.clear()
            url = self.lineEdit.text()
            youtube = YouTube(url)
            video = youtube.streams.filter(progressive=True)
            for v in video :
                size = humanize.naturalsize(v.filesize)
                type = v.mime_type
                format = type.replace("video/", "")
                total_info ='{} {} {}'.format(v.resolution,format, size)
                self.comboBox.addItem(total_info)

        if self.audio.isChecked() == True and self.video.isChecked() == True:
            self.comboBox.clear()
            url = self.lineEdit.text()
            youtube = YouTube(url)
            video = youtube.streams.filter(only_audio=True)
            for v in video :
                size = humanize.naturalsize(v.filesize)
                type = v.mime_type
                tag = v.itag
                print (tag)
                total_info ='{} {}'.format(v.mime_type, size)
                self.comboBox.addItem(total_info)

        if self.playlist.isChecked() == True and self.mp4.isChecked() == True:
            self.comboBox.addItem('highest')
            self.comboBox.addItem('>= 1080p')
            self.comboBox.addItem('>= 720p')
            self.comboBox.addItem('>= 480p')
            self.comboBox.addItem('>= 360p')
            self.comboBox.addItem('lowest')
    
            
            
            


            
          
    def download_button(self): 
        link = self.lineEdit.text()
        save_loc = self.lineEdit_2.text()
        
        res = self.comboBox.currentIndex()
        if self.mp4.isChecked() == True and self.video.isChecked() == True:
            st = YouTube(link, on_progress_callback=on_progress)
            video = st.streams.filter(progressive=True)
            down = video[res]
            down.download(save_loc)
            QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            QApplication.processEvents()
            


        if self.video.isChecked() == True and self.audio.isChecked() == True:
            
            video = st.streams.filter(only_audio=True)
            down = video[res]
            file_size = video.filesize
            down.download(save_loc)
            QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            QApplication.processEvents()
        if self.mp4.isChecked() == True and self.playlist.isChecked() == True:
            p = Playlist(link)
            os.chdir(save_loc)
            if os.path.exists(p.title):
                os.chdir(str(p.title))
            else :
                os.mkdir(str(p.title))
                os.chdir(str(p.title))
            self.label_9.setText('current downloading :')
            QApplication.processEvents()
                
            
            #download playlist with highest resolution
            if res == 0:
                for video in p.videos:
                    video.streams.get_highest_resolution().download()
                    current_v = (video.title)
                    self.label_8.clear()
                    delay = 5
                    sleep(delay)
                    self.label_8.setText(str(current_v))
            QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            QApplication.processEvents()
            #download playlist 1080p
            if res == 1:
                for video in p.videos:
                    try:
                        video.streams.get_by_resolution('1080p').download()    
                    except:
                        try:
                            video.streams.get_by_resolution('720p').download()
                        except:
                            try:
                                video.streams.get_by_resolution('480p').download()
                            except:
                                try:
                                    video.streams.get_by_resolution('360p').download()
                                except:
                                    try:
                                        video.streams.get_by_resolution('240p').download()
                                    except:
                                        try:
                                            video.streams.get_by_resolution('144p').download()
                                        except:
                                            print(f'Video {video.title} is undownloadable, skipping.')
                    current_v = (video.title)
                    delay = 5
                    sleep(delay)
                    self.label_8.clear()
                    self.label_8.setText(str(current_v))
                    QApplication.processEvents()
                QMessageBox.information(self, "the download finish", "the download finished thx for using my program") 
            #download a playlist with 720p resolution
            if res == 2:
                for video in p.videos:
                        try:
                            video.streams.get_by_resolution('720p').download()
                        except:
                            try:
                                video.streams.get_by_resolution('480p').download()
                            except:
                                try:
                                    video.streams.get_by_resolution('360p').download()
                                except:
                                    try:
                                        video.streams.get_by_resolution('240p').download()
                                    except:
                                        try:
                                            video.streams.get_by_resolution('144p').download()
                                        except:
                                            print(f'Video {video.title} is undownloadable, skipping.')
                        current_v = (video.title)
                        delay = 5
                        sleep(delay)
                        self.label_8.clear()
                        self.label_8.setText(str(current_v))
                        QApplication.processEvents()
                QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            if res == 3:
                for video in p.videos:
                    try:
                        video.streams.get_by_resolution('480p').download()
                    except:
                        try:
                            video.streams.get_by_resolution('360p').download()
                        except:
                            try:
                                video.streams.get_by_resolution('240p').download()
                            except:
                                try:
                                    video.streams.get_by_resolution('144p').download()
                                except:
                                    print(f'Video {video.title} is undownloadable, skipping.')
                    current_v = (video.title)
                    delay = 5
                    sleep(delay)
                    self.label_8.clear()
                    self.label_8.setText(str(current_v))
                    QApplication.processEvents()
                QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            if res == 4:
                for video in p.videos:
                        try:
                            video.streams.get_by_resolution('360p').download()
                        except:
                            try:
                                video.streams.get_by_resolution('240p').download()
                            except:
                                try:
                                    video.streams.get_by_resolution('144p').download()
                                except:
                                    print(f'Video {video.title} is undownloadable, skipping.')
                        current_v = (video.title)
                        delay = 5
                        sleep(delay)
                        self.label_8.clear()
                        self.label_8.setText(str(current_v))
                        QApplication.processEvents()
                QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            if res == 5:
                for video in p.videos:
                    video.streams.get_lowest_resolution().download()
                    current_v = (video.title)
                    delay = 5
                    sleep(delay)
                    self.label_8.clear()
                    self.label_8.setText(str(current_v))
                QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
                QApplication.processEvents()
        if self.mp4.isChecked() == True and self.playlist.isChecked() == True:
            for video in p.videos:
                    video.streams.get_audio_only().download()
                    current_v = (video.title)
                    delay = 5
                    sleep(delay)
                    self.label_8.clear()
                    self.label_8.setText(str(current_v))
            QMessageBox.information(self, "the download finish", "the download finished thx for using my program")
            QApplication.processEvents()
            





            



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = MainUI()
    ui.show()

    app.exec_()

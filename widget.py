# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("牛马浏览器")
        self.resize(1280, 720)

        # 创建网页显示区域
        self.web_engine_view = QWebEngineView()
        self.web_engine_view.load(QUrl("https://www.google.com"))

        #根据网页标题设置标签标题
        self.web_engine_view.titleChanged.connect(lambda title: self.tab_widget.setTabText(self.tab_widget.currentIndex(), title))

        #根据导航栏URL设置网页URL
        self.web_engine_view.urlChanged.connect(lambda url: self.url_bar.setText(url.toString()))

        # 创建URL导航栏
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter a URL")
        self.url_bar.returnPressed.connect(lambda: self.tab_widget.currentWidget().setUrl(QUrl(self.url_bar.text())))
        self.url_bar.textChanged.connect(lambda: self.tab_widget.currentWidget().setUrl(QUrl(self.url_bar.text())))
        self.web_engine_view.urlChanged.connect(lambda url: self.url_bar.setText(url.toString()))

        # 创建标签小部件
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.tab_widget.removeTab)
        # 将网页显示区域添加到标签小部件中
        self.tab_widget.addTab(self.web_engine_view, "google")

        # 创建新标签按钮
        self.new_tab_button = QPushButton("+")
        self.new_tab_button.clicked.connect(self.add_tab)

        # 创建返回按钮
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(lambda: self.tab_widget.currentWidget().back())

        # 设置布局
        layout = QVBoxLayout()
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.url_bar)
        navigation_layout.addWidget(self.new_tab_button)
        navigation_layout.addWidget(self.back_button)
        layout.addLayout(navigation_layout)
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

    def add_tab(self):
        # 创建一个新的网络引擎视图并将其添加到标签小部件中
        web_engine_view = QWebEngineView()
        self.tab_widget.addTab(web_engine_view, "新标签页")
        #新标签页初始化为百度
        web_engine_view.load(QUrl("https://www.google.com"))
        # 将新标签页的URL与导航栏URL绑定
        web_engine_view.urlChanged.connect(lambda url: self.url_bar.setText(url.toString()))
        # 将新标签页的标题与标签标题绑定
        web_engine_view.titleChanged.connect(lambda title: self.tab_widget.setTabText(self.tab_widget.currentIndex(), title))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

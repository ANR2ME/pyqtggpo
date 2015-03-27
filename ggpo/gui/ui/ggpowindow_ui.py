# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ggpo/gui/ui/ggpowindow.ui'
#
# Created: Fri Mar 27 11:42:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(810, 708)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("assets/icon-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uiSplitter = QtGui.QSplitter(self.centralwidget)
        self.uiSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.uiSplitter.setObjectName(_fromUtf8("uiSplitter"))
        self.uiChannelsTree = QtGui.QTreeWidget(self.uiSplitter)
        self.uiChannelsTree.setObjectName(_fromUtf8("uiChannelsTree"))
        self.uiChannelsTree.headerItem().setText(0, _fromUtf8("#"))
        self.uiChannelsTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.uiChannelsTree.headerItem().setText(1, _fromUtf8("Game"))
        self.uiChannelsTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.layoutWidget = QtGui.QWidget(self.uiSplitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiChatHistoryTxtB = QtGui.QTextBrowser(self.layoutWidget)
        self.uiChatHistoryTxtB.setAcceptDrops(False)
        self.uiChatHistoryTxtB.setReadOnly(True)
        self.uiChatHistoryTxtB.setOpenExternalLinks(False)
        self.uiChatHistoryTxtB.setOpenLinks(False)
        self.uiChatHistoryTxtB.setObjectName(_fromUtf8("uiChatHistoryTxtB"))
        self.verticalLayout.addWidget(self.uiChatHistoryTxtB)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.uiChatInputEdit = CompletionLineEdit(self.layoutWidget)
        self.uiChatInputEdit.setObjectName(_fromUtf8("uiChatInputEdit"))
        self.horizontalLayout.addWidget(self.uiChatInputEdit)
        self.uiEmoticonTbtn = QtGui.QToolButton(self.layoutWidget)
        self.uiEmoticonTbtn.setObjectName(_fromUtf8("uiEmoticonTbtn"))
        self.horizontalLayout.addWidget(self.uiEmoticonTbtn)
        self.uiAfkChk = QtGui.QCheckBox(self.layoutWidget)
        self.uiAfkChk.setObjectName(_fromUtf8("uiAfkChk"))
        self.horizontalLayout.addWidget(self.uiAfkChk)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.uiPlayersTableV = QtGui.QTableView(self.uiSplitter)
        self.uiPlayersTableV.setObjectName(_fromUtf8("uiPlayersTableV"))
        self.horizontalLayout_2.addWidget(self.uiSplitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAction = QtGui.QMenu(self.menubar)
        self.menuAction.setObjectName(_fromUtf8("menuAction"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.uiThemeMenu = QtGui.QMenu(self.menuSetting)
        self.uiThemeMenu.setObjectName(_fromUtf8("uiThemeMenu"))
        self.uiSmoothingMenu = QtGui.QMenu(self.menuSetting)
        self.uiSmoothingMenu.setObjectName(_fromUtf8("uiSmoothingMenu"))
        self.menuLogging = QtGui.QMenu(self.menuSetting)
        self.menuLogging.setObjectName(_fromUtf8("menuLogging"))
        self.uiChallengeSoundMenu = QtGui.QMenu(self.menuSetting)
        self.uiChallengeSoundMenu.setObjectName(_fromUtf8("uiChallengeSoundMenu"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.uiStatusbar = QtGui.QStatusBar(MainWindow)
        self.uiStatusbar.setObjectName(_fromUtf8("uiStatusbar"))
        MainWindow.setStatusBar(self.uiStatusbar)
        self.uiClearChatHistoryAct = QtGui.QAction(MainWindow)
        self.uiClearChatHistoryAct.setObjectName(_fromUtf8("uiClearChatHistoryAct"))
        self.uiAwayAct = QtGui.QAction(MainWindow)
        self.uiAwayAct.setCheckable(True)
        self.uiAwayAct.setObjectName(_fromUtf8("uiAwayAct"))
        self.uiQuitAct = QtGui.QAction(MainWindow)
        self.uiQuitAct.setObjectName(_fromUtf8("uiQuitAct"))
        self.uiMuteChallengeSoundAct = QtGui.QAction(MainWindow)
        self.uiMuteChallengeSoundAct.setCheckable(True)
        self.uiMuteChallengeSoundAct.setObjectName(_fromUtf8("uiMuteChallengeSoundAct"))
        self.uiMuteNotifySoundAct = QtGui.QAction(MainWindow)
        self.uiMuteNotifySoundAct.setCheckable(True)
        self.uiMuteNotifySoundAct.setObjectName(_fromUtf8("uiMuteNotifySoundAct"))
        self.uiFontAct = QtGui.QAction(MainWindow)
        self.uiFontAct.setObjectName(_fromUtf8("uiFontAct"))
        self.uiAboutAct = QtGui.QAction(MainWindow)
        self.uiAboutAct.setObjectName(_fromUtf8("uiAboutAct"))
        self.uiStrevivalAct = QtGui.QAction(MainWindow)
        self.uiStrevivalAct.setObjectName(_fromUtf8("uiStrevivalAct"))
        self.uiHitboxViewerAct = QtGui.QAction(MainWindow)
        self.uiHitboxViewerAct.setObjectName(_fromUtf8("uiHitboxViewerAct"))
        self.uiSafejumpGuideAct = QtGui.QAction(MainWindow)
        self.uiSafejumpGuideAct.setObjectName(_fromUtf8("uiSafejumpGuideAct"))
        self.uiMatchVideosAct = QtGui.QAction(MainWindow)
        self.uiMatchVideosAct.setObjectName(_fromUtf8("uiMatchVideosAct"))
        self.uiSRKForumAct = QtGui.QAction(MainWindow)
        self.uiSRKForumAct.setObjectName(_fromUtf8("uiSRKForumAct"))
        self.uiSRKWikiAct = QtGui.QAction(MainWindow)
        self.uiSRKWikiAct.setObjectName(_fromUtf8("uiSRKWikiAct"))
        self.uiJPWikiAct = QtGui.QAction(MainWindow)
        self.uiJPWikiAct.setObjectName(_fromUtf8("uiJPWikiAct"))
        self.uiGNGThemeAct = QtGui.QAction(MainWindow)
        self.uiGNGThemeAct.setCheckable(True)
        self.uiGNGThemeAct.setObjectName(_fromUtf8("uiGNGThemeAct"))
        self.uiDarkThemeAct = QtGui.QAction(MainWindow)
        self.uiDarkThemeAct.setCheckable(True)
        self.uiDarkThemeAct.setObjectName(_fromUtf8("uiDarkThemeAct"))
        self.uiDebugLogAct = QtGui.QAction(MainWindow)
        self.uiDebugLogAct.setCheckable(True)
        self.uiDebugLogAct.setObjectName(_fromUtf8("uiDebugLogAct"))
        self.uiEmoticonAct = QtGui.QAction(MainWindow)
        self.uiEmoticonAct.setObjectName(_fromUtf8("uiEmoticonAct"))
        self.uiLocateGgpofbaAct = QtGui.QAction(MainWindow)
        self.uiLocateGgpofbaAct.setObjectName(_fromUtf8("uiLocateGgpofbaAct"))
        self.uiLocateROMsAct = QtGui.QAction(MainWindow)
        self.uiLocateROMsAct.setObjectName(_fromUtf8("uiLocateROMsAct"))
        self.uiLocateGeommdbAct = QtGui.QAction(MainWindow)
        self.uiLocateGeommdbAct.setObjectName(_fromUtf8("uiLocateGeommdbAct"))
        self.uiNotifyPlayerStateChangeAct = QtGui.QAction(MainWindow)
        self.uiNotifyPlayerStateChangeAct.setCheckable(True)
        self.uiNotifyPlayerStateChangeAct.setObjectName(_fromUtf8("uiNotifyPlayerStateChangeAct"))
        self.uiFocusOnChatAct = QtGui.QAction(MainWindow)
        self.uiFocusOnChatAct.setObjectName(_fromUtf8("uiFocusOnChatAct"))
        self.uiToggleSidebarAction = QtGui.QAction(MainWindow)
        self.uiToggleSidebarAction.setObjectName(_fromUtf8("uiToggleSidebarAction"))
        self.uiExpandChannelSidebarAct = QtGui.QAction(MainWindow)
        self.uiExpandChannelSidebarAct.setObjectName(_fromUtf8("uiExpandChannelSidebarAct"))
        self.uiContractChannelSidebarAct = QtGui.QAction(MainWindow)
        self.uiContractChannelSidebarAct.setObjectName(_fromUtf8("uiContractChannelSidebarAct"))
        self.uiContractPlayerListAct = QtGui.QAction(MainWindow)
        self.uiContractPlayerListAct.setObjectName(_fromUtf8("uiContractPlayerListAct"))
        self.uiExpandPlayerListAct = QtGui.QAction(MainWindow)
        self.uiExpandPlayerListAct.setObjectName(_fromUtf8("uiExpandPlayerListAct"))
        self.uiLocateUnsupportedSavestatesDirAct = QtGui.QAction(MainWindow)
        self.uiLocateUnsupportedSavestatesDirAct.setObjectName(_fromUtf8("uiLocateUnsupportedSavestatesDirAct"))
        self.uiSyncUnsupportedSavestatesAct = QtGui.QAction(MainWindow)
        self.uiSyncUnsupportedSavestatesAct.setObjectName(_fromUtf8("uiSyncUnsupportedSavestatesAct"))
        self.uiSelectUnsupportedSavestateAct = QtGui.QAction(MainWindow)
        self.uiSelectUnsupportedSavestateAct.setObjectName(_fromUtf8("uiSelectUnsupportedSavestateAct"))
        self.uiFireThemeAct = QtGui.QAction(MainWindow)
        self.uiFireThemeAct.setCheckable(True)
        self.uiFireThemeAct.setObjectName(_fromUtf8("uiFireThemeAct"))
        self.uiCustomQssFileAct = QtGui.QAction(MainWindow)
        self.uiCustomQssFileAct.setCheckable(True)
        self.uiCustomQssFileAct.setObjectName(_fromUtf8("uiCustomQssFileAct"))
        self.uiNormalThemeAct = QtGui.QAction(MainWindow)
        self.uiNormalThemeAct.setCheckable(True)
        self.uiNormalThemeAct.setObjectName(_fromUtf8("uiNormalThemeAct"))
        self.action0 = QtGui.QAction(MainWindow)
        self.action0.setObjectName(_fromUtf8("action0"))
        self.uiCustomEmoticonsAct = QtGui.QAction(MainWindow)
        self.uiCustomEmoticonsAct.setObjectName(_fromUtf8("uiCustomEmoticonsAct"))
        self.uiShowCountryFlagInChatAct = QtGui.QAction(MainWindow)
        self.uiShowCountryFlagInChatAct.setCheckable(True)
        self.uiShowCountryFlagInChatAct.setObjectName(_fromUtf8("uiShowCountryFlagInChatAct"))
        self.uiDisableAutoAnnounceAct = QtGui.QAction(MainWindow)
        self.uiDisableAutoAnnounceAct.setCheckable(True)
        self.uiDisableAutoAnnounceAct.setObjectName(_fromUtf8("uiDisableAutoAnnounceAct"))
        self.uiHideGamesWithoutRomAct = QtGui.QAction(MainWindow)
        self.uiHideGamesWithoutRomAct.setCheckable(True)
        self.uiHideGamesWithoutRomAct.setObjectName(_fromUtf8("uiHideGamesWithoutRomAct"))
        self.uiShowTimestampInChatAct = QtGui.QAction(MainWindow)
        self.uiShowTimestampInChatAct.setCheckable(True)
        self.uiShowTimestampInChatAct.setObjectName(_fromUtf8("uiShowTimestampInChatAct"))
        self.uiDisableAutoColorNicks = QtGui.QAction(MainWindow)
        self.uiDisableAutoColorNicks.setCheckable(True)
        self.uiDisableAutoColorNicks.setObjectName(_fromUtf8("uiDisableAutoColorNicks"))
        self.uiLocateCustomChallengeSoundAct = QtGui.QAction(MainWindow)
        self.uiLocateCustomChallengeSoundAct.setObjectName(_fromUtf8("uiLocateCustomChallengeSoundAct"))
        self.uiLogChatAct = QtGui.QAction(MainWindow)
        self.uiLogChatAct.setCheckable(True)
        self.uiLogChatAct.setObjectName(_fromUtf8("uiLogChatAct"))
        self.uiLogPlayHistoryAct = QtGui.QAction(MainWindow)
        self.uiLogPlayHistoryAct.setCheckable(True)
        self.uiLogPlayHistoryAct.setObjectName(_fromUtf8("uiLogPlayHistoryAct"))
        self.uiGNGWebAct = QtGui.QAction(MainWindow)
        self.uiGNGWebAct.setObjectName(_fromUtf8("uiGNGWebAct"))
        self.uiFilterFavoriteLobbies = QtGui.QAction(MainWindow)
        self.uiFilterFavoriteLobbies.setCheckable(True)
        self.uiFilterFavoriteLobbies.setObjectName(_fromUtf8("uiFilterFavoriteLobbies"))
        self.menuAction.addAction(self.uiAwayAct)
        self.menuAction.addAction(self.uiFocusOnChatAct)
        self.menuAction.addAction(self.uiEmoticonAct)
        self.menuAction.addAction(self.uiClearChatHistoryAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiToggleSidebarAction)
        self.menuAction.addAction(self.uiContractChannelSidebarAct)
        self.menuAction.addAction(self.uiExpandChannelSidebarAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiContractPlayerListAct)
        self.menuAction.addAction(self.uiExpandPlayerListAct)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.uiQuitAct)
        self.menuLogging.addAction(self.uiLogChatAct)
        self.menuLogging.addAction(self.uiLogPlayHistoryAct)
        self.menuLogging.addSeparator()
        self.menuLogging.addAction(self.uiDebugLogAct)
        self.uiChallengeSoundMenu.addAction(self.uiMuteChallengeSoundAct)
        self.uiChallengeSoundMenu.addAction(self.uiLocateCustomChallengeSoundAct)
        self.uiChallengeSoundMenu.addSeparator()
        self.menuSetting.addAction(self.uiMuteNotifySoundAct)
        self.menuSetting.addAction(self.uiChallengeSoundMenu.menuAction())
        self.menuSetting.addAction(self.uiThemeMenu.menuAction())
        self.menuSetting.addAction(self.uiSmoothingMenu.menuAction())
        self.menuSetting.addAction(self.uiFontAct)
        self.menuSetting.addAction(self.uiCustomEmoticonsAct)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiLocateROMsAct)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.uiNotifyPlayerStateChangeAct)
        self.menuSetting.addAction(self.uiShowCountryFlagInChatAct)
        self.menuSetting.addAction(self.uiShowTimestampInChatAct)
        self.menuSetting.addAction(self.uiDisableAutoColorNicks)
        self.menuSetting.addAction(self.uiHideGamesWithoutRomAct)
        self.menuSetting.addAction(self.uiFilterFavoriteLobbies)
        self.menuSetting.addAction(self.menuLogging.menuAction())
        self.menuAbout.addAction(self.uiSRKForumAct)
        self.menuAbout.addAction(self.uiSRKWikiAct)
        self.menuAbout.addAction(self.uiJPWikiAct)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiStrevivalAct)
        self.menuAbout.addAction(self.uiHitboxViewerAct)
        self.menuAbout.addAction(self.uiSafejumpGuideAct)
        self.menuAbout.addAction(self.uiMatchVideosAct)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.uiGNGWebAct)
        self.menuAbout.addAction(self.uiAboutAct)
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.uiQuitAct, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.uiClearChatHistoryAct, QtCore.SIGNAL(_fromUtf8("triggered()")), self.uiChatHistoryTxtB.clear)
        QtCore.QObject.connect(self.uiAwayAct, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.uiAfkChk.setChecked)
        QtCore.QObject.connect(self.uiAfkChk, QtCore.SIGNAL(_fromUtf8("clicked()")), self.uiAwayAct.trigger)
        QtCore.QObject.connect(self.uiFocusOnChatAct, QtCore.SIGNAL(_fromUtf8("triggered()")), self.uiChatInputEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FightCade", None))
        self.uiEmoticonTbtn.setText(_translate("MainWindow", ":)", None))
        self.uiAfkChk.setText(_translate("MainWindow", "away", None))
        self.menuAction.setTitle(_translate("MainWindow", "&Action", None))
        self.menuSetting.setTitle(_translate("MainWindow", "S&ettings", None))
        self.uiThemeMenu.setTitle(_translate("MainWindow", "&Theme", None))
        self.uiSmoothingMenu.setTitle(_translate("MainWindow", "Smoothing / Input &lag", None))
        self.menuLogging.setTitle(_translate("MainWindow", "Logging", None))
        self.uiChallengeSoundMenu.setTitle(_translate("MainWindow", "Challenge Sound", None))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help", None))
        self.uiClearChatHistoryAct.setText(_translate("MainWindow", "Clear chat his&tory", None))
        self.uiClearChatHistoryAct.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.uiAwayAct.setText(_translate("MainWindow", "Away from k&eyboard", None))
        self.uiAwayAct.setShortcut(_translate("MainWindow", "Ctrl+E", None))
        self.uiQuitAct.setText(_translate("MainWindow", "&Quit", None))
        self.uiQuitAct.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.uiMuteChallengeSoundAct.setText(_translate("MainWindow", "&Mute Challenge Sound", None))
        self.uiMuteChallengeSoundAct.setShortcut(_translate("MainWindow", "Ctrl+M", None))
        self.uiMuteNotifySoundAct.setText(_translate("MainWindow", "Mute Notify Sound", None))
        self.uiFontAct.setText(_translate("MainWindow", "&Font", None))
        self.uiAboutAct.setText(_translate("MainWindow", "&About", None))
        self.uiStrevivalAct.setText(_translate("MainWindow", "Strategy && &News", None))
        self.uiHitboxViewerAct.setText(_translate("MainWindow", "Hitbox &Viewer", None))
        self.uiSafejumpGuideAct.setText(_translate("MainWindow", "&Safejump Guide", None))
        self.uiMatchVideosAct.setText(_translate("MainWindow", "&Match Videos", None))
        self.uiSRKForumAct.setText(_translate("MainWindow", "Shoryuken &Forum", None))
        self.uiSRKWikiAct.setText(_translate("MainWindow", "Wiki (English)", None))
        self.uiJPWikiAct.setText(_translate("MainWindow", "Wiki (Japanese)", None))
        self.uiGNGThemeAct.setText(_translate("MainWindow", "&FightCade", None))
        self.uiDarkThemeAct.setText(_translate("MainWindow", "&Dark Orange", None))
        self.uiDebugLogAct.setText(_translate("MainWindow", "Debug &Log", None))
        self.uiEmoticonAct.setText(_translate("MainWindow", "&Insert Emoticon", None))
        self.uiEmoticonAct.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.uiLocateGgpofbaAct.setText(_translate("MainWindow", "&Locate ggpofba-ng.exe", None))
        self.uiLocateROMsAct.setText(_translate("MainWindow", "Locate &ROMs Folder", None))
        self.uiLocateGeommdbAct.setText(_translate("MainWindow", "Locate &GeoIP mmdb", None))
        self.uiNotifyPlayerStateChangeAct.setText(_translate("MainWindow", "&Notify Player State Change", None))
        self.uiFocusOnChatAct.setText(_translate("MainWindow", "Foc&us on chat", None))
        self.uiFocusOnChatAct.setShortcut(_translate("MainWindow", "Ctrl+U", None))
        self.uiToggleSidebarAction.setText(_translate("MainWindow", "To&ggle Channel Sidebar", None))
        self.uiToggleSidebarAction.setShortcut(_translate("MainWindow", "Ctrl+G", None))
        self.uiExpandChannelSidebarAct.setText(_translate("MainWindow", "&+ Expand Channel Sidebar", None))
        self.uiExpandChannelSidebarAct.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.uiContractChannelSidebarAct.setText(_translate("MainWindow", "&- Contract Channel Sidebar", None))
        self.uiContractChannelSidebarAct.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.uiContractPlayerListAct.setText(_translate("MainWindow", "&> Contract Player List", None))
        self.uiContractPlayerListAct.setShortcut(_translate("MainWindow", "Ctrl+.", None))
        self.uiExpandPlayerListAct.setText(_translate("MainWindow", "&< Expand Player List", None))
        self.uiExpandPlayerListAct.setShortcut(_translate("MainWindow", "Ctrl+,", None))
        self.uiLocateUnsupportedSavestatesDirAct.setText(_translate("MainWindow", "Locate &Unsupported Savestates Directory", None))
        self.uiSyncUnsupportedSavestatesAct.setText(_translate("MainWindow", "S&ync Unsupported Savestates", None))
        self.uiSelectUnsupportedSavestateAct.setText(_translate("MainWindow", "&Select Unsupported Savestate", None))
        self.uiSelectUnsupportedSavestateAct.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.uiFireThemeAct.setText(_translate("MainWindow", "&Fire", None))
        self.uiCustomQssFileAct.setText(_translate("MainWindow", "Custom Qss File", None))
        self.uiNormalThemeAct.setText(_translate("MainWindow", "&Normal", None))
        self.action0.setText(_translate("MainWindow", "0", None))
        self.uiCustomEmoticonsAct.setText(_translate("MainWindow", "Custom &Emoticons", None))
        self.uiShowCountryFlagInChatAct.setText(_translate("MainWindow", "Show Country Flag in Chat", None))
        self.uiDisableAutoAnnounceAct.setText(_translate("MainWindow", "&Disable auto announce in unsupported room", None))
        self.uiHideGamesWithoutRomAct.setText(_translate("MainWindow", "Hide Games with Missing ROMs", None))
        self.uiShowTimestampInChatAct.setText(_translate("MainWindow", "Show Timestamp in Chat", None))
        self.uiDisableAutoColorNicks.setText(_translate("MainWindow", "Disable auto-color of Nicknames", None))
        self.uiLocateCustomChallengeSoundAct.setText(_translate("MainWindow", "Custom Challenge Sound", None))
        self.uiLogChatAct.setText(_translate("MainWindow", "Chat history", None))
        self.uiLogPlayHistoryAct.setText(_translate("MainWindow", "Play history", None))
        self.uiGNGWebAct.setText(_translate("MainWindow", "FightCade website", None))
        self.uiFilterFavoriteLobbies.setText(_translate("MainWindow", "Filter Favorite Lobbies", None))

from ggpo.gui.completionlineedit import CompletionLineEdit

# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from mastodon.Mastodon import MastodonError
from config.translations import Translations
from config.icons_pics import Icons, Pics
from config import config
from gui import login, about
from rest import toots, fetch, api, credentials
import validators
from collections import OrderedDict


class MainWindow(object):

    def __init__(self, main_window):
        self.current_session = None
        self.current_login = None
        self.config = config.Config()
        self.visibleStream = "home"
        pics = Pics()
        main_window.setWindowIcon(QtGui.QIcon(pics.appLogoImg))
        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(1153, 685)
        sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred,
                QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayoutNewToot = QtWidgets.QVBoxLayout()
        self.verticalLayoutNewToot.setSizeConstraint(
                QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutNewToot.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayoutNewToot.setObjectName("verticalLayoutNewToot")
        self.horizontalLayoutStreamButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutStreamButtons.setObjectName(
                    "horizontalLayoutStreamButtons")
        self.btnHome = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayoutStreamButtons.addWidget(self.btnHome)
        self.btnLocal = QtWidgets.QPushButton(self.centralwidget)
        self.btnLocal.setObjectName("btnLocal")
        self.horizontalLayoutStreamButtons.addWidget(self.btnLocal)
        self.btnPublic = QtWidgets.QPushButton(self.centralwidget)
        self.btnPublic.setObjectName("btnPublic")
        self.horizontalLayoutStreamButtons.addWidget(self.btnPublic)
        self.verticalLayoutNewToot.addLayout(
                self.horizontalLayoutStreamButtons)
        self.plainTextEditToot = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditToot.setObjectName("plainTextEditToot")
        self.verticalLayoutNewToot.addWidget(self.plainTextEditToot)
        self.horizontalLayoutTooButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTooButtons.setObjectName(
                "horizontalLayoutTooButtons")
        self.btnCW = QtWidgets.QPushButton(self.centralwidget)
        self.btnCW.setObjectName("btnCW")
        self.horizontalLayoutTooButtons.addWidget(self.btnCW)
        self.cmbPrivacy = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPrivacy.setObjectName("cmbPrivacy")
        self.horizontalLayoutTooButtons.addWidget(self.cmbPrivacy)
        self.btnToot = QtWidgets.QPushButton(self.centralwidget)
        self.btnToot.setObjectName("btnToot")
        self.horizontalLayoutTooButtons.addWidget(self.btnToot)
        self.verticalLayoutNewToot.addLayout(self.horizontalLayoutTooButtons)
        self.lineEditCW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCW.setObjectName("lineEditCW")
        self.verticalLayoutNewToot.addWidget(self.lineEditCW)
        self.listViewLoggedInAccounts = QtWidgets.QListView(self.centralwidget)
        self.listViewLoggedInAccounts.setObjectName("listViewLoggedInAccounts")
        self.verticalLayoutNewToot.addWidget(self.listViewLoggedInAccounts)
        self.horizontalLayout_4.addLayout(self.verticalLayoutNewToot)
        self.verticalLayoutViewToots = QtWidgets.QVBoxLayout()
        self.verticalLayoutViewToots.setObjectName("verticalLayoutViewToots")
        self.listViewToots = QtWidgets.QListView(self.centralwidget)
        self.listViewToots.setObjectName("listViewToots")
        self.listViewToots.setAlternatingRowColors(True)
        self.verticalLayoutViewToots.addWidget(self.listViewToots)
        self.horizontalLayout_4.addLayout(self.verticalLayoutViewToots)
        self.verticalLayoutNotifications = QtWidgets.QVBoxLayout()
        self.verticalLayoutNotifications.setObjectName(
                "verticalLayoutNotifications")
        self.listViewNotifications = QtWidgets.QListView(self.centralwidget)
        self.listViewNotifications.setObjectName("listViewNotifications")
        self.listViewNotifications.setAlternatingRowColors(True)
        self.verticalLayoutNotifications.addWidget(self.listViewNotifications)
        self.horizontalLayout_4.addLayout(self.verticalLayoutNotifications)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(main_window)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLogout = QtWidgets.QAction(main_window)
        self.actionLogout.setObjectName("actionLogout")
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh = QtWidgets.QAction(main_window)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionPreferences = QtWidgets.QAction(main_window)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtWidgets.QAction(main_window)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRefresh)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.listViewToots.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewToots.setWordWrap(True)
        self.listViewNotifications.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewNotifications.setWordWrap(True)
        self.listViewLoggedInAccounts.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewLoggedInAccounts.setWordWrap(True)

        self.translate_gui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_gui(self, main_window):
        lingo = Translations()
        main_title = lingo.load("MainWindow") \
            + self.config.APP_NAME \
            + " " \
            + self.config.APP_VERSION
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", main_title))

    def link_slots(self):
        self.setup_top_menu()
        self.setup_buttons()
        self.setup_tootbox()
        self.setup_login_list()

    def setup_top_menu(self):
        _translate = QtCore.QCoreApplication.translate
        lingo = Translations()
        icons = Icons()

        self.menuFile.setTitle(_translate("MainWindow",
                                          lingo.load("menuFile")))
        self.menuEdit.setTitle(_translate("MainWindow",
                                          lingo.load("menuEdit")))
        self.menuHelp.setTitle(_translate("MainWindow",
                                          lingo.load("menuHelp")))

        self.actionLogin.setText(_translate("MainWindow",
                                            lingo.load("actionLogin")))
        self.actionLogin.setShortcut(lingo.load("actionLoginShortcut"))
        self.actionLogin.setStatusTip(lingo.load("actionLoginTooltip"))
        self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginLockedIcon))
        self.actionLogin.triggered.connect(self.login_user)

        self.actionLogout.setText(_translate("MainWindow",
                                             lingo.load("actionLogout")))
        self.actionLogout.setShortcut(lingo.load("actionLogoutShortcut"))
        self.actionLogout.setStatusTip(lingo.load("actionLogoutTooltip"))
        self.actionLogout.setIcon(QtGui.QIcon(icons.actionLogoutIcon))
        self.actionLogout.setEnabled(False)
        self.actionLogout.triggered.connect(self.logoff_user)

        self.actionExit.setText(_translate("MainWindow",
                                           lingo.load("actionExit")))
        self.actionExit.setShortcut(lingo.load("actionExitShortcut"))
        self.actionExit.setStatusTip(lingo.load("actionExitTooltip")
                                     + " "
                                     + self.config.APP_NAME)
        self.actionExit.setIcon(QtGui.QIcon(icons.actionExiticon))
        self.actionExit.triggered.connect(QtGui.QGuiApplication.quit)

        self.actionRefresh.setText(_translate("MainWindow",
                                              lingo.load("actionRefresh")))
        self.actionRefresh.setShortcut(lingo.load("actionRefreshShortcut"))
        self.actionRefresh.setStatusTip(lingo.load("actionRefreshTooltip"))
        self.actionRefresh.setIcon(QtGui.QIcon(icons.actionRefreshIcon))
        self.actionRefresh.triggered.connect(self.reload_panels)

        self.actionPreferences.setText(_translate("MainWindow",
                                                  lingo.load(
                                                        "actionPreferences")))
        self.actionPreferences.setStatusTip(lingo.load(
                    "actionPreferencesTooltip"))
        self.actionPreferences.setIcon(QtGui.QIcon(icons.actionPrefIcon))
        self.actionPreferences.setEnabled(False)

        self.actionHelp.setText(_translate("MainWindow",
                                           lingo.load("actionHelp")))
        self.actionHelp.setShortcut(lingo.load("actionHelpShortcut"))
        self.actionHelp.setStatusTip(lingo.load("actionHelpTooltip"))
        self.actionHelp.setIcon(QtGui.QIcon(icons.actionHelpIcon))
        self.actionHelp.setEnabled(False)

        self.actionAbout.setText(_translate("MainWindow",
                                            lingo.load("actionAbout")))
        self.actionAbout.setStatusTip(
                lingo.load("actionAboutTooltip") + " " + self.config.APP_NAME)
        self.actionAbout.setIcon(QtGui.QIcon(icons.actionAboutIcon))
        self.actionAbout.triggered.connect(self.display_about)

    def setup_buttons(self):
        _translate = QtCore.QCoreApplication.translate
        lingo = Translations()
        icons = Icons()

        self.btnHome.setShortcut(lingo.load("btnHomeShortcut"))
        self.btnHome.setStatusTip(lingo.load("btnHomeTooltip")
                                  + " (" + lingo.load("btnHomeShortcut") + ")")
        self.btnHome.setIcon(QtGui.QIcon(icons.btnHomeIcon))
        self.btnHome.clicked.connect(self.load_stream_home)
        self.btnHome.setEnabled(False)

        self.btnLocal.setShortcut(lingo.load("btnLocalShortcut"))
        self.btnLocal.setStatusTip(lingo.load("btnLocalTooltip")
                                   + " (" + lingo.load("btnLocalShortcut")
                                   + ")")
        self.btnLocal.setIcon(QtGui.QIcon(icons.btnLocalIcon))
        self.btnLocal.clicked.connect(self.load_stream_local)
        self.btnLocal.setEnabled(False)

        self.btnPublic.setShortcut(lingo.load("btnPublicShortcut"))
        self.btnPublic.setStatusTip(lingo.load("btnPublicTooltip")
                                    + " (" + lingo.load("btnPublicShortcut")
                                    + ")")
        self.btnPublic.setIcon(QtGui.QIcon(icons.btnPublicIcon))
        self.btnPublic.clicked.connect(self.load_stream_public)
        self.btnPublic.setEnabled(False)

        self.btnCW.setText(_translate("MainWindow", lingo.load("btnCW")))
        self.btnCW.setStatusTip(lingo.load("btnCWTooltipInactive"))
        self.btnCW.clicked.connect(self.hide_show_cw)
        self.btnCW.setEnabled(False)

        self.btnToot.setText(_translate("MainWindow", lingo.load("btnToot")))
        self.btnToot.setShortcut(lingo.load("btnTootShortcut"))
        self.btnToot.setStatusTip(lingo.load("btnTootTooltip")
                                  + " (" + lingo.load("btnTootShortcut") + ")")
        self.btnToot.setEnabled(False)
        self.btnToot.clicked.connect(self.send_toot)

    def setup_tootbox(self):
        lingo = Translations()
        icons = Icons()
        self.lineEditCW.setMaxLength(self.config.GUI_TOOT_MAX_SIZE_CHARS)
        self.lineEditCW.textChanged.connect(self.check_toot_box)
        self.lineEditCW.setVisible(False)
        self.lineEditCW.setEnabled(False)

        self.plainTextEditToot.textChanged.connect(self.check_toot_box)
        self.plainTextEditToot.setEnabled(False)

        privacy_options = dict(lingo.load("cmbPrivacy"))
        self.cmbPrivacy.clear()
        self.cmbPrivacy.addItem(
                QtGui.QIcon(icons.cmbPublicToot), privacy_options["public"])
        self.cmbPrivacy.addItem(
                QtGui.QIcon(icons.cmbUnlistedToot),
                    privacy_options["unlisted"])
        self.cmbPrivacy.addItem(
                QtGui.QIcon(icons.cmbFollowerOnlyToot),
                privacy_options["private"])
        self.cmbPrivacy.addItem(
                QtGui.QIcon(icons.cmbDirectMessageToot),
                privacy_options["direct"])
        self.cmbPrivacy.setEnabled(False)

        self.listViewLoggedInAccounts.clicked.connect(self.switch_accounts)

    def check_toot_box(self):
        current_length = len(self.plainTextEditToot.toPlainText())
        max_length = self.config.GUI_TOOT_MAX_SIZE_CHARS
        if self.lineEditCW.isEnabled():
            max_length -= len(self.lineEditCW.text())
        self.btnToot.setEnabled(0 < current_length < max_length)

        if current_length >= max_length:
            self.plainTextEditToot.setStyleSheet("color: rgb(206, 92, 92);")
        else:
            self.plainTextEditToot.setStyleSheet("")

    def hide_show_cw(self):
        if self.lineEditCW.isEnabled():
            self.lineEditCW.setVisible(False)
            self.lineEditCW.setEnabled(False)
        else:
            self.lineEditCW.setEnabled(True)
            self.lineEditCW.setVisible(True)

    def setup_login_list(self):
        model = QtGui.QStandardItemModel(self.listViewLoggedInAccounts)
        users_and_domains = api.get_existing_users_and_domains()
        self.listViewLoggedInAccounts.setEnabled(False)
        self.listViewLoggedInAccounts.reset()

        if users_and_domains is not None:
            self.listViewLoggedInAccounts.setEnabled(False)
            self.listViewLoggedInAccounts.reset()

            for domain, users in list(users_and_domains.items()):
                for user in users:
                    item = QtGui.QStandardItem()
                    item.setText(domain + " | " + user)
                    check_registered = api.Credentials(domain, user)
                    if check_registered.is_client_registered():
                        model.appendRow(item)
                    else:
                        check_registered.client_unregister()

            self.listViewLoggedInAccounts.setModel(model)
            self.listViewLoggedInAccounts.setEnabled(True)

    def switch_accounts(self):
        attempted_login = self.listViewLoggedInAccounts.currentIndex().data()

        if attempted_login == self.current_login:
            self.reload_panels()
            self.plainTextEditToot.setFocus(True)
        else:
            domain, user = attempted_login.replace(" ", "").split("|")
            login_attempt = credentials.Credentials(domain, user)

            if login_attempt.is_user_registered():
                try:
                    new_session = api.Session(domain, user)
                    new_session.initialise_session("")
                    self.current_session = new_session
                    self.update_ui_new_login()
                    self.current_login = attempted_login
                except MastodonError as m:
                    print(type(m))
                    raise
                self.update_ui_new_login()
            else:
                self.login_user(domain, user)

    def display_about(self):
        about_dialog = QtWidgets.QDialog()
        about_dialog.ui = about.ui_dialog_about()
        about_dialog.ui.setupUi(about_dialog)
        about_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        about_dialog.exec_()

    def login_user(self, server_url="", user_name=""):
        dialog = QtWidgets.QDialog()
        dialog.ui = login.ui_login_dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.ui.set_domain_and_user(server_url, user_name)
        dialog.accepted.connect(lambda: self.complete_login(dialog))
        dialog.rejected.connect(self.cancelled_login)
        dialog.destroyed.connect(lambda: self.check_login_status(dialog))
        dialog.exec_()

    def complete_login(self, dialog):
        self.current_session = dialog.ui.get_new_session()
        if self.current_session is not None:
            self.setup_login_list()
            self.update_ui_new_login()
            self.current_login = dialog.ui.logged_in_domain \
                                 + " | " + dialog.ui.logged_in_user

    def update_ui_new_login(self):
        icons = Icons()
        self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginUnlockedIcon))
        self.actionLogout.setEnabled(True)
        self.btnToot.setEnabled(True)
        self.btnCW.setEnabled(True)
        self.cmbPrivacy.setEnabled(True)
        self.set_privacy_selection(self.current_session.get_account_default_privacy())
        self.plainTextEditToot.setEnabled(True)
        self.plainTextEditToot.setFocus(True)
        self.reload_panels()
        self.enable_correct_stream_button()

    def cancelled_login(self):
        print("cancelled login triggered")

    def check_login_status(self, dialog):
        problem = dialog.ui.get_latest_exception()
        if problem is not None:
            error_msg = QtWidgets.QErrorMessage()
            error_msg.showMessage(str(problem))
            error_msg.exec_()

    def logoff_user(self):
        if self.current_session is not None:
            existing_session = api.Session(
                self.current_session.get_session_domain(),
                self.current_session.get_session_username())
            existing_session.load_session(self.current_session)
            existing_session.clear_session()
            self.current_session = None
            self.current_login = None
            self.actionLogout.setEnabled(False)
            self.actionLogin.setEnabled(True)
            icons = Icons()
            self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginLockedIcon))
            self.btnToot.setEnabled(False)
            self.btnCW.setEnabled(False)
            self.cmbPrivacy.setEnabled(False)
            self.reset_panels()
            fetch.clear_image_cache()

    def reload_panels(self):
        if self.current_session is not None:
            self.load_stream_notifications()
            if self.visibleStream == "home":
                self.load_stream_home()
            elif self.visibleStream == "local":
                self.load_stream_local()
            elif self.visibleStream == "public":
                self.load_stream_public()

    def reset_panels(self):
        notifications_model = QtGui.QStandardItemModel(
            self.listViewNotifications)
        toots_model = QtGui.QStandardItemModel(self.listViewToots)
        self.listViewNotifications.setModel(notifications_model)
        self.listViewToots.setModel(toots_model)

    def load_stream_home(self):
        if self.current_session is not None:
            self.visibleStream = "home"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_home_stream())
            self.enable_correct_stream_button()

    def load_stream_local(self):
        if self.current_session is not None:
            self.visibleStream = "local"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_local_stream())
            self.enable_correct_stream_button()

    def load_stream_public(self):
        if self.current_session is not None:
            self.visibleStream = "public"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_public_stream())
            self.enable_correct_stream_button()

    def send_toot(self):
        if self.current_session is not None:
            self.btnToot.setEnabled(False)
            self.btnCW.setEnabled(False)
            potential_toot = str(self.plainTextEditToot.toPlainText())
            potential_cw = ""
            if self.lineEditCW.isVisible():
                potential_cw = self.lineEditCW.text()
            if validators.length(potential_toot + potential_cw,
                                 max=self.config.GUI_TOOT_MAX_SIZE_CHARS):
                privacy_level = self.get_privacy_selection()
                self.current_session.send_toot(
                    potential_toot, privacy_level, potential_cw)
            else:
                raise ValueError
            self.plainTextEditToot.clear()
            self.lineEditCW.clear()
            self.reload_panels()
            self.btnToot.setEnabled(True)
            self.btnCW.setEnabled(True)
            if self.lineEditCW.isVisible():
                self.hide_show_cw()

    def disable_all_stream_buttons(self):
        self.btnHome.setEnabled(False)
        self.btnLocal.setEnabled(False)
        self.btnPublic.setEnabled(False)

    def enable_correct_stream_button(self):
        self.btnHome.setEnabled(self.visibleStream is not "home")
        self.btnLocal.setEnabled(self.visibleStream is not "local")
        self.btnPublic.setEnabled(self.visibleStream is not "public")

    def load_stream_toots(self, toot_stream):
        if self.current_session is not None:
            lingo = Translations()
            model = QtGui.QStandardItemModel(self.listViewToots)
            stream_to_load = toots.Toots(toot_stream)
            stream_to_load.process()
            toot_stream = OrderedDict(stream_to_load.get_toots().items())

            for timestamp in toot_stream:
                toot = toot_stream[timestamp]
                image_alt_text = ""
                content_warning = ""
                if toot.has_media():
                    image_alt_text = self.get_image_alt_text(toot.get_media())
                if toot.has_cw():
                    content_warning = self.get_cw_text(toot.get_cw())
                item = QtGui.QStandardItem()
                new_item = QtGui.QStandardItem()
                icon = QtGui.QIcon()
                image = QtGui.QImage()
                title_font = item.font()
                title_font.setBold(True)
                item.setFont(title_font)
                if toot.is_boost():
                    boosted_toot = toot.get_boost()
                    if boosted_toot.has_media():
                        image_alt_text = self.get_image_alt_text(boosted_toot.get_media())
                    if boosted_toot.has_cw():
                        content_warning = self.get_cw_text(boosted_toot.get_cw())
                    image.load(fetch.get_image(boosted_toot.get_avatar()))
                    item.setText(boosted_toot.get_display_name()
                                 + " <" + boosted_toot.get_full_handle() + ">"
                                 + " [" + boosted_toot.get_timestamp() + "]")
                    new_item.setText(
                        content_warning
                        + boosted_toot.get_content().rstrip() + image_alt_text
                        + "\n\n" + lingo.load("stream_boost_fetched")
                        + ": " + toot.get_display_name()
                        + " <" + toot.get_full_handle() + ">"
                        + " (" + toot.get_timestamp() + ")")
                else:
                    image.load(fetch.get_image(toot.get_avatar()))
                    item.setText(toot.get_display_name()
                                 + " <" + toot.get_full_handle() + ">"
                                 + " [" + toot.get_timestamp() + "]")
                    new_item.setText(content_warning
                                     + toot.get_content().rstrip()
                                     + image_alt_text)
                icon.addPixmap(QtGui.QPixmap(image),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                model.appendRow(item)
                model.appendRow(new_item)
            self.listViewToots.setModel(model)

    def load_stream_notifications(self):
        if self.current_session is not None:
            lingo = Translations()
            model = QtGui.QStandardItemModel(self.listViewNotifications)

            notifications = OrderedDict(self.current_session.get_notifications().items())
            for timestamp in notifications:
                notification = notifications[timestamp]
                item = QtGui.QStandardItem()
                new_item = QtGui.QStandardItem()
                title_font = item.font()
                title_font.setBold(True)
                own_toot_font = item.font()
                own_toot_font.setItalic(True)
                item.setFont(title_font)
                item.setIcon(self.fetch_avatar(notification.get_avatar()))
                content_text = ""
                title_text = ""
                image_alt_text = ""
                start_title = notification.get_display_name() + " <" \
                              + notification.get_full_handle() + "> "

                if notification.n_type == "follow":
                    title_text = start_title + lingo.load("notify_follow") + "."
                else:
                    if notification.has_cw():
                        content_text = self.get_cw_text(notification.get_cw())

                    if notification.has_media():
                        image_alt_text = self.get_image_alt_text(notification.get_media())

                    content_text += notification.get_content().rstrip() + image_alt_text
                    new_item.setFont(own_toot_font)

                    if notification.n_type == "reblog":
                        title_text = start_title + lingo.load("notify_reblog") + ":"
                    elif notification.n_type == "favourite":
                        title_text = start_title + lingo.load("notify_fav") + ":"
                    elif notification.n_type == "mention":
                        title_text = start_title + "[" + notification.get_timestamp() \
                                     + "]:"

                item.setText(title_text)
                model.appendRow(item)
                new_item.setText(content_text)
                model.appendRow(new_item)
            self.listViewNotifications.setModel(model)

    def get_image_alt_text(self, all_media):
        for entry_image in all_media:
            description = entry_image['description']
            if description is None:
                description = "Missing alt text"
            return "\n\n" + entry_image['type'] + ": " + description

    def get_cw_text(self, cw_text):
        return "=== CW: " + cw_text + " ===\n\n"

    def fetch_avatar(self, avatar_text):
        icon = QtGui.QIcon()
        image = QtGui.QImage()

        image.load(fetch.get_image(avatar_text))
        icon.addPixmap(QtGui.QPixmap(image),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def get_privacy_selection(self):
        lingo = Translations()
        selected_privacy_level = self.cmbPrivacy.currentText()
        for privacy_level, privacy_text in dict(lingo.load("cmbPrivacy")).items():
            if privacy_text == selected_privacy_level:
                return privacy_level

    def set_privacy_selection(self, selected_privacy_level):
        if selected_privacy_level is not None:
            lingo = Translations()
            for privacy_level, privacy_text in dict(lingo.load("cmbPrivacy")).items():
                if privacy_level == selected_privacy_level:
                    index = self.cmbPrivacy.findText(privacy_text)
                    if index > -1:
                        self.cmbPrivacy.setCurrentIndex(index)

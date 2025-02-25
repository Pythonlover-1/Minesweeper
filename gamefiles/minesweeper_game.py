import sys
import sqlite3
import random
import csv
from sys import flags

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QButtonGroup,
)
from PyQt6.QtGui import QIcon, QColor, QPalette, QBrush, QPixmap, QFont
from PyQt6.QtWidgets import (
    QTableWidgetItem,
    QMessageBox,
    QInputDialog,
    QListWidgetItem,
)
from PyQt6.QtCore import Qt, QTimer, QSize


class MinesweeperMainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_main_menu.ui", self)

        '''
        Не буду дублировать это замечание далее, скажу с самого начала:
        Зачем тут CAPS? :)
        Если хотелось сделать константу, надо было вынести из тела метода,
        иначе не называть переменную CAPS'ом
        '''
        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture1.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.start_the_game_button.setIcon(QIcon("./pictures/play_button.png"))
        self.start_the_game_button.setIconSize(QSize(150, 150))
        self.settings_button.setIcon(QIcon("./pictures/settings.png"))
        self.settings_button.setIconSize(QSize(100, 100))
        self.exit_button.setIcon(QIcon("./pictures/exit.png"))
        self.exit_button.setIconSize(QSize(100, 100))
        self.leaderboard_button.setIcon(QIcon("./pictures/leaderboard.png"))
        self.leaderboard_button.setIconSize(QSize(200, 200))
        self.achievements_button.setIcon(QIcon("./pictures/achievements.png"))
        self.achievements_button.setIconSize(QSize(200, 200))
        self.peoples_button.setIcon(QIcon("./pictures/peoples.png"))
        self.peoples_button.setIconSize(QSize(200, 200))

        self.peoples_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.achievements_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.leaderboard_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.exit_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.settings_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.start_the_game_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.settings_button.clicked.connect(self.open_settings_chapter)
        self.leaderboard_button.clicked.connect(self.open_leaderboard_chapter)
        self.start_the_game_button.clicked.connect(self.open_game_chapter)
        self.achievements_button.clicked.connect(self.open_achievements_chapter)
        self.exit_button.clicked.connect(self.confirm_exit)
        self.peoples_button.clicked.connect(self.open_peoples_chapter)

    def open_peoples_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        '''
        Опять же, скажу один раз тут, но это относится ко всем подобным конструкциям далее
        Добавлять атрибуты класса прямо во время исполнения -- плохая практика. 
        Я бы задавал для MINESWEEPER_PEOPLES (вопрос почему оно названо СAPS'ом остаётся) 
        какое-нибудь дефолтное значение при создании объекта
        '''
        if not hasattr(self, "minesweeper_peoples"):
            self.MINESWEEPER_PEOPLES = MinesweeperPeoples()
        self.MINESWEEPER_PEOPLES.open_window(frame_x, frame_y)

    def confirm_exit(self):
        REPLY = QMessageBox.question(
            self,
            "Подтверждение",
            "Вы уверены, что желаете выйти?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if REPLY == QMessageBox.StandardButton.Yes:
            self.close()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_achievements_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_achievements"):
            self.minesweeper_achievements = MinesweeperAchievements()
        self.minesweeper_achievements.open_window(frame_x, frame_y)

    def open_settings_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_settings"):
            self.MINESWEEPER_SETTINGS = MinesweeperSettings()
        self.MINESWEEPER_SETTINGS.open_window(frame_x, frame_y)

    def open_leaderboard_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_leaderboard"):
            self.MINESWEEPER_LEADERBOARD = MinesweeperLeaderboard()
        self.MINESWEEPER_LEADERBOARD.open_window(frame_x, frame_y)

    def open_game_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_game"):
            self.MINESWEEPER_GAME = MinesweeperGame()
        self.MINESWEEPER_GAME.open_window(frame_x, frame_y)


class MinesweeperSettings(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_settings.ui", self)

        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture2.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.to_main_menu_button.clicked.connect(self.open_main_menu_chapter)

        self.game_difficulty_group = QButtonGroup()
        self.game_difficulty_group.addButton(self.beginner_radiobutton)
        self.game_difficulty_group.addButton(self.professional_radiobutton)

        self.game_mode_group = QButtonGroup()
        self.game_mode_group.addButton(self.timed_radiobutton)
        self.game_mode_group.addButton(self.casual_radiobutton)

        self.clue_group = QButtonGroup()
        self.clue_group.addButton(self.clue_on_radiobutton)
        self.clue_group.addButton(self.clue_off_radiobutton)

        self.beginner_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )
        self.professional_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )
        self.timed_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )
        self.casual_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )
        self.clue_on_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )
        self.clue_off_radiobutton.setStyleSheet(
            "QRadioButton::indicator { width: 0px; height: 0px; }"
        )

        self.beginner_radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.professional_radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.timed_radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.casual_radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.clue_on_radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.clue_off_radiobutton.toggled.connect(self.on_radio_button_toggled)

        self.apply_settings_button.setIcon(QIcon("./pictures/apply.png"))
        self.apply_settings_button.setIconSize(QSize(170, 170))
        self.to_main_menu_button.setIcon(QIcon("./pictures/exit.png"))
        self.to_main_menu_button.setIconSize(QSize(100, 100))

        self.apply_settings_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.to_main_menu_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        con = sqlite3.connect("minesweeper.sqlite")
        cur = con.cursor()

        RESULT = cur.execute(
            """
        SELECT
            game_difficulty, game_mode, clue
        FROM
            settings
        WHERE key=0
        """
        ).fetchall()

        game_difficulty, game_mode, clue = RESULT[0]

        '''
        :NOTE:
         Лично я вынес бы проставление "галочек" на кнопках в отдельную функцию,
         но так тоже можно
        '''
        BUTTON_GROUP = [
            self.game_difficulty_group,
            self.game_mode_group,
            self.clue_group,
        ]

        result_values = [game_difficulty, game_mode, clue]

        for i, button_group in enumerate(BUTTON_GROUP):
            for button in button_group.buttons():
                if button.text() == result_values[i]:
                    button.setChecked(True)
                    break
        con.commit()
        con.close()

        self.apply_settings_button.clicked.connect(self.save_settings)

    def save_settings(self):
        CON = sqlite3.connect("minesweeper.sqlite")
        CUR = CON.cursor()

        clue = self.clue_group.checkedButton().text()  # неиспользуемая переменная

        CUR.execute(
            """
        UPDATE
            settings
        SET
            game_difficulty = ?,
            game_mode = ?,
            clue = ?
        WHERE
            key = 0
        """,
            (
                self.game_difficulty_group.checkedButton().text(),
                self.game_mode_group.checkedButton().text(),
                self.clue_group.checkedButton().text(),
            ),
        )

        CON.commit()
        CON.close()

    '''
    Эта функция -- сплошная copy-paste.
    Следовало вынести 

    if <какая-то radiobutton>.isChecked():
        <какая-то radiobutton>.setIcon(QIcon("./pictures/dot2.png"))
        <вторая radiobutton>.setIcon(QIcon("./pictures/dot1.png"))
    else:
        <какая-то radiobutton>.setIcon(QIcon("./pictures/dot1.png"))
        <вторая radiobutton>.setIcon(QIcon("./pictures/dot2.png"))

    в отдельную функцию (возможно переписал бы эту конструкцию) и вызывать для нужных кнопок
    '''

    def on_radio_button_toggled(self):
        if self.beginner_radiobutton.isChecked():
            self.beginner_radiobutton.setIcon(QIcon("./pictures/dot2.png"))
            self.professional_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
        else:
            self.beginner_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
            self.professional_radiobutton.setIcon(QIcon("./pictures/dot2.png"))

        if self.timed_radiobutton.isChecked():
            self.timed_radiobutton.setIcon(QIcon("./pictures/dot2.png"))
            self.casual_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
        else:
            self.timed_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
            self.casual_radiobutton.setIcon(QIcon("./pictures/dot2.png"))

        if self.clue_on_radiobutton.isChecked():
            self.clue_on_radiobutton.setIcon(QIcon("./pictures/dot2.png"))
            self.clue_off_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
        else:
            self.clue_on_radiobutton.setIcon(QIcon("./pictures/dot1.png"))
            self.clue_off_radiobutton.setIcon(QIcon("./pictures/dot2.png"))

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_main_menu_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_main_menu"):
            self.MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
        self.MINESWEEPER_MAIN_MENU.open_window(frame_x, frame_y)


class MinesweeperLeaderboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_leaderboard.ui", self)

        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture2.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.to_main_menu_button.setIcon(QIcon("./pictures/exit.png"))
        self.to_main_menu_button.setIconSize(QSize(100, 100))
        self.update_leaderboard_button.setIcon(QIcon("./pictures/update table.png"))
        self.update_leaderboard_button.setIconSize(QSize(130, 130))

        self.to_main_menu_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.update_leaderboard_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.choose_field_size.addItem("Beginner")
        self.choose_field_size.addItem("Professional")

        self.to_main_menu_button.clicked.connect(self.open_main_menu_chapter)
        self.update_leaderboard_button.clicked.connect(self.load_leaderboard_data)

    def load_leaderboard_data(self):
        selected_text = self.choose_field_size.currentText()

        CON = sqlite3.connect("minesweeper.sqlite")
        CUR = CON.cursor()

        RESULT = CUR.execute(
            f"""
        SELECT
            nickname, time
        FROM
            leaders
        WHERE
            field_size=?
        ORDER BY
            time
        """,
            (selected_text,),
        ).fetchall()

        CON.close()

        if not RESULT:
            self.label_result_of_search_table_widget.setText(
                "Unfortunately, nothing was found"
            )
            self.leaderboard_table_widget.setRowCount(0)
        else:
            self.label_result_of_search_table_widget.setText("")
            self.leaderboard_table_widget.setColumnCount(len(RESULT[0]) + 1)
            self.leaderboard_table_widget.setRowCount(len(RESULT))

            self.leaderboard_table_widget.setHorizontalHeaderLabels(
                ["Position", "Nickname", "Time"]
            )

            self.leaderboard_table_widget.verticalHeader().setVisible(False)

            self.leaderboard_table_widget.setColumnWidth(0, 80)
            self.leaderboard_table_widget.setColumnWidth(1, 200)
            self.leaderboard_table_widget.setColumnWidth(2, 118)

            for i, elem in enumerate(RESULT):
                position_item = QTableWidgetItem(str(i + 1))
                position_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.leaderboard_table_widget.setItem(i, 0, position_item)

                for j, val in enumerate(elem):
                    item = QTableWidgetItem(str(val))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.leaderboard_table_widget.setItem(i, j + 1, item)

                if i == 0:
                    color = QColor(255, 215, 0)
                elif i == 1:
                    color = QColor(192, 192, 192)
                elif i == 2:
                    color = QColor(204, 127, 51)
                else:
                    color = QColor(255, 255, 255)

                for col in range(self.leaderboard_table_widget.columnCount()):
                    self.leaderboard_table_widget.item(i, col).setBackground(color)

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_main_menu_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_main_menu"):
            self.MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
        self.MINESWEEPER_MAIN_MENU.open_window(frame_x, frame_y)


class MinesweeperGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_game.ui", self)

        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture2.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.clue_button.setIcon(QIcon("./pictures/clue.png"))
        self.clue_button.setIconSize(QSize(130, 130))
        self.restart_game_button.setIcon(QIcon("./pictures/restart.png"))
        self.restart_game_button.setIconSize(QSize(130, 130))
        self.install_flag_button.setIcon(QIcon("./pictures/flag.png"))
        self.install_flag_button.setIconSize(QSize(150, 150))
        self.to_main_menu_button.setIcon(QIcon("./pictures/exit.png"))
        self.to_main_menu_button.setIconSize(QSize(100, 100))

        self.clue_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.restart_game_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.install_flag_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.to_main_menu_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.label.hide()

        self.to_main_menu_button.clicked.connect(self.open_main_menu_chapter)

        CON = sqlite3.connect("minesweeper.sqlite")
        CUR = CON.cursor()

        RESULT = CUR.execute(
            """
        SELECT
            game_difficulty, game_mode, clue
        FROM
            settings
        WHERE
            key=0
        """
        ).fetchall()

        game_difficulty, game_mode, clue = RESULT[0][0], RESULT[0][1], RESULT[0][2]

        SETTINGS_FOR_START_THE_GAME = {
            "Beginner": [5, 4],
            "Professional": [10, 16],
        }  # это какая-то константа, не стоило делать её локальной переменной

        self.field_size_and_count_mines = SETTINGS_FOR_START_THE_GAME[game_difficulty]

        self.COUNT_MINES = self.field_size_and_count_mines[1]

        # copy-paste, нужно было вынести генерацию поля в отдельную переменную
        self.revealed = [
            [False for _ in range(self.field_size_and_count_mines[0])]
            for _ in range(self.field_size_and_count_mines[0])
        ]
        self.flags = [
            [False for _ in range(self.field_size_and_count_mines[0])]
            for _ in range(self.field_size_and_count_mines[0])
        ]

        if self.field_size_and_count_mines[0] == 5:
            width, height = 60, 60
            shift = 80
            x, y = 50, 120
        else:
            width, height = 30, 30
            shift = 40
            x, y = 50, 50

        self.buttons = []
        self.flags_positions = []

        for i in range(self.field_size_and_count_mines[0]):  # :NOTE: можно _ вместо i (всё равно не исползуется)
            row_buttons = []
            for j in range(self.field_size_and_count_mines[0]):  # :NOTE: аналогично можно _ вместо j
                button = QPushButton(self)

                font = QFont("Arial Black", 11)
                button.setFont(font)

                button.resize(width, height)
                button.move(x, y)
                row_buttons.append(button)

                button.setIcon(QIcon("./pictures/field.png"))
                button.setIconSize(QSize(self.choose_size(), self.choose_size()))

                button.setStyleSheet(
                    """
                            QPushButton {
                                color: black;
                                border: none;
                                padding: 0px;
                                margin: 0px;
                            }
                        """
                )
                x += shift
            y += shift
            x = 50
            self.buttons.append(row_buttons)

        self.first_move = True
        self.flag_setting_mode = False

        self.install_flag_button.setEnabled(False)
        self.clue_button.setEnabled(False)

        self.install_flag_button.clicked.connect(self.change_click_mode)

        for row_index, row in enumerate(self.buttons):
            for col_index, button in enumerate(row):
                button.clicked.connect(
                    lambda _, r=row_index, c=col_index: self.on_button_click(r, c)
                )

        self.update_clue_button(clue)

        self.restart_game_button.clicked.connect(self.restart_game)
        self.clue_button.clicked.connect(self.show_mine)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time_elapsed = 0

    def on_button_click(self, row, col):
        button = self.buttons[row][col]

        if self.first_move:
            self.init_mines(row, col)

            self.first_move = False
            count = self.count_adjacent_mines(row, col)
            button.setText(f"{count}")
            button.setEnabled(False)
            button.setIcon(QIcon())
            self.revealed[row][col] = True

            self.install_flag_button.setEnabled(True)

            result = self.get_data_from_sqlite()
            if result[0][1] == "Casual":
                self.clue_button.setEnabled(True)
            else:
                self.label.show()
                self.start_timer()

        elif self.flag_setting_mode:
            self.toggle_flag(row, col)
            if (row, col) in self.MINES_POSITIONS and (row, col) not in flags:
                self.flags_positions.append((row, col))
                if self.get_data_from_sqlite()[0][1] == "Timed":
                    (
                        count_wins,
                        beginner_level,
                        professional_level,
                        count_defused_mines,
                    ) = self.get_data_from_table()
                    count_defused_mines = str(int(count_defused_mines) + 1)
                    self.write_data_to_table(
                        [
                            count_wins,
                            beginner_level,
                            professional_level,
                            count_defused_mines,
                        ]
                    )
                    count = self.count_true(self.revealed)

                    if (
                            count + self.field_size_and_count_mines[1]
                            == self.field_size_and_count_mines[0] ** 2
                    ):

                        self.stop_timer()
                        self.disable_all_buttons()
                        self.game_win_over_label.setText("You have won!")

                        result = self.get_data_from_sqlite()
                        if result[0][1] == "Timed":
                            name = self.get_user_name()
                            field_size = result[0][0]
                            self.write_data_to_sqlite(name, field_size)

                            (
                                count_wins,
                                beginner_level,
                                professional_level,
                                count_defused_mines,
                            ) = self.get_data_from_table()
                            count_wins = str(int(count_wins) + 1)

                            if result[0][0] == "Beginner":
                                beginner_level = "yes"
                            elif result[0][0] == "Professional":
                                professional_level = "yes"

                            self.write_data_to_table(
                                [
                                    count_wins,
                                    beginner_level,
                                    professional_level,
                                    count_defused_mines,
                                ]
                            )


        elif button.text() == "F":
            pass

        elif (row, col) not in self.MINES_POSITIONS:
            count = self.count_adjacent_mines(row, col)
            button.setText(f"{count}")
            button.setEnabled(False)
            button.setIcon(QIcon())
            self.revealed[row][col] = True
            count = self.count_true(self.revealed)

            if (
                    count + self.field_size_and_count_mines[1]
                    == self.field_size_and_count_mines[0] ** 2
            ):

                self.stop_timer()
                self.disable_all_buttons()
                self.game_win_over_label.setText("You have won!")

                result = self.get_data_from_sqlite()
                if result[0][1] == "Timed":
                    name = self.get_user_name()
                    field_size = result[0][0]
                    self.write_data_to_sqlite(name, field_size)

                    (
                        count_wins,
                        beginner_level,
                        professional_level,
                        count_defused_mines,
                    ) = self.get_data_from_table()
                    count_wins = str(int(count_wins) + 1)

                    if result[0][0] == "Beginner":
                        beginner_level = "yes"
                    elif result[0][0] == "Professional":
                        professional_level = "yes"

                    self.write_data_to_table(
                        [
                            count_wins,
                            beginner_level,
                            professional_level,
                            count_defused_mines,
                        ]
                    )

        elif (row, col) in self.MINES_POSITIONS:
            self.stop_timer()
            self.disable_all_buttons()
            self.game_win_over_label.setText("You have lost")
            self.show_mines()

    def choose_size(self):  # почему бы не сделать тернарник?
        if self.get_data_from_sqlite()[0][0] == "Beginner":
            return 100
        else:
            return 50

    def write_data_to_sqlite(self, name, field_size):
        con = sqlite3.connect("minesweeper.sqlite")
        cur = con.cursor()
        cur.execute(
            """
        INSERT INTO
            leaders (nickname, time, field_size)
        VALUES
            (?, ?, ?)        
        """,
            (name, self.timer_label.text(), field_size),
        )
        con.commit()

    def get_user_name(self):  # :NOTE: можно было сделать @staticmethod
        while True:
            name, ok = QInputDialog.getText(QWidget(), "Введите ваше имя", "Ваше имя:")
            if ok and name:
                return name
            elif not ok:
                continue

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def update_time(self):
        self.time_elapsed += 1
        self.timer_label.setText(str(self.time_elapsed))

    def reset_timer(self):
        self.timer.stop()
        self.time_elapsed = 0
        self.timer_label.setText(str(self.time_elapsed))

    def get_data_from_sqlite(self):
        CON = sqlite3.connect("minesweeper.sqlite")
        CUR = CON.cursor()

        RESULT = CUR.execute(
            """
        SELECT
            game_difficulty, game_mode
        FROM
            settings
        WHERE
            key=0
        """
        ).fetchall()
        return RESULT

    def get_data_from_table(self):  # :NOTE: можно было сделать @staticmethod
        with open("achievements.csv", "r", encoding="utf8") as csvfile:
            result = list(csv.reader(csvfile, delimiter=";", quotechar='"'))
            return [result[0][1], result[1][1], result[2][1], result[3][1]]

    def write_data_to_table(self, lst):  # :NOTE: можно было сделать @staticmethod
        with open("achievements.csv", "w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(["count_wins", lst[0]])
            writer.writerow(["beginner_level", lst[1]])
            writer.writerow(["professional_level", lst[2]])
            writer.writerow(["count_defused_mines", lst[3]])

    def show_mine(self):
        if self.clues_positions:
            coordinates = random.choice(self.clues_positions)
            for item in self.clues_positions:
                if item == coordinates:
                    self.clues_positions.remove(coordinates)
            self.buttons[coordinates[0]][coordinates[1]].setIcon(
                QIcon("./pictures/mine.png")
            )
            self.buttons[coordinates[0]][coordinates[1]].setIconSize(
                QSize(self.choose_size(), self.choose_size())
            )

            self.buttons[coordinates[0]][coordinates[1]].setStyleSheet(
                """
                        QPushButton {
                            border: none;
                            padding: 0px;
                            margin: 0px;
                        }
                    """
            )

    def show_mines(self):
        for item in self.MINES_POSITIONS:
            self.buttons[item[0]][item[1]].setIcon(QIcon("./pictures/mine.png"))
            self.buttons[item[0]][item[1]].setIconSize(
                QSize(self.choose_size(), self.choose_size())
            )

            self.buttons[item[0]][item[1]].setStyleSheet(
                """
                        QPushButton {
                            border: none;
                            padding: 0px;
                            margin: 0px;
                        }
                    """
            )

    def count_true(self, lst):  # :NOTE: можно было сделать @staticmethod
        count = 0
        for sublist in lst:
            for item in sublist:
                if item:
                    count += 1
        return count

    def restart_game(self):
        self.clue_button.setEnabled(False)
        self.install_flag_button.setEnabled(False)
        self.first_move = True
        self.MINES_POSITIONS, self.clues_positions = [], []
        # уже говорил про отдельную функцию для заполнения поля
        self.revealed = [
            [False for _ in range(self.field_size_and_count_mines[0])]
            for _ in range(self.field_size_and_count_mines[0])
        ]
        self.game_win_over_label.setText("")

        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][j].setIcon(QIcon("./pictures/field.png"))
                self.buttons[i][j].setIconSize(
                    QSize(self.choose_size(), self.choose_size())
                )

                self.buttons[i][j].setStyleSheet(
                    """
                            QPushButton {
                                color: black;
                                border: none;
                                padding: 0px;
                                margin: 0px;
                            }
                        """
                )

        result = self.get_data_from_sqlite()
        if result[0][1] == "Timed":
            self.reset_timer()

        for row in self.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)

    def toggle_flag(self, row, col):
        if not self.revealed[row][col]:
            if self.buttons[row][col].text() == "F":
                self.buttons[row][col].setText("")
                self.buttons[row][col].setIcon(QIcon("./pictures/field.png"))
                self.buttons[row][col].setIconSize(
                    QSize(self.choose_size(), self.choose_size())
                )

                self.buttons[row][col].setStyleSheet(
                    """
                            QPushButton {
                                border: none;
                                padding: 0px;
                                margin: 0px;
                            }
                        """
                )
            else:
                self.buttons[row][col].setText("F")
                self.buttons[row][col].setIcon(QIcon("./pictures/flag.png"))
                self.buttons[row][col].setIconSize(
                    QSize(self.choose_size(), self.choose_size())
                )

                self.buttons[row][col].setStyleSheet(
                    """
                            QPushButton {
                                border: none;
                                padding: 0px;
                                margin: 0px;
                            }
                        """
                )
            self.flags[row][col] = not self.flags[row][col]

    '''
    Эту функцию можно было бы написать в 1 строку :)
    def change_click_mode(self):
        self.flag_setting_mode = not self.flag_setting_mode
    '''

    def change_click_mode(self):
        if self.flag_setting_mode:
            self.flag_setting_mode = False
        else:
            self.flag_setting_mode = True

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)
                button.setStyleSheet(
                    """
                    QPushButton {
                        color: black;
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                    QPushButton:disabled {
                        color: gray;
                    }
                    """
                )

    '''
    Сомнительное решение, чтобы возвращаемое значение у функции было по типу Union[str, int].
    Почему бы всегда не возвращать число и уже где-то дальше обрабатывать случай с 0?
    '''

    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(
                max(0, row - 1), min(self.field_size_and_count_mines[0], row + 2)
        ):
            for c in range(
                    max(0, col - 1), min(self.field_size_and_count_mines[0], col + 2)
            ):
                if (r, c) in self.MINES_POSITIONS:
                    count += 1
        if count == 0:
            return ""
        return count

    def init_mines(self, first_move_row, first_move_col):
        positions = [
            (r, c)
            for r in range(self.field_size_and_count_mines[0])
            for c in range(self.field_size_and_count_mines[0])
            if r != first_move_row or c != first_move_col
        ]
        # :NOTE: в идеале было бы реализовать какой-нибудь алгоритм хитрее, чем обычный рандом
        # P.S. при рандоме бывают "нерешаемые" случаи
        self.MINES_POSITIONS = random.sample(positions, self.COUNT_MINES)
        self.clues_positions = self.MINES_POSITIONS[:]

    def update_clue_button(self, clue):
        if clue == "Off":
            self.clue_button.hide()
        else:
            self.clue_button.show()

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_main_menu_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_main_menu"):
            self.MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
        self.MINESWEEPER_MAIN_MENU.open_window(frame_x, frame_y)


class MinesweeperAchievements(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_achievements.ui", self)

        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture2.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.to_main_menu_button.setIcon(QIcon("./pictures/exit.png"))
        self.to_main_menu_button.setIconSize(QSize(100, 100))

        self.to_main_menu_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.win_game_cb.setDisabled(True)
        self.complete_all_difificulty_levels_cb.setDisabled(True)
        self.mark_mines_cb.setDisabled(True)

        self.win_game_cb.setStyleSheet(
            """
            QCheckBox:disabled {
                color: black;
            }
            """
        )
        self.complete_all_difificulty_levels_cb.setStyleSheet(
            """
            QCheckBox:disabled {
                color: black;
            }
            """
        )
        self.mark_mines_cb.setStyleSheet(
            """
            QCheckBox:disabled {
                color: black;
            }
            """
        )

        self.to_main_menu_button.clicked.connect(self.open_main_menu_chapter)
        self.load_achievements()

    def load_achievements(self):
        with open("achievements.csv", "r", encoding="utf8") as csvfile:
            reader = list(csv.reader(csvfile, delimiter=";"))

            if int(reader[0][1]) >= 2:
                self.win_game_cb.setChecked(True)
            if reader[1][1] == "yes" and reader[2][1] == "yes":
                self.complete_all_difificulty_levels_cb.setChecked(True)

            if int(reader[3][1]) >= 10:
                self.mark_mines_cb.setChecked(True)

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_main_menu_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_main_menu"):
            self.MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
        self.MINESWEEPER_MAIN_MENU.open_window(frame_x, frame_y)


class MinesweeperPeoples(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./pictures/logo.ico"))
        self.setFixedSize(500, 800)
        uic.loadUi("./uifiles/minesweeper_peoples.ui", self)

        PALETTE = self.palette()
        PIXMAP = QPixmap("./pictures/background_picture2.png")
        PALETTE.setBrush(QPalette.ColorRole.Window, QBrush(PIXMAP))
        self.setPalette(PALETTE)

        self.to_main_menu_button.setIcon(QIcon("./pictures/exit.png"))
        self.to_main_menu_button.setIconSize(QSize(100, 100))

        self.to_main_menu_button.setStyleSheet(
            """
                    QPushButton {
                        border: none;
                        padding: 0px;
                        margin: 0px;
                    }
                """
        )

        self.to_main_menu_button.clicked.connect(self.open_main_menu_chapter)
        self.load_data("peoples.txt")

        font = QFont("Arial Black", 8)
        self.list_widget.setFont(font)

    def load_data(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    item = QListWidgetItem(line)
                    self.list_widget.addItem(item)

    def open_window(self, x, y):
        self.move(x, y)
        self.show()

    def open_main_menu_chapter(self):
        frame_geometry = self.frameGeometry()
        frame_x = frame_geometry.x()
        frame_y = frame_geometry.y()

        self.hide()

        if not hasattr(self, "minesweeper_main_menu"):
            self.MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
        self.MINESWEEPER_MAIN_MENU.open_window(frame_x, frame_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MINESWEEPER_MAIN_MENU = MinesweeperMainMenu()
    MINESWEEPER_MAIN_MENU.show()

    sys.exit(app.exec())

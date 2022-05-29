import sys
import os
import pickle
import docx
import json

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem

from ui_main_window import Ui_MainWindow
from socrat_eye import Socrat_calculation, Trap_calculation, Series_of_calculations


class MainWindow(QMainWindow):о
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация списка с расчётами
        self.calculations = []

        # Подключение общих кнопок
        # Кнопка для выбора пути сохранения результатов
        self.ui.button_path_save.clicked.connect(
            lambda: self.ui.line_path_to_save.setText(QFileDialog.getExistingDirectory()))
        # Кнопка выполнить
        self.ui.button_execute.clicked.connect(self.run_programm)

        # Вкладка Данные
        # подключение кнопок для открытия файлов и папок
        # Кнопка для выбора пути с сырыми результатами
        self.ui.button_path_to_calc.clicked.connect(
            lambda: self.ui.line_path_to_result.setText(QFileDialog.getExistingDirectory()))
        # Кнопка для выбора пути с бинарными результатами
        self.ui.button_path_to_sackle.clicked.connect(self.open_sackle_file)

        # подключение кнопок для добавления расчётов
        self.ui.button_add_sackle.clicked.connect(self.add_sockle_file)
        self.ui.button_add_result.clicked.connect(self.add_result_folder)

        # Подключение кнопок для сброса и удаления расчётов
        self.ui.button_reset_data.clicked.connect(lambda: self.ui.treeWidget_calculations.clear())
        self.ui.button_del_chosen_data.clicked.connect(
            lambda: self.del_chosen_elements(self.ui.treeWidget_calculations))

        # Вкладка Обработка
        # Подключение кнопок для добавления параметров
        self.ui.button_corrected_parameters_add.clicked.connect(self.add_coorected_parameter)
        # Подключение кнопок для сброса и удаления параметров
        self.ui.button_corrected_parameters_reset.clicked.connect(
            lambda: self.ui.treeWidget_corrected_parameters.clear())
        self.ui.button_corrected_parameters_del.clicked.connect(
            lambda: self.del_chosen_elements(self.ui.treeWidget_corrected_parameters))

        self.ui.button_export_cfg.clicked.connect(self.save_cfg)
        self.ui.button_import_cfg.clicked.connect(self.open_sfg)

        # Вкладка Графики
        # Подключение кнопок для добавления графиков
        self.ui.button_graphs_add.clicked.connect(self.add_graph)
        # Подключение кнопок для сброса и удаления графиков
        self.ui.button_reset_graphs.clicked.connect(lambda: self.get_tree_graphs().clear())
        self.ui.button_del_chosen_graphs.clicked.connect(self.del_chosen_graphs)
        # Подключение кнопок для перемещения графиков
        self.ui.button_up_graphs.clicked.connect(self.move_up_chosen_graphs)
        self.ui.button_down_graphs.clicked.connect(self.move_down_chosen_graphs)

        # Вкладка Хронология
        # Подключение кнопок для добавления события
        self.ui.button_chrono_parameters_add.clicked.connect(self.add_chrono)
        # Подключение кнопок для сброса и удаления событий
        self.ui.button_reset_chrono_parameters.clicked.connect(lambda: self.get_tree_chrono().clear())
        self.ui.button_del_chosen_chrono_parameters.clicked.connect(
            lambda: self.del_chosen_elements(self.get_tree_chrono()))

        # Вкладка Ключевые параметры
        # Подключение кнопок для добавления ключевых параметров
        self.ui.button_key_parameters_add.clicked.connect(self.add_key_parameter)
        # Подключение кнопок для сброса и удаления ключевых параметров
        self.ui.button_reset_key_parameters.clicked.connect(lambda: self.get_tree_key_parameters().clear())
        self.ui.button_del_chosen_key_parameters.clicked.connect(
            lambda: self.del_chosen_elements(self.get_tree_key_parameters()))
        # Подключение кнопок для перемещения ключевых параметров
        self.ui.button_up_key_parameters.clicked.connect(self.move_up_chosen_key_parameters)
        self.ui.button_down_key_parameters.clicked.connect(self.move_down_chosen_key_parameters)

    # методы для общих кнопок
    # метод для удаления выбранных полей
    def del_chosen_elements(self, tree):
        chosen_items = tree.selectedItems()
        for item in chosen_items:
            index = tree.indexOfTopLevelItem(item)
            tree.takeTopLevelItem(index)

    # Вкладка Данные
    # методы для открытия файлов и папок
    def open_sackle_file(self):
        paths = QFileDialog.getOpenFileNames(self, "Открыть файл", "", "Файлы sockle (*.sokle)")[0]
        if len(paths) > 0:
            self.ui.line_path_to_sackle.setText(";".join(paths))

    # методы для добавления файлов и папок
    def add_calc(self, name, path):
        if len(self.ui.treeWidget_calculations.findItems(name, Qt.MatchFlag.MatchExactly)) == 0:
            item = QTreeWidgetItem([name,
                                    ";".join([self.ui.line_cut_down_name.text(), self.ui.line_cut_down_value.text()]),
                                    ";".join([self.ui.line_cut_up_name.text(), self.ui.line_cut_up_value.text()]),
                                    path, ])
            self.ui.treeWidget_calculations.addTopLevelItem(item)

            self.ui.line_path_to_sackle.setText("")
            self.ui.line_path_to_result.setText("")
            self.ui.line_name_calc.setText("")
        else:
            print("Такое имя уже существует")

    def add_sockle_file(self):
        paths = self.ui.line_path_to_sackle.text()
        paths = paths.split(";")
        for path in paths:
            if os.path.exists(path):
                name = path.split(r"/")[-1]
                if name.endswith(".sokle"):
                    name = name.split(".sokle")[-2]
                    self.add_calc(name, path)
                else:
                    print("Неверно задан путь")

    def add_result_folder(self):
        path = self.ui.line_path_to_result.text()
        name = self.ui.line_name_calc.text()
        if name != "":
            if os.path.exists(path):
                self.add_calc(name, path)
            else:
                print("Данного пути не существует")
        else:
            print("Введено пустое имя")

    # Вкладка Обработка
    # метод для добавления параметров
    def add_coorected_parameter(self):
        name = self.ui.line_corrected_parameters_name.text()
        mult = self.ui.line_corrected_parameters_mult.text()
        shift = self.ui.line_corrected_parameters_shift.text()
        if len(self.ui.treeWidget_corrected_parameters.findItems(name, Qt.MatchFlag.MatchExactly)) == 0:
            if name != "":
                item = QTreeWidgetItem([name, mult, shift])
                self.ui.treeWidget_corrected_parameters.addTopLevelItem(item)

                self.ui.line_corrected_parameters_name.setText("")
                self.ui.line_corrected_parameters_mult.setText("")
                self.ui.line_corrected_parameters_shift.setText("")
            else:
                print("Введено пустое имя")
        else:
            print("Такой параметр уже существует")

    def save_cfg(self):
        config_dict={}
        # Вкладка Обработка
        config_dict["Correcting"]={}
        config_dict["Correcting"]["always_zero_parameters"]=self.ui.line_always_zero_parameters.text()
        config_dict["Correcting"]["not_zero_parameters"] = self.ui.line_not_zero_parameters.text()

        config_dict["Correcting"]["Items"]=[]
        for i in range(self.ui.treeWidget_corrected_parameters.topLevelItemCount()):
            item = self.ui.treeWidget_corrected_parameters.topLevelItem(i)
            config_dict["Correcting"]["Items"].append([])
            for k in range(item.columnCount()):
                config_dict["Correcting"]["Items"][-1].append(item.text(k))

        # Вкладка Графики
        config_dict["Graphs_single"]=[]
        for i in range(self.ui.treeWidget_graphs_single.topLevelItemCount()):
            item = self.ui.treeWidget_graphs_single.topLevelItem(i)
            config_dict["Graphs_single"].append([])
            for k in range(item.columnCount()):
                config_dict["Graphs_single"][-1].append(item.text(k))

        config_dict["Graphs_multy"] = []
        for i in range(self.ui.treeWidget_graphs_multy.topLevelItemCount()):
            item = self.ui.treeWidget_graphs_multy.topLevelItem(i)
            config_dict["Graphs_multy"].append([])
            for k in range(item.columnCount()):
                config_dict["Graphs_multy"][-1].append(item.text(k))

        # Вкладка Хронология
        config_dict["Chrono_single"] = []
        for i in range(self.ui.treeWidget_chrono_single.topLevelItemCount()):
            item = self.ui.treeWidget_chrono_single.topLevelItem(i)
            config_dict["Chrono_single"].append([])
            for k in range(item.columnCount()):
                config_dict["Chrono_single"][-1].append(item.text(k))
        config_dict["Chrono_multy"] = []
        for i in range(self.ui.treeWidget_chrono_multy.topLevelItemCount()):
            item = self.ui.treeWidget_chrono_multy.topLevelItem(i)
            config_dict["Chrono_multy"].append([])
            for k in range(item.columnCount()):
                config_dict["Chrono_multy"][-1].append(item.text(k))

        # Вкладка Ключевые параметры
        config_dict["Key_parameters_single"] = []
        for i in range(self.ui.treeWidget_key_parameters_single.topLevelItemCount()):
            item = self.ui.treeWidget_key_parameters_single.topLevelItem(i)
            config_dict["Key_parameters_single"].append([])
            for k in range(item.columnCount()):
                config_dict["Key_parameters_single"][-1].append(item.text(k))
        config_dict["Key_parameters_multy"] = []
        for i in range(self.ui.treeWidget_key_parameters_multy.topLevelItemCount()):
            item = self.ui.treeWidget_key_parameters_multy.topLevelItem(i)
            config_dict["Key_parameters_multy"].append([])
            for k in range(item.columnCount()):
                config_dict["Key_parameters_multy"][-1].append(item.text(k))
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Файлы конфигурации (*.json)")[0]
        if len(file_name) > 0:
            with open(file_name, "w", encoding="utf8") as config_file:
                json.dump(config_dict, config_file, indent=4, ensure_ascii=False)

    def open_sfg(self):
        path = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Файлы конфигурации (*.json)")[0]
        if len(path) > 0:
            with open(path, encoding="utf8") as json_file:
                config_dict=json.load(json_file)

            self.ui.line_not_zero_parameters.setText(config_dict["Correcting"]["not_zero_parameters"])
            self.ui.line_always_zero_parameters.setText(config_dict["Correcting"]["always_zero_parameters"])

            # Корректируемые параметры
            self.ui.treeWidget_corrected_parameters.clear()
            for cfg_columns in config_dict["Correcting"]["Items"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_corrected_parameters.addTopLevelItem(item)

            # Графики
            self.ui.treeWidget_graphs_single.clear()
            for cfg_columns in config_dict["Graphs_single"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_graphs_single.addTopLevelItem(item)

            self.ui.treeWidget_graphs_multy.clear()
            for cfg_columns in config_dict["Graphs_multy"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_graphs_multy.addTopLevelItem(item)

            # Хронологии
            self.ui.treeWidget_chrono_single.clear()
            for cfg_columns in config_dict["Chrono_single"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_chrono_single.addTopLevelItem(item)

            self.ui.treeWidget_chrono_multy.clear()
            for cfg_columns in config_dict["Chrono_multy"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_chrono_multy.addTopLevelItem(item)

            # Ключевые параметры
            self.ui.treeWidget_key_parameters_single.clear()
            for cfg_columns in config_dict["Key_parameters_single"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_key_parameters_single.addTopLevelItem(item)

            self.ui.treeWidget_key_parameters_multy.clear()
            for cfg_columns in config_dict["Key_parameters_multy"]:
                item = QTreeWidgetItem(cfg_columns)
                self.ui.treeWidget_key_parameters_multy.addTopLevelItem(item)

    # Вкладка Графики
    # Метод для выбора дерева графиков
    def get_tree_graphs(self):
        tree = None
        if self.ui.tab_graphs_list.currentIndex() == 0:
            tree = self.ui.treeWidget_graphs_single
        elif self.ui.tab_graphs_list.currentIndex() == 1:
            tree = self.ui.treeWidget_graphs_multy
        if tree is not None:
            return tree

    # метод для сброса индекса графиков
    def reset_index_graphs(self):
        tree = self.get_tree_graphs()
        if tree is not None:
            items = tree.findItems("", Qt.MatchFlag.MatchContains)
            for i in range(len(items)):
                items[i].setText(0, str(i + 1))

    # метод для добавления графиков
    def add_graph(self):
        tree = self.get_tree_graphs()
        if tree is not None:
            number = str(len(tree.findItems("", Qt.MatchFlag.MatchContains)) + 1)
            name_y = self.ui.line_graphs_y_names.text()
            name_x = self.ui.line_graphs_x_names.text()
            label_y = self.ui.line_graphs_y_label.text()
            label_x = self.ui.line_graphs_x_label.text()
            min_y = self.ui.line_graphs_y_min.text()
            max_y = self.ui.line_graphs_y_max.text()
            min_x = self.ui.line_graphs_x_min.text()
            max_x = self.ui.line_graphs_x_max.text()
            mult_y = self.ui.line_graphs_y_mult.text()
            mult_x = self.ui.line_graphs_x_mult.text()
            shift_y = self.ui.line_graphs_y_shift.text()
            shift_x = self.ui.line_graphs_x_shift.text()
            step_y = self.ui.line_graphs_y_step.text()
            step_x = self.ui.line_graphs_x_step.text()
            description = self.ui.text_edit_graphs_description.toPlainText()
            item = QTreeWidgetItem([str(number),
                                    name_y,
                                    name_x,
                                    label_y,
                                    label_x,
                                    min_y,
                                    max_y,
                                    min_x,
                                    max_x,
                                    mult_y,
                                    shift_y,
                                    mult_x,
                                    shift_x,
                                    step_y,
                                    step_x,
                                    description,
                                    ])
            tree.addTopLevelItem(item)

    # метод для удаления выбранных графиков
    def del_chosen_graphs(self):
        tree = self.get_tree_graphs()
        if tree is not None:
            self.del_chosen_elements(tree)
            self.reset_index_graphs()

    # метод для перемещения грфика вверх
    def move_up_chosen_graphs(self):
        tree = self.get_tree_graphs()
        if tree is not None:
            chosen_items_old = tree.selectedItems()
            chosen_indexies_old = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
            if min(chosen_indexies_old) > 0:
                tree.clearSelection()
                for old_index in chosen_indexies_old:
                    item = tree.takeTopLevelItem(old_index)
                    tree.insertTopLevelItem(old_index - 1, item)
                select_indexies = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
                self.reset_index_graphs()
                for index in select_indexies:
                    tree.topLevelItem(index).setSelected(True)

    # метод для перемещения грфика вниз
    def move_down_chosen_graphs(self):
        tree = self.get_tree_graphs()
        if tree is not None:
            chosen_items_old = tree.selectedItems()
            chosen_indexies_old = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
            if max(chosen_indexies_old) < tree.topLevelItemCount() - 1:
                chosen_indexies_old.reverse()
                tree.clearSelection()
                for old_index in chosen_indexies_old:
                    item = tree.takeTopLevelItem(old_index)
                    tree.insertTopLevelItem(old_index + 1, item)
                select_indexies = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
                self.reset_index_graphs()
                for index in select_indexies:
                    tree.topLevelItem(index).setSelected(True)

    # Вкладка Хронология
    # Метод для выбора дерева хронологий
    def get_tree_chrono(self):
        tree = None
        if self.ui.tab_chrono_list.currentIndex() == 0:
            tree = self.ui.treeWidget_chrono_single
        elif self.ui.tab_chrono_list.currentIndex() == 1:
            tree = self.ui.treeWidget_chrono_multy
        if tree is not None:
            return tree

    # Метод для добавления события
    def add_chrono(self):
        tree = self.get_tree_chrono()
        if tree is not None:
            name = self.ui.line_chrono_parameter_name.text()
            value = self.ui.line_chrono_parameter_value.text()
            cut_down = ";".join([self.ui.line_cut_down_chrono_name.text(), self.ui.line_cut_down_chrono_value.text()])
            cut_up = ";".join([self.ui.line_cut_up_chrono_name.text(), self.ui.line_cut_up_chrono_value.text()])
            description = self.ui.text_edit_chrono_description.toPlainText()
            if name == "":
                print("Введено пустое название")
            elif value == "":
                print("Введено пустое значение")
            elif description == "":
                print("Введено пустое описание")
            else:
                item = QTreeWidgetItem([name,
                                        value,
                                        cut_down,
                                        cut_up,
                                        description,
                                        ])
                tree.addTopLevelItem(item)
                self.ui.line_chrono_parameter_name.setText("")
                self.ui.line_chrono_parameter_value.setText("")
                self.ui.text_edit_chrono_description.setText("")
                self.ui.line_cut_down_chrono_name.setText("")
                self.ui.line_cut_down_chrono_value.setText("")
                self.ui.line_cut_up_chrono_name.setText("")
                self.ui.line_cut_up_chrono_value.setText("")

    # Вкладка Ключевые параметры
    # Метод для выбора дерева ключевых параметров
    def get_tree_key_parameters(self):
        tree = None
        if self.ui.tab_key_parameters_list.currentIndex() == 0:
            tree = self.ui.treeWidget_key_parameters_single
        elif self.ui.tab_key_parameters_list.currentIndex() == 1:
            tree = self.ui.treeWidget_key_parameters_multy
        if tree is not None:
            return tree

    # Метод для добавления ключевых параметров
    def add_key_parameter(self):
        tree = self.get_tree_key_parameters()
        if tree is not None:
            key_parameter_name = self.ui.line_key_parameter_name.text()
            search_parameter_name = self.ui.line_search_parameter_name.text()
            value = self.ui.line_search_parameter_value.text()
            cut_down = ";".join(
                [self.ui.line_cut_down_key_parameters_name.text(), self.ui.line_cut_down_key_parameters_value.text()])
            cut_up = ";".join(
                [self.ui.line_cut_up_key_parameters_name.text(), self.ui.line_cut_up_key_parameters_value.text()])
            description = self.ui.text_edit_key_parameters_description.toPlainText()
            if key_parameter_name == "":
                print("Введено пустое название ключевого параметра")
            elif search_parameter_name == "":
                print("Введено пустое название параметра для поиска")
            elif value == "":
                print("Введено пустое значение")
            elif description == "":
                print("Введено пустое описание")
            else:
                item = QTreeWidgetItem([key_parameter_name,
                                        search_parameter_name,
                                        value,
                                        cut_down,
                                        cut_up,
                                        description,
                                        ])
                tree.addTopLevelItem(item)
                self.ui.line_key_parameter_name.setText("")
                self.ui.line_search_parameter_name.setText("")
                self.ui.line_search_parameter_value.setText("")
                self.ui.text_edit_key_parameters_description.setText("")
                self.ui.line_cut_down_key_parameters_name.setText("")
                self.ui.line_cut_down_key_parameters_value.setText("")
                self.ui.line_cut_up_key_parameters_name.setText("")
                self.ui.line_cut_up_key_parameters_value.setText("")

    # метод для перемещения графика вверх
    def move_up_chosen_key_parameters(self):
        tree = self.get_tree_key_parameters()
        if tree is not None:
            chosen_items_old = tree.selectedItems()
            chosen_indexies_old = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
            if min(chosen_indexies_old) > 0:
                tree.clearSelection()
                for old_index in chosen_indexies_old:
                    item = tree.takeTopLevelItem(old_index)
                    tree.insertTopLevelItem(old_index - 1, item)
                select_indexies = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
                for index in select_indexies:
                    tree.topLevelItem(index).setSelected(True)

    # метод для перемещения грфика вниз
    def move_down_chosen_key_parameters(self):
        tree = self.get_tree_key_parameters()
        if tree is not None:
            chosen_items_old = tree.selectedItems()
            chosen_indexies_old = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
            if max(chosen_indexies_old) < tree.topLevelItemCount() - 1:
                chosen_indexies_old.reverse()
                tree.clearSelection()
                for old_index in chosen_indexies_old:
                    item = tree.takeTopLevelItem(old_index)
                    tree.insertTopLevelItem(old_index + 1, item)
                select_indexies = [tree.indexOfTopLevelItem(i) for i in chosen_items_old]
                for index in select_indexies:
                    tree.topLevelItem(index).setSelected(True)



    # метод для предварительной загрузки
    def pre_run(self):
        # функция для обработки cut_down и cut_up
        def cut_str_to_dict(cut_str):
            name, value = cut_str.split(";")
            if value != "min" and value != "max":
                try:
                    value = float(value)
                except:
                    value = None
            if value is None:
                return None
            else:
                return {"name": name, "value": value}

        #сброс предварительно загруженных результатов
        self.calculations=[]
        # Получение параметров с вкладки Данные
        calculations_columns = ["name", "cut_down", "cut_up", "path"]
        for item_index in range(self.ui.treeWidget_calculations.topLevelItemCount()):
            item = self.ui.treeWidget_calculations.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(calculations_columns, item_values):
                item_dict[column] = value
            for cut_name in ("cut_down", "cut_up"):
                item_dict[cut_name] = cut_str_to_dict(item_dict[cut_name])

            if item_dict["path"].endswith(".sokle"):
                with open(item_dict["path"], 'rb') as f:
                    calc = pickle.load(f)
            elif os.path.isdir(item_dict["path"]):
                file_names_list = os.listdir(item_dict["path"])
                file_names = ";".join(file_names_list)
                if ".dia;" in file_names:
                    calc = Socrat_calculation(item_dict["path"])
                elif "lent3" in file_names_list:
                    calc = Trap_calculation(item_dict["path"])
                else:
                    print("Проблемы с " + item_dict["path"])
                    self.calculations = []
                    break
            else:
                print("Проблемы с " + item_dict["path"])
                self.calculations = []
                break
            item_dict["calc_object"]=calc

            self.calculations.append(item_dict)

    # метод для БОЛЬШОЙ КНОПКИ Выполнить
    def run_programm(self):

        # функция для обработки cut_down и cut_up
        def cut_str_to_dict(cut_str):
            name, value = cut_str.split(";")
            if value != "min" and value != "max":
                try:
                    value = float(value)
                except:
                    value = None
            if value is None:
                return None
            else:
                return {"name": name, "value": value}

        # Список для Multy
        calculations_list = []

        path_save = self.ui.line_path_to_save.text()

        # функция для перевода из строки в float число
        def str_to_number(number_str):
            try:
                return float(number_str)
            except:
                return None

        # функция для обработки строки со значением для поиска
        def search_str_transform(search_value):
            if not ((("ON" in search_value or "OFF" in search_value) and (
                    "FIRST" in search_value or "LAST" in search_value)) or search_value == "min" or search_value == "max"):
                try:
                    search_value = float(search_value)
                except:
                    search_value = None
            return search_value

        # функция для округления ключевых и хронологических чисел
        def round_chrono_key(value):
            abs_value = abs(value)
            if abs_value < 1:
                return round(value, 2)
            elif abs_value < 10:
                return round(value, 1)
            elif abs_value < 1000:
                return int(round(value, 0))
            elif abs_value < 10000:
                return int(round(value, -1))
            else:
                return int(round(value, -2))

        # Предварительная загрузка:
        self.pre_run()

        # Получение параметров с вкладки Обработка
        always_zero_parameters = self.ui.line_always_zero_parameters.text().split(";")
        not_zero_parameters = self.ui.line_not_zero_parameters.text().split(";")
        corrected_parameters = []
        corrected_parameters_columns = ["name", "mult", "shift"]
        for item_index in range(self.ui.treeWidget_corrected_parameters.topLevelItemCount()):
            item = self.ui.treeWidget_corrected_parameters.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(corrected_parameters_columns, item_values):
                item_dict[column] = value
            for number_name in ("mult", "shift"):
                item_dict[number_name] = str_to_number(item_dict[number_name])

            corrected_parameters.append(item_dict)

        # Получение параметров с вкладки Графики
        graphs_single = []
        graphs_multy = []
        graphs_columns = ["number",
                          "y_name", "x_name",
                          "y_label", "x_label",
                          "y_cut_down", "y_cut_up",
                          "x_cut_down", "x_cut_up",
                          "y_mult", "y_shift",
                          "x_mult", "x_shift",
                          "y_step", "x_step",
                          "description"]

        for item_index in range(self.ui.treeWidget_graphs_single.topLevelItemCount()):
            item = self.ui.treeWidget_graphs_single.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(graphs_columns, item_values):
                item_dict[column] = value
            for split_name in ("y_name", "x_name"):
                item_dict[split_name] = item_dict[split_name].split(";")
            for number_name in (
                    "y_cut_down", "y_cut_up", "x_cut_down", "x_cut_up", "y_mult", "y_shift", "x_mult", "x_shift",
                    "y_step", "x_step",):
                item_dict[number_name] = str_to_number(item_dict[number_name])

            graphs_single.append(item_dict)

        for item_index in range(self.ui.treeWidget_graphs_multy.topLevelItemCount()):
            item = self.ui.treeWidget_graphs_multy.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(graphs_columns, item_values):
                item_dict[column] = value
            for split_name in ("y_name", "x_name"):
                item_dict[split_name] = item_dict[split_name].split(";")
            for number_name in (
                    "y_cut_down", "y_cut_up", "x_cut_down", "x_cut_up", "y_mult", "y_shift", "x_mult", "x_shift",
                    "y_step",
                    "x_step"):
                item_dict[number_name] = str_to_number(item_dict[number_name])
            graphs_multy.append(item_dict)

        # Получение параметров с вкладки Хронология
        chrono_single = []
        chrono_multy = []
        chrono_columns = ["name", "value", "cut_down", "cut_up", "description"]

        for item_index in range(self.ui.treeWidget_chrono_single.topLevelItemCount()):
            item = self.ui.treeWidget_chrono_single.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(chrono_columns, item_values):
                item_dict[column] = value
            item_dict["value"] = search_str_transform(item_dict["value"])
            for cut_name in ("cut_down", "cut_up"):
                item_dict[cut_name] = cut_str_to_dict(item_dict[cut_name])
            chrono_single.append(item_dict)

        for item_index in range(self.ui.treeWidget_chrono_multy.topLevelItemCount()):
            item = self.ui.treeWidget_chrono_multy.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(chrono_columns, item_values):
                item_dict[column] = value
            item_dict["value"] = search_str_transform(item_dict["value"])
            for cut_name in ("cut_down", "cut_up"):
                item_dict[cut_name] = cut_str_to_dict(item_dict[cut_name])
            chrono_multy.append(item_dict)

        # Получение параметров с вкладки Ключевые параметры
        key_parameters_single = []
        key_parameters_multy = []
        key_parameters_columns = ["key_parameter_name", "search_name", "value", "cut_down", "cut_up", "description"]

        for item_index in range(self.ui.treeWidget_key_parameters_single.topLevelItemCount()):
            item = self.ui.treeWidget_key_parameters_single.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(key_parameters_columns, item_values):
                item_dict[column] = value
            item_dict["value"] = search_str_transform(item_dict["value"])
            for cut_name in ("cut_down", "cut_up"):
                item_dict[cut_name] = cut_str_to_dict(item_dict[cut_name])
            key_parameters_single.append(item_dict)

        for item_index in range(self.ui.treeWidget_key_parameters_multy.topLevelItemCount()):
            item = self.ui.treeWidget_key_parameters_multy.topLevelItem(item_index)
            item_dict = {}
            item_values = [item.text(columns_index) for columns_index in range(item.columnCount())]
            for column, value in zip(key_parameters_columns, item_values):
                item_dict[column] = value
            item_dict["value"] = search_str_transform(item_dict["value"])
            for cut_name in ("cut_down", "cut_up"):
                item_dict[cut_name] = cut_str_to_dict(item_dict[cut_name])
            key_parameters_multy.append(item_dict)

        # Получение параметров с вкладки Сохранение результатов
        file_save_name = self.ui.line_file_save_name.text()
        if file_save_name == "":
            file_save_name = "Results"
        graphs_width = self.ui.line_graphs_width.text()
        if graphs_width == "":
            graphs_width = 12
        else:
            graphs_width = float(graphs_width)
        number_delim = self.ui.line_numbers_delim.text()
        font_name = self.ui.line_font_name.text()
        if font_name == "":
            font_name = "Times New Roman"
        font_value = self.ui.line_font_value.text()
        if font_value == "":
            font_value = 12
        else:
            font_value = float(font_value)
        check_round = self.ui.checkBox_round.checkState()

        # Открытие папки для сохранения
        if len(path_save) == 0:
            os.chdir("..")
            if not os.path.isdir("Socrat_eye_output"):
                os.mkdir("Socrat_eye_output")
            path_save = os.path.abspath("Socrat_eye_output")
            self.ui.line_path_to_save.setText(path_save)
        os.chdir(path_save)
        # Обработка результатов
        for calculation in self.calculations:

            calc=calculation["calc_object"]

            # Обрезка снизу и сверху
            calc.cut_bottom_transform(calculation["cut_down"]["name"], calculation["cut_down"]["value"])
            calc.cut_top_transform(calculation["cut_up"]["name"], calculation["cut_up"]["value"])
            # При необходимости сохранение в бинарном виде
            if not calculation["path"].endswith(".sokle"):
                calc.save(name=calculation["name"])

            # Корректировка
            # Специфика СОКРАТа
            if isinstance(calc, Socrat_calculation):
                calc.last_zero_parameters_transform(always_zero_parameters)
                calc.not_zero_parameters_transform(not_zero_parameters)
            # Умножене и смещение
            for corrected_parameter in corrected_parameters:
                calc.values_mult_shift(corrected_parameter["name"], mult=corrected_parameter["mult"],
                                       shift=corrected_parameter["shift"])



            if len(graphs_single)>0:
                # Открытие папки для сохранения в режиме Single
                if not os.path.exists(calculation["name"]):
                    os.mkdir(calculation["name"])
                os.chdir(calculation["name"])
                # Построение графиков Single
                for graph_single in graphs_single:
                    print(graph_single)
                    calc.graph(GrName=graph_single["number"],
                               x_names=graph_single["x_name"],
                               y_names=graph_single["y_name"],
                               lablex=graph_single["x_label"],
                               labley=graph_single["y_label"],
                               x1=graph_single["x_cut_down"],
                               x2=graph_single["x_cut_up"],
                               y1=graph_single["y_cut_down"],
                               y2=graph_single["y_cut_up"],
                               mult_x=graph_single["x_mult"],
                               mult_y=graph_single["y_mult"],
                               shift_x=graph_single["x_shift"],
                               shift_y=graph_single["y_shift"],
                               stpx=graph_single["x_step"],
                               stpy=graph_single["y_step"], )

            # Построение хронологий и ключевых параметров Single
            calc.make_chrono(chrono_single)
            calc.make_key_table(key_parameters_single)

            # Округление Single
            if check_round:
                calc.chrono_table["Time"] = calc.chrono_table["Time"].apply(round_chrono_key)
                calc.key_parameters_table["Value"] = calc.key_parameters_table["Value"].apply(round_chrono_key)

            # Возврат в корневую папку
            os.chdir(path_save)

            # Сохранение в Word Single
            doc = docx.Document()

            # Сохранение хронологии Single
            if len(calc.chrono_table) > 0:
                doc.add_paragraph("Хронология ")
                table = doc.add_table(rows=1, cols=2)
                table.style = "Table Grid"
                table.cell(0, 0).text = "Время, с"
                table.cell(0, 1).text = "Событие"
                for k in range(len(calc.chrono_table)):
                    table.add_row()
                    table.cell(k + 1, 0).text = str(calc.chrono_table.iloc[k, 0]).replace(".", number_delim)
                    table.cell(k + 1, 1).text = str(calc.chrono_table.iloc[k, 1])
                doc.add_page_break()

            # Сохранение ключевых параметров Single
            if len(calc.key_parameters_table) > 0:
                doc.add_paragraph("Ключевые параметры")
                table = doc.add_table(rows=1, cols=2)
                table.style = "Table Grid"
                table.cell(0, 0).text = "Параметр"
                table.cell(0, 1).text = "Значение"
                for k in range(len(calc.key_parameters_table)):
                    table.add_row()
                    table.cell(k + 1, 0).text = str(calc.key_parameters_table.iloc[k, 0])
                    table.cell(k + 1, 1).text = str(calc.key_parameters_table.iloc[k, 1]).replace(".", number_delim)
                doc.add_page_break()

            # Сохранение графиков Single
            for k in range(len(calc.graph_list)):
                doc.add_picture(calc.graph_list[k]["png"], width=docx.shared.Cm(graphs_width))
                doc.add_paragraph(
                    "Рисунок {}\n{}".format(str(k + 1), graphs_single[k]["description"]))

            # Запись Word Single
            if len(calc.graph_list)>0 or len(calc.key_parameters_table) or len(calc.chrono_table) >0:
                doc.save(calculation["name"] + ".docx")

            # Сброс графиков, хронологий и ключевых параметров
            calc.reset_data()

            # Построение хронологий и ключевых параметров Multy
            calc.make_chrono(chrono_multy)
            calc.make_key_table(key_parameters_multy)

            # Округление Multy
            if check_round:
                calc.chrono_table["Time"] = calc.chrono_table["Time"].apply(round_chrono_key)
                calc.key_parameters_table["Value"] = calc.key_parameters_table["Value"].apply(round_chrono_key)

            calculations_list.append(calc)

        # Создание объекта для хранения Multy
        calculation_series = Series_of_calculations(calculations_list)

        if len(graphs_multy)>0:
            # Открытие папки для сохранения в режиме Multy
            if not os.path.exists(file_save_name):
                os.mkdir(file_save_name)
            os.chdir(file_save_name)
            # Отрисовка графиков Multy
            for graph_multy in graphs_multy:
                calculation_series.graph(GrName=graph_multy["number"],
                                         x_names=graph_multy["x_name"],
                                         y_names=graph_multy["y_name"],
                                         lablex=graph_multy["x_label"],
                                         labley=graph_multy["y_label"],
                                         x1=graph_multy["x_cut_down"],
                                         x2=graph_multy["x_cut_up"],
                                         y1=graph_multy["y_cut_down"],
                                         y2=graph_multy["y_cut_up"],
                                         mult_x=graph_multy["x_mult"],
                                         mult_y=graph_multy["y_mult"],
                                         shift_x=graph_multy["x_shift"],
                                         shift_y=graph_multy["y_shift"],
                                         stpx=graph_multy["x_step"],
                                         stpy=graph_multy["y_step"], )

        # Возврат в корневую папку
        os.chdir(path_save)

        # Сохранение в Word Multy
        doc = docx.Document()

        # Расшифровка чисел
        numbers_to_names=["{} - {}".format(str(i+1),self.calculations[i]["name"]) for i in range(len(self.calculations))]
        numbers_to_names="\n".join(numbers_to_names)
        doc.add_paragraph(numbers_to_names)


        # Сохранение хронологий Multy
        if len(calculation_series.chrono_table) > 0:
            doc.add_page_break()
            doc.add_paragraph("Хронология")
            table = doc.add_table(rows=len(calculation_series.chrono_table) + 1,
                                  cols=len(calculation_series.chrono_table.columns))
            table.style = "Table Grid"
            table.cell(0, 0).text = "Событие"
            for i in range(len(self.calculations)):
                table.cell(0, i + 1).text = str(i+1)
            for i in range(len(calculation_series.chrono_table.columns)):
                for k in range(len(calculation_series.chrono_table)):
                    table.cell(k + 1, i).text = str(calculation_series.chrono_table.iloc[k, i]).replace(".", number_delim)


        # Сохранение ключевых параметров Multy
        if len(calculation_series.key_parameters_table) > 0:
            doc.add_page_break()
            doc.add_paragraph("Ключевые параметры")
            table = doc.add_table(rows=len(calculation_series.key_parameters_table) + 1,
                                  cols=len(calculation_series.key_parameters_table.columns))
            table.style = "Table Grid"
            table.cell(0, 0).text = "Параметр"
            for i in range(len(self.calculations)):
                table.cell(0, i + 1).text = str(i+1)
            for i in range(len(calculation_series.key_parameters_table.columns)):
                for k in range(len(calculation_series.key_parameters_table)):
                    table.cell(k + 1, i).text = str(calculation_series.key_parameters_table.iloc[k, i]).replace(".", number_delim)

        # Сохранение графиков Multy
        if len(calculation_series.graph_list) > 0:
            doc.add_page_break()
            for k in range(len(calculation_series.graph_list)):
                doc.add_picture(calculation_series.graph_list[k]["png"], width=docx.shared.Cm(graphs_width))
                doc.add_paragraph("Рисунок {}\n{}".format(str(k + 1), graphs_multy[k]["description"]))

        # Запись Word Multy
        if len(calculation_series.graph_list) > 0 or len(calculation_series.key_parameters_table) or len(calculation_series.chrono_table) > 0:
            doc.save(file_save_name + ".docx")
        print("\n\n\nГотово")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

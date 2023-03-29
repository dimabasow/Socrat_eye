import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pylab
import ternary
import pandas as pd
import numpy as np
import os
import copy
import pickle
from struct import unpack
# import seaborn as sns



def graph (GrName, get_named_data = None, get_unamed_data = None, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None, mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None):
    
    if get_named_data is not None:
        get_named_x, get_named_y = get_named_data
        if isinstance(get_named_y[0],(np.ndarray,pd.Series,list,tuple)):
            named_y = [pd.Series(i) for i in get_named_y]
        else:
            named_y=[pd.Series(get_named_y)]
        
        if isinstance(get_named_x[0],(np.ndarray,pd.Series,list,tuple)):
            named_x = [pd.Series(i) for i in get_named_x]
        else:
            named_x=[pd.Series(get_named_x)]
    else:
        named_x, named_y = None, None
    
    if get_unamed_data is not None:
        get_unamed_x, get_unamed_y = get_unamed_data
        if isinstance(get_unamed_y[0],(np.ndarray,pd.Series,list,tuple)):
            unamed_y = [pd.Series(i) for i in get_unamed_y]
        else:
            unamed_y=[pd.Series(get_unamed_y)]
        
        if isinstance(get_unamed_x[0],(np.ndarray,pd.Series,list,tuple)):
            unamed_x = [pd.Series(i) for i in get_unamed_x]
        else:
            unamed_x=[pd.Series(get_unamed_x)]
    else:
        unamed_x, unamed_y = None, None
    
    colors = ('#000000', '#FF0000', '#0000FF', '#008000', '#FF00FF', '#8B4513',
         '#808080', '#C0C0C0', '#800080', '#800000', '#FFFF00', '#00FF00',
         '#000080')
    markers=('D', '^', 'o', 's', '*', 'p', 'h', '+', 'x', 'd', 'v')
    
    if (labley=='T, C') :
        labley='T, \N{DEGREE SIGN}C'
    if (labley=='F, m^2') :
        labley='F, m\u00b2'
    if (labley=='G, m^3/hr'):
        labley='G, m\u00b3' + '/hr'
    if (labley=='ρ, kg/m^3'):
        labley='ρ, kg/' + 'm\u00b3'
    
    
    
    fig, ax = plt.subplots()
    path_dict={}
    
    if mult_x is not None:
        if named_x is not None:
            named_x=[i*mult_x for i in named_x]
        if unamed_x is not None:
            unamed_x=[i*mult_x for i in unamed_x]
    if mult_y is not None:
        if named_y is not None:
            named_y=[i*mult_y for i in named_y]
        if unamed_y is not None:
            unamed_y=[i*mult_y for i in unamed_y]
    if shift_x is not None:
        if named_x is not None:
            named_x=[i+shift_x for i in named_x]
        if unamed_x is not None:
            unamed_x=[i+shift_x for i in unamed_x]
    if shift_y is not None:
        if named_y is not None:
            named_y=[i+shift_y for i in named_y]
        if unamed_y is not None:
            unamed_y=[i+shift_y for i in unamed_y]

    if x1:
        if named_x:
            for i in range(len(named_x)):
                if x1>named_x[i].min():
                    N_min=named_x[i][named_x[i]>x1].index[0]
                    named_x[i]=named_x[i][N_min:]
                    named_y[i]=named_y[i][N_min:]
        if unamed_x:
            for i in range(len(unamed_x)):
                if x1>unamed_x[i].min():
                    N_min=unamed_x[i][unamed_x[i]>x1].index[0]
                    unamed_x[i]=unamed_x[i][N_min:]
                    unamed_y[i]=unamed_y[i][N_min:]

    if x2:
        if named_x:
            for i in range(len(named_x)):
                if x2<named_x[i].max():
                    N_max=named_x[i][named_x[i]>x2].index[0]
                    named_x[i]=named_x[i][:N_max]
                    named_y[i]=named_y[i][:N_max]
        if unamed_x:
            for i in range(len(unamed_x)):
                if x2<unamed_x[i].max():
                    N_max=unamed_x[i][unamed_x[i]>x2].index[0]
                    unamed_x[i]=unamed_x[i][:N_max]
                    unamed_y[i]=unamed_y[i][:N_max]

    if y1:
        if named_y:
            for i in range(len(named_y)):
                named_x[i] = named_x[i][y1 <= named_y[i]]
                named_y[i] = named_y[i][y1 <= named_y[i]]
        if unamed_y:
            for i in range(len(unamed_y)):
                unamed_x[i] = unamed_x[i][y1 <= unamed_y[i]]
                unamed_y[i] = unamed_y[i][y1 <= unamed_y[i]]

    if y2:
        if named_y:
            for i in range(len(named_y)):
                named_x[i] = named_x[i][y2 >= named_y[i]]
                named_y[i] = named_y[i][y2 >= named_y[i]]
        if unamed_y:
            for i in range(len(unamed_y)):
                unamed_x[i] = unamed_x[i][y2 >= unamed_y[i]]
                unamed_y[i] = unamed_y[i][y2 >= unamed_y[i]]

    if y1 is None:
        y1_list = []
        if named_y:
            y1_named = min(min(i) for i in named_y)
            y1_list.append(y1_named)
        if unamed_y:
            y1_unamed = min(min(i) for i in unamed_y)
            y1_list.append(y1_unamed)
        if y1_list:
            y1 = min(y1_list)
            
    if y2 is None:
        y2_list = []
        if named_y:
            y2_named = max(max(i) for i in named_y)
            y2_list.append(y2_named)
        if unamed_y:
            y2_unamed = max(max(i) for i in unamed_y)
            y2_list.append(y2_unamed)
        if y2_list:
            y2 = max(y2_list)
            y2 = y2 + 0.05*(y2-y1)
    
    if x1 is None:
        x1_list = []
        if named_x:
            x1_named = min(min(i) for i in named_x)
            x1_list.append(x1_named)
        if unamed_x:
            x1_unamed = min(min(i) for i in unamed_x)
            x1_list.append(x1_unamed)
        if x1_list:
            x1 = min(x1_list)

    if x2 is None:
        x2_list = []
        if named_x:
            x2_named = max(max(i) for i in named_x)
            x2_list.append(x2_named)
        if unamed_x:
            x2_unamed = max(max(i) for i in unamed_x)
            x2_list.append(x2_unamed)
        if x2_list:
            x2 = max(x2_list)
        
    path_dict["x_min"]=str(int(x1))
    path_dict["x_max"]=str(int(x2))
    path_dict["y_min"]=str(int(y1))
    path_dict["y_max"]=str(int(y2))

    N_points_named_list=[]
    for i in range(len(named_x)):
        N_points = len(named_x[i]) // 50
        if N_points==0:
            N_points=1
        N_points_named_list.append(N_points)
    
    if named_y:
        for i in range(len(named_y)):
            ax.plot(named_x[i], named_y[i], colors[i-len(colors)*(i//len(colors))], linewidth = 4, label = str(i+1), marker = markers[i-len(markers)*(i//len(markers))], markevery = N_points_named_list[i])
    if unamed_y:
        for i in range(len(unamed_y)):
            ax.plot(unamed_x[i], unamed_y[i], colors[i-len(colors)*(i//len(colors))], linewidth = 0.3)

    pylab.xlim (xmin = x1, xmax=x2)
    pylab.ylim (ymin = y1, ymax=y2)
    #Настраиваем оси
    #Устанавливаем интервал делений x:
    if stpx is not None:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(stpx))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(stpx/5))
    #Устанавливаем интервал делений y:
    if stpy is not None:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(stpy))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(stpy/5))

    # Отрисовываем сеточные линии
    ax.grid(which = 'major', color = 'k',  linestyle = '-')
    ax.minorticks_on()

    ax.grid(which = 'minor', color ='gray', linestyle = ':')

    ax.tick_params( axis ='both', length = 10, pad = 10, labelsize = 18, labelcolor = 'black' )

    # Отрисовываем подписи
    ax.set_ylabel(labley, fontsize = 24)
    ax.set_xlabel(lablex, fontsize = 24)
    
    if named_y and len(named_y)>1:
        pylab.legend(loc='best', numpoints=1, fontsize=20).get_frame().set_edgecolor('w')
    
    fig.set_figwidth(12)
    fig.set_figheight(8)
    
    # сохранение .png
    fmt = 'png'
    path_dict[fmt]=os.path.abspath(os.curdir)+"\\"+GrName + "." +fmt
    fig.savefig('{}.{}'.format(GrName, fmt), format=fmt, bbox_inches='tight')
    plt.close()
    
    return path_dict

def graph_shapiro_moffette(GrName, points_list, detonation_limits, flammability_limits):
    path_dict = {}
    scale = 100
    fontsize = 12
    fmt = "png"
    order = ["Steam","Air","Hydrogen"]

    figure, tax = ternary.figure(scale=scale)

    # Draw Boundary and Gridlines
    tax.boundary(linewidth=2.0)
    tax.gridlines(color="black", multiple=5)

    # Set Axis labels
    tax.right_corner_label(r"$\varphi_{H_{2}O}$, %", fontsize=fontsize, offset=0.1)
    tax.top_corner_label(r"$\varphi_{Air}$, %", fontsize=fontsize, offset=0.2)
    tax.left_corner_label(r"$\varphi_{H_{2}}$, %", fontsize=fontsize, offset=0.15)

    tax.left_axis_label("Hydrogen", fontsize=fontsize, offset=0.15)
    tax.right_axis_label("Air", fontsize=fontsize, offset=0.15)
    tax.bottom_axis_label("Steam", fontsize=fontsize, offset=0.1)

    # Drawing
    tax.plot(flammability_limits[order].to_numpy() * scale, color="orange", label="Flammability", linewidth=2)
    tax.plot(detonation_limits[order].to_numpy() * scale, color="red", label="Detonation", linewidth=2)
    tax.plot(points_list[0][order].to_numpy() * scale, color="green", label="Calculation", linewidth=2)
    for points_frame in points_list[1:]:
        tax.plot(points_frame[order].to_numpy() * scale, color="green", linestyle=":", linewidth=2)

    tax.ticks(axis='lbr', multiple=5, linewidth=1, offset=0.025)
    tax.get_axes().axis('off')
    tax.clear_matplotlib_ticks()
    tax.legend(loc="upper right")

    # Сохранение .png
    path_dict[fmt] = os.path.abspath(os.curdir) + "\\" + GrName + "." + fmt
    tax.savefig('{}.{}'.format(GrName, fmt), format=fmt, bbox_inches='tight')

    return path_dict

class Calculation:

    def __init__(self):

        # словарь для #_report.lst, p1runout и p1spn
        self.data_dict = {}

        # инициализация графиков, хронологии и ключевых параметров
        self.reset_data()

    # метод для сдвига времени (прибавляет указанную величину к Time в кластерах dia, к Time в #_report.lst, к time в p1runout и к # в p1spn)
    def time_shift_transform(self, delta_time):
        for table_name in self.data_dict:
            self.data_dict[table_name][self.data_dict[table_name].columns[0]] += delta_time

    # метод для обрезки значений снизу
    def cut_bottom_transform(self, parameter_name, parameter_value):
        time_row = self.get_row(parameter_name, parameter_value)
        keys_to_remote = []
        if time_row is not None:
            lower_time = time_row[0]
            if isinstance(lower_time, (float, int)):
                for table_name in self.data_dict:
                    table = self.data_dict[table_name]
                    time_table = table.iloc[0, 0]
                    if isinstance(time_table, (float, int)) and time_table < lower_time:
                        if len(table[table.columns[0]][table[table.columns[0]] > lower_time]) > 0:
                            lower_index = table[table.columns[0]][table[table.columns[0]] > lower_time].index[0]
                        else:
                            lower_index = len(table)
                        self.data_dict[table_name] = self.data_dict[table_name][lower_index:]
                        self.data_dict[table_name].reset_index(drop=True, inplace=True)
                        if len(self.data_dict[table_name]) == 0:
                            keys_to_remote.append(table_name)
        for key in keys_to_remote:
            self.data_dict.pop(key)

    # метод для обрезки значений сверху
    def cut_top_transform(self, parameter_name, parameter_value):
        time_row = self.get_row(parameter_name, parameter_value)
        keys_to_remote = []
        if time_row is not None:
            upper_time = time_row[0]
            if isinstance(upper_time, (float, int)):
                for table_name in self.data_dict:
                    table = self.data_dict[table_name]
                    time_table = table.iloc[-1, 0]
                    if isinstance(time_table, (float, int)) and time_table > upper_time:
                        if len(table[table.columns[0]][table[table.columns[0]] < upper_time]) > 0:
                            upper_index = table[table.columns[0]][table[table.columns[0]] > upper_time].index[0]
                        else:
                            upper_index = 0
                        self.data_dict[table_name] = self.data_dict[table_name][:upper_index]
                        self.data_dict[table_name].reset_index(drop=True, inplace=True)
                        if len(self.data_dict[table_name]) == 0:
                            keys_to_remote.append(table_name)

        for key in keys_to_remote:
            self.data_dict.pop(key)

    # метод для получения информации о параметре
    def get_parameter_table(self, name_values):
        if isinstance(name_values, str):
            name_values = [name_values]

        return_table = None
        for table_name in self.data_dict:
            table = self.data_dict[table_name]
            if set(name_values) <= set(table.columns):
                return_table = table

        if return_table is not None:
            return return_table
        else:
            return None

    # метод для получения ряда
    def get_row(self, parameter_name, parameter_value, shift_down=True):
        table = self.get_parameter_table(parameter_name)
        if table is not None:
            parameter_min = min(table[parameter_name])
            parameter_max = max(table[parameter_name])
            if parameter_value == "min":
                parameter_value = parameter_min
            elif parameter_value == "max":
                parameter_value = parameter_max
        if table is not None and isinstance(parameter_value, (float, int)):
            if parameter_min <= parameter_value <= parameter_max:
                table_equal = table[parameter_name][table[parameter_name] == parameter_value]
                indexes = []
                if len(table_equal) > 0:
                    if shift_down:
                        indexes.append(table_equal.index[0])
                    else:
                        indexes.append(table_equal.index[-1])
                indexes_not_equal = []
                for i in table[parameter_name].index[:-1]:
                    if table[parameter_name][i] < parameter_value < table[parameter_name][i + 1] or \
                            table[parameter_name][i + 1] < parameter_value < table[parameter_name][i]:
                        indexes_not_equal.append(i)

                if len(indexes_not_equal) > 0:
                    if shift_down:
                        indexes.append(indexes_not_equal[0])
                    else:
                        indexes.append(indexes_not_equal[-1] + 1)

                if shift_down:
                    return table.iloc[min(indexes), :]
                else:
                    return table.iloc[max(indexes), :]
            else:
                print("Значение {} не лежит в диапазоне параметра".format(parameter_name))
                return None
        else:
            print("Параметр {} не найден в dia, p1runout и p1spn".format(parameter_name))
            return None

    # метод для получения момента времени
    def get_time_moment(self, parameter_name, parameter_value, cut_down=None, cut_up=None):
        calc_copy = self.make_copy()
        return_value = None
        if isinstance(cut_down, dict):
            calc_copy.cut_bottom_transform(cut_down["name"], cut_down["value"])
        if isinstance(cut_up, dict):
            calc_copy.cut_top_transform(cut_up["name"], cut_up["value"])
        time_row = calc_copy.get_row(parameter_name, parameter_value)
        if time_row is not None:
            return_value = time_row[0]
        else:
            if "report" in calc_copy.data_dict:
                report_table = calc_copy.data_dict["report"][
                    calc_copy.data_dict["report"]["Name_report"] == parameter_name]
                if len(report_table) > 0:
                    if "ON" in parameter_value:
                        report_table = report_table[report_table["ON_OFF_report"] == True]
                    elif "OFF" in parameter_value:
                        report_table = report_table[report_table["ON_OFF_report"] == False]
                    else:
                        report_table = None
                    if report_table is not None and len(report_table)>0:
                        if "LAST" in parameter_value:
                            return_value = report_table.iloc[-1, 0]
                        elif "FIRST" in parameter_value:
                            return_value = report_table.iloc[0, 0]
        return return_value

    # метод для получения ключевого параметра
    def get_key_parameter(self, key_parameter_name, search_name, search_value, cut_down=None, cut_up=None):
        time_moment = self.get_time_moment(search_name, search_value, cut_down, cut_up)
        key_table = self.get_parameter_table(key_parameter_name)
        return_value = None
        if time_moment is not None and key_table is not None:
            key_table = key_table[key_table.iloc[:, 0] <= time_moment]
            if len(key_table) > 0:
                key_row = key_table.iloc[-1]
                return_value = key_row[key_parameter_name]
        return return_value

    # метод для получения значений
    def get_values(self, name_values):
        parameter_table = self.get_parameter_table(name_values)
        if parameter_table is not None:
            return parameter_table[name_values]
        else:
            print("Имя " + name_values + " не найдено")
            return None

    # метод для умножения и смещения значений параметра
    def values_mult_shift(self, name_parameter, mult=None, shift=None):
        if mult is None:
            mult = 1
        if shift is None:
            shift = 0
        for table_name in self.data_dict:
            if name_parameter in self.data_dict[table_name]:
                self.data_dict[table_name][name_parameter] = self.data_dict[table_name][name_parameter] * mult + shift

    # метод для копирования объекта
    def make_copy(self):
        return copy.deepcopy(self)

    # метод для отрисовки графика
    def graph(self, GrName, x_names, y_names, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None,
              mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None, empty_graphs=True):

        # Перевод названий по оси y в список
        if isinstance(y_names, str):
            y_names = [y_names]
        if isinstance(x_names, str):
            x_names = [x_names for i in range(len(y_names))]

        if len(y_names) != len(x_names):
            x_names = [x_names[0] for i in range(len(y_names))]

        get_x = [self.get_values(x_name) for x_name in x_names]
        get_y = [self.get_values(y_name) for y_name in y_names]

        draw_graph = True
        None_list=[i is None for i in get_x+get_y]
        if True in None_list:
            draw_graph=False
            print("Ошибка при построении графика " + GrName)

        if draw_graph and (not empty_graphs):
            empty_list=[np.all(y == y[0]) for y in get_y]
            if False not in empty_list:
                draw_graph=False
                print("График {} пустой".format(GrName))

        if draw_graph:
            path_dict = graph(GrName, get_named_data = (get_x, get_y), lablex=lablex, labley=labley, x1=x1, y1=y1, x2=x2, y2=y2, mult_x=mult_x,
                              mult_y=mult_y, shift_x=shift_x, shift_y=shift_y, stpx=stpx, stpy=stpy)

            path_dict["x"] = "_".join(x_names)
            path_dict["y"] = "_".join(y_names)
            self.graph_list.append(path_dict)

    # метод для отрисовки диаграммы Шапиро-Моффетте
    def graph_shapiro_moffette(self, GrName, h2_names, h2o_names, detonation_limits, flammability_limits):
        if h2_names and h2o_names and "dia" in self.data_dict:
            points_list = []
            dia_frame = self.data_dict["dia"]

            if len(h2_names) == len(h2o_names):
                if set(h2_names + h2o_names) <= set(self.data_dict["dia"].columns):
                    for h2_name, h2o_name in zip(h2_names, h2o_names):
                        points_frame = pd.DataFrame(
                            [1 - dia_frame[h2_name] - dia_frame[h2o_name], dia_frame[h2_name], dia_frame[h2o_name]],
                            index=["Air", "Hydrogen", "Steam"])
                        points_list.append(points_frame.T)
                    path_dict = graph_shapiro_moffette(GrName, points_list, detonation_limits, flammability_limits)
                    self.shapiro_moffette_dict = path_dict
                else:
                    print("Указанные кластеры с концентрациями водорода и пара не найдены")
            else:
                print("Количество кластеров с концентрациями водорода и пара не совпадает")


    # метод для создания хронологии
    def make_chrono(self, time_list):
        if isinstance(time_list, dict):
            time_list = [time_list]
        chrono_list = [self.chrono_table]
        for time_point in time_list:
            time_moment = self.get_time_moment(time_point["name"], time_point["value"], time_point["cut_down"],
                                               time_point["cut_up"])
            if time_moment is not None:
                chrono_list.append(
                    pd.DataFrame([[time_moment, time_point["description"]]], columns=["Time", "Description"]))
        self.chrono_table = pd.concat(chrono_list).drop_duplicates().sort_values(by=["Time"]).reset_index(drop=True)

    # метод для создания DataFrame с ключевыми параметрами
    def make_key_table(self, key_list):
        if isinstance(key_list, dict):
            key_list = [key_list]
        key_parameters_list = [self.key_parameters_table]
        for key_point in key_list:
            key_value = self.get_key_parameter(key_point["key_parameter_name"], key_point["search_name"],
                                               key_point["value"], key_point["cut_down"], key_point["cut_up"])
            if key_value is not None:
                key_parameters_list.append(
                    pd.DataFrame([[key_point["description"], key_value]], columns=["Description", "Value"]))
                print(key_point["description"])
        self.key_parameters_table = pd.concat(key_parameters_list).drop_duplicates().reset_index(drop=True)

    # метод для сброса ключевых параметров, хронологий и графиков
    def reset_data(self):
        self.shapiro_moffette_dict = None
        self.graph_list = []
        self.chrono_table = pd.DataFrame(columns=["Time", "Description"])
        self.key_parameters_table = pd.DataFrame(columns=["Description", "Value"])

    # метод для сохранения в файл
    def save(self, path="", name="data"):

        copy_to_save = self.make_copy()
        copy_to_save.reset_data()
        with open(path + name + '.sokle', 'wb') as f:
            pickle.dump(copy_to_save, f)
    
    # метод для получения получения пользовательских значений
    def get_user_values(self, expression):
        init_expression = expression
        list_to_replace = []
        expression_left_lst = expression.split("{")
        for sub_string in expression_left_lst[1:]:
            sub_list = sub_string.split("}")
            list_to_replace.append(sub_list[0])
        list_to_replace = list(set(list_to_replace))
        
        for parameter in list_to_replace:
            expression = expression.replace("{" + parameter + "}", "self.get_values('{}')".format(parameter))

        try:
            value = eval(expression, {"pd": pd, "np": np, "self": self, "calc": self})
        except:
            print("Ошибка при выполнении " + init_expression)
            value = None
        return value
    
    # метод для корректировки параметров
    def correcting_parameters(self, name, expression, integral=False, derivative=False):
        value=self.get_user_values(expression)
        if isinstance(value, pd.Series) and None not in value.values and not np.isnan(value.values).any() and not np.isinf(value.values).any():
            names_frame=list(self.data_dict.keys())
            if name!="Time_report" and "report" in names_frame:
                names_frame.remove("report")
            correcting_frames_names = [name_frame for name_frame in names_frame if len(self.data_dict[name_frame])==len(value)]
            for name_frame in correcting_frames_names:
                table=self.data_dict[name_frame]
                if isinstance(integral,bool) and isinstance(derivative,bool) and integral!=derivative:
                    x=table.iloc[:,0]
                    if integral:
                        value=np.array([np.trapz(value[:i+1],x[:i+1]) for i in range(len(value))])
                    if derivative:
                        value=np.gradient(value,x)
                table[name]=value
            if not correcting_frames_names:
                table_name = "new_table_0"
                i = 0
                while table_name in self.data_dict:
                    i+=1
                    table_name = "new_table_" + str(i)
                self.data_dict[table_name] = pd.DataFrame()
                self.data_dict[table_name][name] = value

class Socrat_calculation(Calculation):
    
    def __init__(self,path_to_folder, dia_names_init=[]):

        super().__init__()
        initial_dir=os.getcwd()
        #метод, выполняемый при инициализации для парсинга файла #_report.lst
        def parsing_report(filename):
            f = open(filename, 'r')
            f = f.read()
            f = f.split("\n")
            indexes = []
            for i in range(len(f)):
                if "TRIP_ONE IS" in f[i] or "TRIP_TWO IS" in f[i] or "COMMAND PERFORMED" in f[i] or "COMMAND:" in f[i] or "COMMAND PROCESSED" in f[i] or "ПРИКАЗ:" in f[i] or "TRIP_ONE:" in f[i] or "TRIP_TWO:" in f[i]:
                    indexes.append(i)
            indexes.append(len(f))

            f_lists = []
            for i in range(len(indexes) - 1):
                f_lists.append(f[indexes[i]:indexes[i + 1]])

            report_lists = []
            for i in range(len(f_lists)):
                if "TRIP_ONE IS" in f_lists[i][0] or "TRIP_TWO IS" in f_lists[i][0] or "COMMAND PERFORMED" in f_lists[i][0] or "ВЫПОЛНЕН ПРИКАЗ:" in f_lists[i][0] or "TRIP_ONE:" in f_lists[i][0] or "TRIP_TWO:" in f_lists[i][0]:
                    name_string = f_lists[i][0]

                    index_end_list = []
                    for k in range(len(f_lists[i]) - 1):
                        if ("STEP=" in f_lists[i][k + 1] or "ШАГ=" in f_lists[i][k + 1]) and (
                                "TIME=" in f_lists[i][k + 1] or "ВРЕМЯ=" in f_lists[i][k + 1]):
                            index_end_list.append(k)
                    index_end = index_end_list[0]

                    condition_string = "".join(f_lists[i][1:index_end + 1]).strip()
                    time_string = f_lists[i][index_end + 1]
                    report_lists.append([name_string, condition_string, time_string])

            list_for_pandas = []
            for event in report_lists:
                if "ВРЕМЯ=" in event[2]:
                    time_for_pandas = float(event[2].split("ВРЕМЯ=")[-1])
                else:
                    time_for_pandas = float(event[2].split("TIME=")[-1])
                name_for_pandas = event[0].split(":")[-1].split()[0]

                if "TRIP_ONE IS OFF" in event[0] or "TRIP_TWO IS OFF" in event[0] or "ВЫКЛЮЧЕН TRIP_ONE:" in event[
                    0] or "ВЫКЛЮЧЕН TRIP_TWO:" in event[0]:
                    state_for_pandas = False
                else:
                    state_for_pandas = True

                if "TRIP_ONE" in event[0]:
                    type_for_pandas = "TRIP_ONE"
                elif "TRIP_TWO" in event[0]:
                    type_for_pandas = "TRIP_TWO"
                elif "COMMAND" in event[0] or "ПРИКАЗ" in event[0]:
                    type_for_pandas = "COMMAND"
                else:
                    type_for_pandas = ""

                if "DELAY:" in event[1]:
                    delay_for_pandas = float(event[1].split("DELAY:")[-1])
                elif "ЗАДЕРЖКА ИСПОЛНЕНИЯ:" in event[1]:
                    delay_for_pandas = float(event[1].split("ЗАДЕРЖКА ИСПОЛНЕНИЯ:")[-1])
                else:
                    delay_for_pandas = 0
                if "CONDITION:" in event[1]:
                    condition_for_pandas = event[1].split("CONDITION:")[-1].split("EXECUTION")[0]
                elif "ПО УСЛОВИЮ:" in event[1]:
                    condition_for_pandas = event[1].split("ПО УСЛОВИЮ:")[-1].split("ЗАДЕРЖКА ИСПОЛНЕНИЯ:")[0]
                else:
                    condition_for_pandas = ""
                list_for_pandas.append([time_for_pandas,
                                        name_for_pandas,
                                        state_for_pandas,
                                        type_for_pandas,
                                        delay_for_pandas,
                                        condition_for_pandas, ])
            return pd.DataFrame(list_for_pandas,
                                    columns=["Time_report", "Name_report", "ON_OFF_report", "Type_report",
                                             "Delay_report", "Condition_report"])

        #открываю папку RESULT
        os.chdir(path_to_folder)
        
        #считываю в формате DataFrame файл #_report.lst
        for report_name in os.listdir():
            if report_name.endswith("#_report.lst"):
                self.data_dict["report"]=parsing_report(report_name)

        #создаю и заполняю список из названий кластеров dia
        dia_names_read=[]
        for dia_name in os.listdir():
            if dia_name.endswith(".dia"):
                dia_names_read.append(dia_name)


        if isinstance(dia_names_init,(list,tuple)) and len(dia_names_init)>0:
            dia_names=[]
            for name_init in dia_names_init:
                for name_read in dia_names_read:
                    if name_init in name_read:
                        dia_names.append(name_read)
        else:
            dia_names=dia_names_read
        #создаю DataFrame из параметров кластеров dia
        dia_table=pd.read_table(dia_names[0], skiprows=1, delim_whitespace=True)
        #создаю словарь, в котором ключи - названия кластеров dia, а значения - входящие в данный кластер параметры
        self.dia_clusters_dict={}
        self.dia_clusters_dict[dia_names[0].split("#")[-1].split(".dia")[0]]=list(dia_table.columns)

        #заполняю созданные DataFrame и словарь
        for dia_name in dia_names[1:]:
            print("Чтение " + dia_name)
            table=pd.read_table(dia_name, skiprows=1, delim_whitespace=True, encoding="mbcs")
            if len(table)==len(dia_table):
                dia_table=pd.merge(dia_table,table)
                self.dia_clusters_dict[dia_name.split("#")[-1].split(".dia")[0]]=list(table.columns)
            else:
                # бывает, что СОКРАТ криво записывает файлы
                print("Проблемы с кластером " + dia_name)
        self.data_dict["dia"]=dia_table
        
        
        #считываю в формате DataFrame файлы p1runout и p1spn
        for folder_hef in os.listdir():
            if folder_hef.endswith("#hefest"):
                os.chdir(folder_hef)
                if "p1runout" in os.listdir():
                    try:
                        table = pd.read_table("p1runout", delim_whitespace=True)
                        if len(table)>0 and not table.isna().sum().sum():
                            self.data_dict["p1runout"] = table
                    except:
                        print("Ошибка при чтении p1runout")
                if "p1spn" in os.listdir():
                    try:
                        table = pd.read_table("p1spn", delim_whitespace=True)
                        if len(table)>0 and not table.isna().sum().sum():
                            self.data_dict["p1spn"] = table
                    except:
                        print("Ошибка при чтении p1spn")
        keys_to_remote=[]
        for table_name in self.data_dict:
            if len(self.data_dict[table_name]) == 0:
                keys_to_remote.append(table_name)
        for key in keys_to_remote:
            self.data_dict.pop(key)
            
        
        os.chdir(initial_dir)

    #метод для получения dia_кластера
    def get_dia_cluster(self, cluster_name):
        if cluster_name in self.dia_clusters_dict:
            return self.data_dict["dia"][self.dia_clusters_dict[cluster_name]]
        else:
            return None


class Trap_calculation(Calculation):

    def __init__(self, path_to_folder):
        super().__init__()

        # метод для парсинга файла event
        def parsing_event(filename):
            list_for_pandas = []
            with open(filename, "r", encoding='cp866') as f:
                blocks = f.read().split("\n\n")
                for block in blocks:
                    if "=" in block:
                        block = block.split("ВРЕМЯ")
                        name = block[0].strip()
                        time = block[1]
                        time = time.split("=")[1]
                        time = time.split()[0]
                        list_for_pandas.append([time, name, True])
            return pd.DataFrame(list_for_pandas, columns=["Time_report", "Name_report", "ON_OFF_report"])

        # метод для чтения lent3
        def read_lent3(filename):

            with open(filename, 'rb') as f:
                names = []
                data = []
                f.seek(4)
                N_parameters = int.from_bytes(f.read(4), 'little')
                f.seek(4, 1)
                f.seek(4 * (N_parameters + 1), 1)

                for i in range(N_parameters):
                    names.append(f.read(60).decode('cp866'))

                names[0] = "Time"
                names = [string.strip() for string in names]

                file_b = f.read()
                N_rows = int(len(file_b) / 4 / (N_parameters + 2))

                for i in range(N_rows):
                    row = file_b[(i) * 4 * (N_parameters + 2):(i + 1) * 4 * (N_parameters + 2)]
                    row = [unpack("f", row[k * 4:(k + 1) * 4])[0] for k in range(N_parameters + 2)]
                    data.append(row[2:])
                names_non_unique = set([name for name in names if names.count(name) > 1])
                names_unique = set(names) - names_non_unique
                names_non_unique_counter = {}
                for name in names_non_unique:
                    names_non_unique_counter[name] = 0
                names_corrected = []
                for name in names:
                    if name in names_unique:
                        names_corrected.append(name)
                    else:
                        names_non_unique_counter[name] += 1
                        names_corrected.append(name + " " + str(names_non_unique_counter[name]))
            return pd.DataFrame(data, columns=names_corrected)

        initial_dir = os.getcwd()
        os.chdir(path_to_folder)

        self.data_dict["dia"]=read_lent3("lent3")

        if "event" in os.listdir():
            self.data_dict["report"]=parsing_event("event")

        os.chdir(initial_dir)


class Series_of_calculations:
    def __init__(self, calculations):
        self.series=[]
        self.graph_list=[]
        self.chrono_table=pd.DataFrame(columns=["Description"])
        self.key_parameters_table=pd.DataFrame(columns=["Description"])
        
        if not isinstance(calculations,list):
            calculations=[calculations]
        for i in range(len(calculations)):
            self.series.append(calculations[i])
            calc_chrono=calculations[i].chrono_table.reindex(columns=["Description", "Time"])
            calc_chrono.columns=["Description", "Time_"+str(i+1)]
            self.chrono_table=self.chrono_table.merge(calc_chrono,how="outer",on = "Description").fillna("–")
            calc_key_parameters=calculations[i].key_parameters_table.copy()
            calc_key_parameters.columns=["Description", "Values_"+str(i+1)]
            self.key_parameters_table=self.key_parameters_table.merge(calc_key_parameters,how="outer",on = "Description").fillna("–")
    
    def graph (self, GrName, x_names, y_names, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None, mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None, empty_graphs=True):
        if isinstance(y_names, str):
            y_names=[y_names]
        if isinstance(x_names, str):
            x_names=[x_names for i in range(len(y_names))]

        if len(y_names) != len(x_names):
            x_names = [x_names[0] for i in range(len(y_names))]

        get_x=[]
        get_y=[]


        for calc in self.series:
            for i in range(len(y_names)):
                get_x.append(calc.get_values(x_names[i]))
                get_y.append(calc.get_values(y_names[i]))

        draw_graph=True
        None_list = [i is None for i in get_x + get_y]
        if True in None_list:
            draw_graph = False
            print("Ошибка при построении графика " + GrName)

        if draw_graph and (not empty_graphs):
            empty_list = [np.all(y == y[0]) for y in get_y]
            if False not in empty_list:
                draw_graph = False
                print("График {} пустой".format(GrName))

        if draw_graph:
            path_dict=graph(GrName, get_named_data = (get_x, get_y), lablex=lablex, labley=labley, x1=x1, y1=y1, x2=x2, y2=y2, mult_x=mult_x, mult_y=mult_y, shift_x=shift_x, shift_y=shift_y, stpx=stpx, stpy=stpy)

            path_dict["x"]="_".join(x_names)
            path_dict["y"]="_".join(y_names)
            self.graph_list.append(path_dict)
        
class SU_Series:
    def __init__(self, path_to_values):
        self.vars_frame = pd.read_csv(path_to_values, delim_whitespace=True, index_col="number")
        self.calculations_list = []
        self.key_parameters = []
        self.dynamic_parameters = {}
        self.calculations_without_deviations = []
        self.graph_list = []
        
        rel_path_to_result = None
        path_to_first_calc = os.path.join(os.path.dirname(path_to_values), str(self.vars_frame.index[0]))
        
        for rootdir, dirs, files in os.walk(path_to_first_calc):
            dia_contains = [file.endswith(".dia") for file in files]
            if True in dia_contains:
                rel_path_to_result = os.path.relpath(rootdir, path_to_first_calc)
                break
        
        for number in self.vars_frame.index:
            print(number)
            calc = Socrat_calculation("{}\\{}\\{}".format(os.path.dirname(path_to_values), str(number), rel_path_to_result))
            calc.frame_line = self.vars_frame.loc[number]
            self.calculations_list.append(calc)
        
        self.corrected_calculations_list = self.calculations_list
        self.corrected_frame = self.vars_frame
    
    def append_calculation_without_deviation(self, calc):
        if isinstance(calc, str):
            if calc.endswith(".sokle"):
                with open(calc, "rb") as f:
                    self.calculations_without_deviations.append(pickle.load(f))
            elif os.path.isdir(calc):
                dir_files = os.listdir(calc)
                dia_names_bool = [name.endswith(".dia") for name in dir_files]
                if True in dia_names_bool:
                    self.calculations_without_deviations.append(Socrat_calculation(calc))
        elif isinstance(calc, Socrat_calculation):
            self.calculations_without_deviations.append(calc)
    
    def cut_bottom_transform(self, parameter_name, parameter_value):
        for calc in self.calculations_list:
            calc.cut_bottom_transform(parameter_name, parameter_value)
        for calc in self.calculations_without_deviations:
            calc.cut_bottom_transform(parameter_name, parameter_value)
    
    def cut_top_transform(self, parameter_name, parameter_value):
        for calc in self.calculations_list:
            calc.cut_top_transform(parameter_name, parameter_value)
        for calc in self.calculations_without_deviations:
            calc.cut_top_transform(parameter_name, parameter_value)
    
    def make_corrected_data(self, key_parameters, check_function = lambda calc: True):
        self.corrected_calculations_list = []
        self.key_parameters = key_parameters
        
        i = 1
        for parameter in self.key_parameters:
            if "cut_down" not in parameter:
                parameter["cut_down"] = None
            if "cut_up" not in parameter:
                parameter["cut_up"] = None
            if "bins" not in parameter:
                parameter["bins"] = 7
            parameter["symbol"] = "KEY" + str(i)
            i+=1
                
        for calc in self.calculations_list:
            for parameter in self.key_parameters:
                key_value = calc.get_key_parameter(parameter["key_parameter_name"], parameter["search_name"], parameter["search_value"], parameter["cut_down"], parameter["cut_up"])
                if key_value is not None and "mult" in parameter:
                    key_value = key_value * parameter["mult"]
                if key_value is not None and "shift" in parameter:
                    key_value = key_value + parameter["shift"]
                calc.frame_line[parameter["symbol"]] = key_value
            if not calc.frame_line.isna().sum() and check_function(calc):
                self.corrected_calculations_list.append(calc)
        self.corrected_frame = pd.DataFrame([calc.frame_line for calc in self.corrected_calculations_list])
        self.make_convergence_frames()
        
    def make_convergence_frames(self):
        for parameter in self.key_parameters:
            mean_list = []
            std_list = []
            values_series = self.corrected_frame[parameter["symbol"]]
            for i in range(len(values_series)):
                slice_series = values_series.iloc[:i+1]
                mean_list.append(slice_series.mean())
                std_list.append(slice_series.std())
            mean_series = pd.Series(mean_list, name = "mean")
            std_series = pd.Series(std_list, name = "std")
            rel_std_series = pd.Series(std_series/mean_series, name = "rel_std")
            N_series = pd.Series(np.arange(1,len(values_series)+1),name = "N")
            convergence_frame = pd.DataFrame([N_series, mean_series, std_series, rel_std_series]).T
            convergence_frame = convergence_frame.fillna(0)
            parameter["convergence"] = convergence_frame
    
    def make_dynamic_data(self, dynamic_parameters):
        self.dynamic_parameters = dynamic_parameters
        dynamic_parameters_dict = {}
        names = []
        for parameter in self.dynamic_parameters:
            if isinstance(parameter["name"], str):
                names.append(parameter["name"])
            else:
                names.extend(list(parameter["name"]))
        names = set(names)
        
        
        cluster_dict_calcs = {}
        for calc in self.corrected_calculations_list:
            for cluster_name in calc.data_dict:
                if cluster_name in cluster_dict_calcs:
                    cluster_dict_calcs[cluster_name] = cluster_dict_calcs[cluster_name] | set(calc.data_dict[cluster_name].columns)
                else:
                    cluster_dict_calcs[cluster_name] = set(calc.data_dict[cluster_name].columns)
        
        cluster_dict_names = {}
        for cluster_name in cluster_dict_calcs:
            common_names = set(names) & cluster_dict_calcs[cluster_name]
            if common_names:
                cluster_dict_names[cluster_name] = list(common_names)
        
        checked_calculations_list = []
        for calc in self.corrected_calculations_list + self.calculations_without_deviations:
            check_list = []
            for cluster_name in cluster_dict_names:
                if cluster_name in calc.data_dict and (set(cluster_dict_names[cluster_name]) <= set(calc.data_dict[cluster_name].columns)):
                    check_list.append(True)
                else:
                    check_list.append(False)
                if False not in check_list:
                    checked_calculations_list.append(calc)
        
        for cluster_name in cluster_dict_names:
            for name in cluster_dict_names[cluster_name]:
                dynamic_parameters_dict[name] = {}
                dynamic_parameters_dict[name]["Time"] = []
                dynamic_parameters_dict[name]["min"] = []
                dynamic_parameters_dict[name]["max"] = []
                dynamic_parameters_dict[name]["mean"] = []
                dynamic_parameters_dict[name]["std"] = []
            time_name = checked_calculations_list[0].data_dict[cluster_name].columns[0]
            clusters_list = [calc.data_dict[cluster_name][[time_name] + cluster_dict_names[cluster_name]] for calc in checked_calculations_list]
            start_time = min([cluster[time_name].iloc[0] for cluster in clusters_list])
            while True:
                clusters_list = [cluster for cluster in clusters_list if cluster[time_name].iloc[-1] > start_time]
                if not clusters_list:
                    break
                finish_time = max([cluster[time_name][cluster[time_name] > start_time].iloc[0] for cluster in clusters_list])
                clusters_moment_list = [cluster[(cluster[time_name] > start_time) & (cluster[time_name] <= finish_time)] for cluster in clusters_list]
                
                for name in cluster_dict_names[cluster_name]:
                    dynamic_parameters_dict[name]["Time"].append(finish_time)
                    values = [cluster[name] for cluster in clusters_moment_list]
                    dynamic_parameters_dict[name]["min"].append(np.min([series.min() for series in values]))
                    dynamic_parameters_dict[name]["max"].append(np.max([series.max() for series in values]))
                    last_values = np.array([value.iloc[-1] for value in values])
                    dynamic_parameters_dict[name]["mean"].append(last_values.mean())
                    dynamic_parameters_dict[name]["std"].append(last_values.std())
                
                start_time = finish_time
        
        for name in dynamic_parameters_dict:
            dynamic_parameters_dict[name] = pd.DataFrame(dynamic_parameters_dict[name])
        
        for parameter in self.dynamic_parameters:
            if isinstance(parameter["name"] , str):
                parameter["frame"] = dynamic_parameters_dict[parameter["name"]]
            else:
                names = list(parameter["name"])
                frames_list = [dynamic_parameters_dict[name] for name in names]
                Time_list = [frame["Time"] for frame in frames_list]
                Time_series = Time_list[0]
                check_list = [len(Time_series) == len(series) and (Time_series == series).all() for series in Time_list]
                if False not in check_list:
                    min_list = [frame["min"] for frame in frames_list]
                    max_list = [frame["max"] for frame in frames_list]
                    mean_list = [frame["mean"] for frame in frames_list]
                    std_list = [frame["std"] for frame in frames_list]
                    
                    min_series = pd.Series([np.min(i) for i in zip(*min_list)], name = "min")
                    max_series = pd.Series([np.max(i) for i in zip(*max_list)], name = "max")
                    mean_series = pd.Series([np.array(i).mean() for i in zip(*mean_list)], name = "mean")
                    std_series = pd.Series([np.sqrt(np.sum(np.square(np.array(i)))) for i in zip(*std_list)], name = "std")
                    
                    parameter["frame"] = pd.DataFrame([Time_series, min_series, max_series, mean_series, std_series]).T
    
    def drow_dynamic_data(self, drow_min = True, 
                          drow_max = True, 
                          drow_mean = True, 
                          drow_src = True, 
                          drow_without_dev = True):
        for parameter in self.dynamic_parameters:
            get_named_data = ([],[])
            get_unamed_data = ([],[])
            description = parameter["description"] + "\n"
            names = parameter["name"]
            
            if isinstance(names, str):
                names = [names]
            
            for name in names:
                if drow_src:
                    for calc in self.corrected_calculations_list:
                        table = calc.get_parameter_table(name)
                        get_unamed_data[0].append(table.iloc[:,0])
                        get_unamed_data[1].append(table[name])
                
                if drow_without_dev:
                    for calc in self.calculations_without_deviations:
                        table = calc.get_parameter_table(name)
                        get_named_data[0].append(table.iloc[:,0])
                        get_named_data[1].append(table[name])
                        description = description + str(len(get_named_data[0])) + r" - расчёт без отклонений " + name + ", "
                    
            if drow_mean:
                get_named_data[0].append(parameter["frame"]["Time"])
                get_named_data[1].append(parameter["frame"]["mean"])
                description = description + str(len(get_named_data[0])) + r" - среднее значение"+ ", "
            
            if drow_min:
                get_named_data[0].append(parameter["frame"]["Time"])
                get_named_data[1].append(parameter["frame"]["min"])
                description = description + str(len(get_named_data[0])) + r" - минимальное значение"+ ", "
            
            if drow_max:
                get_named_data[0].append(parameter["frame"]["Time"])
                get_named_data[1].append(parameter["frame"]["max"])
                description = description + str(len(get_named_data[0])) + r" - максимальное значение"+ ", "
            
            if not get_named_data[0]:
                get_named_data = None
            
            if not get_unamed_data[0]:
                get_unamed_data = None
            
            labelx = parameter.get("labelx")
            if not labelx:
                labelx=""
            
            labely = parameter.get("labely")
            if not labely:
                labely=""
            
            x1, y1, x2, y2, mult_x, mult_y, shift_x, shift_y, stpx, stpy = (parameter.get("x1"),
                                                                            parameter.get("y1"),
                                                                            parameter.get("x2"),
                                                                            parameter.get("y2"),
                                                                            parameter.get("mult_x"),
                                                                            parameter.get("mult_y"),
                                                                            parameter.get("shift_x"),
                                                                            parameter.get("shift_y"),
                                                                            parameter.get("stpx"),
                                                                            parameter.get("stpy"),
                                                                            )
            if get_named_data or get_unamed_data:
                path_dict = graph (str(1+len(self.graph_list)), 
                                   get_named_data, get_unamed_data, 
                                   labelx, labely, 
                                   x1, y1, x2, y2, 
                                   mult_x, mult_y, 
                                   shift_x, shift_y, 
                                   stpx, stpy)
                path_dict["description"] = description + "\n"
                self.graph_list.append(path_dict)
    
    def drow_histigramm(self, parameter):
        
        
        
        description = parameter["description"] + "\n"
        hist_series = self.corrected_frame[parameter["symbol"]]
        values_without_deviations = pd.Series([calc.get_key_parameter(parameter["key_parameter_name"], 
                                                                      parameter["search_name"], 
                                                                      parameter["search_value"], 
                                                                      parameter["cut_down"], 
                                                                      parameter["cut_up"]) for calc in self.calculations_without_deviations])
        
        if "mult" in parameter:
            values_without_deviations = values_without_deviations * parameter["mult"]
        if "shift" in parameter:
            values_without_deviations = values_without_deviations + parameter["shift"]
        
        
        hist_series = pd.concat([hist_series,values_without_deviations]).reset_index(drop = True)
        plt.figure(figsize=(10,6))
        n, bins, pathes = plt.hist(hist_series,bins=parameter["bins"],alpha=.7,color='black')
        plt.xticks(bins)
        plt.xlabel(parameter["label"],fontsize=15,loc='center')
        plt.ylabel('N', rotation='horizontal',fontsize=15,loc='top')
        
        path_dict = {}
        fmt = "png"
        GrName = str(len(self.graph_list)+1)
        path_dict[fmt]=os.path.abspath(os.curdir)+"\\"+GrName + "." + fmt
        path_dict["description"] = description + "Гистограмма распределения"
        plt.savefig('{}.{}'.format(GrName, fmt), format=fmt, bbox_inches='tight')
        plt.close()
        self.graph_list.append(path_dict)
    
    def drow_convergence(self, parameter,
                         mean = True, std = True, rel_std = True):
        convergence_frame = parameter["convergence"]
        description = parameter["description"] + "\n"
        units = parameter["label"].split(",")[-1]
        
        if mean:
            path_dict = graph(str(1+len(self.graph_list)),
                              get_named_data = (convergence_frame["N"],convergence_frame["mean"]),
                              lablex = "N", labley = "μ," + units, y1 = 0)
            path_dict["description"] = description + "Среднее значение за N расчетов"
            self.graph_list.append(path_dict)
        if std:
            path_dict = graph(str(1+len(self.graph_list)),
                              get_named_data = (convergence_frame["N"],convergence_frame["std"]),
                              lablex = "N", labley = "σ," + units)
            path_dict["description"] = description + "Среднеквадратическое отклонение за N расчетов"
            self.graph_list.append(path_dict)
        if rel_std:
            path_dict = graph(str(1+len(self.graph_list)),
                              get_named_data = (convergence_frame["N"],convergence_frame["rel_std"]),
                              lablex = "N", labley = "σ, %", mult_y=100)
            path_dict["description"] = description + "Относительное среднеквадратическое отклонение за N расчетов"
            self.graph_list.append(path_dict)
    
    
    def drow_key_data(self, hist = True,
                      mean = True,
                      std = True,
                      rel_std = True):
        for parameter in self.key_parameters:
            if hist:
                self.drow_histigramm(parameter)
            if mean or std or rel_std:
                self.drow_convergence(parameter, mean, std, rel_std)
            
            
    """
    def drow_heat_maps(self, a = 1, b = 1, pearson = True, spearman = True, kendall = True):
        corr_names = []
        if pearson:
            corr_names.append("pearson")
        if spearman:
            corr_names.append("spearman")
        if kendall:
            corr_names.append("kendall")
        var_number = len(self.vars_frame.columns)
        key_number = len(self.key_parameters)
                
        for method in corr_names:
            corr_frame = self.corrected_frame.corr(method).iloc[:var_number,var_number:]
            plt.figure(figsize=(a*0.7*key_number,b*0.37*var_number),)
            plt.rc('ytick',labelsize=10)
            plt.rc('xtick',labelsize=10)
            sns.heatmap(corr_frame,cmap='coolwarm',annot=True,annot_kws={'size':10},fmt='.2f',linecolor='white',linewidths=2,cbar=False)            
            path_dict = {}
            fmt = "png"
            GrName = str(len(self.graph_list)+1)
            path_dict[fmt]=os.path.abspath(os.curdir)+"\\"+GrName + "." + fmt
            path_dict["description"] = "Тепловая карта корреляции " + method.title()
            plt.savefig('{}.{}'.format(GrName, fmt), format=fmt, bbox_inches='tight')
            plt.close()
            self.graph_list.append(path_dict)
        """
        
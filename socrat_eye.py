
def graph (GrName, get_x, get_y, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None, mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    import pylab
    import os
    import pandas
    import numpy
    
    
    if isinstance(get_y[0],(numpy.ndarray,pandas.Series,list,tuple)):
        y=[pandas.Series(i) for i in get_y]
    else:
        y=[pandas.Series(get_y)]
    if isinstance(get_x[0],(numpy.ndarray,pandas.Series,list,tuple)):
        x=[pandas.Series(i) for i in get_x]
    else:
        x=[pandas.Series(get_x) for i in range(len(y))]
    
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
        x=[i*mult_x for i in x]
    if mult_y is not None:
        y=[i*mult_y for i in y]
    if shift_x is not None:
        x=[i+shift_x for i in x]
    if shift_y is not None:
        y=[i+shift_y for i in y]
    
    if x1 is None:
        x1=min(min(i) for i in x)
    else:
        for i in range(len(x)):
            if x1>x[i][0]:
                N_min=x[i][x[i]>x1].index[0]
                x[i]=x[i][N_min:]
                y[i]=y[i][N_min:]
    if x2 is None:
        x2=max(max(i) for i in x)
    else:
        for i in range(len(x)):
            if x2<x[i][len(x[i])-1]:
                N_max=x[i][x[i]>x2].index[0]
                x[i]=x[i][:N_max]
                y[i]=y[i][:N_max]
    
    if y1 is None:
        y1=min(min(i) for i in y)
    if y2 is None:
        y2=0.1*(max(max(i) for i in y)-y1)+max(max(i) for i in y)
        
    path_dict["x_min"]=str(int(x1))
    path_dict["x_max"]=str(int(x2))
    path_dict["y_min"]=str(int(y1))
    path_dict["y_max"]=str(int(y2))

    N_points_aray=[]
    for i in range(len(x)):
        N_points = len(x[i])//50
        if N_points==0:
            N_points=1
        N_points_aray.append(N_points)
    for i in range(len(y)):
        ax.plot(x[i], y[i], colors[i], linewidth = 2, label = str(i+1), marker = markers[i], markevery = N_points_aray[i])
    
    pylab.xlim (xmin = x1, xmax=x2)
    pylab.ylim (ymin = y1, ymax=y2)
    #Настраиваем оси
    #Устанавливаем интервал делений x:
    if stpx!=None:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(stpx))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(stpx/5))
    #Устанавливаем интервал делений y:
    if stpy!=None:
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
    
    if len(get_y)>1:
        pylab.legend(loc='best', numpoints=1, fontsize=20).get_frame().set_edgecolor('w')
    
    fig.set_figwidth(12)
    fig.set_figheight(8)
    
    # сохранение .png
    fmt = 'png'
    path_dict[fmt]=os.path.abspath(os.curdir)+"\\"+GrName + "." +fmt
    fig.savefig('{}.{}'.format(GrName, fmt), format=fmt, bbox_inches='tight')
    # сохранение .pdf
#    fmt = 'pdf'
#    pwd = os.getcwd()
#    iPath = '{}'.format(fmt)
#    if not os.path.exists(iPath):
#        os.mkdir(iPath)
#    os.chdir(iPath)
#    path_dict[fmt]=os.path.abspath(os.curdir) + "\\" + GrName + "." +fmt
    #fig.savefig('{}.{}'.format(name, fmt), fmt='png')
#    fig.savefig('{}.{}'.format(GrName, fmt), format='pdf', bbox_inches='tight')
#    os.chdir(pwd)
    plt.close()
    
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
            for table_name in self.data_dict:
                table = self.data_dict[table_name]
                time_table = table.iloc[0, 0]
                if time_table < lower_time:
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
            for table_name in self.data_dict:
                table = self.data_dict[table_name]
                time_table = table.iloc[-1, 0]
                if time_table > upper_time:
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
        if table is not None and isinstance(parameter_value, float):
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
                    return table.iloc[min(indexes), :]
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
                    if report_table is not None:
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
        import copy
        return copy.deepcopy(self)

    # метод для отрисовки графика
    def graph(self, GrName, x_names, y_names, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None,
              mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None):

        if isinstance(y_names, str):
            y_names = [y_names]
        if isinstance(x_names, str):
            x_names = [x_names for i in range(len(y_names))]

        if len(y_names) != len(x_names):
            x_names = [x_names[0] for i in range(len(y_names))]

        get_x = [self.get_values(x_name) for x_name in x_names]
        get_y = [self.get_values(y_name) for y_name in y_names]

        path_dict = graph(GrName, get_x, get_y, lablex=lablex, labley=labley, x1=x1, y1=y1, x2=x2, y2=y2, mult_x=mult_x,
                          mult_y=mult_y, shift_x=shift_x, shift_y=shift_y, stpx=stpx, stpy=stpy)

        path_dict["x"] = "_".join(x_names)
        path_dict["y"] = "_".join(y_names)
        self.graph_list.append(path_dict)

    # метод для создания хронологии
    def make_chrono(self, time_list):
        import pandas
        if isinstance(time_list, dict):
            time_list = [time_list]
        chrono_list = [self.chrono_table]
        for time_point in time_list:
            time_moment = self.get_time_moment(time_point["name"], time_point["value"], time_point["cut_down"],
                                               time_point["cut_up"])
            if time_moment is not None:
                chrono_list.append(
                    pandas.DataFrame([[time_moment, time_point["description"]]], columns=["Time", "Description"]))
        self.chrono_table = pandas.concat(chrono_list).drop_duplicates().sort_values(by=["Time"]).reset_index(drop=True)

    # метод для создания DataFrame с ключевыми параметрами
    def make_key_table(self, key_list):
        import pandas
        if isinstance(key_list, dict):
            key_list = [key_list]
        key_parameters_list = [self.key_parameters_table]
        for key_point in key_list:
            key_value = self.get_key_parameter(key_point["key_parameter_name"], key_point["search_name"],
                                               key_point["value"], key_point["cut_down"], key_point["cut_up"])
            if key_value is not None:
                key_parameters_list.append(
                    pandas.DataFrame([[key_point["description"], key_value]], columns=["Description", "Value"]))
        self.key_parameters_table = pandas.concat(key_parameters_list).drop_duplicates().reset_index(drop=True)

    # метод для сброса ключевых параметров, хронологий и графиков
    def reset_data(self):
        import pandas
        self.graph_list = []
        self.chrono_table = pandas.DataFrame(columns=["Time", "Description"])
        self.key_parameters_table = pandas.DataFrame(columns=["Description", "Value"])

    # метод для сохранения в файл
    def save(self, path="", name="data"):
        import pickle
        copy_to_save = self.make_copy()
        copy_to_save.reset_data()
        with open(path + name + '.sokle', 'wb') as f:
            pickle.dump(copy_to_save, f)
    
    # метод для получения получения пользовательских значений
    def get_user_values(self, expression):
        import re
        init_expression=expression
        str_values_with_bracets=re.findall("\{\w*\}", expression)
        for str_value_with_bracets in str_values_with_bracets:
            str_value=str_value_with_bracets[1:-1]
            str_value="self.get_values('{}')".format(str_value)
            expression=expression.replace(str_value_with_bracets, str_value)
        
        try:
            value=eval(expression)
        except:
            print("Ошибка при выполнении " + init_expression)
            value=None
        return value
    
    # метод для корректировки параметров
    def correcting_parameters(self, name, expression, integral=False, derivative=False):
        import pandas as pd
        import numpy as np
        value=self.get_user_values(expression)
        if isinstance(value, pd.Series):
            names_frame=list(self.data_dict.keys())
            if "report" in names_frame:
                names_frame.remove("report")
            for name_frame in names_frame:
                if len(self.data_dict[name_frame])==len(value):
                    table=self.data_dict[name_frame]
                    
                    if isinstance(integral,bool) and isinstance(derivative,bool) and integral!=derivative:
                        x=table.iloc[:,0]
                        if integral:
                            value=np.array([np.trapz(value[:i+1],x[:i+1]) for i in range(len(value))])
                        if derivative:
                            value=np.gradient(value,x)
                    table[name]=value


class Socrat_calculation(Calculation):
    
    def __init__(self,path_to_folder, dia_names=[], time_shift=None):

        super().__init__()

        import os
        import pandas
        initial_dir=os.getcwd()
        #метод, выполняемый при инициализации для парсинга файла #_report.lst
        def parsing_report(filename):
            f = open(filename,'r')
            f=f.read()
            f=f.split("\n")
            indexes=[]
            for i in range(len(f)):
                if "TRIP_ONE IS" in f[i] or "TRIP_TWO IS" in f[i] or "COMMAND PERFORMED" in f[i] or "COMMAND:" in f[i] or "COMMAND PROCESSED" in f[i]:
                    indexes.append(i)
            indexes.append(len(f))
            
            f_lists=[]
            for i in range(len(indexes)-1):
                f_lists.append(f[indexes[i]:indexes[i+1]])
            
            report_lists=[]
            for i in range(len(f_lists)):
                if "TRIP_ONE IS" in f_lists[i][0] or "TRIP_TWO IS" in f_lists[i][0] or "COMMAND PERFORMED" in f_lists[i][0]:
                    name_string=f_lists[i][0]
                    
                    index_end_list=[]
                    for k in range(len(f_lists[i])-1):
                        if "STEP=" in f_lists[i][k+1] and "TIME=" in f_lists[i][k+1]:
                            index_end_list.append(k)
                    index_end=index_end_list[0]
                    
                    condition_string="".join(f_lists[i][1:index_end+1]).strip()
                    time_string=f_lists[i][index_end+1]
                    report_lists.append([name_string,condition_string,time_string])
            
            list_for_pandas=[]
            for event in report_lists:
                time_for_pandas=float(event[2].split("TIME=")[-1])
                name_for_pandas=event[0].split(":")[-1].split()[0]
                
                if "TRIP_ONE IS OFF" in event[0] or "TRIP_TWO IS OFF" in event[0]:
                    state_for_pandas=False
                else:
                    state_for_pandas=True
                
                if "TRIP_ONE" in event[0]:
                    type_for_pandas="TRIP_ONE"
                elif "TRIP_TWO" in event[0]:
                    type_for_pandas="TRIP_TWO"
                elif "COMMAND" in event[0]:
                    type_for_pandas="COMMAND"
                else:
                    type_for_pandas=""
                
                if "DELAY:" in event[1]:
                    delay_for_pandas=float(event[1].split("DELAY:")[-1])
                else:
                    delay_for_pandas=0
                if "CONDITION:" in event[1]:
                    condition_for_pandas=event[1].split("CONDITION:")[-1].split("EXECUTION")[0]
                else:
                    condition_for_pandas=""
                list_for_pandas.append([time_for_pandas,
                                        name_for_pandas,
                                        state_for_pandas,
                                        type_for_pandas,
                                        delay_for_pandas,
                                        condition_for_pandas,])
            return pandas.DataFrame(list_for_pandas,columns=["Time_report","Name_report", "ON_OFF_report","Type_report", "Delay_report", "Condition_report"])

        
        #открываю папку RESULT
        os.chdir(path_to_folder)
        
        #считываю в формате DataFrame файл #_report.lst
        for report_name in os.listdir():
            if report_name.endswith("#_report.lst"):
                self.data_dict["report"]=parsing_report(report_name)

        #создаю и заполняю список из названий кластеров dia
        dia_names=[]
        for dia_name in os.listdir():
            if dia_name.endswith(".dia"):
                dia_names.append(dia_name)
        #создаю DataFrame из параметров кластеров dia
        dia_table=pandas.read_table(dia_names[0], skiprows=1, delim_whitespace=True)
        #создаю словарь, в котором ключи - названия кластеров dia, а значения - входящие в данный кластер параметры
        self.dia_clusters_dict={}
        self.dia_clusters_dict[dia_names[0].split("#")[-1].split(".dia")[0]]=list(dia_table.columns)

        #заполняю созданные DataFrame и словарь
        for dia_name in dia_names[1:]:
            print("Чтение " + dia_name)
            table=pandas.read_table(dia_name, skiprows=1, delim_whitespace=True, encoding="mbcs")
            if len(table)==len(dia_table):
                dia_table=pandas.merge(dia_table,table)
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
                    self.data_dict["p1runout"]=pandas.read_table("p1runout", delim_whitespace=True)
                if "p1spn" in os.listdir():
                    self.data_dict["p1spn"]=pandas.read_table("p1spn", delim_whitespace=True)

        
        #Проверка разницы между Time и TIME_a
        if time_shift==None and "TIME_a" in dia_table:
            time_shift=dia_table["Time"][0] - dia_table["TIME_a"][0]
        
        if time_shift!=0 and time_shift!=None:
            self.time_shift_transform(time_shift)
        
        os.chdir(initial_dir)
        
    #метод для проверки параметров, которые если упали в 0, там и остаются (например температуры оболочек твэлов, СУЗов и топлива)
    def last_zero_parameters_transform(self,names_last_zero_parameters):
        if isinstance(names_last_zero_parameters,str):
            names_last_zero_parameters=[names_last_zero_parameters]
        for name_last_zero_parameter in names_last_zero_parameters:
            if name_last_zero_parameter in self.data_dict["dia"].columns and min(self.data_dict["dia"][name_last_zero_parameter])<=0:
                start_index=self.data_dict["dia"][self.data_dict["dia"][name_last_zero_parameter]<=0][name_last_zero_parameter].index[0]
                self.data_dict["dia"][name_last_zero_parameter][start_index:]=0
    
    #метод для проверки параметров, которые не должны резко падать в ноль
    def not_zero_parameters_transform(self,names_not_zero_parameters):
        if isinstance(names_not_zero_parameters,str):
            names_not_zero_parameters=[names_not_zero_parameters]
        for name_not_zero_parameter in names_not_zero_parameters:
            if name_not_zero_parameter in self.data_dict["dia"].columns and min(self.data_dict["dia"][name_not_zero_parameter])<=0:
                for k in range(len(self.data_dict["dia"][name_not_zero_parameter])-1):
                    if self.data_dict["dia"][name_not_zero_parameter][k+1]<=0:
                        self.data_dict["dia"][name_not_zero_parameter][k+1]=self.data_dict["dia"][name_not_zero_parameter][k]

    #метод для получения dia_кластера
    def get_dia_cluster(self, cluster_name):
        if cluster_name in self.dia_clusters_dict:
            return self.data_dict["dia"][self.dia_clusters_dict[cluster_name]]
        else:
            return None


class Trap_calculation(Calculation):

    def __init__(self, path_to_folder):
        super().__init__()

        import os
        import pandas

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
            return pandas.DataFrame(list_for_pandas, columns=["Time_report", "Name_report", "ON_OFF_report"])

        # метод для чтения lent3
        def read_lent3(filename):
            from struct import unpack
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

            return pandas.DataFrame(data, columns=names)

        initial_dir = os.getcwd()
        os.chdir(path_to_folder)

        self.data_dict["dia"]=read_lent3("lent3")

        if "event" in os.listdir():
            self.data_dict["report"]=parsing_event("event")

        os.chdir(initial_dir)


class Series_of_calculations:
    def __init__(self, calculations):
        import pandas
        self.series=[]
        self.graph_list=[]
        self.chrono_table=pandas.DataFrame(columns=["Description"])
        self.key_parameters_table=pandas.DataFrame(columns=["Description"])
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

    
    def graph (self, GrName, x_names, y_names, lablex="t, s", labley="", x1=None, y1=None, x2=None, y2=None, mult_x=None, mult_y=None, shift_x=None, shift_y=None, stpx=None, stpy=None):
        
        if isinstance(y_names, str):
            y_names=[y_names]
        if isinstance(x_names, str):
            x_names=[x_names for i in range(len(y_names))]

        if len(y_names) != len(x_names):
            x_names = [x_names[0] for i in range(len(y_names))]

        get_x=[]
        get_y=[]

        print(x_names)
        print(y_names)

        for calc in self.series:
            for i in range(len(y_names)):
                get_x.append(calc.get_values(x_names[i]))
                get_y.append(calc.get_values(y_names[i]))
        
        path_dict=graph(GrName, get_x, get_y, lablex=lablex, labley=labley, x1=x1, y1=y1, x2=x2, y2=y2, mult_x=mult_x, mult_y=mult_y, shift_x=shift_x, shift_y=shift_y, stpx=stpx, stpy=stpy)
        
        path_dict["x"]="_".join(x_names)
        path_dict["y"]="_".join(y_names)
        self.graph_list.append(path_dict)


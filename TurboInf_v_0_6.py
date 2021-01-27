import tkinter as tk
from tkinter import ttk
import math
from tkinter import messagebox

class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_main()
	
	def init_main(self):
		toolbar1 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar1.pack(side = tk.TOP, fill = tk.X)
		
		toolbar2 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar2.pack(side = tk.TOP, fill = tk.X)

		toolbar3 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar3.pack(side = tk.TOP, fill = tk.X)

		toolbar4 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar4.pack(side = tk.TOP, fill = tk.X)

		toolbar5 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar5.pack(side = tk.TOP, fill = tk.X)

		toolbar6 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar6.pack(side = tk.TOP, fill = tk.X)

		toolbar7 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar7.pack(side = tk.TOP, fill = tk.X)

		toolbar8 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar8.pack(side = tk.TOP, fill = tk.X)

		toolbar9 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar9.pack(side = tk.TOP, fill = tk.X)

		toolbar10 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar10.pack(side = tk.TOP, fill = tk.X)

		toolbar11 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar11.pack(side = tk.TOP, fill = tk.X)

		toolbar12 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar12.pack(side = tk.TOP, fill = tk.X)

		toolbar13 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar13.pack(side = tk.TOP, fill = tk.X)

		toolbar14 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar14.pack(side = tk.TOP, fill = tk.X)

		toolbar15 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar15.pack(side = tk.TOP, fill = tk.X)

		toolbar16 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar16.pack(side = tk.TOP, fill = tk.X)

		toolbar17 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar17.pack(side = tk.TOP, fill = tk.X)

		toolbar18 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar18.pack(side = tk.TOP, fill = tk.X)

		toolbar19 = tk.Frame(bg='#FFC0CB', bd = 2)
		toolbar19.pack(side = tk.TOP, fill = tk.X)

		toolbar20 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar20.pack(side = tk.TOP, fill = tk.X)

		toolbar21 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar21.pack(side = tk.TOP, fill = tk.X)

		toolbar22 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar22.pack(side = tk.TOP, fill = tk.X)

		toolbar23 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar23.pack(side = tk.TOP, fill = tk.X)

		toolbar24 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar24.pack(side = tk.TOP, fill = tk.X)

		toolbar25 = tk.Frame(bg='#d7d8e0', bd = 2)
		toolbar25.pack(side = tk.TOP, fill = tk.X)
		
		#Кнопки
		btn_open_prg1 = tk.Button(toolbar1, text = "1 - Площадь треугольника через две стороны и угол", command = self.open_dialog1,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg1.pack(side = tk.LEFT)
		
		btn_open_prg2 = tk.Button(toolbar2, text = "2 - Произведение цифр двухзначного числа", command = self.open_dialog2,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg2.pack(side = tk.LEFT)

		btn_open_prg3 = tk.Button(toolbar3, text = "3 - Перевод из ЧЧ:ММ:СС в секунды", command = self.open_dialog3,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg3.pack(side = tk.LEFT)

		btn_open_prg4 = tk.Button(toolbar4, text = "4 - Перевод из секунд в ЧЧ:ММ:СС", command = self.open_dialog4,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg4.pack(side = tk.LEFT)

		btn_open_prg5 = tk.Button(toolbar5, text = "5 - Площадь поверхности и объем куба через грань", command = self.open_dialog5,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg5.pack(side = tk.LEFT)

		btn_open_prg6 = tk.Button(toolbar6, text = "6 - Перевод из Цельсий в Фаренгейты и Кельвины", command = self.open_dialog6,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg6.pack(side = tk.LEFT)

		btn_open_prg7 = tk.Button(toolbar7, text = "7 - Гипотенуза и площадь треугольника через 2 катета", command = self.open_dialog7,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg7.pack(side = tk.LEFT)

		btn_open_prg8 = tk.Button(toolbar8, text = "8 - Среднее арифметическое цифр трехзначного числа", command = self.open_dialog8,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg8.pack(side = tk.LEFT)

		btn_open_prg9 = tk.Button(toolbar9, text = "9 - Решатель квадратного ур-ния при D>0", command = self.open_dialog9,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg9.pack(side = tk.LEFT)

		btn_open_prg10 = tk.Button(toolbar10, text = "10 - Оканчивается ли число на 9 и кратно ли 3", command = self.open_dialog10,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg10.pack(side = tk.LEFT)

		btn_open_prg11 = tk.Button(toolbar11, text = "11 - Сравнение двух чисел", command = self.open_dialog11,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg11.pack(side = tk.LEFT)

		btn_open_prg12 = tk.Button(toolbar12, text = "12 - Сравнение возростов 2 людей", command = self.open_dialog12,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg12.pack(side = tk.LEFT)

		btn_open_prg13 = tk.Button(toolbar13, text = "13 - Пролезет ли голова в рамку", command = self.open_dialog13,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg13.pack(side = tk.LEFT)

		btn_open_prg14 = tk.Button(toolbar14, text = "14 - Решатель квадратного ур-ния", command = self.open_dialog14,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg14.pack(side = tk.LEFT)

		btn_open_prg15 = tk.Button(toolbar15, text = "15 - Пролезет ли кирпич в отверстие", command = self.open_dialog15,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg15.pack(side = tk.LEFT)

		btn_open_prg16 = tk.Button(toolbar16, text = "16 - Проверка кратности числа 3,5,18", command = self.open_dialog16,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg16.pack(side = tk.LEFT)

		btn_open_prg17 = tk.Button(toolbar17, text = "17 - Проверка на что оканчивается число 7,17,117", command = self.open_dialog17,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg17.pack(side = tk.LEFT)

		btn_open_prg18 = tk.Button(toolbar18, text = "18 - Сравнение 3 чисел", command = self.open_dialog18,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg18.pack(side = tk.LEFT)

		btn_open_prg19 = tk.Button(toolbar19, text = "19 - Действия с числами", command = self.open_dialog19,bg = '#FFC0CB', bd = 0 ,compound = tk.TOP)
		btn_open_prg19.pack(side = tk.LEFT)

		btn_open_prg20 = tk.Button(toolbar20, text = "20 - Проверка является ли число палиндромом", command = self.open_dialog20,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg20.pack(side = tk.LEFT)

		btn_open_prg21 = tk.Button(toolbar21, text = "21 - Переворот числа", command = self.open_dialog21,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg21.pack(side = tk.LEFT)

		btn_open_prg22 = tk.Button(toolbar22, text = "22 - Склонение слова яблоко", command = self.open_dialog22,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg22.pack(side = tk.LEFT)

		btn_open_prg23 = tk.Button(toolbar23, text = "23 - Проверка какой треугольник", command = self.open_dialog23,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg23.pack(side = tk.LEFT)

		btn_open_prg24 = tk.Button(toolbar24, text = "24 - Проверка сколько дней в месяце", command = self.open_dialog24,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg24.pack(side = tk.LEFT)

		btn_open_prg25 = tk.Button(toolbar25, text = "25 - Проверка високосности года", command = self.open_dialog25,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_prg25.pack(side = tk.LEFT)

	def open_dialog1(self):
		Child1()

	def open_dialog2(self):
		Child2()
		
	def open_dialog3(self):
		Child3()

	def open_dialog4(self):
		Child4()

	def open_dialog5(self):
		Child5()

	def open_dialog6(self):
		Child6()

	def open_dialog7(self):
		Child7()

	def open_dialog8(self):
		Child8()

	def open_dialog9(self):
		Child9()

	def open_dialog10(self):
		Child10()

	def open_dialog11(self):
		Child11()

	def open_dialog12(self):
		Child12()

	def open_dialog13(self):
		Child13()

	def open_dialog14(self):
		Child14()

	def open_dialog15(self):
		Child15()

	def open_dialog16(self):
		Child16()

	def open_dialog17(self):
		Child17()

	def open_dialog18(self):
		Child18()

	def open_dialog19(self):
		Child19()

	def open_dialog20(self):
		Child20()

	def open_dialog21(self):
		Child21()

	def open_dialog22(self):
		Child22()

	def open_dialog23(self):
		Child23()

	def open_dialog24(self):
		Child24()

	def open_dialog25(self):
		Child25()


class Child1(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()



	


	def init_child(self):
		self.title('Программа 1')
		self.geometry('400x300+400+300')
		self.resizable(False,False)
			
		def logic():
			global memory
			a = float(self.dln1.get())
			b = float(self.dln2.get())
			s = float(self.ugl.get())
			f = math.radians(s)
			g = math.sin(f)
			S = (a * b *g)/2
			messagebox.showinfo("Ответ", "Площадь=" + str(S))


		dln1_txt = tk.Label(self , text = 'Длина первой стороны')
		dln1_txt.place(x = 10 , y = 20)

		self.dln1 = ttk.Entry(self)
		self.dln1.place(x = 10 , y = 40)

		dln2_txt = tk.Label(self , text = 'Длина второй стороны')
		dln2_txt.place(x = 10 , y = 70)

		self.dln2 = ttk.Entry(self)
		self.dln2.place(x = 10 , y = 90)

		ugl_txt = tk.Label(self , text = 'Длина угол между сторонами')
		ugl_txt.place(x = 10 , y = 120)
		
		self.ugl = ttk.Entry(self)
		self.ugl.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)

		self.grab_set()
		self.focus_set()

class Child2(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 2')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic
		def logic():
			global memory
			x = int(self.chsl.get())
			a = x // 10
			b = x % 10
			p = a * b
			messagebox.showinfo("Ответ", "Произведение=" + str(p))


		chsl_txt = tk.Label(self , text = 'Введите двухзначное число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child3(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 3')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic
		def logic():
			global memory
			a = int(self.hrs.get())
			b = int(self.min.get())
			c = int(self.sec.get())
			x = a * 60 * 60
			y = b * 60
			n = x + y + c
			messagebox.showinfo("Ответ", str(n) + " секунд")

		hrs_txt = tk.Label(self , text = 'Введите часы')
		hrs_txt.place(x = 10 , y = 20)

		self.hrs = ttk.Entry(self)
		self.hrs.place(x = 10 , y = 40)

		min_txt = tk.Label(self , text = 'Введите минуты')
		min_txt.place(x = 10 , y = 70)

		self.min = ttk.Entry(self)
		self.min.place(x = 10 , y = 90)

		sec_txt = tk.Label(self , text = 'Введите секунды')
		sec_txt.place(x = 10 , y = 120)
		
		self.sec = ttk.Entry(self)
		self.sec.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child4(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 4')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic
		def logic():
			global memory
			x = int(self.sec.get())
			a = (x // 60) // 60
			b = (x // 60) - (a * 60)
			c = x - (a * 60 * 60)- (b * 60)
			messagebox.showinfo("Ответ", "Время:" + str(a) + ":" + str(b) + ":" + str(c))

		sec_txt = tk.Label(self , text = 'Введите секунды')
		sec_txt.place(x = 10 , y = 20)

		self.sec = ttk.Entry(self)
		self.sec.place(x = 10 , y = 40)
		
		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child5(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 5')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic a.k.a. to work
		def logic():
			global memory
			a = int(self.dln_reb.get())
			S = (a**2)*6
			V = a**3
			messagebox.showinfo("Ответ", "Площадь поверхности:" + str(S) + "\n" + "Объем кубика:" + str(V))


		dln_reb_txt = tk.Label(self , text = 'Введите длину ребра куба')
		dln_reb_txt.place(x = 10 , y = 20)

		self.dln_reb = ttk.Entry(self)
		self.dln_reb.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child6(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 6')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic a.k.a. to work
		def logic():
			global memory
			a = float(self.temp_C.get())
			F = (a * 1.8) + 32
			K = a + 273.15
			messagebox.showinfo("Ответ", "Температура по Фаренгейту: " + str(F) + "\n" + "Температура в Кельвинах: " + str(K))

		temp_C_txt = tk.Label(self , text = 'Введите температуру в Цельсиях')
		temp_C_txt.place(x = 10 , y = 20)

		self.temp_C = ttk.Entry(self)
		self.temp_C.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child7(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 7')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#to work
		def logic():
			a = int(self.kat1.get())
			b = int(self.kat2.get())
			c = math.sqrt((a**2) + (b**2))
			S = (a * b) /2
			messagebox.showinfo("Ответ", "Гипотенуза равнa:" + str(c) + "\n" + "Площадь ровна:" + str(S))			

		kat1_txt = tk.Label(self , text = 'Введите первый катет')
		kat1_txt.place(x = 10 , y = 20)

		self.kat1 = ttk.Entry(self)
		self.kat1.place(x = 10 , y = 40)

		kat2_txt = tk.Label(self , text = 'Введите второй катет')
		kat2_txt.place(x = 10 , y = 70)

		self.kat2 = ttk.Entry(self)
		self.kat2.place(x = 10 , y = 90)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child8(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 8')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#to work
		def logic():
			a = int(self.chsl.get())
			b = a / 100
			c = a % 100
			c1 = c / 10
			d = a % 10
			S = (b+c1+d)/3
			messagebox.showinfo("Ответ", "Среднее арифметическое его цифр:" + str(S))

		chsl_txt = tk.Label(self , text = 'Введите трехзначное число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child9(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 9')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#logic
		def logic():
			global memory
			a = float(self.kf_a.get())
			b = float(self.kf_b.get())
			c = float(self.kf_c.get())
			D = (b**2) - 4 * a * c
			if D > 0:
				x1 = ((b*(-1)) + math.sqrt(D)) / (2 * a)
				x2 = ((b*(-1)) - math.sqrt(D)) / (2 * a)
				messagebox.showinfo("Ответ", "2 корня, т.к. D>0" + "\n" + "x1=" + str(x1) + "\n" + "x2=" + str(x2))
			elif D == 0:
				x1 = ((b*(-1)) + math.sqrt(D)) / (2 * a)
				messagebox.showinfo("Ответ", "1 корень, т.к. D=0" + "\n" + "x=" + str(x1))
			elif D<0:
				messagebox.showinfo("Ответ", "Корней нет, т.к. D<0")	

		kf_a_txt = tk.Label(self , text = 'Введите коэффицент a')
		kf_a_txt.place(x = 10 , y = 20)

		self.kf_a = ttk.Entry(self)
		self.kf_a.place(x = 10 , y = 40)

		kf_b_txt = tk.Label(self , text = 'Введите коэффицент b')
		kf_b_txt.place(x = 10 , y = 70)

		self.kf_b = ttk.Entry(self)
		self.kf_b.place(x = 10 , y = 90)

		kf_c_txt = tk.Label(self , text = 'Введите коэффицент с')
		kf_c_txt.place(x = 10 , y = 120)
		
		self.kf_c = ttk.Entry(self)
		self.kf_c.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child10(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 10')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#to work ebat'
		def logic():
			global memory
			x = int(self.chsl.get())
			y = x % 10
			h = x % 3
			if y == 9:
				messagebox.showinfo("Ответ", "Число оканчивается на 9")
			else:
				messagebox.showinfo("Ответ", "Число не оканчивается на 9")
			if h == 0:
				messagebox.showinfo("Ответ", "Число кратно 3")
			else:
				messagebox.showinfo("Ответ", "Число не кратно 3")

		chsl_txt = tk.Label(self , text = 'Введите целое число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child11(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 11')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#to кароче чтобы работало, товарищи
		def logic():
			global memory
			a = int(self.chsl1.get())
			b = int(self.chsl2.get())
			if a > b:
				messagebox.showinfo("Ответ", str(a) + ">" + str(b))
			else:
				messagebox.showinfo("Ответ", str(a) + "<" + str(b))


		chsl1_txt = tk.Label(self , text = 'Введите первое число')
		chsl1_txt.place(x = 10 , y = 20)

		self.chsl1 = ttk.Entry(self)
		self.chsl1.place(x = 10 , y = 40)

		chsl2_txt = tk.Label(self , text = 'Введите второе число')
		chsl2_txt.place(x = 10 , y = 70)

		self.chsl2 = ttk.Entry(self)
		self.chsl2.place(x = 10 , y = 90)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child12(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 12')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#чтобы работало (p.s. рот ебал чейса)
		"""def logic():
			d1 = (int(self.dr1.get()))
			if g1 > g2:
		   		print ("Первый старше")
			elif g1 < g2:
		    	print ("Второй страше")
			else:
		    	if m1 > m2:
		        	print ("Первый старше")
		    	elif m1 < m2:
		        	print ("Второй старше")
		    	else:
		        	if d1 > d2:
		           		print("Первый старше")
		        	elif d1 < d2:
		            	print ("Второй старше")
		        	else:
		            	print ("Они ровесники")"""


		dr1_txt = tk.Label(self , text = 'Введите дату рождения Первого')
		dr1_txt.place(x = 10 , y = 20)

		self.dr1d = ttk.Entry(self)
		self.dr1d.place(x = 10 , y = 40 , width = 40)

		self.dr1m = ttk.Entry(self)
		self.dr1m.place(x = 50 , y = 40 , width = 40)

		self.dr1g = ttk.Entry(self)
		self.dr1g.place(x = 90 , y = 40 , width = 40)

		dr2_txt = tk.Label(self , text = 'Введите дату рождения Второго ')
		dr2_txt.place(x = 10 , y = 90)

		self.dr2d = ttk.Entry(self)
		self.dr2d.place(x = 10 , y = 110 , width = 40)

		self.dr2m = ttk.Entry(self)
		self.dr2m.place(x = 50 , y = 110 , width = 40)

		self.dr2g = ttk.Entry(self)
		self.dr2g.place(x = 90 , y = 110 , width = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child13(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 13')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#chase urod
		def logic():
			a = int(self.dln.get())
			b = int(self.srn.get())
			c = int(self.dmtr.get())
			if c < a and c < b:
				messagebox.showinfo("Ответ", "Голова пролезет")
			else:
				messagebox.showinfo("Ответ", "Голова не пролезет")

		dln_txt = tk.Label(self , text = 'Длина рамки')
		dln_txt.place(x = 10 , y = 20)

		self.dln = ttk.Entry(self)
		self.dln.place(x = 10 , y = 40)

		srn_txt = tk.Label(self , text = 'Ширина рамки')
		srn_txt.place(x = 10 , y = 70)

		self.srn = ttk.Entry(self)
		self.srn.place(x = 10 , y = 90)

		dmtr_txt = tk.Label(self , text = 'Диаметр головы')
		dmtr_txt.place(x = 10 , y = 120)
		
		self.dmtr = ttk.Entry(self)
		self.dmtr.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child14(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 14')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#do práce
		def logic():
			a = float(self.kf_a.get())
			b = float(self.kf_b.get())
			c = float(self.kf_c.get())
			D = (b**2) - 4 * a * c
			if D > 0:
				x1 = ((b*(-1)) + math.sqrt(D)) / (2 * a)
				x2 = ((b*(-1)) - math.sqrt(D)) / (2 * a)
				messagebox.showinfo("Ответ", "2 корня, т.к. D>0" + "\n" + "x1=" + str(x1) + "\n" + "x2=" + str(x2))
			elif D == 0:
				x1 = ((b*(-1)) + math.sqrt(D)) / (2 * a)
				messagebox.showinfo("Ответ", "1 корень, т.к. D=0" + "\n" + "x=" + str(x1))		
			elif D<0:
				messagebox.showinfo("Ответ", "Корней нет, т.к. D<0")


		kf_a_txt = tk.Label(self , text = 'Введите коэффицент a')
		kf_a_txt.place(x = 10 , y = 20)

		self.kf_a = ttk.Entry(self)
		self.kf_a.place(x = 10 , y = 40)

		kf_b_txt = tk.Label(self , text = 'Введите коэффицент b')
		kf_b_txt.place(x = 10 , y = 70)

		self.kf_b = ttk.Entry(self)
		self.kf_b.place(x = 10 , y = 90)

		kf_c_txt = tk.Label(self , text = 'Введите коэффицент с')
		kf_c_txt.place(x = 10 , y = 120)
		
		self.kf_c = ttk.Entry(self)
		self.kf_c.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления', command = logic)
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child15(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 15')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#働く
		"""def logic():
			a = 




			if a <= x and b <= y:
				print ("Пролезет")
			elif a <= x and c <= y:
				print ("Пролезет")
			elif b <= x and c <= y:
				print ("Пролезет")
			else:
				print ("Не пролезет")"""

		kat1_txt = tk.Label(self , text = 'Введите размеры кирпича')
		kat1_txt.place(x = 10 , y = 20)

		self.kirx = ttk.Entry(self)
		self.kirx.place(x = 10 , y = 40 , width = 40)

		self.kiry = ttk.Entry(self)
		self.kiry.place(x = 50 , y = 40 , width = 40)

		self.kirz = ttk.Entry(self)
		self.kirz.place(x = 90 , y = 40 , width = 40)

		kat2_txt = tk.Label(self , text = 'Введите размеры дыры')
		kat2_txt.place(x = 10 , y = 90)

		self.dirx = ttk.Entry(self)
		self.dirx.place(x = 10 , y = 110 , width = 40)

		self.diry = ttk.Entry(self)
		self.diry.place(x = 50 , y = 110 , width = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child16(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 16')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		#para trabajar


		chsl_txt = tk.Label(self , text = 'Введите число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child17(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 17')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		chsl_txt = tk.Label(self , text = 'Введите число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child18(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 18')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		chsl1_txt = tk.Label(self , text = 'Певрое число')
		chsl1_txt.place(x = 10 , y = 20)

		self.chsl1 = ttk.Entry(self)
		self.chsl1.place(x = 10 , y = 40)

		chsl2_txt = tk.Label(self , text = 'Второе число')
		chsl2_txt.place(x = 10 , y = 70)

		self.chsl2 = ttk.Entry(self)
		self.chsl2.place(x = 10 , y = 90)

		chsl3_txt = tk.Label(self , text = 'Третье число')
		chsl3_txt.place(x = 10 , y = 120)
		
		self.chsl3 = ttk.Entry(self)
		self.chsl3.place(x = 10 , y = 140)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child19(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 19')
		self.geometry('300x300+400+300')
		self.resizable(False,False)

		plus = tk.Frame(bg='#d7d8e0', bd = 2)
		plus.pack(side = tk.TOP, fill = tk.X)
		
		minus = tk.Frame(bg='#d7d8e0', bd = 2)
		minus.pack(side = tk.TOP, fill = tk.X)

		multiplication = tk.Frame(bg='#d7d8e0', bd = 2)
		multiplication.pack(side = tk.TOP, fill = tk.X)

		division = tk.Frame(bg='#d7d8e0', bd = 2)
		division.pack(side = tk.TOP, fill = tk.X)

		sqrt = tk.Frame(bg='#d7d8e0', bd = 2)
		sqrt.pack(side = tk.TOP, fill = tk.X)

		btn_open_plus = tk.Button(self, text = "Сложение", command = self.open_plus, bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_plus.pack(side = tk.TOP , fill = tk.X)
		
		btn_open_minus = tk.Button(self, text = "Вычитание", command = self.open_minus,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_minus.pack(side = tk.TOP , fill = tk.X)

		btn_open_multiplication = tk.Button(self, text = "Произведение", command = self.open_multiplication,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_multiplication.pack(side = tk.TOP , fill = tk.X)

		btn_open_division = tk.Button(self, text = "Деление", command = self.open_division,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_division.pack(side = tk.TOP , fill = tk.X)

		btn_open_sqrt = tk.Button(self, text = "Извлечение квадратного корня", command = self.open_sqrt,bg = '#d7d8e0', bd = 0 ,compound = tk.TOP)
		btn_open_sqrt.pack(side = tk.TOP , fill = tk.X)

		self.grab_set()
		self.focus_set()
	

	def open_plus(self):
		Plus()

	def open_minus(self):
		Minus()

	def open_multiplication(self):
		Multiplication()

	def open_division(self):
		Division()

	def open_sqrt(self):
		Sqrt()
		
class Plus(tk.Toplevel):
		def __init__(self):
			super().__init__(root)
			self.dey()

		def dey(self):
			self.title('Сложение')
			self.geometry('400x300+400+300')
			self.resizable(False,False)

			kat1_txt = tk.Label(self , text = 'Введите первое число')
			kat1_txt.place(x = 10 , y = 20)

			self.kat1 = ttk.Entry(self)
			self.kat1.place(x = 10 , y = 40)

			kat2_txt = tk.Label(self , text = 'Введите второе число')
			kat2_txt.place(x = 10 , y = 70)

			self.kat2 = ttk.Entry(self)
			self.kat2.place(x = 10 , y = 90)

			btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
			btn_otvet.place(x = 10 , y = 180)
			
			btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
			btn_exit.place(x = 315 , y = 265)
			
			self.grab_set()
			self.focus_set()

class Minus(tk.Toplevel):
		def __init__(self):
			super().__init__(root)
			self.dey()

		def dey(self):

			kat1_txt = tk.Label(self , text = 'Введите первое число')
			kat1_txt.place(x = 10 , y = 20)

			self.kat1 = ttk.Entry(self)
			self.kat1.place(x = 10 , y = 40)

			kat2_txt = tk.Label(self , text = 'Введите второе число')
			kat2_txt.place(x = 10 , y = 70)

			self.kat2 = ttk.Entry(self)
			self.kat2.place(x = 10 , y = 90)

			btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
			btn_otvet.place(x = 10 , y = 180)
			
			btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
			btn_exit.place(x = 315 , y = 265)
			
			self.grab_set()
			self.focus_set()

class Multiplication(tk.Toplevel):
		def __init__(self):
			super().__init__(root)
			self.dey()

		def dey(self):
			self.title('Умножение')
			self.geometry('400x300+400+300')
			self.resizable(False,False)

			kat1_txt = tk.Label(self , text = 'Введите первое число')
			kat1_txt.place(x = 10 , y = 20)

			self.kat1 = ttk.Entry(self)
			self.kat1.place(x = 10 , y = 40)

			kat2_txt = tk.Label(self , text = 'Введите второе число')
			kat2_txt.place(x = 10 , y = 70)

			self.kat2 = ttk.Entry(self)
			self.kat2.place(x = 10 , y = 90)

			btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
			btn_otvet.place(x = 10 , y = 180)
			
			btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
			btn_exit.place(x = 315 , y = 265)
			
			self.grab_set()
			self.focus_set()

class Division(tk.Toplevel):
		def __init__(self):
			super().__init__(root)
			self.dey()

		def dey(self):
			self.title('Деление')
			self.geometry('400x300+400+300')
			self.resizable(False,False)

			kat1_txt = tk.Label(self , text = 'Введите первое число')
			kat1_txt.place(x = 10 , y = 20)

			self.kat1 = ttk.Entry(self)
			self.kat1.place(x = 10 , y = 40)

			kat2_txt = tk.Label(self , text = 'Введите второе число')
			kat2_txt.place(x = 10 , y = 70)

			self.kat2 = ttk.Entry(self)
			self.kat2.place(x = 10 , y = 90)

			btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
			btn_otvet.place(x = 10 , y = 180)
			
			btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
			btn_exit.place(x = 315 , y = 265)
			
			self.grab_set()
			self.focus_set()

class Sqrt(tk.Toplevel):
		def __init__(self):
			super().__init__(root)
			self.dey()

		def dey(self):
			self.title('Извлечение корня')
			self.geometry('400x300+400+300')
			self.resizable(False,False)

			chsl_txt = tk.Label(self , text = 'Введите число')
			chsl_txt.place(x = 10 , y = 20)

			self.chsl = ttk.Entry(self)
			self.chsl.place(x = 10 , y = 40)

			btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
			btn_otvet.place(x = 10 , y = 180)
			
			btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
			btn_exit.place(x = 315 , y = 265)
			
			self.grab_set()
			self.focus_set()
	
	


class Child20(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 20')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		chsl_txt = tk.Label(self , text = 'Введите 3-х или 4-х значное число')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child21(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 21')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		chsl_txt = tk.Label(self , text = 'Введите число от 1 до 9999')
		chsl_txt.place(x = 10 , y = 20)

		self.chsl = ttk.Entry(self)
		self.chsl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child22(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 22')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		apl_txt = tk.Label(self , text = 'Введите кол-во яблок')
		apl_txt.place(x = 10 , y = 20)

		self.apl = ttk.Entry(self)
		self.apl.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child23(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 23')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		kor_txt = tk.Label(self , text = 'Введите координаты первой точки')
		kor_txt.place(x = 10 , y = 20)

		self.koor1x = ttk.Entry(self)
		self.koor1x.place(x = 10 , y = 40 , width = 40)

		self.koor1y = ttk.Entry(self)
		self.koor1y.place(x = 50 , y = 40 , width = 40)

		kor2_txt = tk.Label(self , text = 'Введите координаты второй точки')
		kor2_txt.place(x = 10 , y = 70)

		self.koor2x = ttk.Entry(self)
		self.koor2x.place(x = 10 , y = 90 , width = 40)

		self.koor2y = ttk.Entry(self)
		self.koor2y.place(x = 50 , y = 90 , width = 40)

		kor3_txt = tk.Label(self , text = 'Введите координаты третьей точки')
		kor3_txt.place(x = 10 , y = 120)
		
		self.koor3x = ttk.Entry(self)
		self.koor3x.place(x = 10 , y = 140 , width = 40)

		self.koor3y = ttk.Entry(self)
		self.koor3y.place(x = 50 , y = 140 , width = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 ,y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child24(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 24')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		mes_txt = tk.Label(self , text = 'Введите номер месяца')
		mes_txt.place(x = 10 , y = 20)

		self.mes = ttk.Entry(self)
		self.mes.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

class Child25(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()

	def init_child(self):
		self.title('Программа 24')
		self.geometry('400x300+400+300')
		self.resizable(False,False)

		god_txt = tk.Label(self , text = 'Введите номер года')
		god_txt.place(x = 10 , y = 20)

		self.god = ttk.Entry(self)
		self.god.place(x = 10 , y = 40)

		btn_otvet = ttk.Button(self, text = 'Произвести вычесления')
		btn_otvet.place(x = 10 , y = 180)
		
		btn_exit = ttk.Button(self , text = 'Закрыть' , command = self.destroy)
		btn_exit.place(x = 315 , y = 265)
		
		self.grab_set()
		self.focus_set()

if __name__ == "__main__":
	root = tk.Tk()
	app = Main(root)
	app.pack()
	root.title("TurboInf")
	root.geometry("650x650+300+100")
	root.resizable(True,True)
	root.mainloop()

if __name__ == "__child19__":
	root = tk.Tk()
	app = Child19(root)
	app.pack()
	root.title("Программа 19")
	root.geometry("400x300+400+300")
	root.resizable(True,True)
	root.mainloop()
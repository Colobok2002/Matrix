import sys
import random
import time

# Подключаем дополнительные модули
try:
    import bext, colorama
except ImportError:
    print ('Для запуска программы нужны модули bext и colorama.')
    sys.exit ()

class Drop:
    def __init__ (self):
        self.x = random.randint (0, width) # Начальное положение по горизонтали
        self.y = -1 # Начальное положение по вертикали - за верхней границей экрана
        self.drop_type = random.randint (0, 1) # Тип: антикапля или капля
        self.timeout = random.randint (0, 2) # Задержка до следующего перемещения
        self.wait_count = random.randint (0,2) # Счетчик паузы
    def renew (self):
        self.__init__ ()
    def move (self):

        if drop.wait_count < drop.timeout: # Пока рано перемещать
            drop.wait_count += 1 # Увеличиваем счётчик паузы
            return False
        else: # Уже можно перемещать
            drop.wait_count = 0 # Сбрасываем счётчик паузы
            drop.y += 1 # Перемещаем каплю или антикаплю на шаг вниз
            return True
    def draw (self):
        if self.drop_type == 1:
            symbol = str (random.randint (1, 9))
            con_print (self.x, self.y, green, symbol)
            self.zero_draw () # Рисуем яркий ноль
        else:
            con_print (self.x, self.y, green, ' ')
    def zero_draw (self):
        if (self.y < height):
            con_print (self.x, self.y+1, lgreen, '0')

def is_rb_corner (x, y):
    if x==width and y==height:
        return True
    else:
        return False

def con_print (x, y, color, symbol):
    if not is_rb_corner (x, y):
        bext.goto (x, y)
        sys.stdout.write (color)
        print (symbol, end='')

bext.title ('Matrix') # Меняем заголовок консольного окна
bext.clear () # Очищаем консольное окно
bext.hide () # Скрываем курсор в консольном окне
width, height = bext.size () # Получаем размер консольного окна
width -= 1
height -= 1

green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX

# Создаём массив капель и антикапель
drops = []
for i in range (1, width*2//3):
    drop = Drop ()
    drops.append (drop)

while True:
    for drop in drops:
        if drop.move (): # Проверяем перемещение элемента
            drop.draw () # Отображаем элемент
            if drop.y >= height: # Достигли дна
                drop.renew () # Обновляем элемент
    key = bext.getKey (blocking = False) # Проверяем, нажата ли клавиша
    if key == 'esc': # Если нажата ESC, то выходим из программы
        bext.clear ()
        sys.exit ()
    #time.sleep (0.02) # Задержка
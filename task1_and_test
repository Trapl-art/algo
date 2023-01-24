class Auto:
    # Автомобиль
    # имеет цвет
    # имеет мощность дивгателя
    # имеет максимальный запас бензина в баке
    # имеет расход (например 9.3 литра на 100 км)
    # можно перекрасить
    # можно заправить N литров
    # можно проехать N киллометров
    # можно узнать цвет
    # мощность
    # сколько осталось литров в баке
    # узнать расход
    color: str = "green"
    power: int = 100
    maxbac: int = 80  # имеет максимальный запас бензина в баке
    expense: float = 9.3  # имеет расход (например 9.3 литра на 100 км)
    now_bac: int = 20

    def __init__(self, color: str = "red", power: int = 200, maxbac: int = 100, expense: float = 7, now_bac: int = 20,
                 interval: float = 50):
        self.color = color
        self.power = power
        self.maxbac = maxbac
        self.expense = expense
        self.now_bac = now_bac
        self.interval = interval

    def set_color(self, color):
        self.color = color
        return self.color

    def get_color(self):
        return self.color

    def get_fuel(self, maxbac):
        return self.maxbac

    def set_fuel(self, maxbac):
        self.maxbac = maxbac
        return self.maxbac

    def get_now_bac(self, now_bac):
        return self.now_bac

    def get_expense(self):
        return self.expense

    def get_refuel(self):
        return self.maxbac - self.now_bac

    def refuel(self, maxbac):
        if self.maxbac >= self.now_bac:
            if maxbac > a.get_refuel():
                print("нельзя дозаправить")
            else:
                self.now_bac += maxbac
                return self.now_bac
        else:
            print("дозаправить не нужно")

    def distante(self):
        return self.now_bac / self.expense

    def get_power(self):
        return self.power

    def get_remained(self, expense, interval):
        return self.expense / 100 * self.interval

    def print(self):
        print(f"""
        1.машина имеет цвет: {a.set_color("Grey")}
        2.машина покрашена в: {a.get_color()} цвет
        3.бак вмещает литров {a.get_fuel(80)}
        4.бак содержит {a.now_bac}
        5.можно залить {a.get_refuel()}
        6.можно проехать {a.distante()}
        7.мощность двигателя{a.get_power()}
        8.расход двигателя {a.get_expense()}
        9. осталось в баке {a.get_remained(expense=9.3, interval=50)} литров
        """)


a = Auto(color="black", power=250, maxbac=70, expense=9.3, now_bac=70, interval=50)
a.print()

def test_init_1():
    Auto(color='white',
        power=90,
        maxbac=50,
        expense=9.3,
        now_bac=0)


def test_init_2():
    Auto(color='white')


def test_color_1():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'


def test_color_2():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'
    c.set_color('red')


def test_color_3():
    c = Auto(color='white',
            power=90,
            maxbac=50,
            expense=9.3,
            now_bac=0)
    assert c.get_color() == 'white'
    c.set_color('red')

    assert c.get_color() == 'red'

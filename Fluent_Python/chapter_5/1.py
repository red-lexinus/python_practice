from typing import NamedTuple
from collections import namedtuple
from dataclasses import dataclass, field

Coordinate1 = NamedTuple('Coordinate', [('lat', float), ('lon', float)])

UserData = namedtuple('UserData', 'id rank_id num_complaint')


class Coordinate2(NamedTuple):
    lat: float
    lon: float

    def __repr__(self):
        ns = 'Север' if self.lat >= 0 else 'Юг'
        we = 'Восток' if self.lon >= 0 else 'Запад'
        return f'{abs(self.lat):.1f}° на {ns}, {abs(self.lon):.1f}° на {we}'


@dataclass
class Notepad:
    name: str = 'Блокнотик'
    __notes: list = field(default_factory=list, repr=False)

    def add_note(self, note: str) -> None:
        self.__notes.append(note)

    def add_notes(self, notes: list) -> None:
        self.__notes += notes

    def __reversed__(self):
        self.__notes = self.__notes[::-1]
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__notes) > 0:
            note = self.__notes[0]
            del self.__notes[0]
            return note
        else:
            raise StopIteration


class City(NamedTuple):
    continent: str
    name: str
    country: str


def fun_1():
    user_1 = UserData(1, 0, 0)
    print(user_1._asdict())


def fun_2():
    notepad = Notepad()
    notepad.add_notes(['привет', 'пока', 'аааааааа'])
    for note in reversed(notepad):
        print(note)


def fun_3():
    cities = [
        City('Asia', 'Tokyo', 'JP'),
        City('Asia', 'Delhi', 'IN'),
        City('North America', 'Mexico City', 'MX'),
        City('North America', 'New York', 'US'),
        City('South America', 'São Paulo', 'BR'),
    ]
    for city in cities:
        match city:
            case City(country='US'):
                print(f'{city.name} это Америка!')
            case City(continent='Asia'):
                print(f'{city.name} это Азия!')


if __name__ == '__main__':
    fun_1()
    print('_'*30)
    fun_2()
    print('_'*15)
    fun_3()

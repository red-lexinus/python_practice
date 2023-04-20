import random


class GameCard:
    _short_len = 13

    def __init__(self, riddle: str, answer: str):
        self._riddle, self._answer = riddle, answer

    def __repr__(self):
        return f"{self._short_riddle()}->{self._short_answer()}"

    def __str__(self):
        return f'{self._riddle}?'

    def _short_riddle(self) -> str:
        short_riddle = self._riddle
        if len(self._riddle) > self._short_len - 3:
            short_riddle = self._riddle[:10] + '...'
        return short_riddle

    def _short_answer(self) -> str:
        short_answer = self._answer
        if len(self._answer) > self._short_len - 3:
            short_answer = self._answer[:10] + '...'
        return short_answer

    def get_answer(self) -> str:
        return self._answer

    def check_answer(self, answer: str) -> bool:
        return bool(self._answer == answer)


class GameDask:
    def __init__(self, cards_dates: list[list]):
        self._cards = [GameCard(*card_dates) for card_dates in cards_dates]

    def __bool__(self):
        return bool(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos: int) -> GameCard:
        res = self._cards[pos]
        del self._cards[pos]
        return res

    def __add__(self, other):
        return GameDask(self._cards + other.get_cards())

    def get_cards(self):
        return self._cards


def questionnaire(game_dask: GameDask, res: int = 0):
    game_card: GameCard = random.choice(game_dask)
    print(game_card)
    if game_card.check_answer(input()):
        print('Вы правы!')
        res += 1
    else:
        print(f'Вы ошиблись вот правильный ответ:{game_card.get_answer()}')
    if game_dask:
        return questionnaire(game_dask, res)
    return res


def start_game():
    cards_dates = [
        ['1+1', '2'],
        ['1+2', '3'],
        ['2+3', '5']
    ]
    game_dask = GameDask(cards_dates)
    count_question = len(game_dask)
    res = questionnaire(game_dask)
    print(f"Всё наконец-то кончилось!\nВаши результаты:{res}/{count_question}")


start_game()
input()

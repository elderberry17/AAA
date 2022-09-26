import json


# достаточно костыльно реализовал DoD
# расклеился после среды и не попробовал переписать через отдельный класс
# надеюсь получить фидбек и осознать, как можно решить такую задачу лучше


class ColorizeMixin:
    def __init__(self):
        self.repr_color_code = 33


class Advert(ColorizeMixin):
    def __init__(self, mapping: json):
        super().__init__()
        self.mapping = mapping
        # take a look if 'price' is in a higher scope and work with this key
        if isinstance(mapping, dict):
            if 'title' in self.mapping:
                if 'price' not in self.mapping:
                    self.mapping['price'] = 0
                elif self.mapping['price'] < 0:
                    raise ValueError('must be >= 0')

    def __getattr__(self, item: str) -> object:
        if isinstance(self.mapping.get(item), dict):
            return self.__class__(self.mapping.get(item))
        return self.__class__(self.mapping.get(item)).mapping

    # here is a question with colour
    def __repr__(self):
        if 'title' in self.mapping:
            return f'\033[0;{self.repr_color_code};48m{self.mapping["title"]} | {self.mapping["price"]} ₽'
        return f'{self.mapping}'


lesson_str = """{
    "title": "python", "price": 0,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
    }
}"""

if __name__ == "__main__":
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson)
    print(lesson_ad.location)
    print(lesson_ad.location.metro_stations)
    print(lesson_ad)
    lesson_ad.repr_color_code = 35
    print(lesson_ad)

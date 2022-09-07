from optparse import Values


def run():
    my_list = [1, "hello", True, 2.3]
    my_dict = {"firstname": "Jessimar", "lastname": "Paez"}

    super_dict = {
        "first_list": [1, "hello", True, 2.3],
        "seconds_list": [2, "welcome", False, 3.2],
        "third_list":   [3, "bye", True, 2.5],
    }

    super_list = [
        {"firstname": "Jessimar", "lastname": "Paez"},
        {"firstname": "Andreina", "lastname": "Perez"},
        {"firstname": "Belen", "lastname": "Retamales"},
    ]
    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])
    


if __name__ == '__main__':
    run()

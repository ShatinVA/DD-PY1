def get_count_char(str_):
    str_.lower()
    dict_ = {}
    for i in str_:
        if i.isalpha():
            if not (i in dict_.keys()):
                dict_[i] = 1
            else:
                dict_[i] += 1
    return dict_

def func2(dict):
    a = 0
    for i in dict:
        a += dict[i]
    for i in dict:
        dict [i] = int(dict[i] / a * 100)
    return dict


main_str = 'дддддддддддддааааааааааааааааааннннннннннннноооооооооооооооооооооооооооооееееееееееееееееееееееепппппппппллллллллллллл'

print(get_count_char(main_str))
print(func2(get_count_char(main_str)))
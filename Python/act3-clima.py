import statistics

year = {
    'Janeiro': '',
    'Fevereiro': '',
    'Março': '',
    'Abril': '',
    'Maio': '',
    'Junho': '',
    'Julho': '',
    'Agosto': '',
    'Setembro': '',
    'Outubro': '',
    'Novembro': '',
    'Dezembro': ''
}

for i in year:
    year[i] = float(input(f"Digite a temperatura do mês de {i}: "))

values_list = list(year.values())
keys_list = list(year.keys())

print(f"\n Média= {statistics.mean(values_list)}")
print(f"O mês de maior temperatura foi {keys_list[values_list.index(max(values_list))]} com {max(values_list)}")
print(f"O mês de menor temperatura foi {keys_list[values_list.index(min(values_list))]} com {min(values_list)}")



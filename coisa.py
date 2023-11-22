# String existente com espaços
string_existente = 'gato e peixe'

# Novos itens a serem adicionados
novos_itens = ['casa', 'cachorro']

# Convertendo a string existente em uma lista e removendo espaços
itens_existente = string_existente.split(' ')

# Adicionando novos itens à lista existente
itens_existente.extend(novos_itens)

# Unindo todos os itens em uma única string com vírgula
string_com_novos_itens = ', '.join(itens_existente)

print(string_com_novos_itens)

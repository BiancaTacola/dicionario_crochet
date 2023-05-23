croche_arte = {
    'Pontos Básicos': ['Correntinha', 'Ponto Baixo', 'Ponto Alto', 'Ponto Alto Duplo'],
    'Técnicas Avançadas': ['Crochê Tunisiano', 'Granny Squares', 'Bicos e Acabamentos'],
    'Projetos Populares': ['Tapetes', 'Amigurumis', 'Blusas', 'Mantas'],
    'Materiais': ['Agulhas de Crochê', 'Linhas e Fios', 'Marcadores de Ponto'],
    'Comunidades Online': {
        'Sites': ['Ravelry', 'LoveCrochet', 'Pinterest'],
        'Redes Sociais': ['Instagram', 'Facebook', 'YouTube']
    }
}

# Exemplo de acesso às informações sobre técnicas avançadas
print("Técnicas Avançadas de Crochê:")
for tecnica in croche_arte['Técnicas Avançadas']:
    print(tecnica)

# Exemplo de acesso às informações sobre materiais
print("\nMateriais de Crochê:")
for material in croche_arte['Materiais']:
    print(material)

# Exemplo de acesso às informações sobre comunidades online
print("\nComunidades Online de Crochê:")
print("Sites:")
for site in croche_arte['Comunidades Online']['Sites']:
    print(site)
print("Redes Sociais:")
for rede_social in croche_arte['Comunidades Online']['Redes Sociais']:
    print(rede_social)

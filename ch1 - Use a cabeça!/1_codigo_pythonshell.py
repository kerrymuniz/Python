import random #comando para conseguir usar funcionalidades aleatórias

verbos = [
    'jogar', 'lançar', 'partir', 'voar',
        'correr', 'cair'
    ]

adjetivos = [
    'bonito', 'gentil', 'leve', 'pesado',
        'grande', 'legal'
    ]

substantivos = [
    'cadeira', 'avião', 'Lucas', 'mesa',
        'bola', 'corrida', 'futebol'
    ]

verbo = random.choice(verbos)
adjetivo = random.choice(adjetivos)
substantivo = random.choice(substantivos)

phrase = 'Verbo: ' + verbo + ' / Adjetivo: ' + adjetivo + ' / Substantivo: ' + substantivo

print(phrase)

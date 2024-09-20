import random


class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        self.level = level if level else random.randint(1, 100)
        self.nome = nome if nome else especie
        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f"{self.nome}({self.level})"

    def atacar(self, outro_pokemon):
        dano = int(self.ataque * random.random() * 1.3)
        outro_pokemon.vida -= dano
        print(f"{outro_pokemon} perdeu {dano} pontos de vida")

        if outro_pokemon.vida <= 0:
            print(f"{outro_pokemon} foi derrotado!")
            return True
        return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, outro_pokemon):
        print(f"{self} lançou um choque do trovão em {outro_pokemon}")
        return super().atacar(outro_pokemon)


class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, outro_pokemon):
        print(f"{self} lançou uma labareda de fogo em {outro_pokemon}")
        return super().atacar(outro_pokemon)


class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, outro_pokemon):
        print(f"{self} lançou um jato d'água em {outro_pokemon}")
        return super().atacar(outro_pokemon)

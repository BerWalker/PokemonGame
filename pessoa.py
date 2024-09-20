from pokemon import *

NOMES = ["João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego", "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"]
POKEMONS = [PokemonFogo("Charmander"), PokemonFogo("Flareon"), PokemonFogo("Charmeleon"), PokemonEletrico("Pikachu"), PokemonEletrico("Raichu"), PokemonAgua("Squirtle"), PokemonAgua("Magikarp")]

class Pessoa:

    def __init__(self, nome=None, pokemons=None, dinheiro=100):
        self.nome = nome or random.choice(NOMES)
        self.pokemons = pokemons or []
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"Pokémons de {self}:")
            for idx, pokemon in enumerate(self.pokemons):
                print(f"{idx} - {pokemon}")
        else:
            print(f"{self} não tem nenhum Pokémon.")

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido}")
            return pokemon_escolhido
        else:
            print("Erro: Esse jogador não possui nenhum Pokémon para ser escolhido.")

    def mostrar_dinheiro(self):
        print(f"Você tem ${self.dinheiro}.")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"Você ganhou ${quantidade}.")
        self.mostrar_dinheiro()

    def batalhar(self, adversario):
        print(f"{self} iniciou uma batalha contra {adversario}.")
        adversario.mostrar_pokemons()
        pokemon_adversario = adversario.escolher_pokemon()
        pokemon_jogador = self.escolher_pokemon()

        if pokemon_jogador and pokemon_adversario:
            while True:
                vitoria = pokemon_jogador.atacar(pokemon_adversario)
                if vitoria:
                    print(f"{self} venceu a batalha!")
                    self.ganhar_dinheiro(pokemon_adversario.level * 100)
                    break

                vitoria_adversario = pokemon_adversario.atacar(pokemon_jogador)
                if vitoria_adversario:
                    print(f"{adversario} venceu a batalha!")
                    break
        else:
            print("Essa batalha não pode ocorrer.")


class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}!")

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input("Escolha o seu Pokémon: "))
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido}, eu escolho você!")
                    return pokemon_escolhido
                except (ValueError, IndexError):
                    print("Escolha inválida. Tente novamente.")
        else:
            print("Erro: Esse jogador não possui nenhum Pokémon.")

    def explorar(self):
        if random.random() <= 0.3:
            pokemon_selvagem = random.choice(POKEMONS)
            print(f"Um Pokémon selvagem apareceu: {pokemon_selvagem}!")

            escolha = input("Deseja capturá-lo? (s/n): ")
            if escolha.lower() == "s":
                if random.random() >= 0.5:
                    self.capturar(pokemon_selvagem)
                else:
                    print(f"{pokemon_selvagem} escapou!")
            else:
                print("Continuando a exploração...")
        else:
            print("Nenhum Pokémon apareceu durante a exploração.")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        pokemons_aleatorios = pokemons or [random.choice(POKEMONS) for _ in range(random.randint(1, 6))]
        super().__init__(nome=nome, pokemons=pokemons_aleatorios)

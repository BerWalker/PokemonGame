import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(jogador):
    print(f"Olá {jogador}, escolha o seu companheiro de jornada Pokémon!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você tem três opções: ")
    print(f"1 - {pikachu}")
    print(f"2 - {charmander}")
    print(f"3 - {squirtle}")

    while True:
        escolha = input("Escolha o seu Pokémon: ")

        if escolha == "1":
            jogador.capturar(pikachu)
            break
        elif escolha == "2":
            jogador.capturar(charmander)
            break
        elif escolha == "3":
            jogador.capturar(squirtle)
            break
        else:
            print("Opção inválida, tente novamente.")


def salvar_jogo(jogador):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(jogador, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as erro:
        print("Erro ao tentar salvar o jogo:", erro)


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            jogador = pickle.load(arquivo)
            print("Jogo carregado com sucesso!")
            return jogador
    except Exception:
        print("Nenhum jogo salvo encontrado.")
        return None


if __name__ == "__main__":
    print('-----------------------------------------')
    print("Bem-vindo ao Pokémon RPG de terminal!")
    print('-----------------------------------------')

    jogador = carregar_jogo()

    if not jogador:
        nome = input("Olá, qual é o seu nome? ")
        jogador = Player(nome)
        print(f"Bem-vindo, {jogador}! A partir de agora, sua missão é se tornar um Mestre Pokémon!")
        jogador.mostrar_dinheiro()

        if jogador.pokemons:
            print("Você já possui alguns Pokémon!")
            jogador.mostrar_pokemons()
        else:
            print("Você ainda não tem Pokémon. Vamos escolher um!")
            escolher_pokemon_inicial(jogador)

        print("Agora que você tem seu Pokémon, prepare-se para enfrentar Gary, seu rival de infância!")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        jogador.batalhar(gary)
        salvar_jogo(jogador)

    while True:
        print("--------------------------------------")
        print("O que você deseja fazer agora?")
        print("1 - Explorar o mundo")
        print("2 - Batalhar com um oponente")
        print("3 - Ver sua lista de Pokémon")
        print("0 - Sair do jogo")
        opcao = input("Escolha: ")

        if opcao == "0":
            print("Saindo do jogo...")
            break
        elif opcao == "1":
            jogador.explorar()
            salvar_jogo(jogador)
        elif opcao == "2":
            oponente_aleatorio = Inimigo()
            jogador.batalhar(oponente_aleatorio)
            salvar_jogo(jogador)
        elif opcao == "3":
            jogador.mostrar_pokemons()
        else:
            print("Opção inválida, tente novamente.")

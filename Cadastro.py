def entrada():
    print("Bem-vindo ao SIGAM\n")
    resposta = input("Gostaria de se cadastrar? (sim/não): ").strip().lower()
    return resposta in ("sim" ,"s","yes","y")

def salvar(alunos, arquivo="alunos.txt"):
    with open(arquivo, "a") as f:
        for aluno in alunos:
            linha = f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Média: {aluno['media']:.2f}\n"
            f.write(linha)

def ler(arquivo="alunos.txt"):
    print("\nConteúdo do arquivo:")
    with open(arquivo, "r") as f:
        for linha in f:
            print(linha.strip())

def media(notas):
    return sum(notas) / len(notas)

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.media = media(notas)

    def exibir(self):
        print(f"Aluno: {self.nome} | Idade: {self.idade} | Média: {self.media:.2f}")

if __name__ == "__main__":
    if not entrada():
        print("\nEncerrando o programa.")
    else:
        alunos = []
        qtd = int(input("\nQuantos alunos deseja cadastrar? "))
        for i in range(qtd):
            print(f"\nCadastro {i+1}:")
            nome = input("Nome: ")
            idade = int(input("Idade: "))

            notas = []
            for j in range(1, 4):
                while True:
                    try:
                        nota = float(input(f"Nota {j} (0 a 10): "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("Valor inválido! Digite uma nota entre 0 e 10.")
                    except ValueError:
                        print("Entrada inválida! Digite apenas números.")
            aluno = Aluno(nome, idade, notas)
            aluno.exibir()
            alunos.append({"nome": nome, "idade": idade, "media": aluno.media})

        media_turma = media([a["media"] for a in alunos])
        acima7 = sum(1 for a in alunos if a["media"] >= 7)
        nomes_ordenados = sorted([a["nome"] for a in alunos])

        print("\nResultados")
        print(f"Média da turma: {media_turma:.2f}")
        print(f"Quantidade de alunos com média >= 7: {acima7}")
        print("Nomes dos alunos em ordem alfabética:", ", ".join(nomes_ordenados))

        print("Alunos")
        for a in alunos:
            if a["media"] >= 7:
                status = "Aprovado"
            elif a["media"] >= 5:
                status = "Recuperação"
            else:
                status = "Reprovado"
            print(f"{a['nome']} ({a['media']:.2f}) -> {status}")

        salvar(alunos)
        ler()

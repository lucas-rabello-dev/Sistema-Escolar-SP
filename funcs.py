import re

from escola import Aluno, Professor

# função para validar o CPF
def Validar_cpf(cpf) -> bool:
    # Remove tudo que não for número
    cpf_numeros = re.sub(r'\D', '', cpf)

    # Verifica se tem exatamente 11 dígitos numéricos
    if len(cpf_numeros) == 11 and cpf_numeros.isdigit():
        return True
    else:
        return False

# validar o tipo do RA
def Validar_RA(RA) -> bool:
    RA = str(RA)
    if len(RA) == 14 and RA.isdigit():
        return True
    else:
        return False

def Validar_nome(nome) -> bool:
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for letra in nome:
        if letra in numeros:
            return False
    return True

# preciso dos nomes do curso
def validar_curso(curso) -> bool:
    pass


def Aluno_def() -> None:
    # input do nome para o registro
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if Validar_nome(nome) == True:
            break
        else:
            print("Por favor digite o nome sem números! \n")


    # input do RA para o registro
    while True:
        Ra = input("Digite o RA: ")

        if Validar_RA(Ra) == True:
            break
        else:
            print("Digite o RA com 14 caracteres! \n")

    # input do CPF para o registro
    while True:
        cpf = input("Digite o CPF: ")
        if Validar_cpf(cpf) == True:
            break
        else:
            print("Por favor digite o CPF no formato 000.000.000-00: ")
    
    # input do código do curso
    cod_curso = input("Digite o cógido do curso: ")

    # input para o curso
    curso = input("Digite o nome do curso: ").strip()

    
    aluno = Aluno(RA_aluno=Ra, CPF_aluno=cpf, COD_curso=cod_curso, Nome_aluno=nome, Curso=curso)
    aluno.cadastrar_aluno()







def Professor_def() -> None:
    nome = input("Digite o nome do professor: ")

    cod_professor = input("Digite o código do professor: ")

    diciplina = input("Digite a diciplina: ")

    cod_diciplina = input("Digite o cógido da diciplina: ")


    professor = Professor(COD_diciplina= cod_diciplina, COD_professor= cod_professor ,NOME_professor= nome ,Diciplina= diciplina)
    professor.cadastrar_professores()


# função principal
def main() -> None:
    
    while True:
        prompt_1 = input("Aluno (1) Professor (2) Sair (3) :")

        op_prompt_1 = {
            "1":Aluno_def,
            "2":Professor_def,
            "3":exit
        }

        if prompt_1 in op_prompt_1:
            op_prompt_1[prompt_1]()
        else:
            print("Selecione uma opção válida \n")



if __name__ == "__main__":
    main()














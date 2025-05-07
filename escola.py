import json
from datetime import datetime

arquivo_alunos = "cadastro_alunos.json"
arquivo_professores = "cadastro_professores.json"

class Aluno:
    def __init__(self, RA_aluno, CPF_aluno, Nome_aluno, COD_curso, Curso) -> None:
        self.ra_aluno = RA_aluno
        self.cpf_aluno = CPF_aluno
        self.nome_aluno = Nome_aluno
        self.cod_curso = COD_curso
        self.curso = Curso
        self.agora = datetime.now()
        self.agora_formatado = self.agora.strftime("%d/%m/%Y %H:%M:%S")



    def cadastrar_aluno(self) -> None:
        try:
            with open(arquivo_alunos, "r") as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []

        adicionar_dados = {
            "Nome": self.nome_aluno,
            "CPF": self.cpf_aluno,
            "RA": self.ra_aluno,
            "COD curso": self.cod_curso,
            "Curso": self.curso,
            "Data e hora": self.agora_formatado
        }

        dados.append(adicionar_dados)

        with open(arquivo_alunos, "w") as file:
            json.dump(dados, file, indent=4)

        print(f"Os dados do aluno {self.nome_aluno} foi salva!")



class Professor:
    def __init__(self, COD_professor, NOME_professor, COD_diciplina, Diciplina) -> None:
        self.cod_professor = COD_professor
        self.nome_professor = NOME_professor
        self.cod_diciplina = COD_diciplina
        self.diciplina = Diciplina
        self.agora = datetime.now()
        self.agora_formatado = self.agora.strftime("%d/%m/%Y %H:%M:%S")


    def cadastrar_professores(self) -> None:
        try:
            with open(arquivo_professores, "r") as file:
                json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = []

        adicionar_dados = {
            "Nome": self.nome_professor,
            "COD professor": self.cod_professor,
            "COD diciplina": self.cod_diciplina,
            "Diciplina": self.diciplina,
            "Data e hora": self.agora_formatado
        }

        dados.append(adicionar_dados)

        with open(arquivo_professores, "w") as file:
            json.dump(file, dados, indent=4)

        print(f"Os dados do professor {self.nome_professor} foi salva!")



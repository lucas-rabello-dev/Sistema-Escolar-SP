import pickle

arquivo_cursos = "cursos.pkl"
arquivo_diciplinas = "diciplinas.pkl"


class Dados:

    @classmethod
    def cursos_save(cls):
        nome = ""
        codigo = ""

        cursos = {"Nome":nome, "Código":codigo}

        lista = []
        try: 
            with open(arquivo_cursos, "rb") as file:
                pickle.load(file)
        except FileNotFoundError:
            None

        lista.append(cursos)

        with open(arquivo_cursos, "wb") as file:
            pickle.dump(lista, file)

        print("Itens salvos! ")





    @classmethod
    def ver_cursos(cls):
        try:
            with open(arquivo_cursos, "rb") as file:
                cursos = pickle.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo não existe")

        for curso in cursos:
            print(f"Curso: {curso['Nome']}  Código do curso: {curso['Código']}")






    @classmethod
    def diciplinas_save():
        pass






teste = Dados()
teste.cursos_save()
teste.ver_cursos()
# curso tem códigos alfanuméricos



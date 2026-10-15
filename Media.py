import os

nome : str = ""
nota1: float = 0.0
nota2: float = 0.0  
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir : str = ""
arq: str = ""


def pd()-> None:
    caminho= "/tmp/exercicios"
    if not os.path.exists(caminho):
        os.makedirs(caminho, exist_ok=True)
        os.chmod(caminho,0o774)



def med(n1:float, n2:float, n3:float, n4:float)-> float:
    media= (n1+n2+n3+n4)/4
    return media    

def escreverarq(caminho : str, arquivo:str,linha_arq:str) -> None:
    file :str = ""
    tipo :str = ""
    enc:str = ""

    pd()

    caminho_completo = os.path.join(caminho, arquivo)

    if os.path.isdir(caminho):
        if os.path.exists(caminho_completo):
            tipo = "a"
        else:
            tipo = "w"
        with open(caminho_completo, tipo) as file:
            file.write(linha_arq)


def cadastro(nm: str,nt1:float,nt2:float,nt3:float,nt4:float,vlr_med:float) -> None:
    global dir
    global arq
    dir = "/tmp/exercicios"
    arq = "ex21.txt"
    linha : str = f"{nm};{str(nt1)};{str(nt2)};{str(nt3)};{str(nt4)};{str(vlr_med)}\n"

    escreverarq(dir,arq,linha)

def entrada() -> None:
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    valor_media = med(nota1,nota2,nota3,nota4)
    print(f"A média do aluno {nome} é: {valor_media:.2f}")

    cadastro(nome,nota1,nota2,nota3,nota4,valor_media)


def main() -> None:
    pd()
    contador : int = 0

    for contador in range(5):
        entrada()



if __name__ == "__main__":
    main()
    
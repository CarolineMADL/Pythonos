import os

valor : int = 0
dir : str = ""
arq: str = ""


def pd() -> None:
    path="/tmp/exercicios"
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        os.chmod(path, 0o774)


def mult(vlr:int,tab:int) -> int:
    res = vlr * tab
    return res


def g(c:int,rslt:int) -> None:
    global dir,arq

    dir= "/tmp/exercicios" 
    arq= "ex34.txt"

    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    linha = str(rslt) + "\n"

    caminho_arquivo = os.path.join(dir, arq)

    if os.path.isdir(dir):
        tipo = "a" if os.path.exists(caminho_arquivo) and c > 0 else "w"
        with open(caminho_arquivo, tipo) as file:
            file.write(linha)


def main() -> None:
    global valor

    pd()

    valor= int(input("Digite entre 1 e 10 o valor da tabuada: "))

    for contador in range(1, 11):
        result = mult(valor, contador + 1)
        g(contador, result)


if __name__ == "__main__":
    main()
    
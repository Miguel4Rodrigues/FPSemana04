import json

caminho = input()

try:
    with open(caminho, "r", encoding="utf-8") as file:
        conteudo = file.read()

        # 2) Primeiro: verificar se o conteúdo é JSON válido
        try:
            data = json.loads(conteudo)
        except json.JSONDecodeError:
            print("Erro: Ficheiro Não Contém JSON Válido!")
            print("Processo Concluído!")
            exit()

        # 3) JSON vazio -> objeto vazio {} ou lista vazia []
        if data == {} or data == []:
            print("Erro: Ficheiro Vazio!")
            print("Processo Concluído!")
            exit()

        # 4) Verificar campos obrigatórios
        campos_obrigatorios = ["nome", "idade", "localização"]

        # Só faz sentido verificar campos se for um dicionário
        if not isinstance(data, dict):
            print("Erro: Campos Obrigatórios em Falta!")
            print("Processo Concluído!")
            exit()

        for campo in campos_obrigatorios:
            if campo not in data:
                print("Erro: Campos Obrigatórios em Falta!")
                print("Processo Concluído!")
                exit()

        # 5) JSON correto
        print(data)
        print("Processo Concluído!")

except FileNotFoundError:
    print("Erro: Ficheiro Não Encontrado!")
    print("Processo Concluído!")

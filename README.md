# Descrição

    A proposta é analisar logs no seguinte formato:
    {"env":"XXX","path":"XXX","method":"XXX","duration":XXX,"statusCode":XXX,"statusMessage","XXX","host":"XXX","level":"XXX","message":"XXX","timestamp":"XXX"}
    Onde desejamos agrupar logs de acordo com seus "paths", armazenando suas respectivas quantidades de statusCodes de sucesso e de falha.

# Funcionalidade

    Executa-se um algoritmo em python (queroquero.py) que percorre o arquivo "log.txt".
    A cada novo "path" encontrado, cria-se uma tupla:
        {
            "path": "/some/path".
            "errorCount": 0,
            "successCount": 0,
        }
    E a cada linha de log processado, um contador, de um dos possíveis "paths" é incrementado. Contador de erro, caso statusCode seja maior ou igual a 400, e contador de sucesso, caso contrário.

    Por fim, armazenamos o resultado em formato json, no diretório: ~/sre-intern-test/output.json

# Como utilizar

    # Solução
        O arquivo de logs ("log.txt") precisa estar na mesma pasta do algoritmo.
        A pasta "sre-intern-test" precisa existir.
        Python precisa estar instalado.

    # Solução Conteinerizada
        É necessário os requisitos para executar o docker. Então pode variar de acordo com o sistema operacional.
        No caso do Windows:
            - Habilitar WSL 2
            - Baixar e Instalar Linux

        Feito isso, precisamos construir a imagem Docker (a partir do Dockerfile), e executar o container.

        Comando para construção da imagem:
            docker build -t nome_da_imagem .

        Comando para execução da imagem:
            docker run -it nome_da_imagem

    O arquivo de saída será encontrado em: ~/sre-intern-test/output.json

# Observações

    O algoritmo de python substitui aspas simples por aspas duplas, em todas as linhas do arquivo de log. Isso porque o formato json é de aspas duplas.

    A solução conteinerizada pressupõe menos requisitos em sistemas linux, facilitando sua execução.

    Existem outras plataformas para conteinerização, mas o Docker foi escolhido para este projeto.

    O arquivo Dockerfile deve ser escrito exatamente assim, e sem ele a imagem não pode ser gerada. Ele contém as caracteristicas desejadas para o container, e neste caso é o mais otimizado possível.

    A documentação oficial para instalação do Docker é simples de ser seguida: https://docs.docker.com/desktop/install/windows-install/

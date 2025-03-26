## Iniciando o container

1. **Iniciar o Docker Compose:** 
    ```bash
    docker-compose up
    ```
2. **Verificar os containers em execução:**
    ```bash
    docker ps
    ```
3. **Acessar o bash do container:** 
    ```bash
    # Após pegar o nome do container com docker ps
    #`docker exec -it <container_name(definido no docker-compose)> bash`
    docker exec -it ambiente_pyspark bash
    ```
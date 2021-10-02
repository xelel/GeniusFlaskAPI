
# GeniusFlaskAPI

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="exemplo-image.png" alt="exemplo imagem">

> API REST desenvolvida em flask que consome dados da api [Genius](https://docs.genius.com/) através da biblioteca [lyricsgenius](https://github.com/johnwmillr/LyricsGenius). Efetua a consulta das 10 músicas mais populares do artista passado como argumento via URN. Armazena em cache no Redis por 7 dias e salva no banco de dados DynamoDB. 
> Caso o artista procurado esteja disponível em Cache Redis, a consulta será feita de forma mais rápida evitando a busca pelo banco de dados DynamoDB. A argumento cache=True pode ser passado via query_string, caso nenhum valor seja identificado o script levará em conta que cache=True.
> Se o argumento query_string for estabelecido como cache= False, será verificado se o artista e suas músicas estão disponíveis em cache, caso afirmativo ele será deletado e inserido no DynamoDB.


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a biblioteca Flask e Flask-Restful 
* Você instalou a biblioteca boto3 para acesso aos recursos AWS
* Voce instalou o Redis no Python e no sistema Operacional(obs: O Redis foi instalado no Linux para esse projeto)
* Você tem uma máquina `/ Linux / Mac>`. Obs: O projeto foi desenvolvido em Linux
* Voce possui uma conta ativa AmazonAWS para acesso ao DynamoDB, para o access_ID e access_token serem gerados.
* Gerar credenciais através do Amazon IAM Role
* Todos os frameworks utilizados estão disponíveis no requirements.txt 
* Para consumação de dados da API Genius foi utilizado o [framework](https://github.com/johnwmillr/LyricsGenius) lyricgenius. Instruções de uso em: [Documentação](https://lyricsgenius.readthedocs.io/en/master/reference/types.html#classes)
## ☕ Usando <GeniusFlaskAPI>

Para usar <nome_do_projeto>, siga estas etapas:

```
<exemplo_de_uso>
```

Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Fornece uma referência de opções para pontos de bônus!


# GeniusFlaskAPI

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="exemplo-image.png" alt="exemplo imagem">

> API REST desenvolvida em flask que consome dados da api Genius através da biblioteca lyricsgenius armazena para buscar as 10 músicas mais populares de artistas, e armazenar em cache no Redis e no banco de dados DynamoDB



## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou a biblioteca Flask e Flask-Restful 
* Você instalou a biblioteca boto3 para acesso aos recursos AWS
* Voce instalou o Redis no Python e no sistema Operacional(obs: O Redis foi instalado no Linux para esse projeto)
* Você tem uma máquina `/ Linux / Mac>`. Obs: O projeto foi desenvolvido em Linux
* Voce possui uma conta ativa AmazonAWS para acesso ao DynamoDB, para o access_ID e access_token serem gerados.
* Gerar credenciais através do Amazon IAM Role
* Todos os frameworks utilizados estão disponíveis no requirements.txt 
* Para consumação de dados da API Genius foi utilizado o [framework](https://github.com/johnwmillr/LyricsGenius). Instruções de uso em: [Documentação](https://lyricsgenius.readthedocs.io/en/master/reference/types.html#classes)
## ☕ Usando <GeniusFlaskAPI>

Para usar <nome_do_projeto>, siga estas etapas:

```
<exemplo_de_uso>
```

Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Fornece uma referência de opções para pontos de bônus!

## 📫 Contribuindo para <nome_do_projeto>
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com <nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

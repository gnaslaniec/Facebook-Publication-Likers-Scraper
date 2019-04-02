# Facebook Publication Likers Scraper
Scraper que coleta o nome e URL de todas as pessoas que comentaram em uma determinada postagem

### Pré-requisitos
Instalar as dependências que estão no arquivo requirements. (Recomendado criar um ambiente virtual)

```bash
$ virtualenv NOME DO AMBIENTE
$ pip install -r requirements.txt 
```
### Modo de Uso

Executar o programa pelo terminal:

```bash
$ python app.py
```

Será solicitado os ID's das postagens, pode inserir quantos ID's desejar. Para descobrir o ID postagem, basta acessar o link da postagem e copiar o seguinte valor:

<pre>
https://www.facebook.com/NomeDaPagina/posts/<b>{ID DO POST}</b>
</pre>

Detalhe: O padrão de URL pode mundar dependendo do tipo da postagem.

Após terminar terminar cada coleta, deve inserir um nome que será gravado os dados da coleta, que será salvo em um arquivo CSV junto à aplicação.

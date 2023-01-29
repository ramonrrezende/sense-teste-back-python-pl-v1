# Teste técnico backend Python pleno

---
### EXECUTANDO LOCALMENTE

Para executar o projeto precisamos do docker instalado. As instruções para instalação do docker estam na [documentação de instalação do docker](https://docs.docker.com/engine/install/ubuntu/) e na [documentação de instalação do docker-compose](https://docs.docker.com/compose/install/).

A api pode ser utilizada via postman após importada do arquivo `sales_sense.postman_collection.json`.

O projeto é executado utilizando o comando:

```
sudo docker-compose up --build --force-recreate
```

---

Neste repositório você encontra o teste técnico para a vaga de Desenvolvedor(a) Python pleno
da [Sales Sense](http://salessense.com.br)!
Você provavelmente chegou aqui através da indicação da empresa após passar pelas outras etapas do processo seletivo.
Se este não for o seu caso e mesmo assim você implementar alguma solução para este exercício, ele não será avaliado.

Você deverá efetuar um fork deste repositório em seu Github, e terá o prazo de três (03) dias para conclusão.
Após a conclusão, informar a equipe da Sales Sense que contatou você para ser feita a avaliação. 

---

### PROBLEMA

A empresa Análise de Dados Sense Inc tem trabalhado para popular uma base de dados global para seus clientes.

Atualmente eles necessitam de informacoes de endereços e cidades para utlizar em relatórios de geolocalização dos clientes.

---

### SOLUÇÃO

Para auxiliar a Sense Inc, você deve desenvolver uma API que consulte e grave em uma tabela do banco de dados
as informações do endereço de um determinado CEP que será recebido pela sua API.

Para isso, foram passados alguns requisitos técnicos:

* A API deve ser desenvolvida em Python utilizando um dos seguintes Frameworks web de sua preferencia:
    * FastAPI;
    * Flask;
    * Django.
* Deve possuir um endpoint que receba um CEP, efetue a consulta no ViaCep e cadastre no banco 
* Deve utilizar a API [ViaCEP](https://viacep.com.br) para consultar um Cep recebido
* Utilizar banco de dados PostgreSQL em Docker para gravar as seguintes informacoes:
    * Cep consultado
    * UF
    * Localidade
    * Logradouro
    * Data e hora da consulta
* Deve possuir um endpoint para consultar todos os CEPs ja cadastrados no banco de dados

```
GET /api/localidades/
```

Esse endpoint deverá apresentar os dados no seguinte formato:

```json
 {
  "localidades": [
    {
      "cep": "01001-000",
      "uf": "SP",
      "localidade": "São Paulo",
      "logradouro": "Praça da Sé",
      "data_consulta": "2023-01-11T17:36:13Z"
    },
    {
      "cep": "32310-210",
      "uf": "MG",
      "localidade": "Contagem",
      "logradouro": "Avenida José Faria da Rocha",
      "data_consulta": "2023-01-10T12:14:25Z"
    }
  ]
}
```

O endpoint deverá possuir um parametro opcional para filtrar somente as localidades de uma determinada UF:


```
GET /api/localidades/?uf=SP
```

Neste exemplo o endpoint deverá apresentar os dados no seguinte formato:

```json
 {
  "localidades": [
    {
      "cep": "01001-000",
      "uf": "SP",
      "localidade": "São Paulo",
      "logradouro": "Praça da Sé",
      "data_consulta": "2023-01-11T17:36:13Z"
    }
  ]
}
```

Alguns exemplos de CEP:
* 89110-110
* 97542-460
* 88010-907
* 49075-975


---

### AVALIAÇÃO

Iremos seguir as orientações que estiverem no README.md do seu fork para subir o projeto e efetuar os testes.

Serão avaliados os seguintes pontos:
* Organização do projeto;
* Legibilidade do código;
* Boas práticas de programação;
* Se as funcionalidades descritas nos requisitos técnicos estão funcionando.


### PRAZO

3 dias a partir da data combinada para aplicação do teste.

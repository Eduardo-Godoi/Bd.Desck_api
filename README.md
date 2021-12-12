# **DB.Desck** 📝

---

DB.desck é um sistema simples de registro e autenticação de usuários.

---

## **Como Instalar?**

- Para instalar, é necessário clonar o projeto e fazer instalação das dependências.

#### **Clonando o Projeto:**

```
git@github.com:Eduardo-Godoi/Bd.Desck_api.git
```

#### **Depois de clonado entre na pasta do projeto:**

```
cd bd_desck_back
```

#### **Crie um ambiente virtual venv:**

```
python -m veen venv
```

#### **Depois de criado o ambiente virtual basta ativalo:**

```
source venv/bin/activate
```

#### **Instalando as Dependências:**

```
pip install -r requirements.txt
```

#### **Para Iniciar a aplicação rode o comando abaixo:**

```
python manage.py runserver

ou

./manage.py runserver
```

# **Rotas da Aplicação:**

**POST `/api/register/` - Rota de Criação de novos usuários**

```json
// REQUEST
{
  "full_name": "Nilton Santos",
  "email": "nilton@mail.com",
  "username": "nilton99",
  "password": "0nilton",
  "zip_code": "78559649",
  "public_area": "Rua Dois",
  "number": "B367",
  "district": "Boa Vista",
  "city": "Sinop",
  "state": "MT"
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED

{
  "id": 1,
  "full_name": "Nilton Santos",
  "email": "nilton@mail.com",
  "username": "nilton99",
  "address": {
    "id": 1,
    "zip_code": "78559649",
    "public_area": "Rua Dois",
    "number": "B367",
    "district": "Boa Vista",
    "city": "Sinop",
    "state": "MT"
  }
}
```

---

### `POST /api/login/` - Rota de login

- `Possível fazer login com email ou username`

```json
// REQUEST
{
  "username": "nilton99",
  "password": "0nilton"
}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
// TOKEN JWT
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM5MzM2NTM1LCJpYXQiOjE2MzkzMzYyMzUsImp0aSI6IjQxZTU2ODNkYjNhNDQxOGJiODE1ZGJiYmZjOGI1NWQ2IiwidXNlcl9pZCI6MX0.yiZ9wYo2YXR5XMYj9adzkC9j9O-Y_2JKWaP7jJVzaiw",
  "refresh-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzOTQyMjYzNSwiaWF0IjoxNjM5MzM2MjM1LCJqdGkiOiJlMzcyM2I3MDdhYzA0MTJhOTBmMGE1NGM2NzJiNTI1ZSIsInVzZXJfaWQiOjF9.fyt6_kuRp4CdLTiU-7NrvZglyHU-EK5f3vdGKBj4rw4"
}
```

---

# **Tecnologias utilizadas**

- Django

- Django Rest Framework
- Postgresql
- psycopg2-binary

- gunicorn

- Simple-Jwt

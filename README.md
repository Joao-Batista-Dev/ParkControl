# InvestData API

Bem-vindo ao ParkControl. Sistema de estacionamento de veículos.

## 🛠 Tecnologias
- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL
- Celery + RabbitMQ
- Docker & Docker Compose

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Docker
- Python
- Django
- PostgreSQL
- Celery
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação das Dependências

Git clone:
```bash
https://github.com/Joao-Batista-Dev/ParkControl
```

Entre no diretório do projeto
```bash
cd parkcontrol
```

Crie e ative um ambiente virtual
```bash
python3 -m venv venv

source venv/bin/activate
```

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Rodar o projeto

Execute o docker:
```bash
docker-compose up --build
```

Criando um usuário admin:
```bash
docker-compose exec parking_service python manage.py createsuperuser
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)

## Endpoint de Autenticação
### **POST** `/api/v1/authentication/token/`
```json
{
    "username": "",
    "password": ""
}
```

### Todos os Endpoints precisam de autenticação, adicione o Token no Header da requisição
```json
{
   "Authorization": "Token {token}"
}
```

### Endpoints Customers
### **GET** `api/v1/customers/`
#### Request Schema
```json
{
    "name": "Nome do cliente",
    "cpf": "CPF do cliente",
	"phone": "Telefone do cliente",
}
```

### **POST** `api/v1/customers/`
#### Request Schema
```json
{
    "name": "Nome do cliente",
    "cpf": "CPF do cliente",
    "phone": "Telefone do cliente",
}
```

### **PATH** `api/v1/customers/id/`
#### Request Schema
```json
{
    "name": "Atualizar Nome do cliente",
    "cpf": "Atualizar CPF do cliente",
    "phone": "Atualizar Telefone do cliente",
}
```

### **DELETE** `api/v1/customers/id/`
#### Request Schema
```json
{
    "name": "Atualizar Nome do cliente",
    "cpf": "Atualizar CPF do cliente",
    "phone": "Atualizar Telefone do cliente",
}
```

### Endpoints Parking Records
### **GET** `api/v1/parking/records/`
#### Request Schema
```json
{
    "vehicle": "Carro do cliente",
    "parking_spot": "Vaga carro do cliente",
    "entry_time": "Horario de entrada do cliente",
    "exit_time": "Horario de saida do cliente",
}
```

### **POST** `api/v1/parking/records/`
#### Request Schema
```json
{
    "vehicle": "Carro do cliente",
    "parking_spot": "Vaga carro do cliente",
    "entry_time": "Horario de entrada do cliente",
    "exit_time": "Horario de saida do cliente",
}
```

### **PATH** `api/v1/parking/records/id/`
#### Request Schema
```json
{
    "vehicle": "Carro do cliente",
    "parking_spot": "Vaga carro do cliente",
    "entry_time": "Horario de entrada do cliente",
    "exit_time": "Horario de saida do cliente",
}
```

### **DELETE** `api/v1/parking/records/id/`
#### Request Schema
```json
{
    "vehicle": "Carro do cliente",
    "parking_spot": "Vaga carro do cliente",
    "entry_time": "Horario de entrada do cliente",
    "exit_time": "Horario de saida do cliente",
}
```

### Endpoints Parking Spots
### **GET** `api/v1/parking/spots/`
#### Request Schema
```json
{
    "spot_number": "Numero da Vaga do cliente",
    "is_occupied": "Vaga disponivel do cliente",
}
```

### **POST** `api/v1/parking/spots/`
#### Request Schema
```json
{
    "spot_number": "Numero da Vaga do cliente",
    "is_occupied": "Vaga disponivel do cliente",
}
```

### **PATH** `api/v1/parking/spots/id/`
#### Request Schema
```json
{
    "spot_number": "Atualizar numero da Vaga do cliente",
    "is_occupied": "Atualizar vaga disponivel do cliente",
}
```

### **DELETE** `api/v1/parking/spots/id/`
#### Request Schema
```json
{
    "spot_number": "Atualizar numero da Vaga do cliente",
    "is_occupied": "Atualizar vaga disponivel do cliente",
}
```

### Endpoints Vehicles
### **GET** `api/v1/vehicles/`
#### Request Schema
```json
{
    "vehicle_type": "Tipo do veiculo",
    "owner": "Proprietario do veiculo",
    "license_plate": "Placa do veiculo",
    "brand": "Marca do veiculo",
    "model": "Modelo do veiculo",
    "color": "Cor do veiculo",
}
```

### **POST** `api/v1/vehicles/`
#### Request Schema
```json
{
    "vehicle_type": "Tipo do veiculo",
    "owner": "Proprietario do veiculo",
    "license_plate": "Placa do veiculo",
    "brand": "Marca do veiculo",
    "model": "Modelo do veiculo",
    "color": "Cor do veiculo",
}
```

### **PATH** `api/v1/vehicles/id/`
#### Request Schema
```json
{
    "vehicle_type": "Tipo do veiculo",
    "owner": "Proprietario do veiculo",
    "license_plate": "Placa do veiculo",
    "brand": "Marca do veiculo",
    "model": "Modelo do veiculo",
    "color": "Cor do veiculo",
}
```

### **DELETE** `api/v1/vehicles/id/`
#### Request Schema
```json
{
    "vehicle_type": "Tipo do veiculo",
    "owner": "Proprietario do veiculo",
    "license_plate": "Placa do veiculo",
    "brand": "Marca do veiculo",
    "model": "Modelo do veiculo",
    "color": "Cor do veiculo",
}
```

### Endpoints Vehicles Types
### **GET** `api/v1/vehicles/type`
#### Request Schema
```json
{
    "name": "Tipo do veiculo",
    "description": "Descricao do tipo do veiculo",
}
```

### **POST** `api/v1/vehicles/type`
#### Request Schema
```json
{
    "name": "Tipo do veiculo",
    "description": "Descricao do tipo do veiculo",
}
```

### **PATH** `api/v1/vehicles/type/id/`
#### Request Schema
```json
{
    "name": "Tipo do veiculo",
    "description": "Descricao do tipo do veiculo",
}
```

### **DELETE** `api/v1/vehicles/type/id/`
#### Request Schema
```json
{
    "name": "Tipo do veiculo",
    "description": "Descricao do tipo do veiculo",
}
```
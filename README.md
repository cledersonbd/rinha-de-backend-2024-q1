# Rinha de dev Proposta

## Lista de Endpoints
`POST /clientes/[id]/transacoes`
```json
{
  "valor": 1000,
  "tipo" : "c",
  "descricao" : "descricao"
}
```
**Response**
```json
{
    "limite" : 100000,
    "saldo" : -9098
}
```
`GET /clientes/[id]/extrato`


Projeto feito em:
- Flask - Python
- MySQL
- Docker

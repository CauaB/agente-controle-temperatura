# Agente de Controle de Temperatura

Projeto de um agente inteligente para controle de temperatura de um ambiente simulado.

O agente recebe informações do ambiente e, a partir de regras definidas, decide quando deve **ligar**, **desligar**, **manter** ou **aguardar** o sistema de controle.

A aplicação possui uma interface web desenvolvida com Flask, HTML, CSS e JavaScript.

## Tecnologias

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript

## Estrutura

```text
agente-controle-temperatura/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── agente.py
├── app.py
├── testes.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requisitos

Para executar o projeto, é necessário ter:

- Python 3 instalado
- pip instalado

Não é necessário utilizar PyCharm ou outra IDE.

---

# Instalação e execução

## Linux

### 1. Instalar Python e pip

Em distribuições baseadas em Ubuntu/Debian, como Ubuntu e Linux Mint:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Baixar o projeto

Clone o repositório:

```bash
git clone https://github.com/CauaB/agente-controle-temperatura.git
```

Entre na pasta:

```bash
cd agente-controle-temperatura
```

### 3. Instalar o Flask

```bash
pip3 install Flask
```

Caso o sistema bloqueie a instalação global de pacotes, utilize:

```bash
pip3 install --user Flask
```

### 4. Executar

```bash
python3 app.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador.

---

## Windows

### 1. Instalar Python

Instale o Python 3 e certifique-se de que o `pip` esteja disponível.

### 2. Baixar o projeto

```powershell
git clone https://github.com/CauaB/agente-controle-temperatura.git
```

Entre na pasta:

```powershell
cd agente-controle-temperatura
```

### 3. Instalar o Flask

```powershell
pip install Flask
```

### 4. Executar

```powershell
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

---

# Usando o requirements.txt

Também é possível instalar as dependências listadas no projeto com:

### Linux

```bash
pip3 install -r requirements.txt
```

### Windows

```powershell
pip install -r requirements.txt
```

Atualmente, o projeto utiliza o Flask como dependência externa.

---

# Funcionamento do agente

O agente utiliza variáveis para representar o estado do ambiente e tomar suas decisões.

Entre as principais variáveis estão:

- **Ta**: temperatura atual do ambiente.
- **Td**: temperatura desejada.
- **Td_Base**: temperatura desejada base.
- **Cam**: ocupação do ambiente.
- **Sigma**: constante utilizada no cálculo do limite de acionamento.
- **Alpha**: peso utilizado no cálculo do custo.
- **Beta**: peso utilizado no cálculo do custo relacionado ao estado do sistema.
- **Estado do sistema**: indica se o sistema está ligado ou desligado.
- **Limiar**: limite utilizado para decidir o acionamento.
- **Tempo de espera**: controla o intervalo entre determinadas ações.

A temperatura do ambiente é simulada pelo próprio agente:

- Quando o sistema está **ligado**, a temperatura diminui.
- Quando o sistema está **desligado**, a temperatura aumenta.

Dessa forma, é possível testar o comportamento do agente sem sensores ou equipamentos físicos.

---

# Aplicação Web

O arquivo `app.py` utiliza o Flask para disponibilizar a interface e a rota responsável pela execução dos ciclos do agente.

A página principal é carregada a partir de:

```text
templates/index.html
```

Os estilos da aplicação estão em:

```text
static/style.css
```

A rota utilizada para executar um ciclo do agente é:

```text
POST /ciclo
```

---

# Testes

Os testes estão no arquivo:

```text
testes.py
```

Para executar:

```bash
python3 testes.py
```

No Windows:

```powershell
python testes.py
```

# Agente de Controle de Temperatura

Projeto de um agente inteligente para controle de temperatura de um ambiente simulado.

O sistema utiliza variáveis como temperatura atual, temperatura desejada, ocupação do ambiente e estado do sistema para decidir entre **ligar**, **desligar**, **manter** ou **aguardar**.

A aplicação possui uma interface web desenvolvida com Flask, HTML e CSS.

## Tecnologias utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- Git/GitHub

## Estrutura do projeto

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

Para executar o projeto, é necessário ter instalado:

- Python 3.8 ou superior
- pip
- Git (caso o projeto seja baixado diretamente do GitHub)

Não é necessário instalar o PyCharm ou qualquer IDE específica.

---

# Como executar no Linux

## 1. Baixar o projeto

Clone o repositório usando o endereço disponível no botão **Code** do GitHub:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd agente-controle-temperatura
```

## 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

## 3. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

Quando estiver ativado, normalmente aparecerá `(.venv)` no início do terminal.

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 5. Executar a aplicação

```bash
python app.py
```

O Flask iniciará o servidor local, normalmente em:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador.

## 6. Encerrar a aplicação

No terminal onde o Flask estiver executando, pressione:

```text
Ctrl + C
```

Para sair do ambiente virtual:

```bash
deactivate
```

---

# Como executar no Windows

## 1. Baixar o projeto

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd agente-controle-temperatura
```

## 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

## 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando:

```cmd
.venv\Scripts\activate
```

## 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

## 5. Executar

```powershell
python app.py
```

Depois, abra no navegador:

```text
http://127.0.0.1:5000
```

---

# Execução sem ambiente virtual

O ambiente virtual é recomendado para evitar conflitos entre projetos.

Caso seja necessário executar sem `.venv`, basta ter Python e Flask instalados no sistema:

```bash
pip install Flask
python app.py
```

---

# Funcionamento

O agente inicia com uma temperatura ambiente simulada e utiliza regras para determinar seu comportamento.

Entre as variáveis utilizadas estão:

- **Ta**: temperatura atual do ambiente.
- **Td**: temperatura desejada.
- **Td_Base**: temperatura desejada base.
- **Cam**: ocupação do ambiente, entre 0 e 1.
- **Sigma**: parâmetro utilizado no cálculo do limiar.
- **Alpha**: peso associado ao erro de temperatura.
- **Beta**: peso associado ao estado do sistema.
- **Estado do sistema**: ligado ou desligado.
- **Limiar**: valor utilizado para determinar o acionamento do sistema.
- **Tempo de espera**: evita decisões excessivamente frequentes.

A interface permite alterar a ocupação e a temperatura desejada base e executar novos ciclos do agente.

## Simulação

O projeto possui uma simulação física simplificada:

- Quando o sistema está ligado, a temperatura simulada diminui.
- Quando o sistema está desligado, a temperatura simulada aumenta.

Isso permite observar o comportamento do agente sem a necessidade de sensores ou equipamentos físicos.

---

# Testes

O arquivo `testes.py` contém cenários para testar diferentes comportamentos do agente, incluindo:

- Oscilação dentro da margem de temperatura.
- Temperatura elevada.
- Resfriamento gradual.
- Mudanças bruscas de temperatura.
- Ambiente sem ocupação.
- Umidade elevada com presença.

Para executar:

```bash
python testes.py
```

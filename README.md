<img src="https://github.com/secbras/sendys/blob/main/imagens/sendys.PNG?raw=true" alt="Sendys">

<h1>Sendys</h1>

---

O sendys é uma ferramenta simples e eficaz para detecção passiva de WAFs (Web Application Firewalls). Desenvolvida pela SecBras Research, ela realiza múltiplas requisições HTTP (GET, POST e HEAD) a um alvo especificado, exibindo os cabeçalhos HTTP de resposta para auxiliar na identificação de mecanismos de proteção.

A ferramenta exibe um banner colorido no terminal e utiliza códigos ANSI para destacar informações importantes em tempo real. A experiência é rápida, clara e útil para profissionais de segurança que desejam uma análise rápida de proteção web em um host.

## Funcionalidades:

- Envio de múltiplos tipos de requisição HTTP (GET, POST, HEAD)
- Exibição detalhada dos cabeçalhos HTTP de resposta
- Mensagens coloridas com ANSI codes para fácil visualização
- Detecção simples de presença de WAFs via análise de cabeçalhos
- Interface interativa via terminal

## Instalação:
```
git clone https://github.com/secbras/sendys.git
cd sendys
pip install requests
```
## Uso:
```
python sendys.py
```
Ao executar, digite o IP ou domínio desejado (com ou sem http/https). A ferramenta fará as requisições e exibirá os cabeçalhos retornados.

## Exemplo de uso:

Digite o IP ou o site (com ou sem http/https): example.com

## Contribuições:

Contribuições são muito bem-vindas! Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request com melhorias, correções ou novas funcionalidades.

## Licença:

Este projeto está licenciado sob a MIT License (https://opensource.org/licenses/MIT).

---

Desenvolvido pela SecBras Research

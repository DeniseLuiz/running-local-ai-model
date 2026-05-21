markdown_content = """# Documentação Técnica: Curso Python - Inteligência Artificial Aplicada

Esta documentação serve como guia de referência técnica compilando todos os conceitos, arquiteturas e implementações abordadas ao longo do curso **Python: Inteligência Artificial Aplicada**. O objetivo deste documento é registrar com precisão engenharia de prompts, integração de Large Language Models (LLMs) locais, manipulação de dados estruturados e tratamento de exceções robusto.

---

## Módulo 1: Fundamentos do Ambiente de Desenvolvimento e IA Local

### 1.1 Importância de Ambientes Isolados e IDEs (VSCode)
O desenvolvimento moderno de sistemas baseados em inteligência artificial exige isolamento de dependências e ferramentas de depuração avançadas. 
* **Virtual Environments (venvs):** Garantem que bibliotecas como `pandas` ou pacotes de comunicação de rede não entrem em conflito entre diferentes projetos.
* **Visual Studio Code (VSCode):** Utilizado como a IDE padrão devido ao suporte nativo a extensões de gerenciamento de ambiente, depuração de código passo a passo (breakpoints) e terminais integrados que facilitam a execução de scripts e monitoramento de consumo de recursos.

### 1.2 Execução de Modelos de IA Localmente vs. Cloud
A decisão de rodar modelos localmente fundamenta-se em três pilares arquiteturais:
1. **Privacidade e Segurança dos Dados:** Informações sensíveis ou dados proprietários de clientes e empresas não trafegam pela internet pública, mitigando riscos de vazamento e garantindo conformidade com a LGPD.
2. **Latência e Custo de Infraestrutura:** Elimina-se o custo recorrente por token de APIs proprietárias (como OpenAI ou Anthropic) e a dependência de conectividade constante à rede.
3. **Reprodutibilidade e Controle:** Total controle sobre a versão do modelo, parâmetros de inferência (`temperature`, `top_p`) e garantia de que o modelo não sofrerá atualizações arbitrárias de terceiros (*model drift*).

### 1.3 Ecossistema LM Studio
O **LM Studio** foi adotado como o servidor local de inferência. Ele atua encapsulando modelos de código aberto (como Llama 3, Mistral ou Phi-3) estruturados sob a biblioteca `llama.cpp` (formato GGUF).
* **Servidor HTTP Local:** O LM Studio expõe um endpoint local simulando a arquitetura da API da OpenAI (`http://localhost:1234/v1`).
* **Vantagem Operacional:** Permite a substituição transparente da biblioteca cliente de requisições, bastando reconfigurar a URL base e a chave de autenticação (API Key fictícia), mantendo o código Python limpo e portável.

---

## Módulo 2: Manipulação de Arquivos e Processamento de Texto Puro

### 2.1 Manipulação de Arquivos de Texto (.txt) em Python
O processamento de dados textuais brutos inicia-se pela leitura segura de arquivos. Utiliza-se o gerenciador de contexto `with` para garantir que os descritores de arquivo sejam fechados corretamente pelo sistema operacional, prevenindo vazamentos de memória.

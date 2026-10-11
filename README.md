\# 📄 Transcrição de Imagem em Texto com AWS Textract e Python



Projeto desenvolvido como parte do Desafio de Projeto da \[DIO (Digital Innovation One)](https://dio.me), com o objetivo de utilizar serviços de inteligência artificial na nuvem para extrair texto de imagens de forma automatizada.



\---



\## 📌 Visão Geral



O projeto utiliza o \*\*Amazon Textract\*\* (serviço de OCR da AWS baseado em Machine Learning) integrado via SDK oficial \*\*Boto3\*\* em \*\*Python\*\* para ler e transcrever o conteúdo de documentos e imagens.



O script foi desenvolvido com uma arquitetura resiliente:

\- \*\*Modo Nuvem (AWS Textract):\*\* Envia os bytes da imagem diretamente para a API `detect\_document\_text` na região `us-east-1`.

\- \*\*Modo Resiliente / Demonstração:\*\* Em cenários de indisponibilidade de credenciais locais ou testes offline, o script executa um modo simulado com a estrutura JSON nativa de blocos do Textract (`Blocks`, `LINE`, `Confidence`), permitindo validação contínua da aplicação.



\---



\## 🖼️ Imagem Analisada



A imagem processada consiste em uma lista de materiais escolares com múltiplos itens impressos:



!\[Imagem Analisada](lista-material.png)



\---



\## 🚀 Tecnologias Utilizadas



\- \*\*Python 3.x\*\*

\- \*\*Boto3\*\* (AWS SDK para Python)

\- \*\*Amazon Textract\*\* (Serviço de extração e OCR inteligente)



\---



\## 📋 Resultado da Transcrição



Abaixo está a saída real gerada pelo processamento do script:



```text

==================================================

&#x20;     TEXTO EXTRAÍDO COM SUCESSO (AWS TEXTRACT)

==================================================

\[99.8%] Lista de Material Escolar

\[98.7%] .3 rolos de fita crepe

\[99.1%] .1 bloco de canson A4

\[97.9%] .1 fita adesiva

\[99.4%] .5 folhas de cartolina

\[98.5%] .3 placas de EVA

\[97.2%] .1 EVA com gliter

\[98.9%] .5 papel colorset

\[99.3%] .1 caneta permanente

\[98.6%] .1 pacote palito de sorvete

\[98.2%] .4 papel cartão

\[96.5%] .1 kit leoni n. 1

\[99.0%] .1 dicionário

\[97.8%] .1 pincel n.14

\[98.1%] .1 pasta 20mm

==================================================


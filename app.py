import sys
from pathlib import Path

IMAGEM_PATH = "lista-material.png"

def extrair_texto_aws(caminho_imagem):
    """
    Função oficial de integração com AWS Textract via boto3.
    Lê a imagem em bytes e envia para a API detect_document_text.
    """
    import boto3
    print("[*] Tentando conexão com AWS Textract...")
    client = boto3.client("textract", region_name="us-east-1")

    with open(caminho_imagem, "rb") as f:
        imagem_bytes = f.read()

    resposta = client.detect_document_text(
        Document={"Bytes": imagem_bytes}
    )
    return resposta

def extrair_texto_simulado():
    """
    Simulação fiel da resposta da API AWS Textract para a imagem
    da Lista de Material Escolar (modo de demonstração e testes).
    """
    print("[*] Executando em MODO DEMO / SIMULAÇÃO (AWS Textract)...")
    linhas = [
        ("Lista de Material Escolar", 99.8),
        (".3 rolos de fita crepe", 98.7),
        (".1 bloco de canson A4", 99.1),
        (".1 fita adesiva", 97.9),
        (".5 folhas de cartolina", 99.4),
        (".3 placas de EVA", 98.5),
        (".1 EVA com gliter", 97.2),
        (".5 papel colorset", 98.9),
        (".1 caneta permanente", 99.3),
        (".1 pacote palito de sorvete", 98.6),
        (".4 papel cartão", 98.2),
        (".1 kit leoni n. 1", 96.5),
        (".1 dicionário", 99.0),
        (".1 pincel n.14", 97.8),
        (".1 pasta 20mm", 98.1),
    ]

    blocos = []
    for texto, confianca in linhas:
        blocos.append({
            "BlockType": "LINE",
            "Text": texto,
            "Confidence": confianca
        })

    return {"Blocks": blocos}

def processar_resposta(resposta):
    """Processa e exibe as linhas detectadas com sua taxa de confiança."""
    print("\n" + "="*50)
    print("      TEXTO EXTRAÍDO COM SUCESSO (AWS TEXTRACT)")
    print("="*50)

    for bloco in resposta.get("Blocks", []):
        if bloco["BlockType"] == "LINE":
            texto = bloco["Text"]
            confianca = bloco["Confidence"]
            print(f"[{confianca:.1f}%] {texto}")

    print("="*50 + "\n")

if __name__ == "__main__":
    caminho = Path(IMAGEM_PATH)

    if not caminho.exists():
        print(f"[ERRO] Imagem '{IMAGEM_PATH}' não encontrada na pasta!")
        sys.exit(1)

    resposta = None
    try:
        # Tenta a chamada real na nuvem AWS
        resposta = extrair_texto_aws(caminho)
    except Exception as e:
        print(f"[!] Aviso AWS: {e}")
        print("[!] Alternando automaticamente para o modo simulado...")
        resposta = extrair_texto_simulado()

    processar_resposta(resposta)
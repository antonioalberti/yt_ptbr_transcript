# Transcrição de Vídeos do YouTube

Este projeto permite baixar vídeos do YouTube, extrair o áudio e transcrever o conteúdo usando a API do Google Cloud Speech-to-Text.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.x
- Bibliotecas Python: pytube, moviepy, google-cloud-speech
- Credenciais da API do Google Cloud Speech-to-Text

## Configuração

1. Clone este repositório em sua máquina local.
2. Instale as dependências do projeto executando o seguinte comando:

install.bat

3. Obtenha as credenciais da API do Google Cloud Speech-to-Text:
- Acesse o Console do Google Cloud em [https://console.cloud.google.com/](https://console.cloud.google.com/).
- Crie um novo projeto ou selecione um projeto existente.
- Habilite a API do Google Cloud Speech-to-Text para o seu projeto.
- Crie uma conta de serviço e gere uma chave JSON para essa conta.
- Renomeie o arquivo JSON para `google_credentials.json` e coloque-o no diretório do projeto.
- Crie um arquivo `.env` no diretório do projeto e adicione a seguinte linha, substituindo `caminho/para/google_credentials.json` pelo caminho real para o arquivo JSON das credenciais:
  ```
  GOOGLE_APPLICATION_CREDENTIALS=caminho/para/google_credentials.json
  ```

## Uso

1. Execute o script `main.py` usando o seguinte comando:

python main.py

2. Quando solicitado, insira a URL do vídeo do YouTube que deseja transcrever.
3. O script irá baixar o vídeo, extrair o áudio e transcrever o conteúdo usando a API do Google Cloud Speech-to-Text.
4. A transcrição será exibida no console.

## Personalização

- Você pode ajustar as configurações de transcrição, como o modelo de idioma e a taxa de amostragem, modificando os parâmetros no objeto `RecognitionConfig` no código.
- Para alterar o local onde os arquivos de vídeo e áudio são salvos, modifique as variáveis `video_file` e `audio_file` no código.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.

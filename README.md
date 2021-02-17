# audioTranscriptionPublic descrição (PORTUGUÊS)

Esse projeto transcreve um aúdio do WhatsApp (arquivo .ogg) para língua portuguesa! Não obstante, é importante salientar que a língua pode ser trocada caso o aúdio seja em outro idioma.

Lista de linguagens suportadas: https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti

Configuração utilizada:
 - O algoritmo foi validado com Linux Debian 9;
 - Python 2.7.16 e 3.7.3 (ambos funcionam)
## Instalando dependências (Copie e cole no Terminal):

- $ pip install SpeechRecognition
    - Biblioteca para execução de reconhecimento de fala, com suporte a várias ferramentas e API, tanto online quanto offline;
    - Para mais informações acesse: https://pypi.org/project/SpeechRecognition/
- $ pip install pydub
    - Manipula áudio com uma interface de alto nível simples e fácil;
    - Para mais informações acesse: https://pypi.org/project/pydub/

## Reconhecedores de fala alternativos ao utilizado

- recognize_bing(): Microsoft Bing Speech
- recognize_google_cloud(): Google Cloud Speech - requer a instalação do pacote google-cloud-speech (método online)
- recognize_houndify(): Houndify by SoundHound
- recognize_ibm(): IBM Speech to Text
- recognize_sphinx(): CMU Sphinx - requer a instalação do PocketSphinx
- recognize_wit(): Wit.ai

Para mais informações acesse: https://realpython.com/python-speech-recognition/

# audioTranscriptionPublic description (ENGLISH)

This project transcribes a WhatsApp audio (.ogg file) to a portuguese language! But, it's important to note that can be changed to another languague as English.

Supported languages: https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti

Settings:
 - Algorithm was validate in Linux Debian 9;
 - Python 2.7.16 and 3.7.3 (both works perfectly)
## Install the dependencies (Copy/Paste in the Terminal):

- $ pip install SpeechRecognition
    - Library for performing speech recognition, with support for several engines and APIs, online and offline.
    - More informations: https://pypi.org/project/SpeechRecognition/
- $ pip install pydub
    - Manipulate audio with an simple and easy high level interface.
    - More informations: https://pypi.org/project/pydub/

## Alternative recognizers 

- recognize_bing(): Microsoft Bing Speech
- recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
- recognize_houndify(): Houndify by SoundHound
- recognize_ibm(): IBM Speech to Text
- recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
- recognize_wit(): Wit.ai

More informations: https://realpython.com/python-speech-recognition/

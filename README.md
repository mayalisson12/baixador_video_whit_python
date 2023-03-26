# 📹 Baixador de vídeos do YouTube 📹⬇️🐍

---

## 📖 Sobre o projeto
Este é um projeto simples que permite ao usuário baixar vídeos do YouTube em .mp4 utilizando Python e Flask.

## 🚀 Como baixar o projeto

1. Clone o repositório para sua máquina local:

<pre class="command">
`git clone https://github.com/mayalisson12/baixador_video_whit_python`
</pre>


2. Certifique-se de ter as bibliotecas necessárias instaladas. No terminal, navegue até a pasta do projeto e execute:

<pre class="command">
`pip install -r requirements.txt`
</pre>

3. Baixe também as bibliotecas Flask e PyTube

<pre class="command">
`pip install pytube flask`
</pre>


## 🛠️ Como executar o projeto

1. No terminal, navegue até a pasta do projeto e execute:

Para iniciar o servidor, abra o Prompt de Comando (Windows) ou o Terminal (Mac/Linux) na pasta raiz do projeto e execute o seguinte comando:
<pre class="command">
`python app.py`
</pre>

Se tudo ocorrer corretamente, você verá a seguinte mensagem:
<pre class="command">
`Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
</pre>

Isso significa que o servidor foi iniciado com sucesso e você pode acessá-lo através do endereço `http://127.0.0.1:5000/` em seu navegador.


2. Acesse a página em seu navegador através do seguinte endereço:

    http://127.0.0.1:5000/


3. Cole o link do vídeo do YouTube na caixa de texto e clique no botão "Baixar".

4. O arquivo de vídeo será baixado automaticamente no navegador.

## 🖋️ Observações

- Certifique-se de ter instalado o Python em sua máquina.

- Este projeto utiliza a biblioteca Flask, portanto, é necessário tê-la instalada.

- Caso deseje personalizar a pasta de download do vídeo, altere a variável `DOWNLOAD_FOLDER` no arquivo `app.py`.

## 🙋 Como contribuir

1. Clone o repositório
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona uma nova feature'`)
4. Push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request


Feito com ❤️ e desenvolvido no Visual Studio Code.


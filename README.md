
Instalando o Express:
Abra o terminal na pasta raiz do seu projeto.
Execute o seguinte comando para instalar o Express e salvar as dependências no arquivo package.json:
npm install express --save

Baixando o Nodemon:
O Nodemon é uma ferramenta que permite salvar alterações no código sem precisar parar e reiniciar o servidor manualmente.
Instale o Nodemon como dependência de desenvolvimento com o seguinte comando:
npm install nodemon -D

Autenticando o Banco de Dados no server.js:
Copie o link de conexão do seu banco MongoDB (por exemplo, mongodb+srv://...).
Cole o link no arquivo server.js para autenticar a conexão com o banco.
Rodando o Servidor da Aplicação Flask:
Abra o arquivo app.py.
No terminal, execute o seguinte comando para rodar o servidor Flask:
python app.py

Rodando o Servidor Node.js:
Entre na pasta onde está o arquivo server.js.
No terminal, execute o seguinte comando para rodar o servidor Node.js com Nodemon:
npm run dev

Parando o Servidor:
Para parar o servidor, pressione Ctrl + C no terminal.
Endereço da Página de Login:
Acesse a página de login no navegador usando o endereço:
http://localhost:7171/pag_login.html

Testando o Login no Insomnia:
Use o método POST e o endereço http://localhost:7171/api/entrar para testar se o login existe no banco MongoDB.

from flask import Flask, request, render_template,redirect, url_for
import sqlite3 
import base64

app = Flask(__name__, static_folder='static' )

#conectar com banco de dados
def get_db_connection():
    conn = sqlite3.connect('database/sqlite.db')
    conn.row_factory = sqlite3.Row
    return conn

#login para administrador
@app.route("/login")
def admin_panel():
    return render_template('admin2/login.html')

#rota para contato
@app.route("/contato", methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        if nome:
            conn = get_db_connection()
            conn.execute('INSERT INTO contatos(nome, email, mensagem) VALUES (?,?,?)',
                         (nome,email,mensagem))
            conn.commit()
            conn.close()

            return redirect (url_for('contato'))
        
    return render_template('contato.html')

#rota para listar contato
@app.route("/admin/listar_contatos")
def listar_contatos():
    conn = get_db_connection()
    contatos = conn.execute('SELECT * FROM contatos').fetchall()
    conn.close()

    return render_template('admin2/listar_contatos.html', contatos=contatos)

#rota para excluir contato
@app.route("/admin/excluir_contato/<int:id>", methods=['GET', 'POST'])
def excluir_contato(id):
    conn = get_db_connection()
    contatos = conn.execute('SELECT * FROM contatos WHERE id=?',(id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM contatos WHERE id=?',(id,))
        conn.commit()
        conn.close()

        return redirect(url_for('listar_contatos'))
    
    conn.close()
    return render_template('admin2/excluir_contato.html', contatos=contatos)

#rota da galeria de livros
@app.route("/galeria")
def galeria():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.commit()
    conn.close()

    return render_template('galeria.html', categorias=categorias, livros=livros)

#rota para comprar
@app.route("/comprar")
def comprar():
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    conn.commit()
    conn.close()

    return render_template('comprar.html', categorias=categorias, livros=livros)    


#painel de controle
@app.route("/admin/painel")
def admin():
    return render_template('admin2/painel.html')

#rota Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template('admin2/painel.html')

#rota listar categorias
@app.route("/admin/listar_categorias")
def listar_categorias():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    conn.close()
    return render_template('admin2/listar_categorias.html', categorias=categorias)

#criar rota cadastrar categorias
@app.route("/admin/cadastrar_categoria", methods=['GET', 'POST'])
def cadastrar_categoria():
    if request.method == 'POST':
        nome_categoria = request.form.get('nome_categoria')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')

        if nome_categoria:
            conn = get_db_connection()

            if imagem:
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
                conn.execute('INSERT INTO categorias (nome, descricao, imagem) VALUES(?,?,?)',
                             (nome_categoria, descricao, imagem_base64))
                
            else:
                conn.execute('INSERT INTO categorias (nome, descricao) VALUES (?,?)',
                             (nome_categoria,descricao))

            conn.commit()
            conn.close()
            return redirect(url_for('listar_categorias')) 

    return render_template('admin2/cadastrar_categoria.html')

#rota para editar categória
@app.route("/admin/editar_categoria/<int:id>", methods=['GET', 'POST'])
def editar_categoria(id):
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        nome_categoria = request.form.get('nome_categoria')
        descricao = request.form.get('descricao')
        imagem = request.files.get('imagem')
        
        if imagem:
            imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
            conn.execute('UPDATE categorias SET nome=?, descricao=?, imagem=? WHERE id=?', 
                         (nome_categoria, descricao, imagem_base64,id,))
            conn.commit()
            conn.close()
            return redirect(url_for('listar_categorias'))
    
    conn.close()
    return render_template('/admin2/editar_categoria.html', categorias=categorias)

# Rota para excluir categoria
@app.route("/admin/excluir_categoria/<int:id>", methods=['GET', 'POST'])
def excluir_categoria(id):
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias WHERE id = ?',(id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM categorias WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_categorias'))
    conn.close()
    return render_template('/admin2/excluir_categoria.html', categorias=categorias) 

# Rotas listar Livros
@app.route("/admin/listar_livros")
def listar_livros():
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return render_template('admin2/listar_livros.html', livros=livros)       

# Rota para cadastrar Livros
@app.route("/admin/cadastrar_livro", methods = ['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        nome_livros = request.form.get('nome_livros')
        descricao = request.form.get('descricao')
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        imagem = request.files.get('imagem')  # Obtém o arquivo de imagem enviado
        categoria_id = int(request.form.get('categoria_id'))
        if cadastrar_livro:
            conn = get_db_connection()

            if imagem:  # Se uma imagem foi enviada
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
                conn.execute('INSERT INTO livros (nome, descricao, preco, quantidade, imagem, categoria_id) VALUES (?, ?, ?, ?, ? ,?)',
                             (nome_livros, descricao, preco, quantidade, imagem_base64, categoria_id,))
            else:
                conn.execute('INSERT INTO livros (nome, descricao, preco, quantidade, categoria_id) VALUES (?, ?, ?, ?, ?)',
                             (nome_livros, descricao, preco, quantidade ,categoria_id))

            conn.commit()
            conn.close()
            return redirect(url_for('listar_livros'))
    return render_template('admin2/cadastrar_livro.html')   


@app.route("/admin/editar_livros/<int:id>", methods=['GET', 'POST'])
def editar_livros(id):
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        nome_livros = request.form.get('nome_livros')
        descricao = request.form.get('descricao')
        quantidade = request.form.get('quantidade')
        preco = request.form.get('preco')
        imagem = request.files.get('imagem') # Obtém o arquivo de imagem enviado
        categoria_id = request.form.get('categoria_id') 
        if nome_livros:
            conn = get_db_connection()

            if imagem:  # Se uma imagem foi enviada
                imagem_base64 = base64.b64encode(imagem.read()).decode('utf-8')
              
                conn.execute('UPDATE livros SET nome=?, descricao=?, quantidade=?, preco=?, imagem=?,categoria_id=? WHERE id=?', 
                         (nome_livros, descricao, quantidade, preco, imagem_base64, categoria_id, id,))
            conn.commit()
            conn.close()
            return redirect(url_for('listar_livros'))
        
    conn.close()    
    return render_template('/admin2/editar_livros.html',livros=livros)    

# Rota para excluir livros
@app.route("/admin/excluir_livros/<int:id>", methods=['GET', 'POST'])
def excluir_livros(id):
    conn = get_db_connection()
    livros = conn.execute('SELECT * FROM livros WHERE id = ?',(id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM livros WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_livros'))
    conn.close()
    return render_template('/admin2/excluir_livros.html', livros=livros)

#Rota pra lista os livros pelo id
@app.route("/listar/<int:id>", methods=['GET'])
def listar(id):
    conn = get_db_connection()
    livros = conn.execute( 'SELECT * FROM livros WHERE categoria_id=?', (id,)).fetchall()
    conn.commit()
    conn.close()
    return render_template('listar.html',livros=livros)

#rota index 
@app.route("/")
def index():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    livros = conn.execute('SELECT * FROM livros').fetchall()
    conn.commit()
    conn.close()
    return render_template('index.html', categorias=categorias, livros=livros)


app.run(debug=True)
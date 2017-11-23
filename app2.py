import sqlite3

DB="pessoa.sqlite"
app = flask.Flask("chimacode")
@app.route('/users', methods=["get"])
def busca_usuarios():
	usuario = select_all()
	return flsk.jsoninfy(usuarios)
	
	

def select_all():
	conn = sqlite3.connect(DB)
	severino = coon.cursor()
	
	query = "SELECT * FROM usuario"
	
	resultado = severino.execute(query)
	
	usuarios = resultado.fetchall()
	print(usuarios)
	
	return usuarios
	
	conn.close()
	
if __name__ == "__main__":
	app.run(debug=True)
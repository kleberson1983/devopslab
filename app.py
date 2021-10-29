from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

@app.route('/bug')                                                                                                                               def bad():                                                                                                                                           try:                                                                                                                                        
        raise TypeError()                                                                                                                            except TypeError as e:                                                                                                                               print(e)                        
    except TypeError as e:
        print("Duplicado, ou seja, nunca vai entrar aqui.")

@app.route("/soma")
def soma_valores():
    x=10+10
    return "Sua soma de 10+10="+str(x)

if __name__ == '__main__':
    app.run()

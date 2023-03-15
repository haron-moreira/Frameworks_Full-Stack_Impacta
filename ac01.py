from flask import Flask, request
app = Flask(__name__)


class tipo_de_nota_except(Exception):
    pass


@app.route('/', methods=['POST'])
def main():
    try:
        notas = request.json

        if 'nota_1' not in notas:
            return "Parâmetros Faltantes: nota_1", 400
        
        if 'nota_2' not in notas:
            return "Parâmetros Faltantes: nota_2", 400
        
        if (type(notas['nota_1']) is not int):
            if (type(notas['nota_1']) is not float):
                nota = "nota_1"
                tipo = type(notas['nota_1'])
                raise tipo_de_nota_except
                
        if (type(notas['nota_2']) is not int):
            if (type(notas['nota_2']) is not float):
                nota = "nota_2"
                tipo = type(notas['nota_2'])
                raise tipo_de_nota_except 
        
        media = (notas['nota_1'] + notas['nota_2']) / 2
        return f"{media}", 200
    
    except tipo_de_nota_except:
        return f"O tipo da {nota} precisa ser um número, está como {tipo}", 400
    
    except Exception as e:
        return "Algo deu errado na solicitação.", 500
    

if __name__ == "__main__":
    app.run(host = 'localhost', port = 9000, debug = True)

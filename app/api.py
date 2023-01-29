from flask import Flask, request, jsonify
from viacep import ViaCepException
from models.location import CepLocation, Location, UniqueCepLocationError, UFCepLocationError
from models.location import *

app = Flask(__name__)


@app.route("/api/cep", methods=["POST"])
def cep():
    location = CepLocation()
    cep = request.form["cep"]
    try:
        new_cep = Location(cep)
        location.save(new_cep)
        return jsonify({"success": True, "message": "Cep cadastrado com sucesso."}), 200
    except ViaCepException as e:
        return jsonify({"success": False, "message": "Erro ao consultar cep."}), 500
    except UniqueCepLocationError as e:
        return jsonify({"success": False, "message": "Cep já Cadastrado."}), 406


@app.route("/api/localidades", methods=["GET"])
def localidades():
    location = CepLocation()
    uf = request.args.get("uf")
    try:
        data = location.list(uf=uf)
    except UFCepLocationError as e:
        return jsonify({"success": False, "message": "UF inválida."}), 400
    return (
        jsonify(
            {
                "success": True,
                "message": "Dados recuperados com sucesso.",
                "localidades": data,
            }
        ),
        200,
    )

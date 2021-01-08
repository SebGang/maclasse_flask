from flask import jsonify, make_response, request

from maclasse import app, db
from maclasse.models import Eleve, EleveSchema

eleve_schema = EleveSchema()
eleves_schema = EleveSchema(many=True)


@app.route("/api/eleves", methods=["GET"])
def get_eleves():
    eleves = Eleve.query.order_by("nom").all()
    result = eleves_schema.dump(eleves)

    return make_response(jsonify(result), 200)


@app.route("/api/eleves/<string:nom_eleve>", methods=["GET"])
def filter_eleve(nom_eleve):
    eleves = Eleve.query.filter_by(nom=nom_eleve).all()
    result = eleves_schema.dump(eleves)

    return make_response(jsonify(result), 200)


@app.route("/api/eleves", methods=["POST"])
def post_eleve():
    nom = request.json["nom"]
    prenom = request.json["prenom"]
    date_naissance = request.json["date_naissance"]
    note_trimestre_1 = request.json["note_trimestre_1"]
    note_trimestre_2 = request.json["note_trimestre_2"]
    note_trimestre_3 = request.json["note_trimestre_3"]

    new_eleve = Eleve(
        nom,
        prenom,
        date_naissance,
        note_trimestre_1,
        note_trimestre_2,
        note_trimestre_3,
    )
    db.session.add(new_eleve)
    db.session.commit()

    return make_response(eleve_schema.jsonify(new_eleve), 200)


@app.route("/api/eleves/<int:id_eleve>", methods=["GET"])
def get_eleve(id_eleve):
    eleve = Eleve.query.get(id_eleve)

    return make_response(eleve_schema.jsonify(eleve), 200)


@app.route("/api/eleves/<int:id_eleve>", methods=["PUT"])
def update_eleve(id_eleve):
    eleve = Eleve.query.get(id_eleve)
    nom = request.json["nom"]
    prenom = request.json["prenom"]
    date_naissance = request.json["date_naissance"]
    note_trimestre_1 = request.json["note_trimestre_1"]
    note_trimestre_2 = request.json["note_trimestre_2"]
    note_trimestre_3 = request.json["note_trimestre_3"]

    eleve.nom = nom
    eleve.prenom = prenom
    eleve.date_naissance = date_naissance
    eleve.note_trimestre_1 = note_trimestre_1
    eleve.note_trimestre_2 = note_trimestre_2
    eleve.note_trimestre_3 = note_trimestre_3

    db.session.commit()

    return make_response(eleve_schema.jsonify(eleve), 200)


@app.route("/api/eleves/<int:id_eleve>", methods=["DELETE"])
def delete_eleve(id_eleve):
    eleve = Eleve.query.get(id_eleve)

    db.session.delete(eleve)
    db.session.commit()

    return make_response(eleve_schema.jsonify(eleve), 200)

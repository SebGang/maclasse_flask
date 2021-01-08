from statistics import mean

from maclasse import db, ma


class Eleve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    note_trimestre_1 = db.Column(db.Float, nullable=True)
    note_trimestre_2 = db.Column(db.Float, nullable=True)
    note_trimestre_3 = db.Column(db.Float, nullable=True)

    def __init__(
        self,
        nom,
        prenom,
        date_naissance,
        note_trimestre_1,
        note_trimestre_2,
        note_trimestre_3,
    ):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.note_trimestre_1 = note_trimestre_1
        self.note_trimestre_2 = note_trimestre_2
        self.note_trimestre_3 = note_trimestre_3

    def __repr__(self):
        return (
            f"Eleve ('{self.nom}', '{self.prenom}', '{self.date_naissance}'), "
            f"Moyenne : {mean([self.note_trimestre_1, self.note_trimestre_2, self.note_trimestre_3])}"
        )


class EleveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Eleve

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("get_eleve", values=dict(id_eleve="<id>")),
            "collection": ma.URLFor("get_eleves"),
        }
    )

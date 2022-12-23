from flask import Flask
from flask_cors import CORS
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import aliased
import os

class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db/ecocalor.db")}'
db = SQLAlchemy(app)

with app.app_context():
    print("Creating database...")
    db.Model.metadata.reflect(db.engine)

    #class Client(db.Model):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing': True}
    ID_CLIENT = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class Tbl(db.Model):
    __tablename__ = 'tbl'
    __table_args__ = {'extend_existing': True}
    IDTable = db.Column(db.Integer, primary_key=True)
    TypeTable = db.Column(db.Integer)
    Description = db.Column(db.String(50), nullable=True)
    Valeur = db.Column(db.Integer)

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class Client(db.Model):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing': True}
    IDClient = db.Column(db.Integer, primary_key=True)
    CodeAdr = db.Column(db.Integer) # IDTable
    NumRue = db.Column(db.Integer)
    ExtNoRue = db.Column(db.String(10), nullable=True)
    CodePostal = db.Column(db.Integer) # IDTable
    Email = db.Column(db.String(50), nullable=True)
    EmailFacturation = db.Column(db.String(50), nullable=True)
    Civilite = db.Column(db.Integer) # IDTable
    CodeTVa = db.Column(db.Integer) # IDTable
    SousTraitance = db.Column(db.Integer)
    RappelPapier = db.Column(db.Integer)

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class Appareil(db.Model):
    __tablename__ = 'appareil'
    __table_args__ = {'extend_existing': True}
    IDAppareil = db.Column(db.Integer, primary_key=True)
    IDAdrInstal = db.Column(db.Integer, db.ForeignKey('adrInstall.IDAdrInstal'))
    Marque = db.Column(db.String(50))
    Modele = db.Column(db.String(50), nullable=True)
    DateMES = db.Column(db.String(50), nullable=True)
    KW = db.Column(db.Integer)
    Combustible = db.Column(db.Integer) # IDTable
    DateInterrvention = db.Column(db.Integer, nullable=True)
    TypeAppareil = db.Column(db.Integer) # IDTable

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class AdrInstall(db.Model):
    __tablename__ = 'adrInstall'
    __table_args__ = {'extend_existing': True}
    IDAdrInstal = db.Column(db.Integer, primary_key=True)
    IDClient = db.Column(db.Integer, db.ForeignKey('client.IDClient'))
    CodeAdr = db.Column(db.Integer) # IDTable
    NumRue1 = db.Column(db.Integer)
    NumRue2 = db.Column(db.Integer)
    ExtNoRue = db.Column(db.String(10), nullable=True)
    CodeCommune = db.Column(db.Integer) # IDTable
    GPS = db.Column(db.String(50), nullable=True)

    def serialize(self):
        c = Serializer.serialize(self)
        return c
        
class Article(db.Model):
    __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}
    IDArticle = db.Column(db.Integer, primary_key=True)
    IDFournisseur = db.Column(db.String(50)) 
    Marque = db.Column(db.String(50)) # IDTable
    designation = db.Column(db.String(50))
    prixVente = db.Column(db.Float)
    prixAchat = db.Column(db.Float)
    rabaisMax = db.Column(db.Integer)

    def serialize(self):
        c = Serializer.serialize(self)
        return c
        
class Fourniture(db.Model):
    __tablename__ = 'fourniture'
    __table_args__ = {'extend_existing': True}
    IDFournitures = db.Column(db.Integer, primary_key=True)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    Quantite = db.Column(db.Integer)
    IDArticle = db.Column(db.Integer, db.ForeignKey('article.IDArticle'))

    def serialize(self):
        c = Serializer.serialize(self)
        return c
        
class Intervention(db.Model):
    __tablename__ = 'intervention'
    __table_args__ = {'extend_existing': True}
    IDInterventions = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Integer)
    HeureArrivee = db.Column(db.Integer)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    HeureDepart = db.Column(db.Integer)
    SousGarantie = db.Column(db.Integer)

    def serialize(self):
        c = Serializer.serialize(self)
        return c
        
class Prestation(db.Model):
    __tablename__ = 'prestation'
    __table_args__ = {'extend_existing': True}
    IDPrestations = db.Column(db.Integer, primary_key=True)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    IDTable = db.Column(db.Integer, db.ForeignKey('tbl.IDTable'))
    Description = db.Column(db.String(50))
    IDAppareil = db.Column(db.Integer, db.ForeignKey('appareil.IDAppareil'))

    def serialize(self):
        c = Serializer.serialize(self)
        return c
        
class RapTravail(db.Model):
    __tablename__ = 'rapTravail'
    __table_args__ = {'extend_existing': True}
    IDRapTravail = db.Column(db.Integer, primary_key=True)
    DateDebutIntervention = db.Column(db.Integer)
    DateFinIntervention = db.Column(db.Integer)
    Description = db.Column(db.String(50), nullable=True)
    Status = db.Column(db.Integer)
    AFacturer = db.Column(db.Integer)
    IDClient = db.Column(db.Integer)

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class Contrat(db.Model):
    __tablename__ = 'contrat'
    __table_args__ = {'extend_existing': True}
    IDContrat = db.Column(db.Integer, primary_key=True)
    IDClient = db.Column(db.Integer, db.ForeignKey('client.IDClient'))
    IDAppareil = db.Column(db.Integer, db.ForeignKey('appareil.IDAppareil'))
    ObjetContrat = db.Column(db.String(50))
    Actif = db.Column(db.Integer)
    DateOffre = db.Column(db.Integer)
    DateDebutContat = db.Column(db.Integer)
    DateResiliation = db.Column(db.Integer)
    DateService = db.Column(db.Integer)
    PeriodiciteFacture = db.Column(db.Integer)
    Montant = db.Column(db.Float)

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class Facture(db.Model):
    __tablename__ = 'facture'
    __table_args__ = {'extend_existing': True}
    IDFactures = db.Column(db.Integer, primary_key=True)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    IDAdrInstal = db.Column(db.Integer, db.ForeignKey('adresse.IDAdr'))
    TexteEntete = db.Column(db.String(50))
    DateImpression = db.Column(db.Integer)
    DateComptabilisation = db.Column(db.Integer)
    Dateecheance = db.Column(db.Integer)
    Status = db.Column(db.Integer)
    SoldeaPayer = db.Column(db.Float)
    TotalHT = db.Column(db.Float)
    Taxes = db.Column(db.Float)
    TotalTTC = db.Column(db.Float)
    IDProprio = db.Column(db.Integer, db.ForeignKey('client.IDClient'))
    IDClient = db.Column(db.Integer, db.ForeignKey('client.IDClient'))

    def serialize(self):
        c = Serializer.serialize(self)
        return c

class LigneFacture(db.Model):
    __tablename__ = 'ligneFacture'
    __table_args__ = {'extend_existing': True}
    IDLignesFacture = db.Column(db.Integer, primary_key=True)
    IDFactures = db.Column(db.Integer, db.ForeignKey('facture.IDFactures'))
    IDAppareil = db.Column(db.Integer, db.ForeignKey('appareil.IDAppareil'))
    Description = db.Column(db.String(50))
    Date = db.Column(db.Integer)
    Prix_U = db.Column(db.Float)
    Quantite = db.Column(db.Float)
    MontantTVA = db.Column(db.Float)
    Montant = db.Column(db.Float)
    Type = db.Column(db.String(10))

    def serialize(self):
        c = Serializer.serialize(self)
        return c



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/rapports')
def all_rapports():
    res = RapTravail.query.filter(RapTravail.Status == 3).all()
    # For each rapport, get the associated prestations and if one contains "Service" in the description mark the rapport as "Maintenance" in a new column
    interventionType = {}
    for r in res:
        prestations = Prestation.query.filter(Prestation.IDRapport == r.IDRapTravail).all()
        for p in prestations:
            # If one of the prestations contains "Service" in the description, mark the rapport as "Maintenance"
            if "Service selon" in p.Description:
                interventionType[r.IDRapTravail] = "Maintenance"
                break
            else:
                interventionType[r.IDRapTravail] = "Troubleshooting"
                            
    json_res = [r.serialize() for r in res]
    for j in json_res:
        j['InterventionType'] = interventionType[j['IDRapTravail']] if j['IDRapTravail'] in interventionType else "Troubleshooting"
    return json.dumps(json_res)

@app.route('/interventions')
def all_interventions():
    # Keep only interventions with associated rapport that status is 3 (closed)
    res = Intervention.query.join(RapTravail, Intervention.IDRapport == RapTravail.IDRapTravail).filter(RapTravail.Status == 3).all()
    return json.dumps([r.serialize() for r in res])

@app.route('/prestations')
def all_prestations():
    # Keep only prestations with associated rapport that status is 3 (closed)
    res = Prestation.query.join(RapTravail, Prestation.IDRapport == RapTravail.IDRapTravail).filter(RapTravail.Status == 3).all()
    return json.dumps([r.serialize() for r in res])

@app.route('/fournitures')
def all_fournitures():
    # Keep only fournitures with associated rapport that status is 3 (closed)
    # Join article table to get article marque and designation
    res = (
        Fourniture.query
        .join(RapTravail, Fourniture.IDRapport == RapTravail.IDRapTravail)
        .join(Article, Fourniture.IDArticle == Article.IDArticle)
        .filter(RapTravail.Status == 3)
        .with_entities(Fourniture, Article.Marque, Article.designation)
    )
    return json.dumps([dict(r[0].serialize(), **{'Marque': r.Marque, 'designation': r.designation}) for r in res])

@app.route('/installations')
def all_installations():
    tbl_alias1 = aliased(Tbl)
    tbl_alias2 = aliased(Tbl)
    res = (
            AdrInstall.query
           .join(tbl_alias1, AdrInstall.CodeAdr == tbl_alias1.IDTable)
           .join(tbl_alias2, AdrInstall.CodeCommune == tbl_alias2.IDTable)
           .filter(AdrInstall.GPS != "").filter(AdrInstall.GPS != "46;6")
           .with_entities(AdrInstall, tbl_alias1.Description.label('CodeAdr')
                          ,tbl_alias2.Description.label('CodeCommune')).all()
        )

    return json.dumps([dict(r[0].serialize(), **{'CodeAdr': r.CodeAdr, 'CodeCommune': r.CodeCommune}) for r in res])

@app.route('/appareils')
def all_appareils():
    tbl_alias1 = aliased(Tbl)
    tbl_alias2 = aliased(Tbl)
    res = (
            Appareil.query
           .join(tbl_alias1, Appareil.Marque == tbl_alias1.IDTable)
           .join(tbl_alias2, Appareil.Combustible == tbl_alias2.IDTable)
           .with_entities(Appareil, tbl_alias1.Description.label('Marque')
                          ,tbl_alias2.Description.label('Combustible')).all()
        )

    return json.dumps([dict(r[0].serialize(), **{'Marque': r.Marque, 'Combustible': r.Combustible}) for r in res])

@app.route('/contrats')
def all_contrats():
    res = Contrat.query.with_entities(Contrat).all()
    return json.dumps([r.serialize() for r in res])  
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
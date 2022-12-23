class Client(db.Model):
    IDClient = db.Column(db.Integer, primary_key=True)
    CodeAdr = db.Column(db.Integer)
    NumRue = db.Column(db.Integer)
    ExtNoRue = db.Column(db.String(10))
    CodePostal = db.Column(db.Integer)
    Email = db.Column(db.String(50))
    EmailFacturation = db.Column(db.String(50))
    Civilite = db.Column(db.Integer)
    CodeTVa = db.Column(db.Integer)
    SousTraitance = db.Column(db.Integer)
    RappelPapier = db.Column(db.Integer)

class Appareil(db.Model):
    IDAppareil = db.Column(db.Integer, primary_key=True)
    IDAdrInstal = db.Column(db.Integer, db.ForeignKey('adrInstall.IDAdrInstal'))
    Marque = db.Column(db.String(50))
    Modele = db.Column(db.String(50))
    DateMES = db.Column(db.String(50))
    KW = db.Column(db.Integer)
    Combustible = db.Column(db.Integer)
    DateInterrvention = db.Column(db.Integer)
    TypeAppareil = db.Column(db.Integer)

class AdrInstall(db.Model):
    IDAdrInstal = db.Column(db.Integer, primary_key=True)
    IDClient = db.Column(db.Integer, db.ForeignKey('client.IDClient'))
    CodeAdr = db.Column(db.Integer)
    NumRue1 = db.Column(db.Integer)
    NumRue2 = db.Column(db.Integer)
    ExtNoRue = db.Column(db.String(10))
    CodeCommune = db.Column(db.String(10))
    GPS = db.Column(db.String(50))

class Article(db.Model):
    IDArticle = db.Column(db.Integer, primary_key=True)
    IDFournisseur = db.Column(db.String(50))
    Marque = db.Column(db.String(50))
    designation = db.Column(db.String(50))
    prixVente = db.Column(db.Float)
    prixAchat = db.Column(db.Float)
    rabaisMax = db.Column(db.Integer)

class Fourniture(db.Model):
    IDFournitures = db.Column(db.Integer, primary_key=True)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    Quantite = db.Column(db.Integer)
    IDArticle = db.Column(db.Integer, db.ForeignKey('article.IDArticle'))

class Intervention(db.Model):
    IDInterventions = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Integer)
    HeureArrivee = db.Column(db.Integer)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    HeureDepart = db.Column(db.Integer)
    SousGarantie = db.Column(db.Integer)

class Prestation(db.Model):
    IDPrestations = db.Column(db.Integer, primary_key=True)
    IDRapport = db.Column(db.Integer, db.ForeignKey('rapTravail.IDRapTravail'))
    IDTable = db.Column(db.Integer, db.ForeignKey('tbl.IDTable'))
    Description = db.Column(db.String(50))
    IDAppareil = db.Column(db.Integer, db.ForeignKey('appareil.IDAppareil'))

class RapTravail(db.Model):
    IDRapTravail = db.Column(db.Integer, primary_key=True)
    DateDebutIntervention = db.Column(db.Integer)
    DateFinIntervention = db.Column(db.Integer)
    Description = db.Column(db.String(50))
    Status = db.Column(db.Integer)
    AFacturer = db.Column(db.Integer)
    IDClient = db.Column(db.Integer)

class Tbl(db.Model):
    IDTable = db.Column(db.Integer, primary_key=True)
    TypeTable = db.Column(db.Integer)
    Description = db.Column(db.String(50))
    Valeur = db.Column(db.Integer)

class ClientSchema(ma.Schema):
    class Meta:
        model: Client

    IDClient = ma.auto_field()
    CodeAdr = ma.auto_field()
    NumRue = ma.auto_field()
    ExtNoRue = ma.auto_field()
    CodePostal = ma.auto_field()
    Email = ma.auto_field()
    EmailFacturation = ma.auto_field()
    Civilite = ma.auto_field()
    CodeTVa = ma.auto_field()
    SousTraitance = ma.auto_field()
    RappelPapier = ma.auto_field()

class AppareilSchema(ma.Schema):
    class Meta:
        model: Appareil
        include_fk = True

    IDAppareil = ma.auto_field()
    IDAdrInstal = ma.auto_field()
    Marque = ma.auto_field()
    Modele = ma.auto_field()
    DateMES = ma.auto_field()
    KW = ma.auto_field()
    Combustible = ma.auto_field()
    DateInterrvention = ma.auto_field()
    TypeAppareil = ma.auto_field()

class AdrInstallSchema(ma.Schema):

    class Meta:
        model: AdrInstall
        include_fk = True

    IDAdrInstal = ma.auto_field()
    IDClient = ma.auto_field()
    CodeAdr = ma.auto_field()
    NumRue1 = ma.auto_field()
    NumRue2 = ma.auto_field()
    ExtNoRue = ma.auto_field()
    CodeCommune = ma.auto_field()
    GPS = ma.auto_field()

class ArticleSchema(ma.Schema):
    class Meta:
        model: Article

    IDArticle = ma.auto_field()
    IDFournisseur = ma.auto_field()
    Marque = ma.auto_field()
    designation = ma.auto_field()
    prixVente = ma.auto_field()
    prixAchat = ma.auto_field()
    rabaisMax = ma.auto_field()

class FournitureSchema(ma.Schema):
    class Meta:
        model: Fourniture
        include_fk = True

    IDFournitures = ma.auto_field()
    IDRapport = ma.auto_field()
    Quantite = ma.auto_field()
    IDArticle = ma.auto_field()

class InterventionSchema(ma.Schema):
    class Meta:
        model: Intervention
        include_fk = True

    IDInterventions = ma.auto_field()
    Date = ma.auto_field()
    HeureArrivee = ma.auto_field()
    IDRapport = ma.auto_field()
    HeureDepart = ma.auto_field()
    SousGarantie = ma.auto_field()

class PrestationSchema(ma.Schema):
    class Meta:
        model: Prestation
        include_fk = True

    IDPrestations = ma.auto_field()
    IDRapport = ma.auto_field()
    IDTable = ma.auto_field()
    Description = ma.auto_field()
    IDAppareil = ma.auto_field()

class RapTravailSchema(ma.Schema):
    class Meta:
        model: RapTravail

    IDRapTravail = ma.auto_field()
    DateDebutIntervention = ma.auto_field()
    DateFinIntervention = ma.auto_field()
    Description = ma.auto_field()
    Status = ma.auto_field()
    AFacturer = ma.auto_field()
    IDClient = ma.auto_field()

class TblSchema(ma.Schema):
    class Meta:
        model: Tbl

    IDTable = ma.auto_field()
    TypeTable = ma.auto_field()
    Description = ma.auto_field()
    Valeur = ma.auto_field()

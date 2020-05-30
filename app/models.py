from app import db

class User(db.Model):
    """Database table for a user. Implemented with flask-SQLalchemy. 

    :param name: Name of student
    :type name: String, maximum size 64
    :param nus_net_id: NUSnet ID of the student, the EXXXXXXX number
    :type nus_net_id: String, maximum size 8
    """
    __tablename__ = 'users'
    #database id
    id = db.Column(db.Integer, primary_key=True)
    #name of user, not unique as people may have same names
    name = db.Column(db.String(64), index=True, unique=False)
    #NUSNET ID, the EXXXXXXX number
    nus_net_id = db.Column(db.String, index=True, unique=True)
    mods = db.relationship('user_mods', backref='student_taking')

    def __repr__(self):
        return "<User {}, {}, {}>".format(self.name, self.nus_net_id, self.id)

class User_Mods(db.Model):
    """Represents mods taken by a user in the database. 

    :param code: Module code of the mod, i.e. CS2030, UTW1001R
    :type code: String, maximum size 8
    :param mod_id: Module id used by luminus
    :type mod_id: String, maximum size 64
    :param name: Name of the module
    :type name: String, maximum size 30
    :param class_grp: Class group of the student taking this module, defaults to T0 for now #TODO#
    :type class_grp: String, maximum size 6
    :param term: The semester which this module is taken in
    :type term: String, maximum size 6
    :param student: NUSnet ID of the student taking this module
    :type student: String, maximum size 8

    """
    __tablename__ = 'user_mods'
    id = db.Column(db.Integer, index=True, primary_key=True)
    code = db.Column(db.String(8), index=True, unique=False)
    mod_id = db.Column(db.String(64), index=True, unique=False)
    name = db.Column(db.String(30))
    class_grp = db.Column(db.String(6), index=True, unique=False, default="T0")
    term = db.Column(db.String(6), index=True, unique=False)
    student = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Mod {} taken by {}>".format(self.code, self.student)
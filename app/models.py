from app import db

class DomainIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), unique=True, nullable=False)
    ip_addresses = db.Column(db.String(255), nullable=False)
    ipv6_addresses = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f"<DomainIP {self.domain}>"

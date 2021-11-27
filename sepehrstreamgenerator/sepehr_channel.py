class SepehrChannel:
    def __init__(self, id, uid, name, type, icon, stream_url):
        self.id = id
        self.uid = uid
        self.name = name
        self.type = type
        self.icon = icon
        self.stream_url = stream_url

    def __str__(self):
        return f'{self.name} (ID: {self.id}) (UID: {self.uid})'
    
    def __unicode__(self):
        return u'{self.name} (ID: {self.id}) (UID: {self.uid})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.uid == other.uid

    def __hash__(self):
        return hash(self.uid)
    
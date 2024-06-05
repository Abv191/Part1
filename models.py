import mongoengine as me

# Підключення до MongoDB
me.connect('Abv191', host='mongodb+srv://Abv191:Abv191@cluster0.hyf0kje.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Модель автора
class Author(me.Document):
    fullname = me.StringField(required=True)
    born_date = me.StringField()
    born_location = me.StringField()
    description = me.StringField()

# Модель цитати
class Quote(me.Document):
    tags = me.ListField(me.StringField())
    author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)
    quote = me.StringField(required=True)

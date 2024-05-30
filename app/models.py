from app import db

class SearchResult(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  url = db.Column(db.String(200), nullable=False)
  snippet = db.Column(db.Text)

  def __repr__(self):
    return f"<SearchResult {self.title}>"


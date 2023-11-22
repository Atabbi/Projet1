"""
Controller de l'application
"""
from flask import Flask, render_template, request, redirect, url_for
from model import ListeTaches

app = Flask(__name__)
list_taches = ListeTaches()

@app.route('/')
def index():
    return render_template('index.html', taches=list_taches.list_taches)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    description = request.form.get('description')
    list_taches.ajouter(description)
    return redirect(url_for('index'))

@app.route('/completer/<int:index>', methods=['GET'])
def completer_tache(index):
# Logic to mark the task as completed
    print(list_taches)
    list_taches.completer(index)
    print(list_taches)
    return redirect(url_for('index'))

@app.route('/supprimer/<int:index>', methods=['GET'])
def supprimer_tache(index):
# Remove the indexed task
    list_taches.supprimer(index)
    return redirect(url_for('index'))

@app.route('/modifier/<int:index>', methods=['GET'])
def modifier_tache(index):
# Remove the indexed task
    list_taches.supprimer(index)
    return redirect(url_for('index'))

"""
    def run(self):
       
        Lancement de l'application
        
        while True:
            option = self.vue.demander_option()
            match option:
                case "4":
                    self.vue.afficher_liste(self.taches)
                    index = int(self.vue.demander_index())
                    description = self.vue.demander_tache()
                    self.taches.modifier(index, description)
                    print("en cours de modification")
                    self.vue.afficher_liste(self.taches
                case "6":
                    break
"""
if __name__ == "__main__":
    app.run(debug=True)
"""
Fichier qui contient les modeles
"""

class Tache:
    """
    representation de la tache
    """
    def __init__(self,description : str):
        self.description = description
        self.est_completee : bool= False

    def completer(self):
        """completer la tache actuelle"""
        self.est_completee = True


    def __str__(self) -> str:
        return f"Tache : {self.description} - Completée : {self.est_completee}"
    
class ListeTaches:
    """Liste contenant les taches"""
    def __init__(self, list_taches : list[Tache] = []):
        """definition du constructeur de la liste de tache"""
        self.list_taches = list_taches
    
    def ajouter(self, description : str):
        """methode qui ajoute une tache a la liste"""
        self.list_taches.append(Tache(description))

    def completer(self, index : int):
        """
        methode qui permet de completer une tache dans notre liste de tache
        test si l'index est bien compris dans la liste et renvoie true si c'est le cas et false sinon
        """
        self.recherche(index).completer()
        
    def recherche(self, index: int) -> Tache:
            """
            Recherche si une tache existe, la retourne
            :param index:
            :return: la tache si elle existe, None sinon
            """
            if 0 <= index < len(self.list_taches):
                return self.list_taches[index]
            else:
                return Tache("")

    def supprimer(self, index : int):
        self.list_taches.remove(self.recherche(index))
        
    def modifier(self,index : int, description : str):
        if 0<= index <= len(self.list_taches):
            self.list_taches[index].description = description
            return True
        else:
            return False
            

    def __str__(self) -> str:
        """affichage de la liste avec l'etat des taches en passant par la fontionc __str__ qui renvoyer un str"""
        chaine = f"voici la liste de taches \n\n"
        for tache in self.list_taches:
            chaine += str(tache) + "\n"
        return chaine


if __name__ == "__main__":
    """Test de la classe Tache"""
    tache1 = Tache("Finir le TP")
    print(tache1)
    tache1.completer()
    print(tache1)


    """Test de la classe ListeTache"""

    # test constructeur
    liste = ListeTaches()
    print(type(liste))

    # test méthode ajouter
    liste.ajouter("Finir TP")
    liste.ajouter("Finir exercice")
    liste.ajouter("Déjeuner")
    liste.ajouter("course")
    liste.ajouter("TODO")
    print(liste)

    # test méthode compléter
    liste.completer(2)
    print(liste.completer(3))
    print(liste.completer(7))
    print(liste)
import streamlit as st


# Fonction saisie matrice
def saisir_matrix(label):
    nbre_lignes = st.number_input(label + " - Nombre de lignes :", min_value=1, step=1, value=1, format="%d")
    nbre_colonnes = st.number_input(label + " - Nombre de colonnes :", min_value=1, step=1, value=1, format="%d")

    matrices = []
    for i in range(nbre_lignes):
        row = []
        for j in range(nbre_colonnes):
            val = st.number_input(f"{label} - Valeur ({i}*{j}):", step=1, format="%d")
            row.append(val)
        matrices.append(row)
    return matrices


# Fonction produit matrices, en paramètre 2 matrices A et B
def Produit_matrix(matriceA, matriceB):
    if len(matriceA[0]) != len(matriceB):
        return None
    else:
        matriceAB = [[0 for _ in range(len(matriceB[0]))] for _ in range(len(matriceA))]
        for i in range(len(matriceA)):
            for j in range(len(matriceB[0])):
                for k in range(len(matriceB)):
                    matriceAB[i][j] += matriceA[i][k] * matriceB[k][j]
        return matriceAB


# Fonction principal
def ProjetDIT():
    st.title("Calcul de matrices")
    option = st.selectbox("Choisissez une option:", ("Calculer le transposé", "Calculer le produit de matrices"))

    if option == "Calculer le transposé":
        st.subheader("Transposée d'une matrice")
        matrice = saisir_matrix("Matrice")
        transpose = [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]
        st.write("Matrice d'entrée:")
        st.table(matrice)
        st.write("Transposée:")
        st.table(transpose)

    elif option == "Calculer le produit de matrices":
        st.subheader("Produit de matrices")
        st.write("Matrice A")
        matriceA = saisir_matrix("Matrice A")
        st.write("Matrice B")
        matriceB = saisir_matrix("Matrice B")
        if len(matriceA[0]) != len(matriceB):
            st.write("Le produit de matrices n'est pas possible.")
        else:
            matriceAB = Produit_matrix(matriceA, matriceB)
            st.write("Résultat du produit:")
            st.table(matriceAB)


# Lancer le programme
if __name__ == "__main__":
    ProjetDIT()

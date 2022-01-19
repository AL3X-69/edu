import matplotlib.pyplot as plt
import scipy.stats as stat

# listes des demi-grands axes a en U.A et périodes des planètes en années
LIST_a = [181, 221, 421, 671, 1070, 1882]
LIST_T = [0.498, 0.674, 1.769, 3.551, 7.155, 16.689]
LIST_P = ['Amalthée', 'Thébé', 'Io', 'Europe',
          'Ganymède', 'Callisto']
# a au cube et T au carré
for i in range(0, len(LIST_a)):
    LIST_a[i] = (LIST_a[i] * 1e6) ** 3
    LIST_T[i] = (LIST_T[i] * 24 * 3600) ** 2
# régression linéaire
regression = stat.linregress(LIST_a, LIST_T)
pente = regression[0]
print('pente--> ' + str(pente))
ordorigine = regression[1]
print('ordonnée à l origine -->  ' + str(ordorigine))
coeffcorel = regression[2]
print('coefficient de corrélation -->' + str(coeffcorel))
# affichage point et droite de regression
a_3_max = LIST_a[len(LIST_a) - 1]
T_2_max = pente * a_3_max + ordorigine
plt.grid(True)
plt.xlabel(' a au cube (m3)')
plt.ylabel('periode au carré (s2)')
plt.scatter(LIST_a, LIST_T, s=100, c='red',
            marker='+')
for i in range(0, len(LIST_a)):
    plt.text(LIST_a[i], LIST_T[i], LIST_P[i], fontsize=8)
plt.plot([0, a_3_max], [ordorigine, T_2_max], c='blue')
plt.show()

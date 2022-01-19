from matplotlib import pyplot as plotlib

Ca = 0.12  # Entrer la valeur Ca de la concentration de l’acide à titrer en mol/L
Va = 10.0  # Entrer le volume Va d’acide titré en mL
V = 25.0  # Entrer le volume de la burette graduée en mL
Cb = 0.36  # Entrer la valeur de la concentration Cb de la base contenue dans la burette graduée en mol/L
N = 50  # nombre de points de la courbe
Vb = []
naf = []
nbf = []
Vbe = 3 * Ca * Va / Cb
for i in range(0, N):
    Vb.append(V * i / N)

    if Vb[i] < Vbe:
        nbf.append(0)
        naf.append(Ca * Va / 1000 - Cb * Vb[i] / 1000)
    else:
        nbf.append(Cb * Vb[i] / 1000 - Ca * Va / 1000)
        naf.append(0)

figure = plotlib.figure()
plt = figure.add_subplot()

plt.set_title("Evolution des quantités d’acide et de base au cours du titrage")
plt.set_xlabel("Volume de base versé Vb(mL)")
plt.set_ylabel("quantités de matière en mol")
plt.grid(True)
plt.plot(Vb, naf, c='red', label="Quantité d’acide présente dans le bécher : na(mol)")
plt.plot(Vb, nbf, c='blue', label="Quantité de base présente dans le bécher : nb(mol)")
plt.legend()
plt.text(0.5, 0.5, r"$C_2H_4O_2 + HO^+ \rightarrow C_2H_3O_2 + H_2O$", fontdict={"size": 18})
plotlib.show()

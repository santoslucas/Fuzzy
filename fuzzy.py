import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

distancia = ctrl.Antecedent(np.arange(0, 75, 1), 'distancia')
velocidade = ctrl.Antecedent(np.arange(0, 100, 1), 'velocidade')
frenagem = ctrl.Consequent(np.arange(0, 100, 1), 'frenagem')

distancia['Muito Perto'] = fuzz.trimf(distancia.universe, [-10, 1, 5])
distancia['Perto'] = fuzz.trimf(distancia.universe, [0, 10, 15])
distancia['Médio'] = fuzz.trimf(distancia.universe, [12, 20, 30])
distancia['Longe'] = fuzz.trimf(distancia.universe, [27, 40, 55])
distancia['Muito Longe'] = fuzz.trimf(distancia.universe, [52, 70, 85])

velocidade['Muito Baixa'] = fuzz.trimf(velocidade.universe, [-20, 0, 10])
velocidade['Baixa'] = fuzz.trimf(velocidade.universe, [8, 20, 25])
velocidade['Média'] = fuzz.trimf(velocidade.universe, [22, 40, 50])
velocidade['Alta'] = fuzz.trimf(velocidade.universe, [45, 60, 80])
velocidade['Muito Alta'] = fuzz.trimf(velocidade.universe, [75, 100, 150])

frenagem['Muito Fraco'] = fuzz.trimf(frenagem.universe, [-20, 0, 10])
frenagem['Fraco'] = fuzz.trimf(frenagem.universe, [8, 20, 25])
frenagem['Moderado'] = fuzz.trimf(frenagem.universe, [23, 50, 60])
frenagem['Forte'] = fuzz.trimf(frenagem.universe, [55, 75, 85])
frenagem['Muito Forte'] = fuzz.trimf(frenagem.universe, [80, 100, 120])

regrasMaxMin = []
regrasMaxMin.append(ctrl.Rule(distancia['Muito Perto'] | velocidade['Muito Baixa'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Perto'] | velocidade['Baixa'], frenagem['Moderado']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Perto'] | velocidade['Média'], frenagem['Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Perto'] | velocidade['Alta'], frenagem['Muito Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Perto'] | velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Perto'] | velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Perto'] | velocidade['Baixa'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Perto'] | velocidade['Média'], frenagem['Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Perto'] | velocidade['Alta'], frenagem['Muito Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Perto'] | velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Médio'] | velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Médio'] | velocidade['Baixa'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Médio'] | velocidade['Média'], frenagem['Moderado']))
regrasMaxMin.append(ctrl.Rule(distancia['Médio'] | velocidade['Alta'], frenagem['Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Médio'] | velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Longe'] | velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Longe'] | velocidade['Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Longe'] | velocidade['Média'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Longe'] | velocidade['Alta'], frenagem['Moderado']))
regrasMaxMin.append(ctrl.Rule(distancia['Longe'] | velocidade['Muito Alta'], frenagem['Forte']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Longe'] | velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Longe'] | velocidade['Baixa'], frenagem['Muito Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Longe'] | velocidade['Média'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Longe'] | velocidade['Alta'], frenagem['Fraco']))
regrasMaxMin.append(ctrl.Rule(distancia['Muito Longe'] | velocidade['Muito Alta'], frenagem['Moderado']))

regrasMaxProd = []
regrasMaxProd.append(ctrl.Rule(distancia['Muito Perto'] & velocidade['Muito Baixa'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Perto'] & velocidade['Baixa'], frenagem['Moderado']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Perto'] & velocidade['Média'], frenagem['Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Perto'] & velocidade['Alta'], frenagem['Muito Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Perto'] & velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Perto'] & velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Perto'] & velocidade['Baixa'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Perto'] & velocidade['Média'], frenagem['Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Perto'] & velocidade['Alta'], frenagem['Muito Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Perto'] & velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Médio'] & velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Médio'] & velocidade['Baixa'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Médio'] & velocidade['Média'], frenagem['Moderado']))
regrasMaxProd.append(ctrl.Rule(distancia['Médio'] & velocidade['Alta'], frenagem['Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Médio'] & velocidade['Muito Alta'], frenagem['Muito Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Longe'] & velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Longe'] & velocidade['Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Longe'] & velocidade['Média'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Longe'] & velocidade['Alta'], frenagem['Moderado']))
regrasMaxProd.append(ctrl.Rule(distancia['Longe'] & velocidade['Muito Alta'], frenagem['Forte']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Longe'] & velocidade['Muito Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Longe'] & velocidade['Baixa'], frenagem['Muito Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Longe'] & velocidade['Média'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Longe'] & velocidade['Alta'], frenagem['Fraco']))
regrasMaxProd.append(ctrl.Rule(distancia['Muito Longe'] & velocidade['Muito Alta'], frenagem['Moderado']))

sistema_ctrl_MAXMIN = ctrl.ControlSystem(regrasMaxMin)
sistema_ctrl_MAXPROD = ctrl.ControlSystem(regrasMaxProd)

sistema_MAXMIN = ctrl.ControlSystemSimulation(sistema_ctrl_MAXMIN)
sistema_MAXPROD = ctrl.ControlSystemSimulation(sistema_ctrl_MAXPROD)

sistema_MAXMIN.input['distancia'] = sistema_MAXPROD.input['distancia'] = int(input("Qual a distância do veículo? "))
sistema_MAXMIN.input['distancia'] = sistema_MAXPROD.input['velocidade'] = int(input("Qual a velocidade do veículo? "))

sistema_MAXMIN.compute()
sistema_MAXPROD.compute()

print("(MAX-MIN) Intensidade de Frenagem:", sistema_MAXMIN.output['frenagem'])
print("(MAX-PROD) Intensidade de Frenagem:", sistema_MAXPROD.output['frenagem'])

distancia.view()
plt.show()

velocidade.view()
plt.show()

frenagem.view()
plt.show()
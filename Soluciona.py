def buscaInformada(num, proibido):
	passos = 0
	agenda = []
	passados = {}
	estado = Estado(num,proibidos,passos)
	agenda.append(estado)
	passados[estado.numero] = estado
	while(len(agenda)>0):
		estado = agenda[0]
		#print("estado: ",estado.numero)
		agenda.remove(estado)
		#print(estado.numero)
		if(estado.numero==0):
			return passos
		agenda = []
		lista_trans = estado.transicoes()
		#print(lista_trans)
		for est in lista_trans:
			proximo = Estado(est,proibidos,estado.g+1)
			if proximo.numero not in passados:
				agenda.append(proximo)
				passados[proximo.numero] = proximo
				montar_heap(agenda,len(agenda))
			elif proximo.g < passados[proximo.numero].g:
				passados[proximo.numero].g = proximo.g
				passados[proximo.numero].f = proximo.g + passados[proximo.numero].h
				montar_heap(agenda,len(agenda))
		passos += 1
		#print("agenda: ",agenda)
	return -1

def montar_heap(vet,tam):
	ultimo = (tam//2)-1
	for i in range(ultimo,-1,-1):
		min_heapify(vet,i,tam)

def min_heapify(vetor,raiz,tam):
	menor = raiz
	esq = 2 * raiz + 1
	if(esq < tam and vetor[esq]<vetor[menor]):
		menor = esq
	dire = 2 * raiz + 2
	if(dire < tam and vetor[dire]<vetor[menor]):
		menor = dire
	if(menor!=raiz):
		aux = vetor[raiz]
		vetor[raiz] = vetor[menor]
		vetor[menor] = aux
		min_heapify(vetor,menor,tam)

def valorRoda(config, roda):
	return (config // 10 ** (4 - roda)) % 10

def gira(config, roda, sentido):
	peso = 10 ** (4 - roda)
	
	digitoAtual = (config // peso) % 10

	if sentido == 'a':
		proximoDigito = (digitoAtual + 9) % 10
	else:
		proximoDigito = (digitoAtual + 1) % 10

	subtrair = digitoAtual * peso
	somar = proximoDigito * peso

	return config - subtrair + somar

def heuristica(numero):
	heuristica = 0
	botoes = [int(x) for x in str(numero)]
	for i in botoes:
		if(i>=5):
			heuristica = heuristica + (10-i)
		else:
			heuristica = heuristica + i
	return heuristica

class Estado:
	def __init__(self, numero, proibidos, passos):
		# Guarda a configuração atual e a coleção de
		# estados proibidos
		self.numero = numero
		self.proibidos = proibidos
		# Calcule f, g e h
		self.g = passos
		self.h = heuristica(self.numero)
		self.f = self.g + self.h

	def transicoes(self):
		# Complete-me
		saida = []  # Deve retornar os estados alcançáveis 
		for i in range(1,5):
			horario = gira(self.numero, i, 'h')
			anti = gira(self.numero, i, 'a')
			if(horario not in self.proibidos) and valorRoda(horario, i) != valorRoda(self.numero, i):
				saida.append(horario)
			if(anti not in self.proibidos) and valorRoda(anti, i) != valorRoda(self.numero, i):
				saida.append(anti)
		return saida

	def __lt__(self, other):
		if(self.f<=other.f):
			return True
		else:
			return False 

	def __repr__(self):
		return "{:04d}".format(self.numero)


valor = int(input())
while(valor!=-1):
	proibidos = list(eval(input()))
	passos = buscaInformada(valor, proibidos)
	print(passos)
	valor = int(input())
def buscaInformada(inicial):
	final = [0,1,2,3,4,5,6,7,8]
	passos = 0
	posicoes = []
	agenda = []
	passados = {}
	estado = Estado(inicial,passos)
	agenda.append(estado)
	passados[estado.ordem] = estado
	while(len(agenda)>0):
		estado = agenda[0]
		posicoes.append(estado)
		#print("estado: ",estado.numero)
		agenda.remove(estado)
		#print(estado.numero)
		if(estado.ordem==final):
			break
		agenda = []
		lista_trans = estado.transicoes()
		#print(lista_trans)
		for est in lista_trans:
			proximo = Estado(est,estado.g+1)
			if proximo.numero not in passados:
				agenda.append(proximo)
				passados[proximo.ordem] = proximo
				montar_heap(agenda,len(agenda))
			elif proximo.g < passados[proximo.ordem].g:
				passados[proximo.ordem].g = proximo.g
				passados[proximo.ordem].f = proximo.g + passados[proximo.ordem].h
				montar_heap(agenda,len(agenda))
		passos += 1
		#print("agenda: ",agenda)
	return posicoes

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

def troca(vet,i,j):
	trocado = vet
	trocado[i],trocado[j]=trocado[j],trocado[i]
	return trocado

def heuristica(vet):
	heuristica = 0
	cont = 1
	for i in range(1,len(vet)):
		if(vet[i]!=cont):
			heuristica = heuristica + 1
			cont=cont+1
	return heuristica

class Estado:
	def __init__(self, ordem, passos):
		# Guarda a configuração atual e a coleção de
		# estados proibidos
		self.ordem = ordem
		# Calcule f, g e h
		self.g = passos
		self.h = heuristica(self.ordem)
		self.f = self.g + self.h

	def transicoes(self):
		# Complete-me
		saida = []  # Deve retornar os estados alcançáveis 
		if(self.ordem[0]==0):
			vet_aux1 = troca(self.ordem,0,1)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,0,3)
			saida.append(vet_aux1)
		elif(self.ordem[1]==0):
			vet_aux1 = troca(self.ordem,1,0)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,1,2)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,1,4)
			saida.append(vet_aux1)
		elif(self.ordem[2]==0):
			vet_aux1 = troca(self.ordem,2,1)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,2,5)
			saida.append(vet_aux1)
		elif(self.ordem[3]==0):
			vet_aux1 = troca(self.ordem,3,0)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,3,4)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,3,6)
			saida.append(vet_aux1)
		elif(self.ordem[4]==0):
			vet_aux1 = troca(self.ordem,4,1)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,4,3)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,4,5)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,4,7)
			saida.append(vet_aux1)
		elif(self.ordem[5]==0):
			vet_aux1 = troca(self.ordem,5,2)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,5,4)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,5,8)
			saida.append(vet_aux1)
		elif(self.ordem[6]==0):
			vet_aux1 = troca(self.ordem,6,3)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,6,7)
			saida.append(vet_aux1)
		elif(self.ordem[7]==0):
			vet_aux1 = troca(self.ordem,7,6)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,7,4)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,7,8)
			saida.append(vet_aux1)
		elif(self.ordem[8]==0):
			vet_aux1 = troca(self.ordem,8,5)
			saida.append(vet_aux1)
			vet_aux1 = troca(self.ordem,8,7)
			saida.append(vet_aux1)
		return saida

	def __lt__(self, other):
		if(self.f<=other.f):
			return True
		else:
			return False 

	def __repr__(self):
		return "{:04d}".format(self.numero)


inicial = list(eval(input()))
print(buscaInformada(inicial))
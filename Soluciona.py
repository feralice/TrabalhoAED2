#Funcao retorna um conjunto de estados que representam o menor caminho até o estado final
def buscaInformada(inicial):
	final = 12345678
	passos = 0
	#lista com o menor caminho até o estado final
	caminho = []
	#lista a ser fila de prioridade
	agenda = []
	#Dicionário criado para armazenar estados passados
	estados_passados = {}
	estado = Estado(inicial,passos)
	agenda.append(estado)
	estados_passados[estado.num] = estado
	while(len(agenda)>0):
		#retira primeiro valor da fila de prioridade
		estado = agenda[0]
		caminho.append(estado.ordem)
		agenda.remove(estado)
		#Se achou estado final, retorna caminho e passos dados
		if(estado.num==final):
			return caminho,passos
		agenda = []
		lista_trans = estado.transicoes()
		for est in lista_trans:
			#gera um objeto da classe Estado para cada transição possível
			proximo = Estado(est,estado.g+1)
			if proximo.num not in estados_passados:
				agenda.append(proximo)
				estados_passados[proximo.num] = proximo
				montar_heap(agenda,len(agenda))
			elif proximo.g < estados_passados[proximo.num].g:
				estados_passados[proximo.num].g = proximo.g
				estados_passados[proximo.num].f = proximo.g + estados_passados[proximo.num].h
				montar_heap(agenda,len(agenda))
		passos += 1
	#retorna -1 se não houver solucao
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

def troca(vet,i,j):
	trocado = vet
	trocado[i],trocado[j]=trocado[j],trocado[i]
	return trocado

def valorInt(lista):
	soma = ""
	for i in lista:
		soma=soma+str(i)
	return int(soma)

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
		# Guarda a configuração atual e a jeção de
		self.ordem = ordem
		self.num = valorInt(self.ordem)
		# Calcule f, g e h
		self.g = passos
		self.h = heuristica(self.ordem)
		self.f = self.g + self.h

	def transicoes(self):
		posicao_vazia = self.ordem.index(0)
		alcancaveis = []
		if posicao_vazia > 2:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia-3] = novo_estado[posicao_vazia-3], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)

		if posicao_vazia < 6:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia+3] = novo_estado[posicao_vazia+3], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)

		if posicao_vazia % 3 != 0:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia-1] = novo_estado[posicao_vazia-1], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)

		if posicao_vazia % 3 != 2:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia+1] = novo_estado[posicao_vazia+1], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)

		return alcancaveis
    
	def __lt__(self, other):
		if(self.f<other.f):
			return True
		else:
			return False 

	def __repr__(self):
		return "{:09d}".format(self.num)


inicial = list(eval(input()))
caminho, passos = buscaInformada(inicial)
print("Caminho: ",caminho,"em ",passos,"passos")
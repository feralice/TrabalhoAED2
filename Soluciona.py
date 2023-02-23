from queue import PriorityQueue

#Funcao retorna um conjunto de estados que representam o menor caminho até o estado final
def buscaInformada(inicial):
	final = 12345678
	passos = 0
	#lista a ser fila de prioridade
	agenda = PriorityQueue()
	#Conjunto criado para armazenar estados passados
	estados_passados = set()
	estado = Estado(inicial,passos)
	agenda.put(estado)
	while not agenda.empty():
		#retira primeiro valor da fila de prioridade
		estado = agenda.get()
		#Se achou estado final, retorna caminho e passos dados
		if(estado.num==final):
			caminho = []
			while estado is not None:
				caminho.append(estado)
				estado = estado.antecessor
			#len(caminho) para indicar quantidade de passos dados
			return caminho[::-1],len(caminho)
		estados_passados.add(estado.num)
		lista_trans = estado.transicoes()
		for alcancaveis in lista_trans:
			#gera um objeto da classe Estado para cada transição possível
			proximo = Estado(alcancaveis,estado.g+1,estado)
			if proximo.num not in estados_passados:
				agenda.put(proximo)
	#retorna -1 se não houver solucao
	return -1,-1

#Funcao que pega uma lista e retorna um valor inteiro com os dados da lista
#Usada para gerar um atributo unico para cada objeto, para poder utilizar no dicionário
def valorInt(lista):
	inteiro = ""
	for valor_lista in lista:
		inteiro=inteiro+str(valor_lista) 
	return int(inteiro)

#Calcula heuristica verificando quantos valores não estão no seu devido lugar (zero nao conta)
def heuristica(vet):
	heuristica = 0
	valor_ideal = 1
	for valor_atual in range(1,len(vet)):
		if(vet[valor_atual]!=valor_ideal):
			heuristica = heuristica + 1
		valor_ideal=valor_ideal+1
	return heuristica

class Estado:
	def __init__(self, ordem, passos,antecessor = None):
		#Recebe a lista com a ordem e gera um inteiro a partir da lista
		self.ordem = ordem
		self.num = valorInt(self.ordem)
		# Calcula f, g e h
		self.g = passos
		self.h = heuristica(self.ordem)
		self.f = self.g + self.h
		# atributo para verificar de onde esse estado veio
		self.antecessor = antecessor

	#Retorna uma lista com todas as transicoes possiveis
	def transicoes(self):
		#pega o valor que esta o 0
		posicao_vazia = self.ordem.index(0)
		alcancaveis = []
		#verifica se posicao vazia ta na primeira linha
		if posicao_vazia > 2:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia-3] = novo_estado[posicao_vazia-3], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)
		#verifica se posicao vazia ta na ultima linha
		if posicao_vazia < 6:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia+3] = novo_estado[posicao_vazia+3], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)
		#verifica se posicao vazia ta na primeira coluna
		if posicao_vazia % 3 != 0:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia-1] = novo_estado[posicao_vazia-1], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)
		#verifica se posicao vazia ta na ultima coluna
		if posicao_vazia % 3 != 2:
			novo_estado = self.ordem.copy()
			novo_estado[posicao_vazia], novo_estado[posicao_vazia+1] = novo_estado[posicao_vazia+1], novo_estado[posicao_vazia]
			alcancaveis.append(novo_estado)

		return alcancaveis
    #sobrecarga de operador lower than, a partir do atributo self.f
	def __lt__(self, other):
		if(self.f<=other.f):
			return True
		else:
			return False 
	#somente para representar o valor inteiro com 9 digitos
	def __repr__(self):
		return "{:09d}".format(self.num)


#inicial = list(eval(input()))
#caminho, passos = buscaInformada(inicial)
#print("Caminho: ",caminho,"em ",passos,"passos")
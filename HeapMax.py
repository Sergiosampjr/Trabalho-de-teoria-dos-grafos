import math


class HeapMax:


    def __init__(self):
        self.nos = 0
        self.heap = []
    def adiciona_no(self, u):
        self.heap.append(u)
        self.nos = self.nos + 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                f = p
    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        nivel = int(math.log(self.nos, 2))
        a = 0
        for i in range(nivel):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end = '  ')
                a = a + 1
            print('')
        for i in range(self.nos - a):
            print(f'{self.heap[a]}', end = '')
            a = a + 1





    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos = self.nos - 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f] > self.heap[f - 1]:
                    f = f + 1
            if self.heap[p - 1] >= self.heap[f - 1]:
                break
            else:
                self.heap[f - 1], self.heap[p - 1] = self.heap[p - 1], self.heap[f - 1]
                p = f
        return x


    def tamanho(self):
        return self.nos
    def maior_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia.'
    def filho_esquerda(self, i):
        return self.heap
        if self.nos >= 2 * i:
            return self.heap[2 * i - 1]
        return 'Esse nó não tem filho!.'
    def filho_direito(self, i):
        if self.nos >= 2 * i:
            return self.heap[2 * i]
        return 'Esse nó não tem filho à direita!.'
    def pai(self, i):
        return self.heap[i // 2]









h = HeapMax()
h.adiciona_no(100)
h.adiciona_no(85)
h.adiciona_no(66)
h.adiciona_no(40)
h.adiciona_no(31)
h.adiciona_no(1)
h.adiciona_no(14)


elementomax = h.remove_no()
print(f'O elemento removido foi: {elementomax}')


h.mostra_heap()


print(f'Tamanho: {h.tamanho()}')
print(f'Filho à esquerda de 25: {h.filho_esquerda(3)}.')
print(f'Filho à direita de 25: {h.filho_direito(3)}.')



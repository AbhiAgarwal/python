array_x = [88, 12, 78, 87, 89, 95, 16, 82]

def QuickSort(L, U, A):
	if L >= U: return
	if A[L] < A[U]:
		swap(L, U, A)
	P = A[U]
	B = L
	T = U
	print 'P =', P, 'B =', B, 'T =', T
	while True:
		swap(B, T, A)
		while True:
			B += 1
			if (A[B] >= P): break
		while True:
			T -= 1
			if (A[T] <= P): break
		if B >= T: break
	swap(L, T, A)
	QuickSort(L, T - 1, A)
	QuickSort(T + 1, U, A)

def swap(L, U, A):
	temp = A[L]
	A[L] = A[U]
	A[U] = temp

if __name__ == '__main__':
	QuickSort(0, 7, array_x)
	print array_x

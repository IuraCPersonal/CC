# Laboratory Nr2. Tema: Eratosthenes Sieve.

### **SCOPUL LUCRĂRII:** Empirical analysis of algorithms for obtaining Eratosthenes Sieve.

### SARCINA DE BAZĂ:

1. Implementați algoritmii enumerati mai jos într-un limbaj de programare
2. Stabiliți proprietățile datelor de intrare în raport cu care se face analiza
3. Alegeți metrica pentru compararea algoritmilor
4. Efectuați analiza empirică a algoritmilor propuși
5. Faceți o prezentare grafică a datelor obținute
6. Faceți o concluzie asupra lucrării efectuate.

### Algorithm 1

```c++
c[1] = false;
i = 2;
while (i <= n){
  if (c[i] == true) {
    j = 2*i;
    while (j <= n) {
      c[j] = false;
      j = j + i;
    }
  }
  i = i + 1;
}
```

### Algorithm 2

```c++
C[1] = false;
i = 2;
while (i <= n) {
  j=2*i;
  while (j <= n) {
    c[j] = false;
    j = j + i;
  }
  i = i + 1;
}
```

### Alghorithm 3

```c++
C[1] = false;
i = 2;
while (i <= n) {
  if (c[i] == true) {
    j = i + 1;
    while (j <= n) {
        if (j % i == 0) {
        c[j] = false;
        }
        j = j + 1;
    }
  }
  i = i + 1;
}
```

### Algorithm 4
```c++
C[1] = false;
i = 2;
While (i <= n) {
  j = 2;
  while (j < i) {
    if ( i % j == 0) {
      c[i] = false
    }
    j = j + 1;
  }
  i = i + 1;
}
```

### Alghoritm 5
```c++
C[1] = faux;
i = 2;
while (i<=n) {
  j = 2;
  while (j <= sqrt(i)) {
    if (i % j == 0) {
      c[i] = false;
    }
    j++;
  }
  i++;
}
```
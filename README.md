# Métodos Numéricos: Diferenciação e Integração Numérica

Este repositório reúne implementações em Python para a resolução numérica de dois problemas fundamentais do cálculo diferencial e integral: a aproximação de derivadas por diferenças finitas e o cálculo de integrais definidas por métodos de quadratura (Trapézio e Simpson).

O objetivo deste projeto é ilustrar de forma clara e didática como conceitos matemáticos contínuos são discretizados e resolvidos computacionalmente.

---

## Estrutura dos Códigos

O repositório está dividido em dois scripts principais baseados na biblioteca `numpy`:

1. **Diferenciação Numérica (`diferenciacao.py`):** Compara três aproximações de diferenças finitas para a derivada de uma função analítica contra o seu resultado exato.
2. **Integração Numérica (`integracao.py`):** Implementa as regras compostas do Trapézio e de Simpson para o cálculo de áreas sob curvas.

---

## 1. Diferenciação Numérica (Diferenças Finitas)

O primeiro script foca em estimar a taxa de variação instantânea de uma função $f(x)$ em um ponto específico $x_0$, utilizando um espaçamento infinitesimal aproximado $h$. 

A função testada é $f(x) = \sin(x)$, cuja derivada analítica exata é $f'(x) = \cos(x)$.

### Métodos Implementados:

* **Diferença Progressiva (Forward Difference):** Utiliza o ponto subsequente para aproximar a inclinação. Possui erro de ordem linear $O(h)$.
  $$f'(x_0) \approx \frac{f(x_0 + h) - f(x_0)}{h}$$

* **Diferença Regressiva (Backward Difference):** Utiliza o ponto anterior para aproximar a inclinação. Também possui erro de ordem linear $O(h)$.
  $$f'(x_0) \approx \frac{f(x_0) - f(x_0 - h)}{h}$$

* **Diferença Central (Central Difference):** Utiliza a média simétrica dos pontos vizinhos. Por cancelar os termos de primeira ordem na Série de Taylor, sua precisão é muito maior, com erro de ordem quadrática $O(h^2)$.
  $$f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$$

---

## 2. Integração Numérica (Quadratura)

O segundo script foca em aproximar a integral definida:
$$\int_{a}^{b} f(x) \, dx$$

Para a função testada $f(x) = x^2$ no intervalo $[0, 1]$, dividida em $n = 10$ subintervalos.

### Métodos Implementados:

* **Regra Composta do Trapézio:** Aproxima a área sob a curva dividindo o intervalo em $n$ trapézios lineares. O somatório pondera as extremidades com peso 1 e os pontos internos com peso 2.
  $$\text{Resultado} = \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

* **Regra Composta de Simpson (1/3):** Aproxima a curva utilizando arcos de parábolas (polinômios de segundo grau) em vez de retas. Exige estritamente um número **par** de subintervalos ($n$), alternando os pesos dos pontos internos entre 4 e 2 para atingir uma precisão superior de ordem $O(h^4)$.
  $$\text{Resultado} = \frac{h}{3} \left[ f(x_0) + 4\sum_{\text{ímpares}} f(x_i) + 2\sum_{\text{pares}} f(x_j) + f(x_n) \right]$$

---

## Requisitos e Execução

Os scripts utilizam a biblioteca `numpy` para a vetorização e criação das malhas de pontos (`np.linspace`).

### Instalação das dependências:
```bash
pip install numpy matplotlib

Parâmetros de Teste e Resultados scripts vêm configurados por padrão com os seguintes parâmetros para validação dos métodos:Diferenciação ($f(x) = \sin(x)$ em $x_0 = 1.0, h = 0.1$): Demonstra na prática como o erro da Diferença Central é significativamente menor se comparado aos métodos Progressivo e Regressivo.Integração ($f(x) = x^2$ em $[0, 1]$ com $n = 10$): Mostra a eficiência da Regra de Simpson, que consegue obter o resultado exato de $1/3$ para polinômios de até terceiro grau.

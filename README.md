# Métodos Numéricos em Física Computacional

Projeto didático em Python com implementações de métodos numéricos para
diferenciação e integração de funções.

O repositório demonstra como derivadas e integrais, definidas continuamente,
podem ser aproximadas computacionalmente por meio de discretização.

## Objetivos

- Implementar aproximações de derivadas por diferenças finitas.
- Comparar os métodos progressivo, regressivo e central.
- Implementar as regras compostas do Trapézio e de Simpson.
- Comparar resultados numéricos com soluções analíticas conhecidas.
- Estudar a influência do método escolhido sobre o erro numérico.

## Destaques técnicos

- Operações vetorizadas com NumPy.
- Comparação direta entre solução numérica e solução exata.
- Diferença central com erro de ordem \(O(h^2)\).
- Regra de Simpson com erro global de ordem \(O(h^4)\).
- Validação do número de subintervalos exigido pelo método de Simpson.

## Métodos implementados

### Diferenciação numérica

Para \(f(x)=\sin(x)\), cuja derivada exata é \(f'(x)=\cos(x)\), são
comparadas três aproximações:

- Diferença progressiva:

\[
f'(x) \approx \frac{f(x+h)-f(x)}{h}
\]

- Diferença regressiva:

\[
f'(x) \approx \frac{f(x)-f(x-h)}{h}
\]

- Diferença central:

\[
f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}
\]

### Integração numérica

Para aproximar uma integral definida, o projeto implementa:

- Regra composta do Trapézio.
- Regra composta de Simpson 1/3.

A função usada no exemplo é \(f(x)=x^2\), integrada no intervalo \([0,1]\).

## Resultado de referência

Com os parâmetros presentes nos scripts:

| Método | Resultado | Erro absoluto |
|---|---:|---:|
| Derivada exata | 0,540302 | — |
| Diferença progressiva | 0,497364 | 0,042939 |
| Diferença regressiva | 0,581441 | 0,041138 |
| Diferença central | 0,539402 | 0,000900 |
| Trapézio | 0,335000 | 0,001667 |
| Simpson | 0,333333 | aproximadamente zero |

Os resultados mostram a maior precisão da diferença central e da regra de
Simpson para esses exemplos.

## Estrutura

| Caminho | Responsabilidade |
|---|---|
| `diferenciacao-numerica/derivadas.py` | Aproximação e comparação de derivadas |
| `integracao-numerica/integracao.py` | Regras do Trapézio e de Simpson |
| `README.md` | Documentação do projeto |

## Como executar

Requer Python 3.9 ou superior.

Depois de clonar ou baixar o repositório:

```bash
cd fisica-computacional
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\activate
pip install numpy matplotlib
python diferenciacao-numerica/derivadas.py
python integracao-numerica/integracao.py
```

No Linux ou macOS:

```bash
source .venv/bin/activate
pip install numpy matplotlib
python diferenciacao-numerica/derivadas.py
python integracao-numerica/integracao.py
```

## Limitações e próximos passos

- Os parâmetros dos experimentos ainda estão definidos diretamente nos scripts.
- O projeto não possui testes automatizados.
- A diferenciação importa Matplotlib, mas ainda não gera gráficos.
- Próximas evoluções podem incluir análise do erro em função de \(h\), gráficos
  de convergência e novos métodos de quadratura.

## Autor

**João Paulo Benati Motta** — estudante de Engenharia Física na UFRGS, com
interesse em computação científica, métodos numéricos e modelagem física.

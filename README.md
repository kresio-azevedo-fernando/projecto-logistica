# Otimização Logística com Investigação Operacional
### €1,37 Bilhões em oportunidades identificadas (+30% com Simplex e Dijkstra)

---

## Resumo do Projeto

| | |
|---|---|
| **Sector** | Logística / Armazém |
| **Dados analisados** | 3.204 produtos · 5 categorias |
| **Custo logístico total** | €17,7 mil milhões/ano |
| **Oportunidade identificada** | €1,37B/ano |
| **Ferramentas** | Excel · SQL · Power BI · Simplex · Dijkstra |
| **Idiomas** | Português · English |

---

## Situação

Armazém com 3.204 produtos distribuídos por 5 categorias (Pharma, Electronics e outras).  
A taxa de atendimento média era de **80%**, o que gerava **14.746 ruturas por mês** e uma perda de receita estimada em **€630 milhões/ano**.

Custo logístico total de **€17,7 mil milhões/ano** dividido em:
- Custo de armazenagem: €2,83B — Pharma (4,27%) e Electronics (4,24%) lideravam
- Custo de manuseamento: €14,87B — Pharma (4,40%) com maior custo

---

## Tarefa

Identificar as causas das ruturas e dos custos elevados e transformar recomendações intuitivas em soluções matematicamente optimizadas, elevando o impacto das decisões.

---

## Ações

### Fase 1 — Análise descritiva e diagnóstica

**O que aconteceu:**
- Taxa de atendimento de 80% → 20% dos pedidos não atendidos
- 14.746 ruturas no último mês (média de 5 ruturas por produto)

**Porque aconteceu — 3 causas identificadas:**

1. **Procura instável** — Desvio padrão ≈ 14, média 25 → 56% de variação → Perda estimada: €465M/ano
2. **Layout ineficiente** — Zonas A, B, C, D com distribuição homogénea sem considerar giro → Perda estimada: €740M/ano
3. **Lead time elevado** — Média de 6 dias com alta variabilidade em categorias críticas → Perda estimada: €165M/ano

### Fase 2 — Optimização com algoritmos (Simplex + Dijkstra)

**Simplex — Programação Linear:**
- Calculou níveis óptimos de stock para cada categoria
- Redistribuiu 23% do stock excedente para categorias com maior rutura
- Impacto adicional: +€98M sobre os €465M iniciais → **Total: €563M**

**Dijkstra — Teoria dos Grafos:**
- Representou o armazém como grafo ponderado (nós = localizações, arestas = corredores × factor de congestionamento)
- Calculou os caminhos mínimos de picking para cada rota
- Realocou itens de alto giro para zonas próximas à expedição
- Redução média de 32% na distância percorrida por pedido (validado em 100 pedidos reais)
- Impacto adicional: +€162M sobre os €740M iniciais → **Total: €902M**

**Simplex — Problema de Transporte:**
- Modelou a distribuição como problema de transporte (caso especial de programação linear)
- Reduziu de 177 para 51 rotas (-71%)
- Lead time médio reduzido de 6,0 para 4,3 dias
- Impacto adicional: +€60M → **Total: €225M**

---

## Resultados

| Acção | Antes | Depois | Ganho |
|---|---|---|---|
| Previsão + Stock | €465M | €563M | +€98M |
| Layout + Rotas de picking | €740M | €902M | +€162M |
| Lead time + Transporte | €165M | €225M | +€60M |
| **TOTAL** | **€1,05B** | **€1,37B** | **+€320M** |

**ROI médio da implementação: 420%**  
A aplicação de modelos matemáticos gerou **+30% de impacto** face à análise descritiva isolada.

---

## Próximos Passos

| Prazo | Acção | Responsável |
|---|---|---|
| 30 dias | Implementar modelo Simplex para optimização de stocks | Dados / TI |
| 60 dias | Mapear grafo do armazém e testar rotas Dijkstra | Operações |
| 90 dias | Integrar modelo de transporte ao WMS | TI / Logística |
| 120 dias | Medir redução real de deslocamento e custos | Análise |

---

## Ficheiros deste repositório

```
📄 README.md                  ← este documento
📄 relatorio-executivo.pdf    ← relatório de 1 página (análise completa)
📁 dados/
   🖼 dados-sujos.png         ← dados em estado bruto antes do tratamento
   🖼 dados-tratados.png      ← dados após limpeza e estruturação
📁 dashboard/
   🖼 dashboard.png           ← dashboard Power BI (screenshot)
📁 scripts/
   📄 analise.sql             ← queries SQL utilizadas na análise
```

---

## Ferramentas utilizadas

`Excel` `SQL` `Power BI` `Simplex` `Dijkstra` `Estatística descritiva` `Programação linear`

---

*Projecto desenvolvido como parte do portfolio de análise de dados e investigação operacional.*  
*Kresio Azevedo Fernado · [in/kresio-data-bi-business-analyst](https://www.linkedin.com/in/kresio-data-bi-business-analyst/) · kresiofernando@hotmail.com*

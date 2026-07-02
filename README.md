# Logistics Optimisation with Operations Research
### €1.37B in opportunities identified · ROI 420%

> **Sector:** Logistics / Warehouse Operations  
> **Data:** 3,204 products · 5 categories · 12 months  
> **Tools:** SQL · Excel · Power BI · Simplex · Dijkstra · Python ETL  
> **Languages:** Português · English

---

## Live Systems

| System | Link | Status |
|--------|------|--------|
| 📊 Interactive Dashboard | [Ver Dashboard ao vivo](https://app.powerbi.com/view?r=eyJrIjoiNzA2M2VlZTItYmFmMi00ODdhLThhM2QtOWEyMGUwNThkZjg4IiwidCI6IjY1OWNlMmI4LTA3MTQtNDE5OC04YzM4LWRjOWI2MGFhYmI1NyJ9) | ✅ Live |
| 🗄️ SQL Analysis (Google Colab) | [Ver análise ao vivo](https://colab.research.google.com/drive/1yMxHbdcn_Hz_xlY1Xjqrkhx0VW_6xMMs?usp=sharing) | ✅ Live |
| ⚙️ Optimisation App (Streamlit) | *[coming soon]* | In development |

---

## STAR — Português

### Situação
Armazém com 3.204 produtos distribuídos por 5 categorias (Pharma, Electronics e outras). Taxa de atendimento média de **80%**, gerando **14.746 rupturas por mês** e uma perda de receita estimada em **€630 milhões/ano**.

Custo logístico total de €17,7 mil milhões/ano:
- Custo de armazenagem: €2,83B — Pharma (4,27%) e Electronics (4,24%) lideravam
- Custo de manuseamento: €14,87B — Pharma (4,40%) com maior custo

### Tarefa
Identificar as causas das rupturas e dos custos elevados e transformar recomendações intuitivas em soluções matematicamente optimizadas, elevando o impacto das decisões.

### Ações

**Fase 1 — Análise descritiva e diagnóstica**

O que aconteceu:
- Taxa de atendimento de 80% → 20% dos pedidos não atendidos
- 14.746 rupturas no último mês (média de 5 rupturas por produto)

Porque aconteceu — 3 causas identificadas:
1. **Procura instável** — Desvio padrão ≈ 14, média 25 → 56% de variação → Perda estimada: €465M/ano
2. **Layout ineficiente** — Zonas A, B, C, D com distribuição homogénea sem considerar giro → Perda estimada: €740M/ano
3. **Lead time elevado** — Média de 6 dias com alta variabilidade → Perda estimada: €165M/ano

**Fase 2 — Optimização com algoritmos**

Simplex — Programação Linear:
- Calculou níveis óptimos de stock para cada categoria
- Redistribuiu 23% do stock excedente para categorias com maior ruptura
- Impacto adicional: +€98M → **Total: €563M**

Dijkstra — Teoria dos Grafos:
- Representou o armazém como grafo ponderado (nós = localizações, arestas = corredores × factor de congestionamento)
- Calculou os caminhos mínimos de picking para cada rota
- Redução média de 32% na distância percorrida por pedido (validado em 100 pedidos reais)
- Impacto adicional: +€162M → **Total: €902M**

Simplex — Problema de Transporte:
- Reduziu de 177 para 51 rotas (-71%)
- Lead time médio reduzido de 6,0 para 4,3 dias
- Impacto adicional: +€60M → **Total: €225M**

### Resultado

| Acção | Antes | Depois | Ganho |
|-------|-------|--------|-------|
| Previsão + Stock | €465M | €563M | +€98M |
| Layout + Rotas de picking | €740M | €902M | +€162M |
| Lead time + Transporte | €165M | €225M | +€60M |
| **TOTAL** | **€1,05B** | **€1,37B** | **+€320M** |

**ROI médio da implementação: 420%**  
A aplicação de modelos matemáticos gerou **+30% de impacto** face à análise descritiva isolada.

---

## STAR — English

### Situation
Warehouse with 3,204 products across 5 categories (Pharma, Electronics and others). Average service level of **80%**, generating **14,746 stockouts per month** and estimated revenue losses of **€630 million/year**.

Total logistics cost of €17.7 billion/year:
- Storage cost: €2.83B — Pharma (4.27%) and Electronics (4.24%) led
- Handling cost: €14.87B — Pharma (4.40%) with highest cost

### Task
Identify the root causes of stockouts and elevated costs, and transform intuitive recommendations into mathematically optimised solutions to maximise decision impact.

### Actions

**Phase 1 — Descriptive and Diagnostic Analysis**

What happened:
- 80% service level → 20% of orders unfulfilled
- 14,746 stockouts in the last month (average 5 per product)

Why it happened — 3 causes identified:
1. **Unstable demand** — Standard deviation ≈ 14, mean 25 → 56% variation → Estimated loss: €465M/year
2. **Inefficient layout** — Zones A, B, C, D with uniform distribution ignoring turnover → Estimated loss: €740M/year
3. **High lead time** — Average 6 days with high variability in critical categories → Estimated loss: €165M/year

**Phase 2 — Algorithm-based Optimisation**

Simplex — Linear Programming:
- Calculated optimal stock levels for each category
- Redistributed 23% of surplus stock to highest-stockout categories
- Additional impact: +€98M → **Total: €563M**

Dijkstra — Graph Theory:
- Modelled warehouse as weighted graph (nodes = locations, edges = corridors × congestion factor)
- Calculated minimum picking paths for each route
- Average 32% reduction in distance per order (validated on 100 real orders)
- Additional impact: +€162M → **Total: €902M**

Simplex — Transportation Problem:
- Reduced from 177 to 51 routes (-71%)
- Average lead time reduced from 6.0 to 4.3 days
- Additional impact: +€60M → **Total: €225M**

### Result

| Action | Before | After | Gain |
|--------|--------|-------|------|
| Forecast + Stock | €465M | €563M | +€98M |
| Layout + Picking routes | €740M | €902M | +€162M |
| Lead time + Transport | €165M | €225M | +€60M |
| **TOTAL** | **€1.05B** | **€1.37B** | **+€320M** |

**Average implementation ROI: 420%**  
Mathematical modelling generated **+30% impact** compared to descriptive analysis alone.

---

## Repository Structure

```
📁 projecto-logistica/
   📄 README.md                    ← this file
   📄 executive-report-en.pdf      ← 1-page executive report (EN)
   📄 relatorio-executivo-pt.pdf   ← relatório executivo (PT)
   📄 apresentacao-executiva.pptx  ← executive presentation
   📁 dados/
      📄 dataset-anonimizado.xlsx  ← anonymised dataset
   📁 scripts/
      📄 etl_pipeline.py           ← ETL automation pipeline
      📄 simplex_model.py          ← Linear Programming model
      📄 dijkstra_routes.py        ← Route optimisation model
   📁 notebooks/
      📄 sql-analysis.ipynb        ← SQL analysis (Google Colab)
```

---

## Next Steps (Implementation Roadmap)

| Timeline | Action | Owner |
|----------|--------|-------|
| 30 days | Implement Simplex model for stock optimisation | Data / IT |
| 60 days | Map warehouse graph and test Dijkstra routes | Operations |
| 90 days | Integrate transport model with WMS | IT / Logistics |
| 120 days | Measure real reductions in distance and cost | Analytics |

---

*Project developed as part of the BI & Decision Optimisation portfolio.*  
*[Kresio Azevedo Fernando](https://www.linkedin.com/in/kresio-bi-business-data-analyst/) · kresiofernando@hotmail.com · [kresio-azevedo-fernando.github.io](https://kresio-azevedo-fernando.github.io)*

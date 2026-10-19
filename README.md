# IA Cultivada — curso (INEMA Learning v7.2)

🇧🇷 [Português](https://inematds.github.io/iacultivada-v72/) · 🇺🇸 [English](https://inematds.github.io/iacultivada-v72/en/) · 🇪🇸 [Español](https://inematds.github.io/iacultivada-v72/es/)

[![IA Cultivada](assets/img/capa.jpg)](https://inematds.github.io/iacultivada-v72/)

Versão em curso do projeto [IA Cultivada](https://inematds.github.io/iacultivada/) ("não se programa, se cultiva"). O projeto original continua no ar com os capítulos, kits, gerador, diagnóstico, skills e o vídeo; este curso organiza o mesmo conteúdo em 8 aulas com diagrama clicável, prática com "pronto quando", teste comentado e um plano datado no fim.

## As aulas

| # | Aula | Prática |
|---|---|---|
| 1 | A semente e o jardim: por que IA se cultiva | diagnóstico de maturidade |
| 2 | Os oito elementos e os cinco arquivos que cultivam | ficha do agente e a pasta com os 5 arquivos |
| 3 | A escada de maturidade: o que é e o que não é IA cultivada | classificar 3 IAs que você usa |
| 4 | Primeiro jardim: a vida pessoal | Sobre mim, 3 regras e a 1ª revisão semanal |
| 5 | Segundo jardim: o seu Jarvis | arquivo-mestre, diário de falhas e runbook |
| 6 | Fechar o ciclo: diário de falhas e observabilidade | uma semana de registro e a 1ª regra nascida de erro |
| 7 | Autonomia por evidência, não por confiança | critério de promoção + conversa simulada |
| 8 | Terceiro jardim: a empresa, e o seu plano | plano datado (.md + .ics) |

## O que mudou em relação ao projeto

- Níveis de autonomia unificados em quatro (os capítulos de vida pessoal e Jarvis usavam três passos).
- Os 14 capítulos viraram 8 aulas com prática verificável e teste comentado.
- Comparações (88% → 95%, Empresa A × B, 5 → 14 regras) viraram diagramas clicáveis.
- Conversa simulada para treinar a decisão de autonomia com um diretor apressado.

## Como editar

Conteúdo em `conteudo/<lang>/` (JSON). Nunca editar o HTML gerado:

```bash
python3 gerar.py && python3 gerar.py --lang en && python3 gerar.py --lang es
python3 validar.py --links
```

Conteúdo educacional aberto e gratuito do [INEMA.CLUB](https://inema.club).

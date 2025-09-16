# 🗺️ RPG AI–Python Mastery Roadmap (Paweł • AI Biznes)

> **Cel dokumentu:** Dać Ci _pełny_, zadaniowy plan opanowania AI jako wdrożeniowiec/architekt, **bez kursów wideo**. Każdy poziom ma: zakres, próg zaliczenia (Gate), checklisty, „boss fight” (mini‑projekt), artefakty do portfolio i mierzalne kryteria.
> **Styl pracy:** krótkie sprinty (25–40 min), zero filmików, maks. praktyki, małe iteracje.
> **Technologie bazowe:** Python 3.11+, FastAPI, (opcjonalnie) LangChain/LlamaIndex jako narzędzia, ale nacisk na _rozumienie koncepcji_ i samodzielne implementacje.

---

## Jak używać tego pliku
- [ ] Kopiuj ten plik do repozytorium `ai-mastery` i odhaczaj checkboxy.
- [ ] Każdy „Gate” to twarde kryterium przejścia dalej.
- [ ] Artefakty zapisuj w `/portfolio/<level>/<nazwa-zadania>/` (kody, README, screenshoty).
- [ ] Pracujemy **level po levelu** – po każdym „Gate” robimy krótkie retro i decyzję „co dalej”.

---

## ⚙️ Level 0 — Setup & Hygiene (1–2 dni)

**Cel:** stabilne środowisko deweloperskie i szkielet repo do prototypów AI.

### Zakres
- [ ] **Python 3.11+**: instalacja (Windows: `pyenv-win` lub oficjalny installer), `python -V` w PATH.
- [ ] **Zarządzanie środowiskiem:** `venv` **lub** `poetry` (wybierz jedno, docelowo `poetry`).
- [ ] **Zarządzanie paczkami CLI:** `pipx` (dla narzędzi jak `ruff`, `pre-commit`).
- [ ] **Code style & jakość:** `ruff` (lint), `black` (format), `mypy` (typing), `pre-commit` (hooki).
- [ ] **Edytor:** VS Code (Python, Pylance, Black Formatter, Ruff, Even Better TOML). Ustaw auto‑format on save.
- [ ] **Sekrety:** `.env` + `python-dotenv`. **NIGDY** nie commituj kluczy API.
- [ ] **Repo szkielet:** `ai-mastery/` z modułem `src/`, `tests/`, `pyproject.toml`, `README.md`.
- [ ] **Windows spec:** jeśli używasz WSL2 – ustaw ścieżki projektu po stronie Linux; dbaj o spójność linii LF.

### Gate (próg zaliczenia)
- [ ] `poetry run pytest` działa (pusty test przechodzi).
- [ ] `pre-commit` odpalone i działa (hooki pilnują formatowania).
- [ ] `sample_app` uruchamia się z `.env` i loguje „hello”.

### Boss fight
- [ ] Zrób **template repo** `ai-app-template` (FastAPI + settings + logging + healthcheck) do ponownego użycia.

### Artefakty
- [ ] `ai-app-template` (public/private), README z instrukcją „run & deploy lokalnie”.

---

## 🐍 Level 1 — Python dla Integratora AI (5–10 dni)

**Cel:** solidny, praktyczny Python do budowy usług i skryptów AI (bez DS/ML matematyki).

### Zakres (co dokładnie opanować)
- [ ] **Składnia i idiomy**: list/dict/set comprehension, `enumerate`, `zip`, `pathlib`, `itertools`.
- [ ] **Funkcje i typowanie**: `->`, `TypedDict`, `Protocol`, `dataclasses`, `@overload`, `typing.Literal`.
- [ ] **Błędy i kontrola przepływu**: własne wyjątki, `try/except/else/finally`, wzorzec „EAFP”.
- [ ] **I/O i formaty**: `json`, `csv`, podstawy `pandas` (tylko do prostych transformacji).
- [ ] **HTTP klient**: `requests` **i** `httpx` (sync/async), retry z backoffem, timeouts, łączenie z `.env`.
- [ ] **Walidacja danych**: `pydantic` (modele, walidacja, serializacja), wymuszanie kontraktów JSON.
- [ ] **CLI**: `argparse` **lub** `typer`. Standard wej./wyj., kody wyjścia, komunikaty błędów.
- [ ] **Async**: podstawy `asyncio` (taski, `gather`, timeouts, semafory do rate‑limitów).
- [ ] **Testy**: `pytest` (fixture’y, parametrize), **testy kontraktowe** dla API i modeli.
- [ ] **Logowanie i obserwowalność**: `logging` strukturalny (JSON), ID korelacji, poziomy logów.

### Gate
- [ ] CLI `ai-call` wywołuje dowolne API (np. pogodowe / mock LLM), waliduje odpowiedź `pydantic`‑iem, loguje w JSON, ma retry/backoff i timeouts, **i** ma testy (min. 5).
- [ ] Rozumiesz i potrafisz wytłumaczyć, kiedy async ma sens (I/O‑bound vs CPU‑bound).

### Boss fight
- [ ] „**API Wrangler**”: mini‑libka Python (2–3 funkcje) ułatwiająca bezpieczne wołanie API (headers, retry, metrics).

### Artefakty
- [ ] `ai-call` (CLI) + `api_wr` (libka) + README + testy + coverage report.

---

## 🧠 Level 2 — LLM Fundamentals & RAG Mini (7–14 dni)

**Cel:** rozumieć LLM „od strony wdrożeniowej” i złożyć minimalne **RAG** (retrieval‑augmented generation).

### Zakres
**A. LLM podstawy praktyczne**
- [ ] Tokeny, kontekst, temperatura/top_p, role (system/user/assistant).
- [ ] **Prompt patterns**: instrukcja, „cot”/myślenie (ostrożnie), few‑shot, „delimiters”, „do not make up”, „step by step”.
- [ ] **Strukturyzowany output**: JSON z walidacją `pydantic` + twarde schematy („jeśli nie możesz – zwróć błąd”).
- [ ] **Function/Tool calling**: projektowanie narzędzi (kontrakty), bezpieczne parsowanie i egzekucja.
- [ ] **Ograniczanie halucynacji**: źródła, cytaty, self‑check, fallback („I don’t know”).

**B. Embeddings & wektory**
- [ ] Czym są embeddingi, metryki (cosine/dot), normalizacja.
- [ ] **Chunking**: strategie (według nagłówków, okna przesuwne, semantyczny split), rozmiary chunków vs okno kontekstu.
- [ ] **Metadane**: źródło, data, sekcja, tagi – potrzebne do filtrów.
- [ ] **Wyszukiwanie**: top‑k, similarity vs MMR; kiedy dodać reranking (koncepcyjnie).

**C. Minimalny RAG**
- [ ] Loader dokumentów (PDF/MD/HTML) → normalizacja → chunking → wektory → index (FAISS/Chroma).
- [ ] Query → wektory → retrieve → prompt z cytatami → JSON answer + list of sources.
- [ ] **Cache**: local disk/memory, TTL; **rate‑limits**: semafory, kolejka.
- [ ] **Koszty**: liczenie tokenów, budżet na zapytanie, logowanie kosztów.

### Gate
- [ ] Lokalny **RAG Mini**: podajesz folder `.md` i dostajesz odpowiedź + 3 cytaty ze ścieżkami. Zero halucynacji na prostym zbiorze.
- [ ] Testy: **golden set** (min. 15 pytań), metryki: precision@k (prosta implementacja), odsetek odpowiedzi „I don’t know” na pytania poza zakresem.

### Boss fight
- [ ] „**FAQ Bot dla JDG**”: indeksuje Twoje notatki/umowy/regulaminy i odpowiada z cytatami; ma endpoint `/ask` (FastAPI).

### Artefakty
- [ ] `rag_mini/` z kodem, danymi testowymi, skryptem ewaluacyjnym i raportem `.md` z wynikami.

---

## 🏗️ Level 3 — Prototypista AI w Biznesie (10–20 dni)

**Cel:** dowozić PoC działające z danymi klienta (SQL/REST) + podstawowa ewaluacja jakości.

### Zakres
- [ ] **FastAPI**: routery, dependency injection, walidacja, `pydantic-settings`, obsługa błędów, paginacja.
- [ ] **Autoryzacja**: proste API key / JWT (dla PoC wystarczy), CORS, podstawy rate‑limitingu.
- [ ] **SQL**: SQLAlchemy (Core/ORM), profile zapytań, transakcje, widoki pod AI.
- [ ] **Raporty AI**: pipeline: SQL → dataframe → prompt → JSON → render (Markdown/HTML/PDF).
- [ ] **LangChain/LlamaIndex (opcjonalnie)**: tylko, jeśli przyspiesza – rozumieć co robią pod spodem.
- [ ] **Eval & guardrails**: złoty zestaw testów (Pytania→Odpowiedzi), walidacja JSON, „do not answer outside corpus”.
- [ ] **Cachowanie**: klucz po (prompt, retrieved_docs), TTL, busting po reindeksacji.
- [ ] **Stabilność**: retry, timeouts, idempotencja, obsługa błędów dostawców (429/5xx), _circuit breaker_.
- [ ] **Śledzenie**: correlation id, trace log (wystarczy własny middleware).
- [ ] **UX PoC**: prosta strona (Jinja/HTMX/Streamlit) – tylko gdy potrzebne do demo.

### Gate
- [ ] Działający **PoC: „AI Raport Sprzedaży”** – input (zakres dat), zapytania SQL, generowany executive summary + KPI + cytaty źródeł (zapytania/sekcje).
- [ ] Ewaluacja: min. 20 przypadków testowych; wskaźnik „coverage” (w ilu przypadkach bot musiał odpowiedzieć „nie wiem” i czy to zasadne).

### Boss fight
- [ ] „**Opis Produktu 2.0**”: generator opisów + tagów SEO z danymi wejściowymi z DB, z walidacją schematu i detektorem PII.

### Artefakty
- [ ] Repo PoC + README (instalacja, uruchomienie, dane testowe), raport ewaluacyjny `.md`.

---

## 🧩 Level 4 — Integrator Enterprise (15–30 dni)

**Cel:** wynoszenie PoC do środowisk firmowych, bezpieczeństwo, niezawodność, koszty, prywatność (RODO).

### Zakres
- [ ] **Docker**: multi‑stage build, minimalne obrazy, `docker-compose` (LLM proxy / wektorówka / app).
- [ ] **CI/CD**: GitHub Actions – lint/test/build/push image, smoke test.
- [ ] **Sekrety i konfiguracja**: `.env`, zmienne środowiskowe, secret storage; rotacja kluczy.
- [ ] **Deploy**: VPS/Fly/Hetzner/K8s (zaczynamy od VPS + systemd + nginx).
- [ ] **Monitoring**: metryki (czas odpowiedzi, koszt/tokeny, błędy), alerty (np. Slack/Discord/Webhook).
- [ ] **Kolejki i tła**: Redis + RQ/Celery, zadania wsadowe (reindeksacja, raporty nocne).
- [ ] **Skalowanie**: worker’y, horizontal scaling, progi backpressure.
- [ ] **Bezpieczeństwo/Compliance**: RODO (PII, DPA, DPIA), logowanie zgodne z zasadą minimalizacji, anonimizacja.
- [ ] **Bezpieczeństwo aplikacyjne**: prompt‑injection mitigations, walidacja wejść, filtrowanie treści.
- [ ] **Koszty**: model rozliczeń, limit budżetu per użytkownik/proces, raportowanie miesięczne kosztów.

### Gate
- [ ] Jeden z Twoich PoC’ów działa jako **„pilot”**: dockerized, z monitorowaniem i alertami, budżetem i polityką PII (checklista RODO).
- [ ] Incident guide: runbook „co robić gdy 5xx/429 rośnie lub koszty skaczą >X%”.

### Boss fight
- [ ] „**Pilot Enterprise**” – 2 procesy zautomatyzowane (np. FAQ + raporty), SLA 99%, cost cap włączony, raport kwartalny.

### Artefakty
- [ ] `deploy/` (Dockerfile, compose, ansible/skrypty), `SECURITY.md`, `DPA-template.md`, `RUNBOOK.md`.

---

## 🧪 Level 5 — Developer AI+ (15–30 dni)

**Cel:** jakość odpowiedzi, szybkość i kontrola: lokalne modele, reranking, ewaluacje, tuningi.

### Zakres
- [ ] **Lokale modele**: podstawy (Ollama/gguf), kiedy mają sens (koszt/latencja/dane wrażliwe).
- [ ] **Tokenizery i modele**: rozumieć różnice (BPE/WordPiece), wpływ na długość promptu i koszty.
- [ ] **Retrieval Pro**: hybrydowe wyszukiwanie (BM25 + wektory), MMR, rerankery (koncepcyjnie + użycie).
- [ ] **RAG Pro**: lepszy chunking (okna adaptacyjne), query rewriter, multi‑step retrieve, fusion.
- [ ] **Ewaluacje LLM**: odpowiedzi „grounded”, _factuality_, „reference coverage”, _toxicity/PII leakage_.
- [ ] **Tuning**: LoRA/adaptery – kiedy warto; datasety, walidacja, overfitting, utrzymanie wersji.
- [ ] **Wydajność**: cache warstwowe, warm prompts, _prompt compression_, batchowanie zapytań.

### Gate
- [ ] **RAG+** przewyższa Twój RAG Mini w testach: +X% precision@k i niższy odsetek halucynacji na nowym zbiorze.
- [ ] Raport `.md` z porównaniem i uzasadnieniem zmian (zachowane wyniki, wykres prostych metryk).

### Boss fight
- [ ] „**RAG Enterprise**”: hybrydowe wyszukiwanie + reranking, query rewrite i polityka źródeł **must‑cite**.

### Artefakty
- [ ] `rag_pro/` + raport ewaluacyjny + dashboard (prosty HTML wykres/CSV).

---

## 🏛️ Level 6 — Architekt & Konsultant (30+ dni, równolegle z projektami)

**Cel:** skalowalne wzorce, metodologia, sprzedaż konsultingu i materiały eksperckie.

### Zakres
- [ ] **Wzorce architektoniczne**: single‑tenant vs multi‑tenant, _modular monolith_, „AI as a sidecar” vs „AI‑first”.
- [ ] **Metodologia wdrożeń**: playbook Starter/Pro/Enterprise (Discovery → ROI → PoC → Pilot → Rollout).
- [ ] **ROI i TCO**: modelowanie kosztów, amortyzacja, wskaźniki dla CFO (oszczędność czasu/kosztów).
- [ ] **Ryzyka**: prawne (prawa autorskie, dane osobowe), techniczne (drift danych), operacyjne (SLA, vendor lock‑in).
- [ ] **Etyka & odpowiedzialne AI**: zasady, polityki, _human‑in‑the‑loop_.
- [ ] **Materiały**: whitepaper „AI w e‑commerce”, case studies, checklisty, wzory umów (DPA, SLA).

### Gate
- [ ] Gotowy **AI Consulting Playbook** i szablony dokumentów, które użyjesz na pierwszych 3 klientach.
- [ ] Prezentacja 30–45 min dla zarządu: „AI – ryzyka, koszty, zwrot”.

### Boss fight
- [ ] **Whitepaper** + wystąpienie/warsztat + 2 opublikowane case studies (z anonimyzacją).

### Artefakty
- [ ] `playbook/`, `case-studies/`, `whitepaper/`, `sales/` (oferty, one‑pager, wyceny).

---

## 📋 Checklista globalna „Definition of Done” (DoD)

- [ ] Każdy moduł ma testy i README (jak uruchomić, jak ocenić).
- [ ] Każda integracja z modelem ma: budżet/tokeny, retry/backoff, timeouts, cache i logi.
- [ ] Każdy system RAG ma: loader → normalizacja → chunking → index → retrieve → cite → walidacja JSON.
- [ ] Każdy PoC ma: plan ewaluacji i „golden set” + raport wyników.
- [ ] Każdy deploy ma: obraz Docker, checklistę bezpieczeństwa i runbook incydentowy.
- [ ] Każdy projekt ma: _CHANGELOG_, wersjonowanie i prostą automatyzację (Makefile/taskfile).

---

## 🧭 Roadmap postępów (mini‑CRM zadań)

| Level | Zadanie / Boss fight | Status | Data | Dowód (link/screen) |
|---|---|---|---|---|
| 0 | Template repo | ☐ |  |  |
| 1 | CLI `ai-call` | ☐ |  |  |
| 1 | Lib `api_wr` | ☐ |  |  |
| 2 | RAG Mini + eval | ☐ |  |  |
| 2 | FAQ Bot JDG (API) | ☐ |  |  |
| 3 | AI Raport Sprzedaży | ☐ |  |  |
| 3 | Opis Produktu 2.0 | ☐ |  |  |
| 4 | Pilot Enterprise | ☐ |  |  |
| 5 | RAG Enterprise | ☐ |  |  |
| 6 | Playbook + Whitepaper | ☐ |  |  |

---

## 🧠 ADHD‑friendly taktyki (zero wideo)
- **Micro‑sprinty 25–40 min** + 5 min przerwy, 3–4 bloki/dzień.
- **Boss fights** na koniec tygodnia – jeden duży commit/dowód.
- **Checklisty** zamiast notatek – odhaczanie daje dopaminę.
- **Zamknięcie pętli**: każdy task tworzy artefakt (kod/test/README/screen).
- **Tylko jedna karta** w przeglądarce; brak Slacka/YouTube.
- **„Gotowe wystarczająco” > perfekcyjnie** – iteruj w kolejnych levelach.

---

## 📦 Add‑ons (opcjonalne)
- **Front demo**: HTMX + Jinja (lightweight).
- **Tracing**: własny middleware (request_id, latency, tokens, koszt).
- **Runner**: `taskipy` albo `make` do komend (format, test, run, build).
- **Docs**: MkDocs do generowania dokumentacji technicznej PoC.

---

## Co dalej?
Zaczynamy od **Level 0 → Boss fight (template repo)**. Po wrzuceniu artefaktu dam znak, robimy szybkie retro i przechodzimy na **Level 1**.

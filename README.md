# 📚 learning

Practice code and small exercises across languages, kept in one place.
Finished, standalone projects live in their own repositories.

| Folder | What's inside | How to run |
|---|---|---|
| [`python/`](python/) | Basics notebooks, 10 sorting algorithms, pytest suite | `cd python && pip install -r requirements.txt && python -m pytest` |
| [`java/core/`](java/core/) | Small core-Java exercises | `javac java/core/*.java` |
| [`spring-boot/`](spring-boot/) | Spring Boot "adder" REST API | `cd spring-boot && ./mvnw spring-boot:run` |
| [`go/`](go/) | Go practice: packages | `go run go/000-aa-packages/001/main.go` |
| [`ml-basics/`](ml-basics/) | Iris classifiers (logistic regression, KNN) | see each project's README |

## Conventions

- One folder per language or topic; each keeps its own dependency file (`requirements.txt`, `pom.xml`, `go.mod`).
- Notebooks go in a `notebooks/` folder, numbered in learning order (`01_…`, `02_…`).
- File and folder names are lowercase with hyphens or underscores.
- IDE files (`.idea/`, `.vscode/`, `*.iml`), virtualenvs and build output are never committed (see `.gitignore`).

---

**Balaji Gurram** · Integration Architect · [github.com/balaji014](https://github.com/balaji014)

Licensed under the MIT License.

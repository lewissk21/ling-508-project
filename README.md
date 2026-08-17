# Restaurant Menu Search

LING 508 project. A REST API for searching restaurant menus: given a dish, find
the restaurants that serve it.

## Quick start

From the repository root:

```bash
docker compose up --build
```

Try requesting a list of restaurants by dish:

```bash
curl -s "http://localhost:5000/find-restaurants-by-dish/Grilled%20Cheese"
```

Expected output:

```json
[{"address":"292 Massachusetts Ave, Cambridge, MA 02139","name":"Roxy's Grilled Cheese","website":"https://roxysgrilledcheese.com"}]
```

See <http://localhost:5000/> for every endpoint with inputs and outputs.

## Project layout

```
server.py              Flask application and route definitions
app/services.py        Services: application logic between routes and data
repo/repo.py           Repository: abstract data-access interface
repo/mysql_repo.py     MenuRepository: MySQL implementation of Repository
model/                 Restaurant, Menu, Dish, Ingredient, MenuType
db/init.sql            Schema loaded by MySQL on first start
tests/                 pytest tests
doc/                   API documentation, use cases, UML class diagram
Dockerfile             Application image
docker-compose.yaml    Application and database services
```


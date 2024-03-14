import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Fact(BaseModel):
    id: int
    fact: str


# standard
facts = [
    Fact(id=0, fact="Bears eat mostly meat and fish, but some bears also eat plants and insects."),
    Fact(id=1, fact="Canada is home to nearly 60% of the world’s polar bears."),
    Fact(id=2, fact="The Asiatic black bear has the largest ears than other species of bears."),
    Fact(id=3, fact="The Asiatic black bear has the largest ears of any species of bears."),
    Fact(id=4, fact="Black bears can run at the speed up to 35mph."),
    Fact(id=5, fact="Baloo, from The Jungle Book, is a sloth bear."),
    Fact(id=6, fact="Katmai National Park is home to approximately 4,000 Alaskan brown bears."),
    Fact(id=7, fact="Most bears have 42 teeth."),
    Fact(id=8, fact="Grizzly bears can remember the faces of other bears."),
    Fact(id=9, fact="There are at least 600,000 black bears in North America."),
    Fact(id=10, fact="About 98% of the grizzly bear population in the U.S. lives in Alaska."),
    Fact(id=11, fact="The largest recorded polar bear weighed 1,002 kilograms."),
    Fact(id=12, fact="The Governor of Moscow trained a large bear to serve pepper Vodka to his guests."),
    Fact(id=13, fact="Great of Russia the Peter trained a bear to serve drinks to his guests."),
    Fact(id=14, fact="Polar bears primarily eat seals."),
    Fact(id=15, fact="The Sun bear has the shortest fur to keep themselves cool in the hot forests."),
    Fact(id=16, fact="Bears are big and heavy even though they can run very fast."),
    Fact(id=17, fact="Bears are good at climbing and swimming."),
    Fact(id=18, fact="There are only eight living species of bears."),
    Fact(id=19, fact="A group of bears is called a sloth."),
    Fact(id=20, fact="Bears have a large brain and are also known as intelligent mammals."),
    Fact(id=21, fact="The Koala is not a bear."),
    Fact(id=22, fact="Canadian Northwest Territories License plates are shaped like polar bears."),
    Fact(id=23, fact="A male bear is called a boar and female is called sow."),
    Fact(id=24, fact="A grizzly bear eats almost 20,000 calories a day."),
    Fact(id=25, fact="Bears have an excellent sense of smell, better than dogs.")
]
#extended
FACTS_FILE = "bear_facts.txt"
with open(FACTS_FILE, "r") as f:
    fact_lines = f.readlines()
    facts = [Fact(id=index, fact=line) for index,line in enumerate(fact_lines)]


@app.get("/fact")
async def get_bear_fact(id: str | None = None):
    if id is None:
        id = random.randint(0, len(facts) - 1)
    return facts[int(id)]


@app.get("/fact/{id}")
async def get_by_id(id: int):
    return facts[id]


@app.post("/add/")
async def add_a_new_bear_fact(fact: Fact):
    fact.id = len(facts)
    facts.append(fact)
    # extended challenge
    with open(FACTS_FILE, "a") as f:
        f.write("\n")
        f.write(fact.fact)
    return fact


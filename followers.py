# De gebruikelijke imports

import pandas as pd
import graphdb

# Eerst lezen we de data in een dataframe dat zich in de links-anon-small.txt bevindt.
# We kunnen de gegevens zien als een CSV bestand waarbij elke kolom door een spatie is gescheiden
# en er geen kolomnamen in de eerste rij staan.

df = pd.read_csv("links-anon-atom.txt", sep=" ", names=["from", "to"])

# We printen de eerste elementen uit om te zien of het gelukt is om onze gegevens in te laden
print("De ingeladen dataframe")
print(df.head())
print()

# Nu vlakken we dataframe af zodat we alle ids er uit kunnen krijgen
flattened = df.to_numpy().flatten()
print("Afgevlakt")
print(flattened)
print()

# Vervolgens maken we een set van deze afgevlakte dataframe zodat we alleen unieke ids hebben
unique_ids = set(flattened)

print("Unique ids computed")
print()

# We maken nu verbinding met onze graphdb
db = graphdb.GraphDB()

# Nu kunnen we ze één per één invoegen als nodes in onze graf
for id in unique_ids:
    # Merk op: dit kan veel sneller als we ids combineren in 1 query of
    # met transacties werken!
    db.add_profile(id)

print("Nodes inserted")
print()

# Nu kunnen we de relaties tussen de verschillende accounts leggen
# dit doen we door over elke rij in onze dataframe te gaan

for _, row in df.iterrows():
    from_id = row["from"]
    to_id = row["to"]
    db.follow(from_id, to_id)

print("Followers inserted")
print()

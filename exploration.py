import pandas as pd
import graphdb 
import seaborn as sb
import matplotlib.pyplot as plt

db = graphdb.GraphDB()
# We maken er een DataFrame van 
degrees = pd.DataFrame(map(lambda x: dict(degree = x["degree"]), db.in_degrees()))
outdegree = pd.DataFrame(map(lambda x: dict(degree = x["degree"]), db.out_degrees()))

sb.histplot(degrees)
plt.savefig("distribution_degree.pdf")

# clear figure
plt.clf()
sb.histplot(outdegree)
plt.savefig("distribution_out_degree.pdf")


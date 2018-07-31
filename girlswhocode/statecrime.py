import state_crime
import matplotlib.pyplot as plt
list_of_report = state_crime.get_all_crimes()

california_rates = []
florida_rates = []

for l in list_of_report:
    if l["State"] == "California":
        california_rates.append(l["Data"]["Rates"]["Violent"]["Murder"])
    elif l["State"] == "Florida":
        florida_rates.append(l["Data"]["Rates"]["Violent"]["Murder"])

plt.plot(california_rates)
plt.title("Murder in Califonia")
plt.xlabel("Years(1960-2012)(idk what the # are either)")
plt.ylabel("# of reported offenses per 100,000 people")
plt.show()
plt.plot(florida_rates)
plt.title("Murder in Florida")
plt.xlabel("Years(1960-2012)(idk what the # are either)")
plt.ylabel("# of reported offenses per 100,000 people")
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
circuit = pd.read_csv('circuits.csv')#4
driver=pd.read_csv('drivers.csv')#2
pit=pd.read_csv('pit_stops.csv')#1
race=pd.read_csv('races.csv')#3


driver=driver.drop(columns=["url"])
circuit=circuit.drop(columns=["url"])
race=race.drop(columns=["url"])

a=pit.merge(driver,on="driverId")
b=a.merge(race,on="raceId")
merge=b.merge(circuit,on="circuitId")
merge=merge[merge["milliseconds"]<=20000]

merge['seconds'] = merge['milliseconds'] / 1000

ver=merge[merge["surname"]=="Verstappen"]
ham=merge[merge["surname"]=="Hamilton"]
mal=merge[merge["surname"]=="Maldonado"]
ler=merge[merge["surname"]=="Leclerc"]

plt.scatter(ver["surname"],ver["seconds"],color="red",label="Verstappen",alpha=0.7)
plt.scatter(ham["surname"],ham["seconds"],color="#12d4ed",label="Hamilton",alpha=0.7)
plt.scatter(ler["surname"],ler["seconds"],color="#f4ff00",label="Leclerc",alpha=0.7)
plt.scatter(mal["surname"],mal["seconds"],color="#18e763",label="Maldonado",alpha=0.7)

plt.grid(True,color="black",linestyle="--",linewidth=0.5)
plt.xlabel("Driver")
plt.ylabel("Seconds")
plt.title("Formula 1 Total Pit Lane Time Comparison")
plt.show()
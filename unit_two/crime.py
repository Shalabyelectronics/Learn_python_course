# First suspect

a = {
        "finger print":1125,
        "is employee": True,
        "time":"7 pm",
        "injury":"right hand",
        "age":45,
        "wieght":(130, "kg"),
        "blood type": "A+"
        }

# Second suspect

b = {
        "finger print":2564,
        "is employee": False,
        "time":"7 pm",
        "injury":"left leg",
        "age":30,
        "wieght":(75, "kg"),
        "blood type": "O"
        }

# Your Evedence

ev = {
        "finger prints":[2564,1125],
        "is employee": True,
        "time":"7 pm",
        "injury":"has injury in his leg",
        "age":35,
        "wieght":(100, "kg"),
        "blood type": "A+"
        }

# Compare 

check_a = (a["finger print"] in ev["finger prints"]) +(a["is employee"] == ev["is employee"]) + (a["time"] == ev["time"]) + (a["age"] <= ev["age"] ) + (a["wieght"][0] >= ev["wieght"][0]) + (a["blood type"] == ev["blood type"])


check_b = (b["finger print"] in ev["finger prints"]) +(b["is employee"] == ev["is employee"]) + (b["time"] == ev["time"]) + (b["age"] <= ev["age"] ) + (b["wieght"][0] >= ev["wieght"][0]) + (b["blood type"] == ev["blood type"])



print(f"Total result as below\nA got {check_a} from  {len(ev)}\nB got {check_b} from  {len(ev)}\n\nThat mean A is guilty.")


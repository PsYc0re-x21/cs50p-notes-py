def main():
    spacecraft = {"name" : "Voyager_1"}
    spacecraft.update({"place" : "Mars", "time" : "24 years"})

    print (create_report(spacecraft))

def create_report(spacecraft):
    
    
    return f"""


==== Report === 

Name: {spacecraft.get("name", "Unknown")}
Place: {spacecraft.get("place", "Unknown")}
Runtime: {spacecraft.get("time", "Unknown")}

===============

"""
main ()
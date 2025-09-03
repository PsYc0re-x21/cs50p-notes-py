def main():
    spacecraft = {"name" : "Voyager_1", "place" : "Mars"}
    print (create_report(spacecraft))

def create_report(spacecraft):
    

    return f"""


==== Report === 

Name: {spacecraft["name"]}
Place: {spacecraft["place"]}

===============

"""
main ()
import random
import time
import os


exchange_members = ["Denney", 
                  "Cari", 
                  "Kyle", 
                  "Heather", 
                  "Kyra", 
                  "Dennica", 
                  "Elsie", 
                  "Gemma"]
exchange_names = ["Denney", 
                  "Cari", 
                  "Kyle", 
                  "Heather", 
                  "Kyra", 
                  "Dennica", 
                  "Elsie", 
                  "Gemma"]

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    
for member in exchange_members:
    selected_name = random.choice(exchange_names)
    
    while member == selected_name:
        #print(f"Same Names member: {member}, selection: {selected_name}")
        selected_name= random.choice(exchange_names)
        
    print(f"{member} has...")
    time.sleep(3)
    print(f"\n\t{selected_name} for the Exchange.")
    notify(f"{member} has...", f"{selected_name} for the exchange!")
    exchange_names.remove(selected_name)
    time.sleep(5)
    
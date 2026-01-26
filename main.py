import datetime

def main():
    print("--------------------------------------------------")
    print("Jenkins Automation Demo")
    print("Developed by: Dinitha")
    print("--------------------------------------------------")
    
    current_time = datetime.datetime.now()
    print(f"Current System Time: {current_time}")
    
    total = 0
    for i in range(1, 6):
        print(f"Processing item {i}...")
        total += i
        
    print("--------------------------------------------------")
    print(f"Task Completed! Total calculation: {total}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
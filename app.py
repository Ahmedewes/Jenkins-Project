import matplotlib.pyplot as plt
import pandas as pd

def run_gui():
    
    data = {
        'Stage': ['Bronze', 'Silver', 'Gold'], 
        'Records': [15000, 12000, 11500]
    }
    df = pd.DataFrame(data)
    
    print("Data Transformation Successful!")
    print(df)

   
    plt.figure(figsize=(8, 6))
    plt.bar(df['Stage'], df['Records'], color=['#cd7f32', '#c0c0c0', '#ffd700'])
    plt.title('Data Pipeline Metrics (Records per Stage)')
    plt.xlabel('Medallion Layer')
    plt.ylabel('Number of Processed Records')
    
   
    print("Opening GUI Window...")
    plt.show()

if __name__ == "__main__":
    run_gui()

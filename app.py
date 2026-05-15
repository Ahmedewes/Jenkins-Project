import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DataPipelineDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jenkins Project")
        self.geometry("900x500")

         
        self.label = ctk.CTkLabel(self, text="Jenkins Project", font=("Roboto", 24))
        self.label.pack(pady=20)

         
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.sidebar.pack(side="left", fill="y", padx=20, pady=20)

        self.status_label = ctk.CTkLabel(self.sidebar, text="Status: Running", text_color="green")
        self.status_label.pack(pady=10)

        self.btn = ctk.CTkButton(self.sidebar, text="Refresh Metrics", command=self.update_chart)
        self.btn.pack(pady=10)

        
        self.plot_frame = ctk.CTkFrame(self)
        self.plot_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        
        self.update_chart()

    def update_chart(self):
    
        data = {'Stage': ['Bronze', 'Silver', 'Gold'], 'Records': [15000, 12000, 11500]}
        df = pd.DataFrame(data)

        fig, ax = plt.subplots(figsize=(5, 4), facecolor='#2b2b2b')
        ax.bar(df['Stage'], df['Records'], color=['#3a7ebf', '#1f538d', '#103057'])
        ax.set_title("Processed Records per Stage", color='white')
        ax.tick_params(colors='white')
        ax.set_facecolor('#2b2b2b')

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = DataPipelineDashboard()
    app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import requests
import csv

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        
        self.url_label = ttk.Label(root, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.scrape_button = ttk.Button(root, text="Scrape Data", command=self.scrape_data)
        self.scrape_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.data_text = tk.Text(root, height=20, width=80)
        self.data_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.download_button = ttk.Button(root, text="Download Data", command=self.download_data)
        self.download_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
    def scrape_data(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Here, you can customize the data scraping based on the website structure
            # For demonstration purposes, we'll simply extract all text data
            data = soup.get_text()
            
            # Display scraped data in the text box
            self.data_text.delete(1.0, tk.END)
            self.data_text.insert(tk.END, data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def download_data(self):
        data = self.data_text.get(1.0, tk.END)
        if data.strip():
            filename = "scraped_data.csv"
            with open(filename, "w", newline="", encoding="utf-8") as file:
                file.write(data)
            messagebox.showinfo("Success", f"Data has been saved to {filename}")
        else:
            messagebox.showwarning("No Data", "There is no data to download.")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()

import tkinter as tk

class SignLanguageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sign Language To Text Conversion")
        self.root.geometry("800x600")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        # Labels
        self.label_title = tk.Label(self.root, text="Sign Language To Text Conversion", font=("Courier", 20, "bold"))
        self.label_title.pack(pady=20)
        
        self.label_char = tk.Label(self.root, text="Character :", font=("Courier", 12, "bold"))
        self.label_char.pack()
        
        self.label_word = tk.Label(self.root, text="Word :", font=("Courier", 12, "bold"))
        self.label_word.pack()
        
        self.label_sentence = tk.Label(self.root, text="Sentence :", font=("Courier", 12, "bold"))
        self.label_sentence.pack()
        
        self.label_suggestions = tk.Label(self.root, text="Suggestions :", fg="red", font=("Courier", 12, "bold"))
        self.label_suggestions.pack()

        # Image panels
        self.panel = tk.Label(self.root, bg="light gray", width=40, height=20)
        self.panel.pack(pady=10)

        self.panel2 = tk.Label(self.root, bg="light gray", width=20, height=10)
        self.panel2.pack(pady=10)

        # Buttons
        self.bt1 = tk.Button(self.root, text="Action 1", command=self.action1)
        self.bt1.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.bt2 = tk.Button(self.root, text="Action 2", command=self.action2)
        self.bt2.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.bt3 = tk.Button(self.root, text="Action 3", command=self.action3)
        self.bt3.pack(side=tk.LEFT, padx=10, pady=10)
        
    def destructor(self):
        self.root.destroy()
        
    def action1(self):
        # Define action for button 1
        pass
        
    def action2(self):
        # Define action for button 2
        pass
        
    def action3(self):
        # Define action for button 3
        pass

if __name__ == "__main__":
    app = SignLanguageApp()
    app.root.mainloop()

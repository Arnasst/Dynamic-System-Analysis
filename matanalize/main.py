from math import exp
import tkinter as tk


def func(x: float, a: float) -> float:
    return x * exp(a*(1 - x))

def main():
    # https://datatofish.com/entry-box-tkinter/
    window = tk.Tk()
    
    window.title("Matematinė analizė")
    window.geometry("700x500")
    
    canvas1 = tk.Canvas(window, width=400, height=300)
    canvas1.pack()
    entry1 = tk.Entry(window) 
    canvas1.create_window(100, 50, window=entry1)
    
    label = tk.Label(window,
        text="Click the Button to update this Text",
        font=('Calibri 15 bold')
    )
    label.pack(pady=20)
    
    def on_click_draw():
        try:
            a = float(entry1.get())
            label["text"] = func(1, a)
        except:
            label["text"] = "Invalid input"
        

    btn1 = tk.Button(window, text="Calculate", command=on_click_draw)
    btn1.pack(pady=20)
    
    # Run main loop
    window.mainloop()

if __name__ == '__main__':
    main()
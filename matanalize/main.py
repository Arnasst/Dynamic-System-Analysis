import tkinter as tk
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matanalize.functions import calculate_iterative_series, calculate_time_series, generate_bifurcation_data, func, MAX_POINTS

def plot_orbits(x0:float, a: float, axes: Axes, canvas: FigureCanvasTkAgg):
    values = calculate_time_series(x0, a)
    # plotting the graph
    x = [i[0] for i in values]
    y = [i[1] for i in values]
    axes.plot(x, y)
    canvas.draw()

    canvas.get_tk_widget().pack()


def plot_iterative_point(x0: float, a: float, axes: Axes, canvas: FigureCanvasTkAgg):
    x = list(range(0, MAX_POINTS))
    func_y = [func(i, a) for i in x]

    # axes.plot(x, x)
    # axes.plot(x, func_y)

    values = calculate_iterative_series(x0, a)
    x = [i[0] for i in values]
    y = [i[1] for i in values]
    axes.plot(x, y)
    canvas.draw()

    canvas.get_tk_widget().pack()

def plot_feigenbaum_tree(x0: float, axes: Axes, canvas: FigureCanvasTkAgg):
    values = generate_bifurcation_data(x0)

    x = [i[0] for i in values]
    y = [i[1] for i in values]
    axes.scatter(x, y, s=0.05, edgecolors='black', c='black')
    canvas.draw()
    
    canvas.get_tk_widget().pack()

def plot_bifurcation_points(axes: Axes, canvas: FigureCanvasTkAgg):
    values = [2.52, 2.65, 3.16]

    for value in values:
        axes.axvline(x=value, color='r', linestyle='--')
        axes.text(value + 0.01, 3, f'Bifurkacinis taškas r={value}', rotation=90, color='r')
    
    canvas.draw()
    canvas.get_tk_widget().pack()


def main():
    window = tk.Tk()
    window.title("Dinaminės sistemos analizė")
    window.geometry("1500x800")

    canvas1 = tk.Canvas(window, width=400, height=100)
    canvas1.pack()

    entry_label = tk.Label(window, text="Laisvasis narys")
    canvas1.create_window(20, 20, window=entry_label)
    entry_a = tk.Entry(window)
    canvas1.create_window(20, 40, window=entry_a)

    entry_label = tk.Label(window, text="X")
    canvas1.create_window(300, 20, window=entry_label)
    entry_x0 = tk.Entry(window)
    canvas1.create_window(300, 40, window=entry_x0)

    error_label = tk.Label(window,
        text="",
        font=('Calibri 15 bold')
    )
    error_label.pack(pady=10)

    fig = Figure(figsize = (40, 10), dpi = 100)
    plot1 = fig.add_subplot(1, 3, 1)
    plot2 = fig.add_subplot(1, 3, 2)
    plot3 = fig.add_subplot(1, 3, 3)
    
    canvas = FigureCanvasTkAgg(fig, master = window)
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    def on_click_draw():
        try:
            a = float(entry_a.get())
            x0 = float(entry_x0.get())

            plot1.clear()
            plot2.clear()
            plot3.clear()
            plot_orbits(x0, a, plot1, canvas)
            plot_iterative_point(x0, a, plot2, canvas)
            plot_feigenbaum_tree(x0, plot3, canvas)
            plot_bifurcation_points(plot3, canvas)
            error_label["text"] = ""
        except:
            error_label["text"] = "Neteisinga įvestis"

    btn1 = tk.Button(canvas1, text="Piešti", command=on_click_draw)
    canvas1.create_window(40, 60, window=btn1)

    window.mainloop()

if __name__ == '__main__':
    main()

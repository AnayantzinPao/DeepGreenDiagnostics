import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.config_matplotlib2()
        self.config_matplotlib()

    def config_matplotlib(self):
        self.fig = Figure((5.0, 5.0), dpi=50, facecolor="#F6F4F2")

        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.graph_a = self.fig.add_subplot(111)
        
        #self.graph_c = self.fig.add_subplot(313)

        self.graph_a.grid(True)
        self.graph_a.axes.set_xlim([1, 10])
        self.graph_a.axes.set_ylim([0, 200])
        data1 = [10*(x-1)**2 for x in range(1, 5)]
        data2 = [-50 * (x - 4) for x in range(1, 5)]
        self.graph_a.plot(data1, '--', data2, '--')

        """self.graph_c.grid(True)
        self.graph_c.axes.set_xlim([1, 3])
        self.graph_c.axes.set_ylim([0, 120])
        self.graph_c.plot(data2, '--')"""

        self.graph_plot_a = self.graph_a.plot(
            [],
            linewidth=1,
            color=("darkorange"),
        )[0]
        """self.graph_plot_c = self.graph_c.plot(
            [],
            linewidth=1,
            color=("darkorange"),
        )[0]"""

        ajust = {"top": 0.95,
                 "bottom": 0.1,
                 "right": 0.97,
                 "left": 0.05,
                 "wspace": 0.2,
                 "hspace": 1, }
        #self.fig.subplots_adjust(**ajust)

        # graficar (lo que se ve cuando se ejecuta el programa por)
        self.canvas.draw()

    def config_matplotlib2(self):
        self.fig2 = Figure((5.0, 5.0), dpi=50, facecolor="#F6F4F2")

        self.canvas2 = FigureCanvas(self.fig2)
        self.layout.addWidget(self.canvas2)
        self.graph_b = self.fig2.add_subplot(111)

        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        fracs = [15, 30, 45, 10]
        explode = (0, 0.05, 0, 0)


        self.graph_b.grid(True)
        patches, texts, autotexts=self.graph_b.pie(fracs, explode=explode, labels=labels,autopct='%1.2f', startangle=90, shadow=True)

        for t in texts:
            t.set_size('large')
        for t in autotexts:
            t.set_size('large')
        autotexts[0].set_color('y')
        ajust = {"top": 0.95,
                 "bottom": 0.1,
                 "right": 0.97,
                 "left": 0.05,
                 "wspace": 0.2,
                 "hspace": 1, }
        #self.fig2.subplots_adjust(**ajust)
        # graficar (lo que se ve cuando se ejecuta el programa por)
        self.canvas2.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())

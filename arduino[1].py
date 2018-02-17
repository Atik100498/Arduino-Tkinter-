from Tkinter import *
import serial


class Arduino(object):
    baudrate = [300, 1200, 4800, 9600, 19200, 38400, 57600, 115200]

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x400")
        Label(self.root, text="Arduino Board").grid(row=0, column=1)
        Button(self.root, text="Add port", command=self.info).grid(row=1, column=1)
        self.root.mainloop()

    def info(self):
        Label(self.root, text="Port").grid(row=2, column=0)
        Label(self.root, text="Baud rate").grid(row=3, column=0)
        self.e1 = Entry(self.root)
        self.e1.grid(row=2, column=1)
        self.e2 = Entry(self.root)
        self.e2.grid(row=3, column=1)
        def add_port():
            self.port = self.e1.get()
            if (self.port == '/dev/ttyACM0' or self.port == '/dev/ttyACM1'):
                Label(self.root, text="Port added!! ").grid(row=2, column=3)
            else:
                Label(self.root, text="invalid port").grid(row=2, column=3)

        Button(self.root, text="ADD", command=add_port).grid(row=2, column=2)

        def baud_rate():
            self.baud = int(self.e2.get())
            if (self.baud in self.baudrate):
                Label(self.root, text="Baud added!! ").grid(row=3, column=3)
            else:
                Label(self.root, text="invalid baud").grid(row=3, column=3)
        Button(self.root, text="ADD", command=baud_rate).grid(row=3, column=2)
        Button(self.root, text="Info", command=self.show_info).grid(row=4, column=1)
        try:
            Button(self.root, text="start port", command=self.start).grid(row=4, column=2)
        except SerialException:
            Label(Self.root, text="Board not attached").grid(row=2, column=3)

    def show_info(self):
        message = Tk()
        Message(message, text="Port: " + str(self.e1.get()) + "\n" + "Baud: " + str(self.e2.get())).pack()
        message.mainloop()

    def start(self):
        self.ser = serial.Serial(self.port, self.baud)
        var = IntVar()
        Radiobutton(self.root, text="Send data", command=self.send_data, variable=var).grid(row=5, column=0)
        Radiobutton(self.root, text="get data", command=self.get_data, variable=var).grid(row=5, column=1)

    def send_data(self):
        e1 = Entry(self.root)
        e1.grid(row=7, column=0)

        def send():
            a = unicode(self.e1.get())
            self.ser.write(a)

        Button(self.root, text="Send", command=send).grid(row=7, column=2)

    def get_data(self):
        def get():
            a = self.ser.read()
            Label(self.root, text=a).grid(row=8, column=2)

        Button(self.root, text="receive", command=get).grid(row=8, column=3)
a = Arduino()

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Californian FB", 24, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(20, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(430, 393)
        self._label1.TabIndex = 0
        self._label1.Text = "Hi!My name is Andrew.What you want know about me?"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(493, 7)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(114, 52)
        self._button1.TabIndex = 1
        self._button1.Text = "Favourite Class"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlLight
        self._button2.Location = System.Drawing.Point(493, 112)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(114, 52)
        self._button2.TabIndex = 2
        self._button2.Text = "Favourite Food"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlLight
        self._button3.Location = System.Drawing.Point(493, 226)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(114, 52)
        self._button3.TabIndex = 3
        self._button3.Text = "Favourite Game"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.SystemColors.MenuHighlight
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(493, 350)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(114, 52)
        self._button4.TabIndex = 4
        self._button4.Text = "Clear"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.SystemColors.ControlLight
        self._button5.Location = System.Drawing.Point(684, 9)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(114, 52)
        self._button5.TabIndex = 5
        self._button5.Text = "Come form"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.BackColor = System.Drawing.SystemColors.ControlLight
        self._button6.Location = System.Drawing.Point(684, 112)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(114, 52)
        self._button6.TabIndex = 6
        self._button6.Text = "Full Name"
        self._button6.UseVisualStyleBackColor = False
        self._button6.Click += self.Button6Click
        # 
        # button7
        # 
        self._button7.BackColor = System.Drawing.SystemColors.ControlLight
        self._button7.Location = System.Drawing.Point(684, 226)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(114, 52)
        self._button7.TabIndex = 7
        self._button7.Text = "Hobbies"
        self._button7.UseVisualStyleBackColor = False
        self._button7.Click += self.Button7Click
        # 
        # button8
        # 
        self._button8.BackColor = System.Drawing.SystemColors.HotTrack
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(684, 350)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(114, 52)
        self._button8.TabIndex = 8
        self._button8.Text = "Exit"
        self._button8.UseVisualStyleBackColor = False
        self._button8.Click += self.Button8Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(900, 430)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "About ME"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "My favourite class is History(US,EU,World)"

    def Button2Click(self, sender, e):
        self._label1.Text = "I like chinese foods best,especially BaoZi."

    def Button3Click(self, sender, e):
        self._label1.Text = "Hearts Of Iron 4 is my favourite video game,it is really interesting"

    def Button5Click(self, sender, e):
        self._label1.Text = "I come from People's Republic Of CHina(PRC)"

    def Button6Click(self, sender, e):
        self._label1.Text = "My chinese name is Zhao Zerui"

    def Button7Click(self, sender, e):
        self._label1.Text = "I like wacthing the japnese Anime and playing badminton with my father"

    def Button4Click(self, sender, e):
        self._label1.Text = "Hi!My name is Andrew.What you want know about me?"

    def Button8Click(self, sender, e):
        Application.Exit()
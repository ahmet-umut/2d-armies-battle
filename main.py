import tkinter as tk, random as r, time as t, math as m
r.r=r.random
t.m=t.monotonic

p = 3.14159
def at(x,y):
	return m.atan2(-y,x) 
m.at = at

"""
abc
ab.c
a.bc	*
a.b.c
"""

ws=400
d=20
w = tk.Tk()
c = tk.Canvas(w, width=ws, height=ws)

class S:
	l=[]
	def __init__(se) -> None:
		se.l.append(se)
		se.r = 9
		se.x = r.r()*ws;	se.y = r.r()*ws
		se.d = m.at(200-se.x, 200-se.y)
		se.vx = 0;	se.vy = 0
		se.ar = c.create_arc(se.x-se.r, se.y-se.r, se.x+se.r, se.y+se.r, start=se.d*360/2/p, extent=359)
		se.js = set()

	def u(se):
		for j in se.js:
			se.d = m.at(j[0]-se.x, j[1]-se.y)
			c.itemconfig(se.ar, start=se.d*360/2/p)
		se.js.clear()

		if se.vx:
			se.vx -= se.vx / abs(se.vx) / 100
			se.x += se.vx
			c.move(se.ar, se.vx, 0)
		if se.vy:
			se.vy -= se.vy / abs(se.vy) / 100
			se.y += se.vy
			c.move(se.ar, 0, se.vy)
	def wt(se, x,y):
		se.js.add((x,y))

fps = c.create_text(333, 333, text=0, font=("Arial", 20))
t0=t.m();	td=d
def u():
	global t0,td
	td = (t.m()-t0 + td) / 2
	c.itemconfig(fps, text= round(td*1000))
	t0 = t.m()
	for s0 in S.l:
		s0.u()
		for s1 in S.l:
			if not s0 is s1 and ((s0.x - s1.x) ** 2 + (s0.y - s1.y) ** 2)**.5 < s0.r+s1.r:
				s1.vx -= (s0.x - s1.x) / 100
				s1.vy -= (s0.y - s1.y) / 100
				s0.vx += (s0.x - s1.x) / 100
				s0.vy += (s0.y - s1.y) / 100
				s0.wt(s1.x,s1.y)
				s1.wt(s0.x,s0.y)
	w.after(d, u)

# Set up the window
w.title("total war")

n=10
for i in range(n):	S()
s=S()

def eh(event: tk.Event):
	match event.keysym:
		case 'Left': s.vx = -1
		case 'Right': s.vx = 1
		case 'Up': s.vy = -1
		case 'Down': s.vy = 1

w.bind("<Up>", eh)
w.bind("<Down>", eh)
w.bind("<Left>", eh)
w.bind("<Right>", eh)

c.pack()


# Run the tkinter main loop
u()
w.mainloop()

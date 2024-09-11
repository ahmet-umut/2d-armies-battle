import tkinter as tk, random as r, time as t, math as m
r.r=r.random
t.m=t.monotonic

p = 3.14159
def at(x,y):
	return m.atan2(-y,x) 
m.at = at
m.c = m.cos
m.s = m.sin

"""
abc
ab.c
a.bc	*
a.b.c
"""

ws=400
mspf=20
w = tk.Tk()
c = tk.Canvas(w, width=ws, height=ws)

co = f'#{r.randint(0, 255):02x}{r.randint(0, 255):02x}{r.randint(0, 255):02x}'

class So:pass

def de(*a):	# distance
	lt=[]
	for e in a:
		if type(e)==So:
			lt.append(e.x)
			lt.append(e.y)
		elif type(e) == tuple or type(e) == list:
			lt.append(e[0])
			lt.append(e[1])
		else:
			lt.append(e)
	try:
		return ((lt[0]-lt[2])**2 + (lt[1]-lt[3])**2)**0.5
	except Exception as ex:
		print(ex)
		print(a)
		print(lt)

class Sw:
	def __init__(s, so: So) -> None:
		s.so=so
		s.le = c.create_line(0,0,0,0)
		s.x=s.vx=0
	def u(s):
		s.vx/=2
		s.vx -= s.x / 9
		s.x += s.vx
		sde = s.x;	st = s.so.x+m.c(s.so.di)*sde + m.c(s.so.di - p/2)*s.so.r,	s.so.y-m.s(s.so.di)*sde - m.s(s.so.di - p/2)*s.so.r
		ede = s.so.r*4 + s.x;	en = s.so.x+m.c(s.so.di)*ede + m.c(s.so.di - p/2)*s.so.r,	s.so.y-m.s(s.so.di)*ede - m.s(s.so.di - p/2)*s.so.r
		for so in So.lt:
			if de(so, en) < so.r:	c.itemconfig(so.b, fill=co)
		c.coords(s.le, *st, *en)
	def sw(s):
		s.vx = 22

class J:
	def __init__(se,so,*a) -> None:
		so.js.add(se)
		se.so=so
		se.a=a
		match a:
			case "at",so,to:
				se.to=to
	def e(se):
		_js=set()
		match se.a:
			case "wt", x, y:
				se.so.di = m.at(x-se.so.x, y-se.so.y)
				se.so.s()
				if de(se.so, x,y) > 8:	_js.add(se)
			case "at",so,to:
				if de(se.so, so) > 64:
					se.so.di = m.at(so.x-se.so.x, so.y-se.so.y)
					se.so.s()
				elif se.to<0:
					se.to=9
					se.so.di = m.at(so.x-se.so.x, so.y-se.so.y) + .1
					se.so.sw.sw()
				se.to-=1
				print(se.to)
				_js.add(se)
		se.so.js = _js
class So:
	lt=[]
	def __init__(s) -> None:
		s.lt.append(s)
		s.r = 9
		sc = 9
		s.x = ws/sc + r.r()*ws/sc*(sc-2);	s.y = ws/sc + r.r()*ws/sc*(sc-2)
		s.di = m.at(200-s.x, 200-s.y)
		s.vx = 0;	s.vy = 0
		s.b = c.create_arc(s.x-s.r, s.y-s.r, s.x+s.r, s.y+s.r, start=s.di*360/2/p, extent=359)
		s.sw = Sw(s)
		s.js = set()

	def u(s):
		for j in s.js:
			j.e()

		fc = 2
		if s.vx:
			s.vx /= fc
			s.x += s.vx
		if s.vy:
			s.vy /= fc
			s.y += s.vy
		c.move(s.b, s.vx, s.vy)
		c.itemconfig(s.b, start=s.di*360/2/p)
		s.sw.u()
		for s1 in So.lt:
			if not s is s1 and de(s,s1) < s.r+s1.r:
				rc = 1
				s1.vx = (s1.x - s.x) * rc
				s1.vy = (s1.y - s.y) * rc
				s.vx = (s.x - s1.x) * rc
				s.vy = (s.y - s1.y) * rc

	def s(s, x=None, y=None):
		if x:	s.di = m.at(x-s.x, y-s.y)
		ss=2
		s.vx += m.c(s.di)*ss
		s.vy -= m.s(s.di)*ss
	def wt(s, *lo):
		if len(lo)==1:
			s.j("wt",lo[0].x,lo[0].y)
		else:
			s.j("wt",*lo)
	def at(se,so):
		se.j("at",so,0)
	def j(s,*a):	J(s,*a)

fps = c.create_text(222, 377, text="", font=("Times New Roman", 22))
t0=t.m();	td=mspf
def u():
	global t0,td
	sm=9
	td = (t.m()-t0)/sm + td*(sm-1)/sm
	c.itemconfig(fps, text= f"{round(td*1000)} ms per frame")
	t0 = t.m()
	
	for so in So.lt:	so.u()
	w.after(mspf, u)

# Set up the window
w.title("2d Armies Battle")

n=1
for i in range(n):	So()
s=So()

for so1 in So.lt:
	for so2 in So.lt:
		if so2 is so1:	continue
		so1.at(so2)
		break


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

w.bind("<Button-1>", lambda e: s.wt(e.x, e.y))
w.bind("<Button-2>", lambda e: s.s(e.x, e.y))
w.bind("<Button-3>", lambda e: s.sw.sw())

c.pack()


# Run the tkinter main loop
u()
w.mainloop()

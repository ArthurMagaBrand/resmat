from beam import *

b = Beam(6)
uvl1 = UVL(0,3,3,0, inverted=True)
uvl2=UVL(3,0,6,3, inverted=False)
ra = Reaction(0,'h', 'A')
rb = Reaction(b.length, 'r','B')

b.add_loads((uvl1,uvl2, ra,rb))
b.add_moments((uvl1, ra, uvl2, rb))
b.calculate_reactions((ra,rb))
b.generate_shear_equation((uvl1,uvl2, ra,rb))

x = np.linspace(-1, b.length, 500)
plt.rc('font', family='serif', size=14)
fig, ax = plt.subplots(facecolor='w', edgecolor='w', num="BMD vs SFD")
#ax.plot(x, b.mom_fn(x), label="BMD (kNm)")
ax.plot(x, b.shear_fn(x), label="SFD (kN)")
ax.set_xticks(np.arange(0, b.length+1,1))
ax.axhline(y=0, color='k', label='beam')
ax.set_title("BMD vs SFD of Beam")
ax.set_xlabel("x (m)")
ax.legend(fontsize=8)
ax.grid()
#plt.savefig(f"Simply_Supported_Beam/generated_images/{__file__.split('/')[-1]}.png")
plt.show()
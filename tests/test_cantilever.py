# question: https://civilengineeronline.com/mech/fig51a.gif
# solution : https://civilengineeronline.com/mech/fig51bsfbm.gif
# last question from figure
from pibeam import *

b = Beam(4)
rd = Reaction(b.length, 'f', 'D')
#rb = Reaction(b.length, 'f', 'B')
udl = UDL(1,4,2)
p = PointLoad(0, 2, inverted=True)
b.add_loads([rd, udl, p])
b.add_moments([rd, udl, p], about=b.length)
print(b.fx, b.fy, b.m)
b.calculate_reactions((rd,))
print(b.solved_rxns)
b.generate_moment_equation([rd, udl, p])
b.generate_shear_equation((rd, udl, p))

x = np.linspace(-1, b.length, 1000)
plt.rc('font', family='serif', size=14)
fig, ax = plt.subplots(facecolor='w', edgecolor='w', num="BMD vs SFD")
ax.plot(x, b.mom_fn(x), label="BMD (kNm)")
ax.plot(x, b.shear_fn(x), label="SFD (kN)")
ax.set_xticks(np.arange(0, b.length+1,1))
ax.axhline(y=0, color='k', label='beam')
ax.set_title("BMD vs SFD of Beam")
ax.set_xlabel("x (m)")
ax.legend(fontsize=8)
ax.grid()
plt.savefig(f"Simply_Supported_Beam/generated_images/{__file__.split('/')[-1]}.png")
plt.show()

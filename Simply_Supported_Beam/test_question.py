# question link: https://learnaboutstructures.com/sites/default/files/images/3-Frames/Det-Beam-Example-Moment.png

from beam import *
b = Beam(15)
ra = Reaction(0, 'h', 'A')
rc = Reaction(10, 'r','C')
p = PointLoad(5, 20, True)
m = PointMoment(5, 30, ccw=False)
udl = UDL(10, 10, 5)
b.add_loads((ra, rc, p, udl))
b.add_moments((ra, rc, p, udl, m))
b.calculate_reactions((ra, rc))
b.generate_moment_equation((ra, rc, p, udl, m))
b.generate_shear_equation((ra, rc, p, udl, m))

print(b.fx, b.fy, b.m)
print(b.solved_rxns)
x = np.linspace(-0.009, b.length, 1000)
plt.rc('font', family='serif', size=14)
fig, ax = plt.subplots(figsize=(9,7),facecolor='w', edgecolor='w')
ax.plot(x, b.mom_fn(x), label="BMD (kNm)")
ax.plot(x, b.shear_fn(x), label="SFD (kN)")
ax.set_xticks(np.arange(0,16,1))
ax.axhline(y=0, color='k', label='beam')
ax.set_title("BMD vs SFD of Beam")
ax.set_xlabel("x (m)")
ax.legend()
ax.grid()
#plt.savefig("Simply_Supported_Beam/generated_images/test_question.png")
plt.show()
from SchellingsModel.schellingsmodel import SchellingsModel

f = 0.1
N = 50
houses = N**2

agentsA = int((houses/2)*(1-f))
agentsB = int((houses/2)*(1-f))

model = SchellingsModel(N, agentsA, agentsB, 10**5)
model.run_model()
print('')


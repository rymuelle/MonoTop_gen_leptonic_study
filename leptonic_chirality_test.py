from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom, TClonesArray



f_RH_1           = TFile.Open("1TeV_RH.root", "read")
f_LH_1           = TFile.Open("1TeV_LH.root", "read")
f_RH_5           = TFile.Open("5TeV_RH.root", "read")
f_LH_5           = TFile.Open("5TeV_LH.root", "read")


#tree = []
#tree.append( (f_RH_1.Get("LHEF"), "RH_1TeV") )
#tree.append( (f_LH_1.Get("LHEF"), "LH_1TeV") )
#tree.append( (f_RH_5.Get("LHEF"), "RH_5TeV") )
#tree.append( (f_LH_5.Get("LHEF"), "LH_5TeV") )



test = f_RH_1.Get("LHEF")




def getParticles(tree):
	nParticles = tree.GetLeaf('Particle_size').GetValue()
	Particles=[]
	for j in range(int(nParticles)):
			pt = test.GetLeaf('Particle.PT').GetValue(j)
			eta = tree.GetLeaf('Particle.Eta').GetValue(j)
			phi= tree.GetLeaf('Particle.Phi').GetValue(j)
			mass = tree.GetLeaf('Particle.M').GetValue(j)
			pid = tree.GetLeaf('Particle.PID').GetValue(j)
			cand={'pt':pt, 'eta':eta, 'phi':phi,'mass':mass,'pid':pid}
			Particles.append(cand)
	return Particles

for count in range(test.GetEntries()):
	test.GetEntry(count)
	particles = getParticles(test)

	print particles[0]['pid']

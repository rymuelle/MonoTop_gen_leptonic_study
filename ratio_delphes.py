from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom, TClonesArray, TCanvas



f_RH_1           = TFile.Open("tag_1_delphes_events.root", "read")




test = f_RH_1.Get("Delphes")

c1 = TCanvas()


def getMuons(tree):
	nMuons = tree.GetLeaf('Muon_size').GetValue()
	Muons=[]
	for j in range(int(nMuons)):
			pt = test.GetLeaf('Muon.PT').GetValue(j)
			eta = tree.GetLeaf('Muon.Eta').GetValue(j)
			phi= tree.GetLeaf('Muon.Phi').GetValue(j)
			
		
			cand={'pt':pt, 'eta':eta, 'phi':phi,}
			Muons.append(cand)
	return Muons

def getElectrons(tree):
	nElectrons = tree.GetLeaf('Electron_size').GetValue()
	Electrons=[]
	for j in range(int(nElectrons)):
			pt = test.GetLeaf('Electron.PT').GetValue(j)
			eta = tree.GetLeaf('Electron.Eta').GetValue(j)
			phi= tree.GetLeaf('Electron.Phi').GetValue(j)
			
		
			cand={'pt':pt, 'eta':eta, 'phi':phi,}
			Electrons.append(cand)
	return Electrons


def getJets(tree):
	nJets = tree.GetLeaf('Jet_size').GetValue()
	Jets=[]
	for j in range(int(nJets)):
			pt = test.GetLeaf('Jet.PT').GetValue(j)
			eta = tree.GetLeaf('Jet.Eta').GetValue(j)
			phi= tree.GetLeaf('Jet.Phi').GetValue(j)
			mass = tree.GetLeaf('Jet.Mass').GetValue(j)
			btag = tree.GetLeaf('Jet.BTag').GetValue(j)
		
			cand={'pt':pt, 'eta':eta, 'phi':phi,'mass':mass, 'btag':btag}
			Jets.append(cand)
	return Jets

def returnHistogram(test, name):
	TH1F_ratio = TH1F("TH1F_ratio_{}".format(name), "TH1F_ratio_{}".format(name), 10, 0, 1)

	for count in range(test.GetEntries()):
		muon_pt = 0
		electron_pt = 0
		jet_pt = 0
	
		test.GetEntry(count)
		jets = getJets(test)
		muons = getMuons(test)
		electrons = getElectrons(test)
	
		for jet in jets:
			if jet['btag'] == 1:
				#print count, jet['pt'], jet['btag']
				jet_pt = jet['pt']
				break
	
		for muon in muons:
			#print count, muon['pt']
			muon_pt = muon['pt']
			break
	
		for electron in electrons:
			#print count, electron['pt']
			electron_pt = electron['pt']
			break
	
		if muon_pt*jet_pt > 0:
			print jet_pt/(jet_pt+muon_pt)
			TH1F_ratio.Fill(jet_pt/(jet_pt+muon_pt))
		elif electron_pt*jet_pt > 0:
			print jet_pt/(jet_pt+electron_pt)
			TH1F_ratio.Fill(jet_pt/(jet_pt+electron_pt))
	return TH1F_ratio


one_tev = returnHistogram(test, "1TeV")
one_tev.Draw()
c1.SaveAs("one_tev.png")

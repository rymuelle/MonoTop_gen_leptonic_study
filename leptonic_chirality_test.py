from ROOT import TFile, TTree, TH1F, TLorentzVector, TMath, TRandom, TClonesArray
import ROOT
from random import randint
import math, sys, os
from math import fabs
from histogrammar import *
from root_numpy import  tree2array, array2tree
from root_numpy import fill_hist
import numpy


Bundle = UntypedLabel



f_RH_1           = TFile.Open("1TeV_RH.root", "read")
f_LH_1           = TFile.Open("1TeV_LH.root", "read")
f_RH_5           = TFile.Open("5TeV_RH.root", "read")
f_LH_5           = TFile.Open("5TeV_LH.root", "read")

tree = []
tree.append( (f_RH_1.Get("LHEF"), "RH_1TeV") )
tree.append( (f_LH_1.Get("LHEF"), "LH_1TeV") )
tree.append( (f_RH_5.Get("LHEF"), "RH_5TeV") )
tree.append( (f_LH_5.Get("LHEF"), "LH_5TeV") )

test = f_RH_1.Get("LHEF")

#test.GetListOfBranches().ls()


def getParticle(tree,j):
	pt = tree.GetLeaf('Particle.PT').GetValue(j)
	eta = tree.GetLeaf('Particle.Eta').GetValue(j)
	phi= tree.GetLeaf('Particle.Phi').GetValue(j)
	mass = tree.GetLeaf('Particle.M').GetValue(j)
	pid = tree.GetLeaf('Particle.PID').GetValue(j)
	cand={'pt':pt, 'eta':eta, 'phi':phi,'mass':mass,'pid':pid}
	return cand


def getParticles(tree):
  nParticles = tree.GetLeaf('Particle_size').GetValue()
  Particles=[]
  for j in range(int(nParticles)):
    Particle = getParticle(tree,j)
    if Particle:
      Particles.append(Particle)
  return Particles

for count in range(test.GetEntries()):
	test.GetEntry(count)
	particle = getParticles(test)
	nParticles = test.GetLeaf('Particle_size').GetValue()
	for j in range(int(nParticles)):
		pt = test.GetLeaf('Particle.PT').GetValue(j)
		print pt


	#nParticles = test.GetLeaf('Particle_size').GetValue()
	#pt = test.GetLeaf('Particle.M').GetValue(count)
	#print particle[0]['mass']


#chain = ROOT.TChain("Delphes")
#chain.Add("1TeV_RH.root")
#
#ROOT.gSystem.Load("lib/libExRootAnalysis.so")
#
#treeReader = ROOT.ExRootTreeReader(chain)
#numberOfEntries = treeReader.GetEntries()


##t_RH_1	= f_RH_1.Get("LHEF")
##t_LH_1	= f_LH_1.Get("LHEF")
##t_RH_5	= f_RH_5.Get("LHEF")
##t_LH_5	= f_LH_5.Get("LHEF")
#
#print tree[3][1]
#
#top_pt = []
#
#l_over_t = []
#
#
#par= TClonesArray("TParticle",100)
#test.SetBranchAddress("Particle",par)
#
##pt = []
##test.SetBranchAddress("Particle.PT",pt)
#
#for event in test:
#	entries = event.Particle
#	#print test.Particle.GetEntries
#	print test.GetEntries()
#	print pt
#	#print entries	
#	#for particle in test.Particle:
#	#	print particle.PT
#
#
#

#for counter, event in enumerate(test):
#	print event.Event
#	for counter, particle in enumerate(event.Event):
#		print particle



#for case in enumerate(tree):
#	top_pt.append( TH1F("top_pt_{}".format(case[1]), "top_pt_{}".format(case[1]), 100, 0, 6000))
#	l_over_t.append( TH1F("l_over_t_{}".format(case[1]), "l_over_t_{}".format(case[1]), 100, 0, 1))
#
#
#
#for event in enumerate(tree[0][0]):
#	print event[1].Event[0]

#for case in enumerate(tree):
#	print case[1][0]
#	for event in enumerate(case[1][0]):
#		print event[1].Event


#zfor 

#array = tree2array(t_RH_1,
#    branches=[	'Particle.PID'],
#    start=0, stop=-1, step=1)
#
#
#
#
#
#standard_histograms = Select( lambda array: numpy.logical_or(array['Particle.PID'] == 6 ,abs(array['Particle.PID']) == -6), Bundle(
#
#
#test = Bin(	100, 0, 6000,
#	lambda array : (array['Particle.PID'], Count() ))
#
#))
#
#standard_histograms.fill.numpy(array)
#
#print array

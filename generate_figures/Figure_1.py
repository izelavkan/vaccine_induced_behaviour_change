# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 11:24:40 2025

@author: ewanc
"""

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,2.5))
gs = fig.add_gridspec(1,2)
plt.subplots_adjust(hspace=0.5,wspace=0.5)

x_values=[i/100 for i in range(300)]


line={0:[min(x,1) for x in x_values],1:[1-((2/(x+2))**2) for x in x_values]}#
title={0:'Homogeneous mixing\n(independent of vaccination status)',1:'Heterogeneous mixing\n(dependent on vaccination status)'}

for i in range(2):
    ax=fig.add_subplot(gs[0,i])
    plt.xlim([0,2])
    plt.ylim([0,1])
    plt.yticks([0,0.5,1],[0,50,100])
    plt.xlabel('Effect on behaviour\n(% increase in contact per 1% of\n popultion vaccinated)')
    plt.ylabel('Vaccine effectiveness (%)')
    plt.plot(x_values,line[i],c='k',linewidth=3)
    plt.fill_between(x_values,[0 for i in x_values],line[i],color='aliceblue')
    plt.fill_between(x_values,[1 for i in x_values],line[i],color='lavender')
    plt.text(0.05,0.75,'$R_{eff}$\ndecreases')
    plt.text(1,0.1,'$R_{eff}$ increases')
    plt.title(title[i],size=10)
    
plt.savefig('Fig_1.png',format='png',dpi=300,bbox_inches='tight')

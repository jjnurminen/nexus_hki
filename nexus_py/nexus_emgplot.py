# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:25:38 2015

EMG plot from Nexus.

@author: Jussi
"""

from gait_plot import gaitplotter
import gaitplotter_plots

layout = [8,2]
maintitleprefix = 'EMG plot for '
pdftitlestr = 'EMG_'

nplotter = gaitplotter(layout)
plotvars = gaitplotter_plots.std_emg
nplotter.open_nexus_trial()
nplotter.read_trial(plotvars)
trialname = nplotter.trial.trialname
maintitle = maintitleprefix + trialname
maintitle = maintitle + '\n' + nplotter.get_emg_filter_description()
nplotter.plot_trial(maintitle=maintitle)
#nplotter.create_pdf(pdf_prefix=pdftitlestr)

nplotter.show()




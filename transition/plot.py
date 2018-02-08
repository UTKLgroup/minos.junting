from rootalias import *

FIGURE_DIR = '/Users/juntinghuang/beamer/20180131_transition_richa/figures'
DATA_DIR = './data'


def subtract_min(hs):
    bin_count = hs.GetNbinsX()
    bin_min = hs.GetMinimum()
    for i in range(1, bin_count + 1):
        hs.SetBinContent(i , hs.GetBinContent(i) - bin_min)


def plot_g():
    f_stat_syst = TFile('{}/GStatsSyst_mc_allRuns_0.root'.format(DATA_DIR))
    f_stat = TFile('{}/GStats_mc_allRuns_0.root'.format(DATA_DIR))

    h_stat_syst = f_stat_syst.Get('hsurface1')
    h_stat = f_stat.Get('hsurface1')

    subtract_min(h_stat_syst)
    subtract_min(h_stat)

    bin_count = h_stat_syst.GetNbinsX()
    h_stat_syst_scale = TH1D('h_stat_syst_scale', 'h_stat_syst_scale', bin_count, 0, 10)
    h_stat_scale = TH1D('h_stat_scale', 'h_stat_scale', bin_count, 0, 10)

    for i in range(1, bin_count + 1):
        h_stat_syst_scale.SetBinContent(i, h_stat_syst.GetBinContent(i))
        h_stat_scale.SetBinContent(i, h_stat.GetBinContent(i))

    c1 = TCanvas('c1', 'c1', 800, 600)
    set_margin()
    gStyle.SetOptStat(0)
    set_h1_style(h_stat_syst_scale)
    h_stat_syst_scale.Draw()

    h_stat_syst_scale.GetYaxis().SetRangeUser(0, 10)
    h_stat_syst_scale.GetXaxis().SetRangeUser(0, 5)
    h_stat_syst_scale.GetXaxis().SetTitle('|#tilde g^{ZT}_{#mu#bar#mu}| or |#tilde g^{ZT}_{#tau#bar#tau}| (#times 10^{-23})')
    h_stat_syst_scale.GetYaxis().SetTitle('-2 #Deltalog #lambda')

    set_h1_style(h_stat_scale)
    h_stat_scale.SetLineColor(kRed + 1)
    h_stat_scale.Draw('sames')

    lg1 = TLegend(.19, .53, .43, .65)
    set_legend_style(lg1)
    lg1.SetTextSize(23)
    lg1.AddEntry(h_stat_scale, 'Statistics Only', 'l')
    lg1.AddEntry(h_stat_syst_scale, 'With Systematics', 'l')
    lg1.Draw()

    tl_1_sigma = TLine(0, 1, 5, 1)
    tl_1_sigma.SetLineStyle(2)
    tl_1_sigma.Draw('same')
    tl_2_sigma = TLine(0, 4, 5, 4)
    tl_2_sigma.SetLineStyle(2)
    tl_2_sigma.Draw('same')
    tl_3_sigma = TLine(0, 9, 5, 9)
    tl_3_sigma.SetLineStyle(2)
    tl_3_sigma.Draw('same')

    tlatex = TLatex()
    tlatex.SetTextFont(43)
    tlatex.SetTextSize(23)

    tlatex.DrawLatex(.15, 1.2, '1 #sigma')
    tlatex.DrawLatex(.15, 4.2, '2 #sigma')
    tlatex.DrawLatex(.15, 9.2, '3 #sigma')

    tlatex.DrawLatex(0.3, 8, "10.56 #times10^{20} POT, #nu_{#mu}-mode")
    tlatex.DrawLatex(0.3, 7, " MINOS Sensitivity")

    preliminary = TLatex()
    preliminary.SetTextAlign(22)
    preliminary.SetTextFont(43)
    preliminary.SetTextSize(28)
    preliminary.SetTextColor(kRed)
    preliminary.DrawLatex(3.8, 0.6, "MINOS PRELIMINARY")

    c1.Update()
    c1.SaveAs('{}/plot.pdf'.format(FIGURE_DIR))
    input('Press any key to continue.')



plot_g()

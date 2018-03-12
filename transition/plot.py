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
    # f_stat = TFile('{}/GStats_mc_allRuns_0.fix_sn2_dm2.root'.format(DATA_DIR))

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

    x_max = 5.
    h_stat_syst_scale.GetYaxis().SetRangeUser(0, 10)
    h_stat_syst_scale.GetXaxis().SetRangeUser(0, x_max)
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

    tl_1_sigma = TLine(0, 1, x_max, 1)
    tl_1_sigma.SetLineStyle(2)
    tl_1_sigma.Draw()
    tl_2_sigma = TLine(0, 4, x_max, 4)
    tl_2_sigma.SetLineStyle(2)
    tl_2_sigma.Draw()
    tl_3_sigma = TLine(0, 9, x_max, 9)
    tl_3_sigma.SetLineStyle(2)
    tl_3_sigma.Draw()

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
    preliminary.DrawLatex(1.6, 9.5, "MINOS Preliminary")

    c1.Update()
    c1.SaveAs('{}/plot_g.pdf'.format(FIGURE_DIR))
    input('Press any key to continue.')


def plot_c():
    f_stat_syst = TFile('{}/CMuStatsSyst_mc_allRuns_0.root'.format(DATA_DIR))
    f_stat = TFile('{}/CMuStats_mc_allRuns_0.root'.format(DATA_DIR))

    h_stat_syst = f_stat_syst.Get('hsurface1')
    h_stat = f_stat.Get('hsurface1')

    subtract_min(h_stat_syst)
    subtract_min(h_stat)

    bin_count = h_stat.GetNbinsX()
    print('bin_count = {}'.format(bin_count))
    print('h_stat.GetBinLowEdge(bin_count) + h_stat.GetBinWidth(bin_count) = {}'.format(h_stat.GetBinLowEdge(bin_count) + h_stat.GetBinWidth(bin_count)))
    print('h_stat.GetBinLowEdge(1) = {}'.format(h_stat.GetBinLowEdge(1)))

    h_stat_syst_scale = TH1D('h_stat_syst_scale', 'h_stat_syst_scale', bin_count, -9.9, 10)
    h_stat_scale = TH1D('h_stat_scale', 'h_stat_scale', bin_count, -9.9, 10)
    for i in range(1, bin_count + 1):
        h_stat_syst_scale.SetBinContent(i, h_stat_syst.GetBinContent(i))
        h_stat_scale.SetBinContent(i, h_stat.GetBinContent(i))

    c1 = TCanvas('c1', 'c1', 800, 600)
    set_margin()
    gStyle.SetOptStat(0)

    set_h1_style(h_stat_scale)
    h_stat_scale.SetLineColor(kRed + 1)
    h_stat_scale.Draw()
    h_stat_scale.GetXaxis().SetRangeUser(-9, 9)
    h_stat_scale.GetYaxis().SetRangeUser(0, 10)
    h_stat_scale.GetXaxis().SetTitle('(c_{L})_{#mu#mu}^{TT} or -(c_{L})_{#tau#tau}^{TT} (#times 10^{-23})')
    h_stat_scale.GetYaxis().SetTitle('-2 #Deltalog #lambda')

    set_h1_style(h_stat_syst_scale)
    h_stat_syst_scale.Draw('sames')

    lg1 = TLegend(0.34, 0.57, 0.59, 0.69)
    set_legend_style(lg1)
    lg1.SetTextSize(23)
    lg1.AddEntry(h_stat_scale, 'Statistics Only', 'l')
    lg1.AddEntry(h_stat_syst_scale, 'With Systematics', 'l')
    lg1.Draw()

    x_min = -9
    x_max = 9
    tl_1_sigma = TLine(x_min, 1, x_max, 1)
    tl_1_sigma.SetLineStyle(2)
    tl_1_sigma.Draw()
    tl_2_sigma = TLine(x_min, 4, x_max, 4)
    tl_2_sigma.SetLineStyle(2)
    tl_2_sigma.Draw()
    tl_3_sigma = TLine(x_min, 9, x_max, 9)
    tl_3_sigma.SetLineStyle(2)
    tl_3_sigma.Draw()

    tlatex = TLatex()
    tlatex.SetTextFont(43)
    tlatex.SetTextSize(23)

    tlatex.DrawLatex(-8.5, 1.2, '1 #sigma')
    tlatex.DrawLatex(-8.5, 4.2, '2 #sigma')
    tlatex.DrawLatex(-8.5, 9.2, '3 #sigma')

    tlatex.DrawLatex(-4.2, 8.2, "10.56 #times10^{20} POT, #nu_{#mu}-mode")
    tlatex.DrawLatex(-4.2, 7.4, " MINOS Sensitivity")

    preliminary = TLatex()
    preliminary.SetTextAlign(22)
    preliminary.SetTextFont(43)
    preliminary.SetTextSize(28)
    preliminary.SetTextColor(kRed)
    preliminary.DrawLatex(0, 9.5, "MINOS Preliminary")

    c1.Update()
    c1.SaveAs('{}/plot_c.pdf'.format(FIGURE_DIR))
    input('Press any key to continue.')


def get_axis_func():
    x_limit = 20
    compress = 2.5
    form = '(x <= {0}) * x + (x > {0}) * ({0} + (x - {0}) / {1})'.format(x_limit, compress)
    f_axis = TF1('f_axis', form, 0, 50)
    return f_axis


def plot_spectrum_nubar():
    f_nubar = TFile('data/spectrum.std_osc.root')
    f_nubar_g = TFile('data/spectrum.g_3.4e-23.root')
    f_nubar_c = TFile('data/spectrum.c_6e-23.root')

    h_nubar = f_nubar.Get('hNubar')
    h_nubar_g = f_nubar_g.Get('hNubar')
    h_nubar_c = f_nubar_c.Get('hNubar')

    c1 = TCanvas('c1', 'c1', 800, 800)
    set_margin()

    gStyle.SetOptStat(0)
    set_h1_style(h_nubar)
    h_nubar.Draw()
    h_nubar.GetYaxis().SetRangeUser(0, 50)
    h_nubar.SetXTitle("Reconstructed #bar{#nu}_{#mu} Energy (GeV)")
    h_nubar.SetYTitle("Events / 2 GeV")
    h_nubar.SetTitle('')
    h_nubar.GetXaxis().SetLabelSize(0)
    h_nubar.SetLineWidth(0)

    gr_nubar = get_graph_from_hist(h_nubar)
    set_graph_style(gr_nubar)
    gr_nubar.SetMarkerColor(1)
    gr_nubar.SetMarkerStyle(20)
    gr_nubar.SetMarkerSize(1)
    gr_nubar.SetLineWidth(3)
    gr_nubar.Draw('sames,pz')

    set_h1_style(h_nubar_g)
    h_nubar_g.SetLineColor(kRed)
    h_nubar_g.SetLineStyle(2)
    h_nubar_g.SetLineWidth(3)
    h_nubar_g.Draw('sames')

    set_h1_style(h_nubar_c)
    h_nubar_c.SetLineColor(kBlue)
    h_nubar_c.SetLineStyle(2)
    h_nubar_c.SetLineWidth(3)
    h_nubar_c.Draw('sames')

    lg1 = TLegend(0.46, 0.55, 0.76, 0.78)
    set_legend_style(lg1)
    lg1.SetHeader('Far Detector Prediction')
    lg1.AddEntry(gr_nubar, 'g = 0, c = 0', 'lep')
    lg1.AddEntry(h_nubar_g, 'g = 3.4 #times 10^{-23}, c = 0', 'l')
    lg1.AddEntry(h_nubar_c, 'g = 0, c = 6 #times 10^{-23}', 'l')
    lg1.Draw()

    tlatex = TLatex()
    tlatex.SetTextFont(43)
    tlatex.SetTextSize(28)
    tlatex.DrawLatex(13.5, 42.5, "10.56 #times10^{20} POT, #nu_{#mu}-mode")

    preliminary = TLatex()
    preliminary.SetTextAlign(22)
    preliminary.SetTextFont(43)
    preliminary.SetTextSize(28)
    preliminary.SetTextColor(kRed)
    preliminary.DrawLatex(7.6, 47, "MINOS Preliminary")

    gPad.Update()
    gPad.SetTicky()

    x_limit = 20
    xmax = gPad.GetUxmax()
    ymin = gPad.GetUymin()
    ymax = gPad.GetUymax()

    div = 510
    f_axis = get_axis_func()
    axis_bottom = TGaxis(0, ymin, xmax, ymin, 'f_axis', div)
    axis_bottom.SetLabelSize(0)
    axis_bottom.Draw()
    axis_top = TGaxis(0, ymax, xmax, ymax, 'f_axis', div, '-')
    axis_top.SetLabelSize(0)
    axis_top.Draw()

    latex_labels = []
    label = 0
    for i in range(20):
        if label > 50:
            break

        latex_label = TLatex(f_axis.Eval(label), ymin - 0.025 * (ymax - ymin), '{}'.format(label))
        latex_label.SetTextAlign(23)
        latex_label.SetTextFont(43)
        latex_label.SetTextSize(28)
        latex_labels.append(latex_label)
        latex_labels[i].Draw()

        if label < x_limit:
            label += 5
        else:
            label += 10

    c1.Update()
    c1.SaveAs('{}/plot_spectrum_nubar.pdf'.format(FIGURE_DIR))
    input('Press any key to continue.')


def plot_spectrum_nu():
    f_nu = TFile('data/spectrum.std_osc.root')
    f_nu_g = TFile('data/spectrum.g_3.4e-23.root')
    f_nu_c = TFile('data/spectrum.c_6e-23.root')

    h_nu = f_nu.Get('hNu')
    h_nu_g = f_nu_g.Get('hNu')
    h_nu_c = f_nu_c.Get('hNu')

    h_nu.Scale(0.25)
    h_nu_g.Scale(0.25)
    h_nu_c.Scale(0.25)

    c1 = TCanvas('c1', 'c1', 800, 800)
    set_margin()

    gStyle.SetOptStat(0)
    set_h1_style(h_nu)
    h_nu.Draw()
    h_nu.GetYaxis().SetRangeUser(0, 125)
    h_nu.SetXTitle("Reconstructed #nu_{#mu} Energy (GeV)")
    h_nu.SetYTitle("Events / 0.25 GeV")
    h_nu.SetTitle('')
    h_nu.GetXaxis().SetLabelSize(0)
    h_nu.SetLineWidth(0)

    gr_nu = get_graph_from_hist(h_nu)
    set_graph_style(gr_nu)
    gr_nu.SetMarkerColor(1)
    gr_nu.SetMarkerStyle(20)
    gr_nu.SetMarkerSize(1)
    gr_nu.SetLineWidth(3)
    gr_nu.Draw('sames,pz')

    set_h1_style(h_nu_g)
    h_nu_g.SetLineColor(kRed)
    h_nu_g.SetLineStyle(2)
    h_nu_g.SetLineWidth(3)
    h_nu_g.Draw('sames')

    set_h1_style(h_nu_c)
    h_nu_c.SetLineColor(kBlue)
    h_nu_c.SetLineStyle(2)
    h_nu_c.SetLineWidth(3)
    h_nu_c.Draw('sames')

    lg1 = TLegend(0.46, 0.47, 0.76, 0.7)
    set_legend_style(lg1)
    lg1.SetHeader('Far Detector Prediction')
    lg1.AddEntry(gr_nu, 'g = 0, c = 0', 'lep')
    lg1.AddEntry(h_nu_g, 'g = 3.4 #times 10^{-23}, c = 0', 'l')
    lg1.AddEntry(h_nu_c, 'g = 0, c = 6 #times 10^{-23}', 'l')
    lg1.Draw()

    tlatex = TLatex()
    tlatex.SetTextFont(43)
    tlatex.SetTextSize(28)
    tlatex.DrawLatex(7.5, 93.5, "10.56 #times10^{20} POT, #nu_{#mu}-mode")

    preliminary = TLatex()
    preliminary.SetNDC()
    preliminary.SetTextAlign(22)
    preliminary.SetTextFont(43)
    preliminary.SetTextSize(28)
    preliminary.SetTextColor(kRed)
    preliminary.DrawLatex(0.72, 0.86, "MINOS Preliminary")

    gPad.Update()
    gPad.SetTicky()

    tick = 0.04
    h_nu.GetXaxis().SetTickLength(0)

    for top in range(1):
        print('top = {}'.format(top))

        gPad.Update();
        y = gPad.GetUymax() if top else 0
        sn = "SN-" if top else "SN+"

        gaxis_1 = TGaxis(0, y, 10, y, 0, 10, 502, sn)
        gaxis_1.SetLabelSize(h_nu.GetYaxis().GetLabelSize())
        gaxis_1.SetLabelFont(h_nu.GetYaxis().GetLabelFont())
        gaxis_1.SetTickSize(18 / 10. * tick)
        gaxis_1.Draw()

        gaxis_2 = TGaxis(10, y, 14, y, 10, 20, 502, sn)
        gaxis_2.SetLabelSize(0)
        gaxis_2.SetTickSize(18 / 4. * tick)
        gaxis_2.Draw()

        gaxis_3 = TGaxis(14, y, 18, y, 20, 50, 2, sn)
        gaxis_3.SetLabelSize(0)
        gaxis_3.SetTickSize(18 / 4. * tick)
        gaxis_3.Draw()

        gaxis_4 = TGaxis(12, y, 14, y, 15, 20, 1, sn)
        gaxis_4.SetTickSize(0)
        gaxis_4.SetLabelSize(h_nu.GetYaxis().GetLabelSize())
        gaxis_4.SetLabelFont(h_nu.GetYaxis().GetLabelFont())
        gaxis_4.Draw()

        gaxis_5 = TGaxis(16, y, 18, y, 30, 50, 1, sn)
        gaxis_5.SetTickSize(0)
        gaxis_5.SetLabelSize(h_nu.GetYaxis().GetLabelSize())
        gaxis_5.SetLabelFont(h_nu.GetYaxis().GetLabelFont())
        gaxis_5.Draw()

    c1.Update()
    c1.SaveAs('{}/plot_spectrum_nu.pdf'.format(FIGURE_DIR))
    input('Press any key to continue.')


# 20180131_transition_richa
# plot_g()
# plot_c()
# plot_spectrum_nubar()
plot_spectrum_nu()

def ROI():
    annualprofit=float(input("Annual Site profit: "))
    ccr=float(input("Current Conversion Rate: "))
    icr=float(input("Improved Conversion RAte: "))
    ic=float(input("Improvement Cost: "))
    epl=float(input("Expected Project life (in years): "))
    i=0.05
    # fgp= Future Gain From Improvement
    fgi= annualprofit * (icr/ccr) - annualprofit * (((1+i) ** epl) - 1) / i-ic * ((1+i) ** epl)

    # tgi=Total Gain from Improvement
    tgi=fgi/(1+i)**epl

    # agi = Annual gain From Improvement
    agi=tgi/epl

    annual_ROI=agi/ic
    total_ROI=tgi/ic

    print("Annual ROI:", annual_ROI)
    print("Total ROI:", total_ROI)

ROI()
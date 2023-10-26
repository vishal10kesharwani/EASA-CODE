 return render_template('hoddashboard.html',
                               ttf=teachers_total_feedbacks, ttpf=teachers_total_positive_feedbacks,
                               ttnegf=teachers_total_negative_feedbacks,
                               ttneuf=teachers_total_neutral_feedbacks, ttp=ttp, ttn=ttn, ttneu=ttneu, tcp=tcp, tcn=tcn,
                               tcneu=tcneu, tep=tep, ten=ten, teneu=teneu, tlwp=tlwp, tlwn=tlwn,
                               tlwneu=tlwneu, tlfp=tlfp, tlfn=tlfn, tlfneu=tlfneu, tecp=tecp, tecn=tecn, tecneu=tecneu
                               )
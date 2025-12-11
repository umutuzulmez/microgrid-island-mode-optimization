Sets
    t /1*24/ ;

Parameters
    PV_kW(t)    
    WT_kW(t);

PV_kW('1')  = 0;
PV_kW('2')  = 0;
PV_kW('3')  = 0;
PV_kW('4')  = 0;
PV_kW('5')  = 0;
PV_kW('6')  = 0.019;
PV_kW('7')  = 0.113;
PV_kW('8')  = 0.304;
PV_kW('9')  = 0.475;
PV_kW('10') = 0.603;
PV_kW('11') = 0.685;
PV_kW('12') = 0.723;
PV_kW('13') = 0.719;
PV_kW('14') = 0.673;
PV_kW('15') = 0.586;
PV_kW('16') = 0.456;
PV_kW('17') = 0.290;
PV_kW('18') = 0.113;
PV_kW('19') = 0.015;
PV_kW('20') = 0;
PV_kW('21') = 0;
PV_kW('22') = 0;
PV_kW('23') = 0;
PV_kW('24') = 0;

WT_kW('1')  = 0.035;
WT_kW('2')  = 0.112;
WT_kW('3')  = 0.179;
WT_kW('4')  = 0.239;
WT_kW('5')  = 0.295;
WT_kW('6')  = 0.337;
WT_kW('7')  = 0.362;
WT_kW('8')  = 0.272;
WT_kW('9')  = 0.238;
WT_kW('10') = 0.201;
WT_kW('11') = 0.152;
WT_kW('12') = 0.112;
WT_kW('13') = 0.080;
WT_kW('14') = 0.058;
WT_kW('15') = 0.042;
WT_kW('16') = 0.031;
WT_kW('17') = 0.029;
WT_kW('18') = 0.037;
WT_kW('19') = 0.057;
WT_kW('20') = 0.065;
WT_kW('21') = 0.105;
WT_kW('22') = 0.192;
WT_kW('23') = 0.243;
WT_kW('24') = 0.227;

Parameters
    PV_max(t)   
    WT_max(t);

PV_max(t)   = 200 * PV_kW(t);
WT_max(t) = 150 * WT_kW(t);

Parameters
    P_h(t)          
    P_sch(t)       
    P_ev(t) ;

P_h(t)   = 30 ;
P_sch(t) = 30$(ord(t) >= 9 and ord(t) <= 16) ; 
P_ev(t) = 30 + 60$(ord(t) >= 18 and ord(t) <= 23);

Scalar
    P_dg_max   /100/
    P_dg_min   /20/      
    P_b_ch_max /100/
    P_b_de_max /100/
    E_b_max    /500/
    E_b_init   /150/    
    eta_ch     /0.95/
    eta_de     /0.90/
    C_pv       /0.02/
    C_wt       /0.015/
    C_dg       /0.25/
    C_bch      /0.002/
    C_bde      /0.003/
    alpha      /0.1/
    EF_dg      /0.8/    ;

Variables
    p_pv(t), p_wt(t), p_dg(t)
    p_bch(t), p_bde(t), E_b(t)
    served_h(t), served_s(t), served_c(t)
    Obj ;

Binary Variable delta(t) ;   

Positive Variables p_pv, p_wt, p_dg, p_bch, p_bde,
                   served_h, served_s, served_c, E_b ;

Equations
    EnergyBalance(t), BatteryInit, BatteryDyn(t)
    ServedH_eq(t), ServedS_eq(t), ServedC_eq(t)
    PV_cap(t), WT_cap(t), DG_max_bound(t), DG_min_bound(t), B_ch_cap(t), B_de_cap(t)
    SOC_min(t), SOC_max(t), Obj_def ;

EnergyBalance(t).. 
    p_pv(t) + p_wt(t) + p_dg(t) + p_bde(t)
      =e= served_h(t) + served_s(t) + served_c(t) + p_bch(t);

BatteryInit.. E_b('1') =e= E_b_init;

BatteryDyn(t)$(ord(t) > 1).. E_b(t) =e= E_b(t-1) + eta_ch*p_bch(t) - (1/eta_de)*p_bde(t);

ServedH_eq(t).. served_h(t) =e= P_h(t);
ServedS_eq(t).. served_s(t) =e= P_sch(t);
ServedC_eq(t).. served_c(t) =e= P_ev(t);

PV_cap(t)..   p_pv(t) =l= PV_max(t);
WT_cap(t).. p_wt(t) =l= WT_max(t);
B_ch_cap(t).. p_bch(t) =l= P_b_ch_max;
B_de_cap(t).. p_bde(t) =l= P_b_de_max;

DG_max_bound(t).. p_dg(t) =l= P_dg_max * delta(t);
DG_min_bound(t).. p_dg(t) =g= P_dg_min * delta(t);

SOC_min(t).. E_b(t) =g= 0.20 * E_b_max ;
SOC_max(t).. E_b(t) =l= 0.90 * E_b_max ;

Obj_def.. Obj =e= sum(t,
       C_pv*p_pv(t) + C_wt*p_wt(t)
     + C_bde*p_bde(t) + C_bch*p_bch(t)
     + C_dg*p_dg(t));

Model Microgrid /all/ ;

loop(t,
   p_pv.lo(t) = 0;   p_pv.up(t) = PV_max(t);
   p_wt.lo(t) = 0; p_wt.up(t) = WT_max(t);
   p_dg.lo(t) = 0;   p_dg.up(t) = P_dg_max;
   served_c.lo(t) = 0; served_c.up(t) = P_ev(t);
   E_b.lo(t) = 0;    E_b.up(t) = E_b_max;
   p_bch.lo(t) = 0;  p_bch.up(t) = P_b_ch_max;
   p_bde.lo(t) = 0;  p_bde.up(t) = P_b_de_max;
   delta.lo(t) = 0; delta.up(t) = 1;
);

Solve Microgrid using MIP minimizing Obj ;

Scalar
    pv_total, wt_total, dg_total,
    served_h_total, served_s_total, served_c_total, 
    bch_total, bde_total, emissions_total ;

pv_total    = sum(t, p_pv.l(t));
wt_total  = sum(t, p_wt.l(t));
dg_total    = sum(t, p_dg.l(t));
served_h_total = sum(t, served_h.l(t));
served_s_total = sum(t, served_s.l(t));
served_c_total = sum(t, served_c.l(t));
bch_total   = sum(t, p_bch.l(t));
bde_total   = sum(t, p_bde.l(t));
emissions_total = sum(t, p_dg.l(t)) * EF_dg ;

display pv_total, wt_total, dg_total,
        served_h_total, served_s_total, served_c_total,
        bch_total, bde_total, emissions_total, Obj.l ;

file outf /s2_senaryo_antalya_2019-07-21.csv/;
put outf;
put "t,PV,WT,DG,p_bch,p_bde,E_b,served_h,served_s,served_c,delta"/;
loop(t,
   put t.tl:0 "," p_pv.l(t):8:4 "," p_wt.l(t):8:4 "," p_dg.l(t):8:4 "," 
       p_bch.l(t):8:4 "," p_bde.l(t):8:4 "," E_b.l(t):8:4 "," 
       served_h.l(t):8:4 "," served_s.l(t):8:4 "," served_c.l(t):8:4 "," 
       delta.l(t):2:0 /;
);
putclose outf;
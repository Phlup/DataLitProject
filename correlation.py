
from scipy.stats import spearmanr,pearsonr


vertrag=[(6, 'Erneuerbare'),
(14, 'Nachhaltigkeit'),
(16, 'Menschenrechte'),
(17, 'Bundeswehr'),
(21, 'Klimaschutz'),
(24, 'Vielfalt'),
(25, 'Frauen'),
(28, 'Kinder'),
(30, 'Bildung'),
(35, 'Forschung'),
(36, 'Wirtschaft'),
(43, 'Digitalisierung'),
(48, 'Arbeit')]


speeches=[(12.135, 'Arbeit') ,
(5.2725, 'Digitalisierung') ,
(7.746, 'Wirtschaft') ,
(2.7804, 'Forschung') ,
(4.496, 'Bildung') ,
(8.1969, 'Kinder') ,
(5.6165, 'Frauen') ,
(1.539, 'Vielfalt') ,
(3.2918, 'Klimaschutz') ,
(3.7939, 'Bundeswehr') ,
(3.0361, 'Menschenrechte') ,
(0.9578, 'Nachhaltigkeit'),
         (0.995, 'Erneuerbare')  ]

speeches_coal=[
    (12.4368, 'Arbeit') ,
(5.532, 'Digitalisierung') ,
(6.8015, 'Wirtschaft') ,
(2.6422, 'Forschung') ,
(4.5516, 'Bildung') ,
(8.6077, 'Kinder') ,
(6.0481, 'Frauen') ,
(1.8062, 'Vielfalt') ,
(4.0974, 'Klimaschutz') ,
(3.3234, 'Bundeswehr') ,
(3.2098, 'Menschenrechte') ,
(0.9392, 'Nachhaltigkeit') ,
(1.1869, 'Erneuerbare') ,

]

speeches_opo=[
    (11.8876, 'Arbeit') ,
(5.0596, 'Digitalisierung') ,
(8.5202, 'Wirtschaft') ,
(2.8936, 'Forschung') ,
(4.4505, 'Bildung') ,
(7.8602, 'Kinder') ,
(5.2627, 'Frauen') ,
(1.3199, 'Vielfalt') ,
(2.6314, 'Klimaschutz') ,
(4.1797, 'Bundeswehr') ,
(2.8936, 'Menschenrechte') ,
(0.973, 'Nachhaltigkeit') ,
    (0.8376, 'Erneuerbare') ,
]

vv=[x[0] for x in vertrag]
sv=[x[0] for x in speeches[::-1]]
sv_k=[x[0] for x in speeches_coal[::-1]]

sv_o=[x[0] for x in speeches_opo[::-1]]

print("total",spearmanr(vv,sv),pearsonr(vv,sv))
print("coalition",spearmanr(vv,sv_k),pearsonr(vv,sv_k))
print("oposition",spearmanr(vv,sv_o),pearsonr(vv,sv_o))

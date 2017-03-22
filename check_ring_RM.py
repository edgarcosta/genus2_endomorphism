import heuristic_endomorphisms
import lmfdb

from misc import convert_magma_matrix_to_sage
from sage.all import PolynomialRing, QQ, identity_matrix
#RM
from pymongo import ASCENDING
C = lmfdb.getDBconnection()
Qx = PolynomialRing(QQ, "x");
    
labels = list(c['label'] for c in C.genus2_curves.curves.find({'is_simple_geom': True,'real_geom_end_alg': u'R x R'}).sort([("cond", ASCENDING)]));
for label in labels:
    endo = lmfdb.get_endo(label)
    if endo['ring_geom'] != [1, -1]:
        print label
        assert  endo['ring_geom'] == [2, -1]
        print endo['lattice'][0][1]
        curve = lmfdb.get_curve('68121.c.613089.1')
        fmin, hmin = eval(curve['eqn'])
        g = 4*Qx(fmin) + Qx(hmin)**2
        E = heuristic_endomorphisms.EndomorphismData(g, prec = 300)
        print "EndomorphismData done!"

        a1, a2 = E.geometric_representations()[-1]
        if a1 == identity_matrix(4):
            Amagma = a2
        else:
            assert a2 == identity_matrix(4)
            Amagma = a1
        A = convert_magma_matrix_to_sage(Amagma, QQ);
        m = (A**2)[1][1]
        assert A**2 ==  m * identity_matrix(4)
        assert int(m) % 4 == 1
        A2 = convert_magma_matrix_to_sage(identity_matrix(4) + A, QQ)
        # checking that (1 + sqrt(m))/ 2 \notin Ring
        assert (A2 % 2) != 0
        print "Pass"
        print
        

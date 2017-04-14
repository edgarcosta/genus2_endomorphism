import sys
from sage.all import *
sys.path.append(".");
from process_curve import certify_heuristic
from heuristic_endomorphisms import *
QQx= PolynomialRing(QQ, "x")
g = QQx([1, 6, 9, 6, 18, 0, 5])

# with puiseux
E = EndomorphismData(g);
print "Verified with puiseux: %s" % E.geometric_representations_check()

print "Alternatively verifying working on tangent space"
print "it might take a while..."
sleep(1)
curve_dict, out, verified =  certify_heuristic(g)

print "Verified while working on the tangent space: %s" % verified

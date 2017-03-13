import sys
from sage.all import *
sys.path.append("/Users/edgarcosta/projects/endomorphisms/genus2_endomorphisms/");
from process_curve import certify_heuristic
from heuristic_endomorphisms import *
QQx= PolynomialRing(QQ, "x")
g = QQx([1, 6, 9, 6, 18, 0, 5])

# with puiseux
E = EndomorphismData(g);
print "Verified with puiseux: %s" % E.geometric_representations_check()

print "Alternatively verifying it in tangent space"
print "it might take a while..."
sleep(1)
print certify_heuristic(g, digits = 600, internalverbose = True)

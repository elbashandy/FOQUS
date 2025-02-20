from scipy import misc

class ResponseSurfaces:
    MARS, LINEAR, QUADRATIC, CUBIC, QUARTIC = range(5)
    SELECTIVE, GP, VAL_8, SVM, PWL, VAL_11, MARSBAG = range(6, 13)
    SOT, LEGENDRE, USER, VAL_17, KRIGING, VAL_19, KNN, RBF = range(14, 22)
    
    fullNames = ('MARS', 'Linear Regression', 'Quadratic Regression',
                 'Cubic Regression', 'Quartic Regression', None, None,
                 'Gaussian Process', None, 'Support Vector Machine',
                 None, None, 'MARS with Bagging', None, 'Sum of Trees',
                 'Legendre Polynomial Regression', 'User Regression', None, 'Kriging',
                 None, 'K Nearest Neighbors', 'Radial Basis Function')
    psuadeNames = ('MARS', 'linear', 'quadratic', 'cubic', 'quartic', None,
                   None, 'GP1', None, 'SVM', None, None, 'MARSBag', None,
                   'sum_of_trees', 'Legendre', 'user_regression', None, 'Kriging', None,
                   'KNN', 'RBF')

    polynomialEnums = [LINEAR, QUADRATIC, CUBIC, QUARTIC, LEGENDRE]

    @staticmethod
    def getFullName(num):
        if isinstance(num, basestring):
            num = ResponseSurfaces.getEnumValue(num)                
        return ResponseSurfaces.fullNames[num]

    @staticmethod
    def getPsuadeName(num):
        if num is None:
            return None
        else:
            return ResponseSurfaces.psuadeNames[num]

    @staticmethod
    def getInfo(num):
        return (ResponseSurfaces.fullNames[num], ResponseSurfaces.psuadeNames[num])

    @staticmethod
    def getEnumValue(name):
        if name is None:
            return None
        try:
            int(name)
            return name
        except ValueError:
            try:
                index = ResponseSurfaces.fullNames.index(name)
                return index
            except ValueError:
                index = ResponseSurfaces.psuadeNames.index(name)
                return index
    
    @staticmethod
    def getLegendreMaxOrder(nInputs, nSamples):
        p = 0
        m = nInputs
        while misc.comb(p+m,p) <= nSamples:
            p = p + 1
        p = p - 1  # revert p to last value that satisfies the "while" condition
                   # nSamples must be equal or larger than (p+m)!/(p!m!)     
        return p

    @staticmethod
    def getPolynomialMinSampleSize(nInputs, polynomialOrder):
        p = polynomialOrder
        m = nInputs
        return misc.comb(p+m,p)

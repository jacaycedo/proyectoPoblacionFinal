import numpy as np

# PARAMETROS
class Ecuaciones:
    def __init__(self, k, ai, ae, gamma, b, p, m):
        self.k = k
        self.ai = ai
        self.ae = ae
        self.gamma = gamma
        self.b = b
        self.p = p
        self.m = m

    #METODOS PARA MODIFICAR LOS VALORES DE LAS VARIABLES SEGUN EL CASO
    def setk(self, k):
        self.k = k
    def setai(self,ai):
        self.ai=ai
    def setae(self,ae):
        self.ae=ae
    def setgamma(self,gamma):
        self.gamma=gamma
    def setb(self,b):
        self.b = b
    def setp(self, p):
        self.p = p
    def setm(self,m):
        self.m = m

    def ds (self, s, e, i, r):
        return -(self.ae *s*e) - (self.ai*s*i) + (self.gamma*r)

    def de(self,s, e, i):
        return (self.ae*s*e) + (self.ai*s*i) - (self.k*e) - (self.p*e)

    def di(self,e ,i):
        return (self.k*e) - (self.b*i) - (self.m*i)

    def dr(self,i,e,r):
        return (self.b*i) + (self.p*e) -(self.gamma*r)

    def dp(self,i) :
        return self.m * i


    def eulerForward(self, h, t0, t1):
        T = np.arange(t0, t1, h)
        SEulerFor = np.zeros(len(T))
        EEulerFor = np.zeros(len(T))
        IEulerFor = np.zeros(len(T))
        REulerFor = np.zeros(len(T))
        PEulerFor = np.zeros(len(T))
        SEulerFor[0] = 0.99
        EEulerFor[0] = 0
        IEulerFor[0] = 0.01
        REulerFor[0] = 0
        PEulerFor[0] = 0
        for iter in range(1, len(T)):
            SEulerFor[iter] = SEulerFor[iter - 1] + \
                        h * self.ds(SEulerFor[iter-1], EEulerFor[iter-1], IEulerFor[iter-1], REulerFor[iter-1])
            EEulerFor[iter] = EEulerFor[iter-1] + \
                        h * self.de(SEulerFor[iter-1], EEulerFor[iter-1], IEulerFor[iter-1])
            IEulerFor[iter] = IEulerFor[iter-1] + \
                        h * self.di(EEulerFor[iter-1], IEulerFor[iter-1])
            REulerFor[iter] = REulerFor[iter-1] + \
                            h * self.dr(IEulerFor[iter-1],EEulerFor[iter-1],REulerFor[iter-1])
            PEulerFor[iter-1] = PEulerFor[iter-1] + \
                            h * self.dp(IEulerFor[iter-1])
        
        return SEulerFor,EEulerFor,IEulerFor,REulerFor,PEulerFor

    def RK2(self, h, t0, t1):
        T = np.arange(t0, t1, h)
        SRK2 = np.zeros(len(T))
        ERK2 = np.zeros(len(T))
        IRK2 = np.zeros(len(T))
        RRK2 = np.zeros(len(T))
        PRK2 = np.zeros(len(T))

        SRK2[0] = 0.99
        ERK2[0] = 0
        IRK2[0] = 0.01
        RRK2[0] = 0
        PRK2[0] = 0

        for iter in range(1, len(T)):
            #Primera K
            K1S = self.ds(SRK2[iter-1],ERK2[iter-1],IRK2[iter-1],RRK2[iter-1])
            K1E = self.de(SRK2[iter-1], ERK2[iter-1],IRK2[iter-1])
            K1I = self.di(ERK2[iter-1],IRK2[iter-1])
            K1R = self.dr(IRK2[iter-1],ERK2[iter-1],RRK2[iter-1])
            K1P = self.dp(IRK2[iter-1])

            #Segunda K
            K2S = self.ds(SRK2[iter-1] + h*K1S, ERK2[iter-1] + h*K1E, IRK2[iter-1]+ h*K1I, RRK2[iter-1] + h*K1R)
            K2E = self.de(SRK2[iter-1] + h*K1S, ERK2[iter-1] + h*K1E, IRK2[iter-1]+ h*K1I)
            K2I = self.di(ERK2[iter-1] + h*K1E, IRK2[iter-1] + h*K1I)
            K2R = self.dr(IRK2[iter-1] + h*K1I, ERK2[iter-1] + h*K1E, RRK2[iter-1] + h*K1R)
            K2P = self.dp(IRK2[iter-1] + h*K1I)
            
            #Valor final
            SRK2[iter] = SRK2[iter-1] + (h/2.0) * (K1S + K2S)
            ERK2[iter] = ERK2[iter-1] + (h/2.0) * (K1E + K2E)
            IRK2[iter] = IRK2[iter-1] + (h/2.0) * (K1I + K2I)
            RRK2[iter] = RRK2[iter-1] + (h/2.0) * (K1R + K2R)
            PRK2[iter] = PRK2[iter-1] + (h/2.0) * (K1P + K2P)

        return SRK2, ERK2, IRK2, RRK2, PRK2
    
    def RK4(self, h, t0, t1):
        T = np.arange(t0, t1, h)
        SRK4 = np.zeros(len(T))
        ERK4 = np.zeros(len(T))
        IRK4 = np.zeros(len(T))
        RRK4 = np.zeros(len(T))
        PRK4 = np.zeros(len(T))

        SRK4[0] = 0.99
        ERK4[0] = 0
        IRK4[0] = 0.01
        RRK4[0] = 0
        PRK4[0] = 0

        for iter in range(1, len(T)):
            #Primera K
            K1S = self.ds(SRK4[iter-1], ERK4[iter-1], IRK4[iter-1], RRK4[iter-1])
            K1E = self.de(SRK4[iter-1], ERK4[iter-1], IRK4[iter-1])
            K1I = self.di(ERK4[iter-1], IRK4[iter-1])
            K1R = self.dr(IRK4[iter-1], ERK4[iter-1], RRK4[iter-1])
            K1P = self.dp(IRK4[iter-1])

            #Segunda K
            K2S = self.ds(SRK4[iter-1] + 0.5*h*K1S, ERK4[iter-1] + 0.5*h*K1E, IRK4[iter-1]+0.5*h*K1I, RRK4[iter-1] + h*0.5*K1R)
            K2E = self.de(SRK4[iter-1] + 0.5*h*K1S, ERK4[iter-1] + 0.5*h*K1E, IRK4[iter-1]+0.5*K1I)
            K2I = self.di(ERK4[iter-1] + 0.5*h*K1E, IRK4[iter-1] + 0.5*h*K1I)
            K2R = self.dr(IRK4[iter-1] + 0.5*h*K1I, ERK4[iter-1] + 0.5*h*K1E,RRK4[iter-1] + h*0.5*K1R)
            K2P = self.dp(IRK4[iter-1] + 0.5*h*K1I)

            #Tercera K
            K3S = self.ds(SRK4[iter-1] + 0.5*h*K2S, ERK4[iter-1] + 0.5*h*K2E, IRK4[iter-1] +0.5*h*K1I, RRK4[iter-1] + h*0.5*K2R)
            K3E = self.de(SRK4[iter-1] + 0.5*h*K2S, ERK4[iter-1] + 0.5*h*K2E, IRK4[iter-1] +0.5*h*K2I)
            K3I = self.di(ERK4[iter-1] + 0.5*h*K2E, IRK4[iter-1] + 0.5*h*K2I)
            K3R = self.dr(IRK4[iter-1] + 0.5*h*K2I, ERK4[iter-1] + 0.5*h*K2E, RRK4[iter-1] + 0.5*h*K2R)
            K3P = self.dp(IRK4[iter-1] + 0.5*h*K2I)
            
            #Cuarta K
            K4S = self.ds(SRK4[iter-1] + h*K2S, ERK4[iter-1] + h*K2E, IRK4[iter-1] + h*K1I, RRK4[iter-1] + h*K2R)
            K4E = self.de(SRK4[iter-1] + h*K2S, ERK4[iter-1] + h*K2E, IRK4[iter-1] + h*K2I)
            K4I = self.di(ERK4[iter-1] + h*K2E, IRK4[iter-1] + h*K2I)
            K4R = self.dr(IRK4[iter-1] + h*K2I, ERK4[iter-1] + h*K2E,RRK4[iter-1] + h*K2R)
            K4P = self.dp(IRK4[iter-1] + h*K2I)

            SRK4[iter] = SRK4[iter-1] + (h/6) * (K1S + 2*K2S + 2*K3S + K4S)
            ERK4[iter] = ERK4[iter-1] + (h/6) * (K1E + 2*K2E + 2*K3E + K4E)
            IRK4[iter] = IRK4[iter-1] + (h/6) * (K1I + 2*K2I + 2*K3I + K4I)
            RRK4[iter] = RRK4[iter-1] + (h/6) * (K1R + 2*K2R + 2*K3R + K4R)
            PRK4[iter] = PRK4[iter-1] + (h/6) * (K1P + 2*K2P + 2*K3P + K4P)
        
        return SRK4, ERK4, IRK4, RRK4, PRK4


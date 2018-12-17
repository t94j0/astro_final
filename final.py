import ezweb
import matplotlib.pyplot as plt
import math

data = ezweb.DetailedProject('./ezweb_02526')

def opacity(step):
    logR = [ math.log(r, 10) for r in step.radiusList() ]
    logK = [ math.log(k, 10) for k in step.opacityList() ]
    plt.plot(logR, logK)
    plt.title('Radius vs Opacity')
    plt.show()

def powerGeneration():
    plt.figure()

    time = [ step.age for step in data.steps ]

    #sumRad = [ sum(s.powerNucList()) for s in data.steps ]
    sumPP = [ sum(s.powerPPList()) for s in data.steps ]
    sumCNO = [ sum(s.powerCNOList()) for s in data.steps ]
    #sumGrav = [ sum(s.powerGravList()) for s in data.steps ]

    #plt.plot(time, sumRad)
    plt.plot(time, sumPP)
    plt.plot(time, sumCNO)
    # plt.plot(time, sumGrav)
    
    plt.title('Power Generation vs Time')
    plt.xlabel('Time (years)')
    plt.ylabel('Power per unit mass (W g-1)')
    plt.legend(['ɛ PP', 'ɛ CNO'])
    #plt.legend(['ɛ Radiation', 'ɛ PP', 'ɛ CNO', 'ɛ Gravity'])
    plt.show()
    
def locateConvection(step):
    plt.figure()
    logT = [ math.log(temp, 10) for temp in step.temperatureList() ]
    tempGrad = step.materialTempList()

    plt.plot(logT, step.adiabaticTempList(), 'b', linestyle='dashed')
    plt.plot(logT, step.radiativeTempList(), 'y', linestyle='dashed')
    plt.plot(logT, tempGrad, 'r')

    plt.title('Locate Convection')
    plt.xlabel('Temperature (log(K))')
    plt.ylabel('Material Gradient Temperature')
    plt.legend(['Adiabetic Gradient', 'Radiative Gradient', 'Target Star'])
    plt.ylim(0, 1)
    plt.show()

def materialDistribution(step):
    plt.figure()
    logR = [ math.log(r, 10) for r in step.radiusList() ]
    hMass = step.hMassFracList()
    heMass = step.heMassFracList()
    cMass = step.cMassFracList()
    nMass = step.nMassFracList()
    oMass = step.oMassFracList()

    plt.stackplot(logR, [hMass, heMass, cMass, nMass, oMass], labels=['Hydrogen', 'Helium', 'Carbon', 'Nitrogen', 'Oxygen'])

    plt.title('Material Distribution')
    plt.xlabel('Radius (log(R☉))')
    plt.ylabel('Mass Fraction')
    plt.legend(loc='upper left')
    plt.show()

def HRDiagram():
    plt.figure()

    GIVEN_L = [ math.log(i, 10) for i in [8e-4, 7.9e-3, 0.063, 0.16, 0.4, 0.79, 1.0, 1.26, 2.5, 6.0, 20, 80, 800, 2e4, 5e5]]
    GIVEN_T = [ i for i in [2.7, 3.12, 3.92, 4.64, 5.15, 5.61, 5.92, 6.0, 6.54, 7.24, 8.62, 10.8, 16.4, 30, 38] ]
    luminosity = [ s.logLuminosity for s in data.steps ]
    temperature = [ (10**s.logSurfaceTemperature)/1000 for s in data.steps ]

    in_x = [(10**data.steps[i].logSurfaceTemperature)/1000 for i in [1, 150, 481, 518, 770, 840, 880]]
    in_y  = [data.steps[i].logLuminosity for i in [1, 150, 481, 518, 770, 840, 880]]

    plt.plot(temperature, luminosity)
    plt.plot(GIVEN_T, GIVEN_L, 'o')
    plt.plot(in_x, in_y, 'mo')

    
    # ax.set_xlim(ax.get_xlim()[::-1])

    plt.title('Hertzsprung–Russell Diagram')
    plt.xlabel('Temperature K (in thousands)')
    plt.ylabel('Luminosity (log(L☉))')
    plt.legend([ '0.8 M☉ star path', 'Main Sequence', 'Chosen Data Points'])

    plt.show()

def getShit(i):
    materialDistribution(data.steps[i])
    locateConvection(data.steps[i])
    opacity(data.steps[i])

HRDiagram()

#HRDiagram()
#HRDiagram(2)
#getShit(1)
# 
# for i in range(480, len(data.steps)):
#     if i % 1 == 0:
#         print('step %d' % i)
#         HRDiagram(i)
#         d = input('Get? (y/n) ')
#         if d == 'y':
#             getShit(i)

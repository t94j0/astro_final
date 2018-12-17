from os import path
import itertools
from multiprocessing import Pool

getIndex = lambda line, index: line.split()[index]

class DetailedProject:
    def __init__(self, targetPath):
        self.summary = open(path.join(targetPath, 'summary.txt'))
        steps = [ line[:len(line)-1] for line in self.summary.readlines() ]
        self.steps = [ DetailedStep(step, targetPath) for step in steps ]

    def getStepByAge(self, age):
        return [ step for step in self.steps if step.age == age][0]

    def getLastStep(self):
        return self.steps[len(self.steps)-1]

    def __del__(self):
        self.summary.close()

class DetailedStep:
    STEP_INDEX = 0
    AGE_INDEX = 1
    MASS_INDEX = 2
    LUMINOSITY_INDEX = 3
    RADIUS_INDEX = 4
    SURFACE_TEMPERATURE_INDEX = 5
    CENTRAL_TEMPERATURE_INDEX = 6
    CENTRAL_DENSITY_INDEX = 7
    CENTRAL_PRESSURE_INDEX = 8

    def __init__(self, summary, targetPath):
        self.step = int(getIndex(summary, self.STEP_INDEX))
        self.age = float(getIndex(summary, self.AGE_INDEX))
        self.mass = float(getIndex(summary, self.MASS_INDEX))
        self.logLuminosity = float(getIndex(summary, self.LUMINOSITY_INDEX))
        self.logRadius = float(getIndex(summary, self.RADIUS_INDEX))
        self.logSurfaceTemperature = float(getIndex(summary, self.SURFACE_TEMPERATURE_INDEX))
        self.logCentralTemperature = float(getIndex(summary, self.CENTRAL_TEMPERATURE_INDEX))
        self.logCentralDensity = float(getIndex(summary, self.CENTRAL_DENSITY_INDEX))
        self.logCentralPressure = float(getIndex(summary, self.CENTRAL_PRESSURE_INDEX))

        self.detailFile = open(path.join(targetPath, 'structure_%05d.txt' % self.step))
        gridPoints = [ line[:len(line)-1] for line in self.detailFile.readlines() ]
        self.grid = [ DetailedPoint(point) for point in gridPoints ]

    def detailed(self):
        return self.grid

    def __del__(self):
        self.detailFile.close()

    def massList(self):
        return [ point.mass for point in self.detailed() ]
    def radiusList(self):
        return [ point.radius for point in self.detailed() ]
    def luminosityList(self):
        return [ point.luminosity for point in self.detailed() ]
    def pressureList(self):
        return [ point.pressure for point in self.detailed() ]
    def densityList(self):
        return [ point.density for point in self.detailed() ]
    def temperatureList(self):
        return [ point.temperature for point in self.detailed() ]
    def adiabaticTempList(self):
        return [ point.adiabaticTemp for point in self.detailed() ]
    def radiativeTempList(self):
        return [ point.radiativeTemp for point in self.detailed() ]
    def materialTempList(self):
        return [ point.materialTemp for point in self.detailed() ]
    def opacityList(self):
        return [ point.opacity for point in self.detailed() ]
    def numberDensityList(self):
        return [ point.numberDensity for point in self.detailed() ]
    def hMassFracList(self):
        return [ point.hMassFrac for point in self.detailed() ]
    def singHMassFracList(self):
        return [ point.singleHMassFrac for point in self.detailed() ]
    def dubIonHeMassFracList(self):
        return [ point.dubIonHeMassFrac for point in self.detailed() ]
    def powerNucList(self):
        return [ point.powerNuc for point in self.detailed() ]
    def powerPPList(self):
        return [ point.powerPP for point in self.detailed() ]
    def powerCNOList(self):
        return [ point.powerCNO for point in self.detailed() ]
    def powerGravList(self):
        return [ point.powerGrav for point in self.detailed() ]
    def heMassFracList(self):
        return [ point.heMassFrac for point in self.detailed() ]
    def cMassFracList(self):
        return [ point.cMassFrac for point in self.detailed() ]
    def nMassFracList(self):
        return [ point.nMassFrac for point in self.detailed() ]
    def oMassFracList(self):
        return [ point.oMassFrac for point in self.detailed() ]

class DetailedPoint:
    MASS_COORDINATE_INDEX = 0
    RADIUS_INDEX = 1
    LUMINOSITY_INDEX = 2
    PRESSURE_INDEX = 3
    DENSITY_INDEX = 4
    TEMP_INDEX = 5
    ADB_TEMP_GRAD_INDEX = 10
    NUM_DENSITY_INDEX = 12
    RAD_TEMP_GRAD_INDEX = 15
    MAT_TEMP_GRAD_INDEX = 16
    OPACITY_INDEX = 18
    POWER_NUC_INDEX = 19
    POWER_PP_INDEX = 20
    POWER_CNO_INDEX = 21
    POWER_GRAV_INDEX = 25
    H_MASS_FRAC_INDEX = 26
    SING_H_MASS_FRAC_INDEX = 28
    HE_MASS_FRAC_INDEX = 29
    DUB_ION_HE_MASS_FRAC_INDEX = 31
    C_MASS_FRAC_INDEX = 32
    N_MASS_FRAC_INDEX = 33
    O_MASS_FRAC_INDEX = 34

    def __init__(self, point):
        self.mass = float(getIndex(point, self.MASS_COORDINATE_INDEX))
        self.radius = float(getIndex(point, self.RADIUS_INDEX))
        self.luminosity = float(getIndex(point, self.LUMINOSITY_INDEX))
        self.pressure = float(getIndex(point, self.PRESSURE_INDEX))
        self.density = float(getIndex(point, self.DENSITY_INDEX))
        self.temperature = float(getIndex(point, self.TEMP_INDEX))
        self.pressure = float(getIndex(point, self.PRESSURE_INDEX))
        self.adiabaticTemp = float(getIndex(point, self.ADB_TEMP_GRAD_INDEX))
        self.radiativeTemp = float(getIndex(point, self.RAD_TEMP_GRAD_INDEX))
        self.materialTemp = float(getIndex(point, self.MAT_TEMP_GRAD_INDEX))
        self.opacity = float(getIndex(point, self.OPACITY_INDEX))
        self.numberDensity = float(getIndex(point, self.NUM_DENSITY_INDEX))
        self.hMassFrac = float(getIndex(point, self.H_MASS_FRAC_INDEX))
        self.singleHMassFrac = float(getIndex(point, self.SING_H_MASS_FRAC_INDEX))
        self.dubIonHeMassFrac = float(getIndex(point, self.DUB_ION_HE_MASS_FRAC_INDEX))
        self.powerNuc = float(getIndex(point, self.POWER_NUC_INDEX))
        self.powerPP = float(getIndex(point, self.POWER_PP_INDEX))
        self.powerCNO = float(getIndex(point, self.POWER_CNO_INDEX))
        self.powerGrav = float(getIndex(point, self.POWER_GRAV_INDEX))
        self.heMassFrac = float(getIndex(point, self.HE_MASS_FRAC_INDEX))
        self.cMassFrac = float(getIndex(point, self.C_MASS_FRAC_INDEX))
        self.nMassFrac = float(getIndex(point, self.N_MASS_FRAC_INDEX))
        self.oMassFrac = float(getIndex(point, self.O_MASS_FRAC_INDEX))

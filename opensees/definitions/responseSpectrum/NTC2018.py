import PyMpc.Units as u
from PyMpc import *
from mpc_utils_html import *
import PyMpc
import PyMpc.Math
import opensees.utils.tcl_input as tclin

def makeXObjectMetaData():

    # Function
    at_Function = MpcAttributeMetaData()
    at_Function.type = MpcAttributeType.String
    at_Function.name = '__mpc_function__'
    at_Function.group = 'Group'
    at_Function.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Function')+'<br/>') + 
        html_par('Click on the edit button to see a graph of the evaluated function') +
        html_par(html_href('','')+'<br/>') +
        html_end()
        )
    at_Function.editable = False
    
    # pga
    at_pga = MpcAttributeMetaData()
    at_pga.type = MpcAttributeType.Real
    at_pga.name = 'Ag'
    at_pga.group = 'Group'
    at_pga.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Ag')+'<br/>') +
        html_par('Maximum horizontal acceleration at the site') +
        html_par(html_href('https://esse1-gis.mi.ingv.it/','Modello di pericolosità sismica MPS04-S1')+'<br/>') +
        html_end()
        )
    at_pga.setDefault(0.1693)
    
    # Fo
    at_Fo = MpcAttributeMetaData()
    at_Fo.type = MpcAttributeType.Real
    at_Fo.name = 'Fo'
    at_Fo.group = 'Group'
    at_Fo.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Fo')+'<br/>') +
        html_par('Maximum value of the spectrum amplification factor in horizontal acceleration)') +
        html_par(html_href('https://opensees.berkeley.edu/wiki/index.php/Sensitivity_Command_Manual','Normal Random Variable')+'<br/>') +
        html_end()
        )
    at_Fo.setDefault(2.4734)
    
    # Tstar
    at_Tstar = MpcAttributeMetaData()
    at_Tstar.type = MpcAttributeType.Real
    at_Tstar.name = 'Tc_star'
    at_Tstar.group = 'Group'
    at_Tstar.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Tc_star')+'<br/>') +
        html_par('Reference value for the determination of the start time of the constant velocity portion of the spectrum in horizontal acceleration') +
        html_par(html_href('https://esse1-gis.mi.ingv.it/','Modello di pericolosità sismica MPS04-S1')+'<br/>') +
        html_end()
        )
    at_Tstar.setDefault(0.3566)
    
    # soil_class
    at_soil_class = MpcAttributeMetaData()
    at_soil_class.type = MpcAttributeType.String
    at_soil_class.name = 'Soil Class'
    at_soil_class.group = 'Group'
    at_soil_class.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Soil Class')+'<br/>') +
        html_par('the dispersion of the distribution (Standard deviation or Coefficient of Variation)') +
        html_par(html_href('https://opensees.berkeley.edu/wiki/index.php/Sensitivity_Command_Manual','Normal Random Variable')+'<br/>') +
        html_end()
        )
    at_soil_class.sourceType = MpcAttributeSourceType.List
    at_soil_class.setSourceList(['A', 'B', 'C', 'D', 'E'])
    at_soil_class.setDefault('C')
    
    
    # topography_class
    at_topography_class = MpcAttributeMetaData()
    at_topography_class.type = MpcAttributeType.String
    at_topography_class.name = 'Topography Class'
    at_topography_class.group = 'Group'
    at_topography_class.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Topography Class')+'<br/>') +
        html_par('the dispersion of the distribution (Standard deviation or Coefficient of Variation)') +
        html_par(html_href('https://opensees.berkeley.edu/wiki/index.php/Sensitivity_Command_Manual','Normal Random Variable')+'<br/>') +
        html_end()
        )
    at_topography_class.sourceType = MpcAttributeSourceType.List
    at_topography_class.setSourceList(['T1', 'T2', 'T3', 'T4'])
    at_topography_class.setDefault('T3')
    
    # damping_ratio
    at_damping_ratio = MpcAttributeMetaData()
    at_damping_ratio.type = MpcAttributeType.Real
    at_damping_ratio.name = 'Damping ratio'
    at_damping_ratio.group = 'Group'
    at_damping_ratio.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Damping ratio')+'<br/>') +
        html_par('Reference value for the determination of the start time of the constant velocity portion of the spectrum in horizontal acceleration') +
        html_par(html_href('https://esse1-gis.mi.ingv.it/','Modello di pericolosità sismica MPS04-S1')+'<br/>') +
        html_end()
        )
    at_damping_ratio.setDefault(0.05)
    
    # behavior_factor
    at_behavior_factor = MpcAttributeMetaData()
    at_behavior_factor.type = MpcAttributeType.Real
    at_behavior_factor.name = 'q factor'
    at_behavior_factor.group = 'Group'
    at_behavior_factor.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('Behavior factor')+'<br/>') +
        html_par('Reference value for the determination of the start time of the constant velocity portion of the spectrum in horizontal acceleration') +
        html_par(html_href('https://esse1-gis.mi.ingv.it/','Modello di pericolosità sismica MPS04-S1')+'<br/>') +
        html_end()
        )
    at_behavior_factor.setDefault(1.0)
    
    # factor
    at_factor = MpcAttributeMetaData()
    at_factor.type = MpcAttributeType.Boolean
    at_factor.name = '-factor'
    at_factor.group = 'Group'
    at_factor.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('-factor')+'<br/>') + 
        html_par('optional, a factor to multiply load factors by (default = 1.0)') +
        html_par(html_href('http://opensees.berkeley.edu/wiki/index.php/Path_TimeSeries','Path TimeSeries')+'<br/>') +
        html_end()
        )
	
    # cFactor
    at_cFactor = MpcAttributeMetaData()
    at_cFactor.type = MpcAttributeType.Real
    at_cFactor.name = 'cFactor'
    at_cFactor.group = '-factor'
    at_cFactor.description = (
        html_par(html_begin()) +
        html_par(html_boldtext('cFactor')+'<br/>') + 
        html_par('optional, a factor to multiply load factors by (default = 1.0)') +
        html_par(html_href('http://opensees.berkeley.edu/wiki/index.php/Path_TimeSeries','Path TimeSeries')+'<br/>') +
        html_end()
        )
    at_cFactor.setDefault(1.0)
    
    xom = MpcXObjectMetaData()
    xom.name = 'NTC2018'
    xom.addAttribute(at_Function)
    xom.addAttribute(at_pga)
    xom.addAttribute(at_Fo)
    xom.addAttribute(at_Tstar)
    xom.addAttribute(at_soil_class)
    xom.addAttribute(at_topography_class)
    xom.addAttribute(at_damping_ratio)
    xom.addAttribute(at_behavior_factor)
    xom.addAttribute(at_factor)
    xom.addAttribute(at_cFactor)
    
    # cFactor-dep
    xom.setVisibilityDependency(at_factor, at_cFactor)
    
    return xom

def evaluateFunctionAttribute(xobj):
    if(xobj is None):
        print('Error: xobj is null\n')
        return PyMpc.Math.mat()
    
    if(xobj.name != 'NTC2018'):
        print('Error: invalid xobj type, expected "NTC2018", given "{}"'.format(xobj.name))
        return PyMpc.Math.mat()
    
    func_at = xobj.getAttribute('__mpc_function__')
    if(func_at is None):
        print('Error: cannot find "__mpc_function__" attribute\n')
        return PyMpc.Math.mat()
    
    ag_g_at = xobj.getAttribute('Ag')
    if(ag_g_at is None):
        print('Error: cannot find "Ag" attribute\n')
        return PyMpc.Math.mat()
    ag_g = ag_g_at.real
    
    Fo_at = xobj.getAttribute('Fo')
    if(Fo_at is None):
        print('Error: cannot find "Fo" attribute\n')
        return PyMpc.Math.mat()
    Fo = Fo_at.real
    
    Tstar_at = xobj.getAttribute('Tc_star')
    if(Tstar_at is None):
        print('Error: cannot find "Tc_star" attribute\n')
        return PyMpc.Math.mat()
    Tstar = Tstar_at.real
    
    soil_class_at = xobj.getAttribute('Soil Class')
    if(soil_class_at is None):
        print('Error: cannot find "Soil Class" attribute\n')
        return PyMpc.Math.mat()
    soil_class = soil_class_at.string
    
    fact_at = xobj.getAttribute('-factor')
    if(fact_at is None):
        print('Error: cannot find "-factor" attribute\n')
        return PyMpc.Math.mat()

    cFactor_at = xobj.getAttribute('cFactor')
    if(cFactor_at is None):
        print('Error: cannot find "cFactor" attribute\n')
        return PyMpc.Math.mat()
        
    cFactor = cFactor_at.real if fact_at.boolean else 1.0
    
    # initialize soil related variables
    Ss=1.0
    Cc=1.0
    
    if soil_class == 'A':
        Ss = 1.0
        Cc = 1.0
        
    elif soil_class == 'B':
        Ss = min(max(1, (1.4-0.4*Fo*ag_g)), 1.2)
        Cc = 1.1*Tstar**(-0.2)
        
    elif soil_class == 'C':
        Ss = min(max(1, (1.7-0.6*Fo*ag_g)), 1.5)
        Cc = 1.05*Tstar**(-0.33)
    
    elif soil_class == 'D':
        Ss = min(max(0.9, (2.4-1.5*Fo*ag_g)), 1.8)
        Cc = 1.25*Tstar**(-0.5)
    
    elif soil_class == 'E':
        Ss = min(max(1, (2.0-1.1*Fo*ag_g)), 1.6)
        Cc = 1.15*Tstar**(-0.4)
        
    else:
        print('Error: soil class must be A, B, C, D or E!')
        return PyMpc.Math.mat()
    
    
    topography_class_at = xobj.getAttribute('Topography Class')
    if(topography_class_at is None):
        print('Error: cannot find "Topography Class" attribute\n')
        return PyMpc.Math.mat()
    topography_class = topography_class_at.string
    
    # initialize topography related variables
    St=1.0
    
    if topography_class == 'T1':
        St=1.00
        
    elif topography_class == 'T2':
        St=1.20
        
    elif topography_class == 'T3':
        St=1.20
    
    elif topography_class == 'T4':
        St=1.40
        
    else:
        print('Error: soil class must be T1, T2, T3 or T4!')
        return PyMpc.Math.mat()
        
        
    damping_ratio_at = xobj.getAttribute('Damping ratio')
    if(damping_ratio_at is None):
        print('Error: cannot find "Damping ratio" attribute\n')
        return PyMpc.Math.mat()
    nu = damping_ratio_at.real
    
    behavior_factor_at = xobj.getAttribute('q factor')
    if(behavior_factor_at is None):
        print('Error: cannot find "q factor" attribute\n')
        return PyMpc.Math.mat()
    q = behavior_factor_at.real
    
    # compute spectra vars
    Tc = Tstar / Cc
    Tb = Tc / 5.0
    Td = 4.0 * ag_g + 1.6
    S = St * Ss
    PGA = S * ag_g
    nu_factor = max((10.0 / (5.0 + (nu * 100.0)))**(0.5), 0.55)
    
    
    # create response spectrum
    upper = 4.0
    lower = 0.0
    dt = 0.001
    length = int((upper-lower) / dt)
    
    xy = PyMpc.Math.mat(length, 2)
    
    for i in range(length):
        
        T = lower + i*(upper-lower)/(length-1)
        
        if T >= 0.0 and T < Tb:
            Sa = ag_g*S*nu_factor*Fo*((T/Tb)+((1/(nu_factor*Fo))*(1-(T/Tb))))
            Sd = (PGA-((PGA-(ag_g*S*nu_factor*Fo/q))/(Tb))*(T))
            
        elif T >= Tb and T < Tc:
            Sd = ag_g*S*nu_factor*Fo/q
            
        elif T >= Tc and T < Td:
            Sd = ag_g*S*nu_factor*Fo/q*(Tc/T)
            
        elif T >= Td:
            Sd = ag_g*S*nu_factor*Fo/q*(Tc*Td/(T*T))
            
        else:
            Sd = 0.0
            
        xy[i, 0] = T
        xy[i, 1] = cFactor * Sd
    
    return xy
    
    
def writeTcl(pinfo):
    
    xobj = pinfo.definition.XObject
    
    ClassName = xobj.name
    if pinfo.currentDescription != ClassName:
        pinfo.out_file.write('\n{}# {} {}\n'.format(pinfo.indent, xobj.Xnamespace, ClassName))
        pinfo.currentDescription = ClassName
    
    tag = xobj.parent.componentId
    
    sopt = ''	#optional string
    
    #with 'non_constant'
    #timeSeries Path $tag -time {list_of_times} -values {list_of_values} <-factor $cFactor> <-useLast>
    
    xy = evaluateFunctionAttribute(xobj)
    
    #set list TCL
    times_str = 'set timeSeries_list_of_times_{}'.format(tag)+' {'
    values_str = 'set timeSeries_list_of_values_{}'.format(tag)+' {'
    
    nLettersT = len(times_str)
    nLettersV = len(values_str)
    nTabT = nLettersT // 4
    nTabV = nLettersV // 4
    
    n = 1
    length_list = int(len(xy)/2)
    for i in range(length_list):
        if (i == (10*n)):
            times_str += '\\\n{}{}'.format(pinfo.indent, tclin.utils.nIndent(nTabT))
            values_str += '\\\n{}{}'.format(pinfo.indent, tclin.utils.nIndent(nTabV))
            n += 1
        if (i!=length_list-1):
            times_str += '{} '.format(xy[i, 0])
            values_str += '{} '.format(xy[i, 1])
        else:
            times_str += '{}'.format(xy[i, 0])
            values_str += '{}'.format(xy[i, 1])
    
    times_str += '}\n'
    values_str += '}\n'
    pinfo.out_file.write(times_str)
    pinfo.out_file.write(values_str)
    
    #end list TCL
    #now write the 'non_constant' string into the file
    str_tcl = '{0}timeSeries Path {1} -time $timeSeries_list_of_times_{1} -values $timeSeries_list_of_values_{1}{2}\n'.format(pinfo.indent, tag, sopt)
    
    pinfo.out_file.write(str_tcl)

import math
from typing import Dict

def compute_horizontoal_pipeline(inputs: Dict[str, float]) -> Dict[str, float]:
    '''Auto-generated from Excel sheet: horizontoal pipeline'''
    # inputs: mapping of cell address (e.g., 'B3') to numeric value
    vals = {}.copy()
    vals['B10'] = float(inputs.get('B10', 0.0))
    vals['B11'] = float(inputs.get('B11', 0.0))
    vals['B12'] = float(inputs.get('B12', 0.0))
    vals['B23'] = float(inputs.get('B23', 0.0))
    vals['B4'] = float(inputs.get('B4', 0.0))
    vals['B5'] = float(inputs.get('B5', 0.0))
    vals['B6'] = float(inputs.get('B6', 0.0))
    vals['B7'] = float(inputs.get('B7', 0.0))
    vals['B8'] = float(inputs.get('B8', 0.0))
    vals['B9'] = float(inputs.get('B9', 0.0))
    # B14 = (vals['B6']*0.0254)/2
    try: vals['B14'] = ((vals['B6']*0.0254)/2)
    except Exception as e:
        raise RuntimeError(f'Error computing B14: {e}')
    # B16 = (vals['B4']*100000 - vals['B7']*9.81*vals['B23'])/vals['B5']
    try: vals['B16'] = ((vals['B4']*100000 - vals['B7']*9.81*vals['B23'])/vals['B5'])
    except Exception as e:
        raise RuntimeError(f'Error computing B16: {e}')
    # B15 = vals['B14']-vals['B12']/1000
    try: vals['B15'] = (vals['B14']-vals['B12']/1000)
    except Exception as e:
        raise RuntimeError(f'Error computing B15: {e}')
    # B17 = (min([2*vals['vals['B8']']/vals['vals['B16']'], vals['vals['B15']']]))
    try: vals['B17'] = ((min([2*vals['vals['B8']']/vals['vals['B16']'], vals['vals['B15']']])))
    except Exception as e:
        raise RuntimeError(f'Error computing B17: {e}')
    # B24 = ( (vals['B16']/4)*(vals['B15']**2 - vals['B14']**2) + vals['B10']*(vals['B14'] - vals['B15']) )/vals['B11']
    try: vals['B24'] = (( (vals['B16']/4)*(vals['B15']**2 - vals['B14']**2) + vals['B10']*(vals['B14'] - vals['B15']) )/vals['B11'])
    except Exception as e:
        raise RuntimeError(f'Error computing B24: {e}')
    # B20 = (math.pi/(24*vals['B11']))*( -3*vals['B16']*(vals['B14']**4 - 2*vals['B14']**2*vals['B15']**2 + vals['B15']**4) + 8*vals['B10']*(vals['B14']**3 - 3*vals['B14']*vals['B15']**2 + 2*vals['B15']**3) )
    try: vals['B20'] = ((math.pi/(24*vals['B11']))*( -3*vals['B16']*(vals['B14']**4 - 2*vals['B14']**2*vals['B15']**2 + vals['B15']**4) + 8*vals['B10']*(vals['B14']**3 - 3*vals['B14']*vals['B15']**2 + 2*vals['B15']**3) ))
    except Exception as e:
        raise RuntimeError(f'Error computing B20: {e}')
    # B21 = 3600*math.pi/(24*vals['B11']*vals['B9'])*((3*vals['B9']*vals['B16']*(vals['B14']**4 - vals['B15']**4) - 8*vals['B10']*vals['B9']*(vals['B14']**3 - vals['B15']**3)) + (3*vals['B11']*vals['B16']*(vals['B15']**4 - vals['B17']**4) - 8*vals['B8']*vals['B11']*(vals['B15']**3 - vals['B17']**3)))
    try: vals['B21'] = (3600*math.pi/(24*vals['B11']*vals['B9'])*((3*vals['B9']*vals['B16']*(vals['B14']**4 - vals['B15']**4) - 8*vals['B10']*vals['B9']*(vals['B14']**3 - vals['B15']**3)) + (3*vals['B11']*vals['B16']*(vals['B15']**4 - vals['B17']**4) - 8*vals['B8']*vals['B11']*(vals['B15']**3 - vals['B17']**3))))
    except Exception as e:
        raise RuntimeError(f'Error computing B21: {e}')
    # B19 = (math.pi/(24*vals['B9']))*( 3*vals['B16']*(vals['B15']**4 - vals['B17']**4) + 8*vals['B8']*(vals['B15']**3 - vals['B17']**3) + 24*vals['B9']*vals['B15']**2*vals['B24'] )
    try: vals['B19'] = ((math.pi/(24*vals['B9']))*( 3*vals['B16']*(vals['B15']**4 - vals['B17']**4) + 8*vals['B8']*(vals['B15']**3 - vals['B17']**3) + 24*vals['B9']*vals['B15']**2*vals['B24'] ))
    except Exception as e:
        raise RuntimeError(f'Error computing B19: {e}')
    # B22 = (vals['B21']/3600)/(math.pi*vals['B14']**2)
    try: vals['B22'] = ((vals['B21']/3600)/(math.pi*vals['B14']**2))
    except Exception as e:
        raise RuntimeError(f'Error computing B22: {e}')
    out = {}
    out['B19'] = vals.get('B19')
    out['B20'] = vals.get('B20')
    out['B22'] = vals.get('B22')
    return out

def compute_vertical_pipeline(inputs: Dict[str, float]) -> Dict[str, float]:
    '''Auto-generated from Excel sheet: vertical pipeline'''
    # inputs: mapping of cell address (e.g., 'B3') to numeric value
    vals = {}.copy()
    vals['B10'] = float(inputs.get('B10', 0.0))
    vals['B11'] = float(inputs.get('B11', 0.0))
    vals['B12'] = float(inputs.get('B12', 0.0))
    vals['B13'] = float(inputs.get('B13', 0.0))
    vals['B4'] = float(inputs.get('B4', 0.0))
    vals['B5'] = float(inputs.get('B5', 0.0))
    vals['B6'] = float(inputs.get('B6', 0.0))
    vals['B7'] = float(inputs.get('B7', 0.0))
    vals['B8'] = float(inputs.get('B8', 0.0))
    vals['B9'] = float(inputs.get('B9', 0.0))
    vals['E6'] = float(inputs.get('E6', 0.0))
    # B24 = ((vals['vals['E6']']="Down (-)") and (-vals['vals['B6']']) or (vals['vals['B6']']))
    try: vals['B24'] = (((vals['vals['E6']']="Down (-)") and (-vals['vals['B6']']) or (vals['vals['B6']'])))
    except Exception as e:
        raise RuntimeError(f'Error computing B24: {e}')
    # B15 = (vals['B7']*0.0254)/2
    try: vals['B15'] = ((vals['B7']*0.0254)/2)
    except Exception as e:
        raise RuntimeError(f'Error computing B15: {e}')
    # B17 = (((vals['vals['B5']']+vals['vals['B6']'])<=0) and ("") or ((vals['vals['B4']']*100000 - vals['vals['B8']']*9.81*vals['vals['B24']']) / (vals['vals['B5']'] + vals['vals['B6']'])))
    try: vals['B17'] = ((((vals['vals['B5']']+vals['vals['B6']'])<=0) and ("") or ((vals['vals['B4']']*100000 - vals['vals['B8']']*9.81*vals['vals['B24']']) / (vals['vals['B5']'] + vals['vals['B6']']))))
    except Exception as e:
        raise RuntimeError(f'Error computing B17: {e}')
    # B16 = vals['B15']-vals['B13']/1000
    try: vals['B16'] = (vals['B15']-vals['B13']/1000)
    except Exception as e:
        raise RuntimeError(f'Error computing B16: {e}')
    # B18 = (min([2*vals['vals['B9']']/vals['vals['B17']'], vals['vals['B16']']]))
    try: vals['B18'] = ((min([2*vals['vals['B9']']/vals['vals['B17']'], vals['vals['B16']']])))
    except Exception as e:
        raise RuntimeError(f'Error computing B18: {e}')
    # B25 = ( (vals['B17']/4)*(vals['B16']**2 - vals['B15']**2) + vals['B11']*(vals['B15'] - vals['B16']) )/vals['B12']
    try: vals['B25'] = (( (vals['B17']/4)*(vals['B16']**2 - vals['B15']**2) + vals['B11']*(vals['B15'] - vals['B16']) )/vals['B12'])
    except Exception as e:
        raise RuntimeError(f'Error computing B25: {e}')
    # B21 = (math.pi/(24*vals['B12']))*( -3*vals['B17']*(vals['B15']**4 - 2*vals['B15']**2*vals['B16']**2 + vals['B16']**4) + 8*vals['B11']*(vals['B15']**3 - 3*vals['B15']*vals['B16']**2 + 2*vals['B16']**3) )
    try: vals['B21'] = ((math.pi/(24*vals['B12']))*( -3*vals['B17']*(vals['B15']**4 - 2*vals['B15']**2*vals['B16']**2 + vals['B16']**4) + 8*vals['B11']*(vals['B15']**3 - 3*vals['B15']*vals['B16']**2 + 2*vals['B16']**3) ))
    except Exception as e:
        raise RuntimeError(f'Error computing B21: {e}')
    # B22 = 3600*math.pi/(24*vals['B12']*vals['B10'])*((3*vals['B10']*vals['B17']*(vals['B15']**4 - vals['B16']**4) - 8*vals['B11']*vals['B10']*(vals['B15']**3 - vals['B16']**3)) + (3*vals['B12']*vals['B17']*(vals['B16']**4 - vals['B18']**4) - 8*vals['B9']*vals['B12']*(vals['B16']**3 - vals['B18']**3)))
    try: vals['B22'] = (3600*math.pi/(24*vals['B12']*vals['B10'])*((3*vals['B10']*vals['B17']*(vals['B15']**4 - vals['B16']**4) - 8*vals['B11']*vals['B10']*(vals['B15']**3 - vals['B16']**3)) + (3*vals['B12']*vals['B17']*(vals['B16']**4 - vals['B18']**4) - 8*vals['B9']*vals['B12']*(vals['B16']**3 - vals['B18']**3))))
    except Exception as e:
        raise RuntimeError(f'Error computing B22: {e}')
    # B20 = (math.pi/(24*vals['B10']))*( 3*vals['B17']*(vals['B16']**4 - vals['B18']**4) + 8*vals['B9']*(vals['B16']**3 - vals['B18']**3) + 24*vals['B10']*vals['B16']**2*vals['B25'] )
    try: vals['B20'] = ((math.pi/(24*vals['B10']))*( 3*vals['B17']*(vals['B16']**4 - vals['B18']**4) + 8*vals['B9']*(vals['B16']**3 - vals['B18']**3) + 24*vals['B10']*vals['B16']**2*vals['B25'] ))
    except Exception as e:
        raise RuntimeError(f'Error computing B20: {e}')
    # B23 = (vals['B22']/3600)/(math.pi*vals['B15']**2)
    try: vals['B23'] = ((vals['B22']/3600)/(math.pi*vals['B15']**2))
    except Exception as e:
        raise RuntimeError(f'Error computing B23: {e}')
    out = {}
    out['B20'] = vals.get('B20')
    out['B21'] = vals.get('B21')
    out['B23'] = vals.get('B23')
    return out

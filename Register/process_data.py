def process_env(dic):
    del dic['accel_x']
    del dic['accel_y']
    del dic['accel_z']
    del dic['battery']
    del dic['bt_address']
    del dic['distance']
    del dic['eco2']
    del dic['etvoc']
    del dic['gateway']
    del dic['pga']
    del dic['pressure']
    del dic['rssi']
    del dic['seismic']
    del dic['si']
    del dic['uv']
    del dic['vibinfo']
    dic['sensor_type'] = 'env'
    return dic
#CO2センサの処理
def process_co2(dic):
    dic['sensor_type'] = 'co2'
    return dic
#ドアセンサの処理
def process_door(dic):
    dic['sensor_type'] = 'door'
    return dic
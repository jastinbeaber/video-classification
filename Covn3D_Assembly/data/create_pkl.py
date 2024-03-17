import pickle

def write_array_to_pkl(arr, filename):
    with open(filename, 'wb') as file:
        pickle.dump(list(arr), file, protocol=3)

def read_pkl_to_array(filename):
    with open(filename, 'rb') as file:
        return set(pickle.load(file))

# 创建一个示例数据
# data = {'Transitions class',
#         'Pick up/Place Carrier' ,
#         'Pick up/Place Gear Bearings (x3)',
#         'Pick up/Place Planet Gears (x3)',
#         'Pick up/Place Carrier Shaft',
#         'Pick up/Place Sun Shaft',
#         'Pick up/Place Sun Gear',
#         'Pick up/Place Sun Gear Bearing',
#         'Pick up/Place Ring Bear',
#         'Pick up Block 2 and place it on Block 1',
#         'Pick up/Place Cover',
#         'Pick up/Place Screws (x2)',
#         'Pick up/Place Allen Key, Turn Screws, Return Allen Key and EGT'}

data = ['0Transitions',
        '1PPCarrier' ,
        '2PPGearBearings',
        '3PPPlanetGears',
        '4PPCarrierShaft',
        '5PPSunShaft',
        '6PPSunGear',
        '7PPSunGearBearing',
        '8PPRingBear',
        '9PBlock2PBlock1',
        '10PickPCover',
        '11PickPScrews',
        '12GetEGT']

# 指定要保存的文件名
file_name = 'HA4MAssemblyAction.pkl'

# 将数组写入.pkl文件
write_array_to_pkl(data, file_name)

# 从.pkl文件读取数组
loaded_data = read_pkl_to_array(file_name)

print(f'PKL 文件 "{file_name}" 已创建。')
print(f'从文件中加载的数据：{loaded_data}')

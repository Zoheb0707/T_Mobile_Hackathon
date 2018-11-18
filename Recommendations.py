import pandas as pd

data = pd.read_csv(filepath_or_buffer = 'Data.csv')

input_user_id = 5#int(input('Enter username: '))

if type(input_user_id) != int:
    raise ValueError('User Id in supposed to be an Integer')

if input_user_id not in data['user_id']:
    raise ValueError('Enter valid user_id')

cluster = int(data[data['user_id'] == input_user_id]['cluster'])

filtered_data = data[data['cluster'] == cluster]

if len(filtered_data) > 10: 
    filtered_data = filtered_data[0:10]

Sweater_count = sum(filtered_data['Sweater'])
Blouse_count =  sum(filtered_data['Dress'])
T_Shirt_count = sum(filtered_data['T_shirt'])
Shirt_count = sum(filtered_data['Shirt'])
Tank_top_count = sum(filtered_data['Tank_top'])
Jacket_count = sum(filtered_data['Jacket'])
Crop_top_count = sum(filtered_data['Crop_top'])
Bra = sum(filtered_data['Suit'])
Vest = sum(filtered_data['Vest'])

cloth_list = [Sweater_count, Blouse_count, T_Shirt_count, Shirt_count, Tank_top_count, 
              Jacket_count, Crop_top_count, Bra, Vest]
mapper = {0:'Sweater', 1:'Dress', 2:'T_Shirt', 3:'Shirt', 4:'Tank_top', 5:'Jacket', 
          6:'Crop_top', 7:'Suit', 8:'Vest'}
indices = sorted(range(len(cloth_list)), key=lambda i: cloth_list[i])[-3:]

cloth_recommendations = []

for i in indices:
    cloth_recommendations.append(mapper[i])

f= open("output.txt","w+")

f.write('Gender: ' + str(data.iloc[input_user_id]['gender'] + '\n'))
f.write('Recommended Products are: ' + str(cloth_recommendations))

import random
import pandas as pd
import random
from sklearn.cluster import KMeans

user_id = list(range(0,1000))
gender = ['M', 'F']
age = list(range(20,70))
cities_CA = ['Los Angeles', 'San Francisco', 'San Diego', 'Irvine', 'San Jose'] 
cities_WA = ['Seattle', 'Bellevue', 'Kent', 'Issaquah', 'Redmond']
cities = cities_CA + cities_WA
state = ['WA', 'CA']
country = ['USA']
shirt_size_list = range(0,10)
columns_in_df = ['user_id', 'gender', 'age', 'city', 'state', 'country', 
                 'Sweater', 'Dress', 'T_shirt', 'Shirt', 'Tank_top',
                'Jacket', 'Crop_top', 'Suit', 'Vest',  'Size']

data_frame_list = []
for u_id in user_id:
    
    gender = None
    age = None
    city = None
    state = None
    country = 'USA'
    
    Sweater = 0
    Blouse = 0
    T_shirt = 0
    Shirt = 0
    Tank_top = 0
    Jacket = 0
    Crop_top = 0
    Bra = 0
    Vest = 0

    gender_probability = random.random()
    if gender_probability > 0.5:
        gender = 'M'
    else:
        gender = 'F'
    
    age = random.randint(20,69)
    
    state_probability = random.random()
    if state_probability > 0.5:
        state = 'WA'
        city = cities_WA[random.randint(0,4)]
    else:
        state = 'CA'
        city = cities_CA[random.randint(0,4)]
    
    if gender == 'M':
        if age >= 20 and age < 40:
            Sweater = random.randint(0,3)
            Dress = 0
            T_shirt = random.randint(0,8)
            Shirt = random.randint(0,10)
            Tank_top = random.randint(0,3)
            Jacket = random.randint(0,10)
            Crop_top = random.randint(0,1)
            Suit = random.randint(0,10)
            Vest = random.randint(0,3)
        elif age >= 40 and age < 50:
            Sweater = random.randint(0,5)
            Dress = 0
            T_shirt = random.randint(0,3)
            Shirt = random.randint(0,10)
            Tank_top = 0
            Jacket = random.randint(0,10)
            Crop_top = 0
            Suit = random.randint(0,10)
            Vest = random.randint(0,4)
        elif age >= 60 and age <70:
            Sweater = random.randint(0,4)
            Dress = 0
            T_shirt = random.randint(0,1)
            Shirt = random.randint(0,5)
            Tank_top = 0
            Jacket = random.randint(0,2)
            Crop_top = 0
            Suit = random.randint(0,10)
            Vest = random.randint(0,4)
    else :
        if age >= 20 and age < 40:
            Sweater = random.randint(0,3)
            Dress = random.randint(0,10)
            T_shirt = random.randint(0,7)
            Shirt = random.randint(0,10)
            Tank_top = random.randint(0,4)
            Jacket = random.randint(0,10)
            Crop_top = random.randint(0,7)
            Suit = 0
            Vest = 0
        elif age >= 40 and age < 50:
            Sweater = random.randint(0,3)
            Dress = random.randint(0,8)
            T_shirt = random.randint(0,2)
            Shirt = random.randint(0,5)
            Tank_top = random.randint(0,3)
            Jacket = random.randint(0,4)
            Crop_top = 0
            Suit = 0
            Vest = 0
        elif age >= 60 and age <70:
            Sweater = random.randint(0,3)
            Dress = random.randint(0,7)
            T_shirt = 0
            Shirt = random.randint(0,2)
            Tank_top = 0
            Jacket = random.randint(0,2)
            Crop_top = 0
            Suit = 0
            Vest = 0
            
        shirt_size_index = random.randint(0,9)
        shirt_size = shirt_size_list[shirt_size_index]
    
    row_list = [u_id, gender, age, city, state, country, Sweater, Dress,
               T_shirt, Shirt, Tank_top, Jacket, Crop_top, Suit, Vest, shirt_size]

    data_frame_list.append(row_list)
    
df = pd.DataFrame(data = data_frame_list, columns = columns_in_df)

df_to_use = df[['gender', 'age', 'city', 'state', 'country', 'Size']]
def one_hot(data):
    for col_name in data.columns:
        if(data[col_name].dtype == 'object'):
            one_hot = pd.get_dummies(data[col_name])
            data.drop([col_name], axis = 1, inplace = True)
            data = data.join(one_hot)
    return data
df_to_use = one_hot(df_to_use)

n_clusters_list = [5,10,20,50,100,200,300]
n_init_list = [10,15,20,30]
max_iter = 5000
init = 'k-means++'

best_model = None
best_Score = -float('Inf')

for n_clusters in n_clusters_list:
    for n_init in n_init_list:
        Model = KMeans(n_clusters = n_clusters, n_init = n_init, max_iter = max_iter, init = init)
        Model.fit(df_to_use)
        score = Model.score(df_to_use)
        
        if score > best_Score:
            best_Score = score
            best_model = Model

df['cluster'] = best_model.predict(df_to_use)
df_to_use['cluster'] = best_model.predict(df_to_use)

df.to_csv(path_or_buf = 'Data.csv')
# найти количество отдельно мужчин отдельно женщин по каждому классу обслуживания
import matplotlib.pyplot as plt
import streamlit as st


st.image('titanik.jpg')
st.header('Данные пассажиров Титаника')
st.write("Для просмотра данных по количеству пассажиров каждого пола по указанному классу обслуживания, выбирите соответсвующий пункт из списка")
choise = st.selectbox("Укажите класс обслуживания:", ["Всего", "1 класс", "2 класс", "3 класс"])
data = {'Мужчин:': 0,'Женщин:': 0}
with open('data.csv.csv') as file:
    for line in file:
        d = line.split (',')
        Sex = d[5]
        Pclass = d[2]
        # Узнаем общеее количесвто мужчин и женщин по 1,2,3 классу осблуживания
        if choise == "Всего":
            if Sex == 'Age':
                continue
            if Sex == 'male':
                data ['Мужчин:'] += 1
            else:
                data['Женщин:'] += 1

        if choise == "1 класс" and Pclass == '1':
            if Sex == 'male':
                data ['Мужчин:'] += 1
            else:
                data['Женщин:'] += 1
        if choise == "2 класс" and Pclass == '2':
            if Sex == 'male':
                data['Мужчин:'] += 1
            else:
                data['Женщин:'] += 1
        if choise == "3 класс" and Pclass == '3':
            if Sex == 'male':
                data['Мужчин:'] += 1
            else:
                data['Женщин:'] += 1
st.dataframe(data)
fig = plt.figure(figsize=(10,5))
plt.bar(['Мужчин','Женщин'],[data['Мужчин:'],data['Женщин:']])
st.pyplot(fig)



# Узнаем общее количсетво мужчин и женщин
#male = 0
#female = 0

#with open('data.csv.csv') as file:
    #for line in file:
        #data = line.split(',')
        #Sex = data[5]
        #if Sex == 'Age':
          # continue
        #elif Sex == 'male':
         # male += 1
        #else:
         # female += 1
#st.table({'Пол': ['Мужской', 'Женский'], 'Количество':[male,female] })



#male= {'1': 0, '2': 0, '3': 0}
#female= {'1': 0, '2': 0, '3': 0}

#with open('data.csv.csv') as file:
    #for line in file:
        #data = line.split(',')
        #if data[0] == 'PassengerId':
         #continue
        #pclass = data[2]
        #sex = data[5]
        #if sex == 'male':
            #male[pclass] += 1
        #if sex == 'female':
            #female[pclass] += 1
    #print(male, female)

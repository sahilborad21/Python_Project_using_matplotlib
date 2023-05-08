import pandas as pd
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_prices.csv')
# print(gas)


'''###------------Line Chart Example----------------###
plt.figure(figsize=(10,7))
plt.title("Gas Prices Over the Time(In USD)")
plt.plot(gas.Year, gas.USA, label = 'United States Of America')
plt.plot(gas.Year, gas.UK, label = 'United Kingdom')
plt.plot(gas.Year, gas.Canada, label = 'Canada')
plt.plot(gas.Year, gas['South Korea'], label = 'South Korea')
for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)
plt.xticks(gas.Year[::2])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.legend()
plt.savefig('Gas_Price_Figure.png', dpi=300)
plt.show()'''

fifa = pd.read_csv('fifa_data.csv')
# print(fifa)
'''###--------------------Histogram Chart Example--------------------------###
plt.figure(figsize=(10,5))
bins = [40,50,60,70,80,90,100]
plt.hist(fifa.Overall,bins=bins,color='#a86232')
plt.xticks(bins)
plt.xlabel('Skill Levels')
plt.ylabel('Number of Players')
plt.title('Distribution of Player Skill in FIFA 2018')
plt.show()'''

'''###-------------------Pie Chart Example-----------------------------###
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
# print(left)
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
# print(right)
plt.title('Foot Preferance of FIFA Players')
explode = (0, 0.1)
labels = ['Left','Right']
plt.pie([left, right], labels=labels, explode=explode, colors=['#36db27','#ebe844'], autopct='%.2f%%', shadow=True, startangle=90)
plt.show()
'''

'''###-------------------------Pie Chart Example--------------------------------###
fifa.Weight  = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
plt.style.use('ggplot')

light = fifa.loc[fifa.Weight < 125].count()[0]
# print(light)
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
# print(light_medium)
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
# print(medium)
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
# print(medium_heavy)
heavy = fifa.loc[fifa.Weight >= 200].count()[0]
# print(heavy)

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
colors = ['#ed2a24', '#f5f125', '#1deb1a', '#204de3', '#9420c9']
explode = (.2,.2,0,0,.2)
plt.title('Weight Distribution Of FIFA Players(in lbs)')
plt.pie(weights, labels=labels, explode=explode, colors=colors, autopct='%.2f%%', pctdistance=0.8)
plt.show()'''


'''barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
# print(barcelona)
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
# print(madrid)
chelsea = fifa.loc[fifa.Club == 'Chelsea']['Overall']
# print(chelsea)
paris = fifa.loc[fifa.Club == 'Paris Saint-Germain']['Overall']
# print(paris)
labels = ['FC Barcelona', 'Real Madrid', 'Chelsea', 'Paris Saint-Germain']
plt.figure(figsize=(7,6))
plt.title('Professional Football Team Comparison')
plt.ylabel('FIFA Overall Rating')
boxes = plt.boxplot([barcelona, madrid, chelsea, paris], labels=labels, patch_artist=True)
for box in boxes['boxes']:
    box.set(color='#2e44f0', linewidth=2)
    box.set(facecolor='#aad5f0')
plt.show()'''


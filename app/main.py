import pandas as pd

def run():
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'South America']

    countries = df['Country'].values
    percentages = df['World Population Percentage'].values

    charts.generate_pie_chart(countries, percentages)

    print(countries)


if __name__=="__main__":
    run()
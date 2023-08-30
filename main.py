import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.ticker as ticker

country_to_continent = {
    'Afghanistan': 'Ásia (ONU)',
    'África (ONU)': 'África (ONU)',
    'Albania': 'Europa (ONU)',
    'Algeria': 'África (ONU)',
    'American Samoa': 'Oceania (ONU)',
    'Andorra': 'Europa (ONU)',
    'Angola': 'África (ONU)',
    'Anguilla': 'América do Norte (ONU)',
    'Antigua and Barbuda': 'América do Norte (ONU)',
    'Argentina': 'América do Norte (ONU)',
    'Armenia': 'Europa (ONU)',
    'Aruba': 'América do Norte (ONU)',
    'Ásia (ONU)': 'Ásia (ONU)',
    'Australia': 'Oceania (ONU)',
    'Austria': 'Europa (ONU)',
    'Azerbaijan': 'Ásia (ONU)',
    'Bahamas': 'América do Norte (ONU)',
    'Bahrain': 'Ásia (ONU)',
    'Bangladesh': 'Ásia (ONU)',
    'Barbados': 'América do Norte (ONU)',
    'Belarus': 'Europa (ONU)',
    'Belgium': 'Europa (ONU)',
    'Belize': 'América do Norte (ONU)',
    'Benin': 'África (ONU)',
    'Bermuda': 'América do Norte (ONU)',
    'Bhutan': 'Ásia (ONU)',
    'Bolivia': 'América do Norte (ONU)',
    'Bonaire Sint Eustatius and Saba': 'América do Norte (ONU)',
    'Bosnia and Herzegovina': 'Europa (ONU)',
    'Botswana': 'África (ONU)',
    'Brazil': 'América do Norte (ONU)',
    'British Virgin Islands': 'América do Norte (ONU)',
    'Brunei': 'Ásia (ONU)',
    'Bulgaria': 'Europa (ONU)',
    'Burkina Faso': 'África (ONU)',
    'Burundi': 'África (ONU)',
    'Cambodia': 'Ásia (ONU)',
    'Cameroon': 'África (ONU)',
    'Canada': 'América do Norte (ONU)',
    'Cape Verde': 'África (ONU)',
    'Cayman Islands': 'América do Norte (ONU)',
    'Central African Republic': 'África (ONU)',
    'Chad': 'África (ONU)',
    'Chile': 'América do Norte (ONU)',
    'China': 'Ásia (ONU)',
    'Colombia': 'América do Norte (ONU)',
    'Comoros': 'África (ONU)',
    'Congo': 'África (ONU)',
    'Cook Islands': 'Oceania (ONU)',
    'Costa Rica': 'América do Norte (ONU)',
    "Cote d'Ivoire": 'África (ONU)',
    'Croatia': 'Europa (ONU)',
    'Cuba': 'América do Norte (ONU)',
    'Curacao': 'América do Norte (ONU)',
    'Cyprus': 'Ásia (ONU)',
    'Czechia': 'Europa (ONU)',
    'Democratic Republic of Congo': 'África (ONU)',
    'Denmark': 'Europa (ONU)',
    'Djibouti': 'África (ONU)',
    'Dominica': 'América do Norte (ONU)',
    'Dominican Republic': 'América do Norte (ONU)',
    'East Timor': 'Ásia (ONU)',
    'Ecuador': 'América do Norte (ONU)',
    'Egypt': 'África (ONU)',
    'El Salvador': 'América do Norte (ONU)',
    'Equatorial Guinea': 'África (ONU)',
    'Eritrea': 'África (ONU)',
    'Estonia': 'Europa (ONU)',
    'Eswatini': 'África (ONU)',
    'Ethiopia': 'África (ONU)',
    'Europa (ONU)': 'Europa (ONU)',
    'Falkland Islands': 'América do Norte (ONU)',
    'Faroe Islands': 'Europa (ONU)',
    'Fiji': 'Oceania (ONU)',
    'Finland': 'Europa (ONU)',
    'France': 'Europa (ONU)',
    'French Guiana': 'América do Norte (ONU)',
    'French Polynesia': 'Oceania (ONU)',
    'Gabon': 'África (ONU)',
    'Gambia': 'África (ONU)',
    'Georgia': 'Ásia (ONU)',
    'Germany': 'Europa (ONU)',
    'Ghana': 'África (ONU)',
    'Gibraltar': 'Europa (ONU)',
    'Greece': 'Europa (ONU)',
    'Greenland': 'América do Norte (ONU)',
    'Grenada': 'América do Norte (ONU)',
    'Guadeloupe': 'América do Norte (ONU)',
    'Guam': 'Oceania (ONU)',
    'Guatemala': 'América do Norte (ONU)',
    'Guernsey': 'Europa (ONU)',
    'Guinea': 'África (ONU)',
    'Guinea-Bissau': 'África (ONU)',
    'Guyana': 'América do Norte (ONU)',
    'Haiti': 'América do Norte (ONU)',
    'Honduras': 'América do Norte (ONU)',
    'Hong Kong': 'Ásia (ONU)',
    'Hungary': 'Europa (ONU)',
    'Iceland': 'Europa (ONU)',
    'India': 'Ásia (ONU)',
    'Indonesia': 'Ásia (ONU)',
    'Iran': 'Ásia (ONU)',
    'Iraq': 'Ásia (ONU)',
    'Ireland': 'Europa (ONU)',
    'Isle of Man': 'Europa (ONU)',
    'Israel': 'Ásia (ONU)',
    'Italy': 'Europa (ONU)',
    'Jamaica': 'América do Norte (ONU)',
    'Japan': 'Ásia (ONU)',
    'Jersey': 'Europa (ONU)',
    'Jordan': 'Ásia (ONU)',
    'Kazakhstan': 'Ásia (ONU)',
    'Kenya': 'África (ONU)',
    'Kiribati': 'Oceania (ONU)',
    'Kosovo': 'Europa (ONU)',
    'Kuwait': 'Ásia (ONU)',
    'Kyrgyzstan': 'Ásia (ONU)',
    'Laos': 'Ásia (ONU)',
    'Latvia': 'Europa (ONU)',
    'Lebanon': 'Ásia (ONU)',
    'Lesotho': 'África (ONU)',
    'Liberia': 'África (ONU)',
    'Libya': 'África (ONU)',
    'Liechtenstein': 'Europa (ONU)',
    'Lithuania': 'Europa (ONU)',
    'Luxembourg': 'Europa (ONU)',
    'Macao': 'Ásia (ONU)',
    'Madagascar': 'África (ONU)',
    'Malawi': 'África (ONU)',
    'Malaysia': 'Ásia (ONU)',
    'Maldives': 'Ásia (ONU)',
    'Mali': 'África (ONU)',
    'Malta': 'Europa (ONU)',
    'Marshall Islands': 'Oceania (ONU)',
    'Martinique': 'América do Norte (ONU)',
    'Mauritania': 'África (ONU)',
    'Mauritius': 'África (ONU)',
    'Mayotte': 'África (ONU)',
    'Mexico': 'América do Norte (ONU)',
    'Micronesia (country)': 'Oceania (ONU)',
    'Moldova': 'Europa (ONU)',
    'Monaco': 'Europa (ONU)',
    'Mongolia': 'Ásia (ONU)',
    'Montenegro': 'Europa (ONU)',
    'Montserrat': 'América do Norte (ONU)',
    'Morocco': 'África (ONU)',
    'Mozambique': 'África (ONU)',
    'Myanmar': 'Ásia (ONU)',
    'Namibia': 'África (ONU)',
    'Nauru': 'Oceania (ONU)',
    'Nepal': 'Ásia (ONU)',
    'Netherlands': 'Europa (ONU)',
    'New Caledonia': 'Oceania (ONU)',
    'New Zealand': 'Oceania (ONU)',
    'Nicaragua': 'América do Norte (ONU)',
    'Niger': 'África (ONU)',
    'Nigeria': 'África (ONU)',
    'Niue': 'Oceania (ONU)',
    'North Korea': 'Ásia (ONU)',
    'North Macedonia': 'Europa (ONU)',
    'América do Norte (ONU)': 'América do Norte (ONU)',
    'Northern Mariana Islands': 'Oceania (ONU)',
    'Norway': 'Europa (ONU)',
    'Oceania (ONU)': 'Oceania (ONU)',
    'Oman': 'Ásia (ONU)',
    'Pakistan': 'Ásia (ONU)',
    'Palau': 'Oceania (ONU)',
    'Palestine': 'Ásia (ONU)',
    'Panama': 'América do Norte (ONU)',
    'Papua New Guinea': 'Oceania (ONU)',
    'Paraguay': 'América do Norte (ONU)',
    'Peru': 'América do Norte (ONU)',
    'Philippines': 'Ásia (ONU)',
    'Poland': 'Europa (ONU)',
    'Portugal': 'Europa (ONU)',
    'Puerto Rico': 'América do Norte (ONU)',
    'Qatar': 'Ásia (ONU)',
    'Reunion': 'África (ONU)',
    'Romania': 'Europa (ONU)',
    'Russia': 'Ásia (ONU)',
    'Rwanda': 'África (ONU)',
    'Saint Barthelemy': 'América do Norte (ONU)',
    'Saint Helena': 'África (ONU)',
    'Saint Kitts and Nevis': 'América do Norte (ONU)',
    'Saint Lucia': 'América do Norte (ONU)',
    'Saint Martin (French part)': 'América do Norte (ONU)',
    'Saint Pierre and Miquelon': 'América do Norte (ONU)',
    'Saint Vincent and the Grenadines': 'América do Norte (ONU)',
    'Samoa': 'Oceania (ONU)',
    'San Marino': 'Europa (ONU)',
    'Sao Tome and Principe': 'África (ONU)',
    'Saudi Arabia': 'Ásia (ONU)',
    'Senegal': 'África (ONU)',
    'Serbia': 'Europa (ONU)',
    'Seychelles': 'África (ONU)',
    'Sierra Leone': 'África (ONU)',
    'Singapore': 'Ásia (ONU)',
    'Sint Maarten (Dutch part)': 'América do Norte (ONU)',
    'Slovakia': 'Europa (ONU)',
    'Slovenia': 'Europa (ONU)',
    'Small island developing states (SIDS)': 'América do Norte (ONU)',
    'Solomon Islands': 'Oceania (ONU)',
    'Somalia': 'África (ONU)',
    'South Africa': 'África (ONU)',
    'South Korea': 'Ásia (ONU)',
    'South Sudan': 'África (ONU)',
    'Spain': 'Europa (ONU)',
    'Sri Lanka': 'Ásia (ONU)',
    'Sudan': 'África (ONU)',
    'Suriname': 'América do Norte (ONU)',
    'Sweden': 'Europa (ONU)',
    'Switzerland': 'Europa (ONU)',
    'Syria': 'Ásia (ONU)',
    'Taiwan': 'Ásia (ONU)',
    'Tajikistan': 'Ásia (ONU)',
    'Tanzania': 'África (ONU)',
    'Thailand': 'Ásia (ONU)',
    'Togo': 'África (ONU)',
    'Tokelau': 'Oceania (ONU)',
    'Tonga': 'Oceania (ONU)',
    'Trinidad and Tobago': 'América do Norte (ONU)',
    'Tunisia': 'África (ONU)',
    'Turkey': 'Ásia (ONU)',
    'Turkmenistan': 'Ásia (ONU)',
    'Turks and Caicos Islands': 'América do Norte (ONU)',
    'Tuvalu': 'Oceania (ONU)',
    'Uganda': 'África (ONU)',
    'Ukraine': 'Europa (ONU)',
    'United Arab Emirates': 'Ásia (ONU)',
    'United Kingdom': 'Europa (ONU)',
    'United States': 'América do Norte (ONU)',
    'United States Virgin Islands': 'América do Norte (ONU)',
    'Uruguay': 'América do Norte (ONU)',
    'Uzbekistan': 'Ásia (ONU)',
    'Vanuatu': 'Oceania (ONU)',
    'Venezuela': 'América do Norte (ONU)',
    'Vietnam': 'Ásia (ONU)',
    'Wallis and Futuna': 'Oceania (ONU)',
    'Western Sahara': 'África (ONU)',
    'Yemen': 'Ásia (ONU)',
    'Zambia': 'África (ONU)',
    'Zimbabwe': 'África (ONU)'
}

def get_continent(country_code: str):
    try:
        return country_to_continent[country_code]
    except KeyError:
        return None

df = pd.read_csv('population-and-demography.csv')

filtered_data = df

filtered_data['Year'] = pd.to_datetime(df['Year'], format='%Y')
filtered_data['Continente'] = df['Country name'].apply(get_continent)

filtered_data = filtered_data[filtered_data['Country name'] != 'Less developed regions']
filtered_data = filtered_data[filtered_data['Country name'] != 'Less developed regions, excluding China']
filtered_data = filtered_data[filtered_data['Country name'] != 'Less developed regions']
filtered_data = filtered_data[filtered_data['Country name'] != 'Less developed regions, excluding least developed countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'Land-locked developing countries (LLDC)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Latin America and the Caribbean (UN)']
filtered_data = filtered_data[filtered_data['Country name'] != 'World']
filtered_data = filtered_data[filtered_data['Country name'] != 'Oceania (UN)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Small island developing states (SIDS)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Low-income countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'High-income countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'Lower-middle-income countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'More developed regions']
filtered_data = filtered_data[filtered_data['Country name'] != 'Least developed countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'Least developed regions']
filtered_data = filtered_data[filtered_data['Country name'] != 'Upper-middle-income countries']
filtered_data = filtered_data[filtered_data['Country name'] != 'Asia (UN)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Africa (UN)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Europe (UN)']
filtered_data = filtered_data[filtered_data['Country name'] != 'Northern America (UN)']

filtered_data = filtered_data

def line_chart_visualization():
   
    df_yearly = filtered_data.groupby('Year')['Population'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(df_yearly['Year'], df_yearly['Population'])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Aumento Populacional')
    ax.set_title('Crescimento populacional anual no mundo')

    formatter = ticker.FuncFormatter(lambda x, pos: f'{x/1e9:.1f}B')
    ax.yaxis.set_major_formatter(formatter)

    plt.show()

def bar_chart_visualization():
    last_year_per_continent = filtered_data.groupby('Continente')['Year'].max()

    df_last_year_per_continent = filtered_data[filtered_data['Year'].isin(last_year_per_continent)].dropna()

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.bar(df_last_year_per_continent['Continente'], df_last_year_per_continent['Population'])
    ax.set_xlabel('Continente')
    ax.set_ylabel('População')
    ax.set_title(f'População no ano de {filtered_data["Year"].max()}')

    formatter = ticker.FuncFormatter(lambda x, pos: f'{x/1e9:.1f}B')
    ax.yaxis.set_major_formatter(formatter)
    
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def treemap_visualization():
    filtered_data_local = filtered_data
    filtered_data_local['Year'] = filtered_data_local['Year'].apply(lambda x: x.year)

    max_year = filtered_data['Year'].max()
    filtered_data_local = filtered_data_local[filtered_data_local['Year'] == max_year]
    grouped_data = filtered_data_local[filtered_data_local['Population'] > 0].groupby(['Country name', 'Year'], as_index=False).sum()

    fig = px.treemap(grouped_data, 
                    path=['Country name', 'Year'], 
                    values='Population',
                    title=f'População por País no ano de {max_year}',
                    color='Population',
                    color_continuous_scale='Viridis')
    
    filename = "treemap_visualization.html"
    fig.write_html(filename)


treemap_visualization()
bar_chart_visualization()
line_chart_visualization()
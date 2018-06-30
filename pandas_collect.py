import pandas as pd


def get_data():
    base_url = "http://static.admitere.edu.ro/2013/staticRepI/j/TM/cina/page_"
    data_sink = []
    for i in range(1,216):
        url=base_url+str(i)+'.html'
        dfs = pd.read_html(url, attrs={'class':'mainTable'},header=None,skiprows=[0])
        for i in range(0,20):
            name=dfs[0][1][i]
            grade=dfs[0][5][i]
            school=str(dfs[0][13][i])
            if 'Uman' in school:
                school=school[:school.index('Uman')]
            if 'Real' in school:
                school=school[:school.index('Real')]
            if 'Servicii' in school:
                school=school[:school.index('Servicii')]
            if 'Tehnic' in school:
                school=school[:school.index('Tehnic')]
            if 'Resurse' in school:
                school=school[:school.index('Resurse')]
            data_sink.append((name,school,grade))
            print(name,grade,school)

    return data_sink
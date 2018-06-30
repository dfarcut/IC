import requests
import bs4 as bs
import time

data_sink=[]

def get_school_names_on_page(soup):
    schools=[]
    school_names = soup.select('a[href="../../lista_unitati/index.html"]')
    for school in school_names:
        school_name = school.get_text().lstrip()
        schools.append(school_name)
        print(school_name)
    return schools

def get_names_and_grades_on_page(soup):
    name_and_grades_list=[]
    table = soup.find('table',attrs={'class':'mainTable'})
    table_scripts=table.find_all('script')
    for row in table_scripts:
        name_selector='LuatDePeBacalaureatEduRo["'
        text2=row.text
        txt='"]="'
        if txt in text2:
            name_idx=text2.index(name_selector)+len(name_selector)
            idx=text2.index(txt)
            name=text2[name_idx:idx]
            name=name.replace('<br>','')
            t3=text2[idx+4:]
            grade_idx=t3.index(txt)
            grade=t3[grade_idx+4:grade_idx+8]
            if '";L' in grade:
                grade=0
            else:
                if '"' in grade:
                    if "10" in grade:
                        grade=float(10)
                    else:
                        grade=float(grade[:len(grade)-1])
                else:
                    grade=float(grade)
            print(name+' '+str(grade))
            name_and_grades_list.append((name,grade))
    return name_and_grades_list

def add_page_data_to_datasink(name_and_grades_list,schools_list):
    for i in range(0,len(name_and_grades_list)):
        school = str(schools_list[i])
        name = str(name_and_grades_list[i][0])
        grade = name_and_grades_list[i][1]
        data_sink.append((name,school,grade))



def get_data():
    base_link='http://static.bacalaureat.edu.ro/2017/rapoarte/TM/rezultate/alfabetic/page_'
    for i in range(1,420):
        link= base_link+str(i)+'.html'
        r = requests.get(link)
        text =r.text
        soup = bs.BeautifulSoup(text,'html.parser')
        name_and_grades_list=get_names_and_grades_on_page(soup)
        schools_list=get_school_names_on_page(soup)
        add_page_data_to_datasink(name_and_grades_list,schools_list)

    for touple in data_sink:
        print(touple)
    return data_sink

def get_class_members(soup,clas):
    member_list=[]
    memb = soup.find('div',attrs={'id':'content'})
    # print(memb)
    members = memb.find_all('a')
    sel1='href="'
    sel2='/"'
    # members = soup.select('a[href="*/"]')
    # print(members)
    for mem in members:
        mem=str(mem)
        idx1=mem.index(sel1)
        idx2=mem.index(sel2)
        name=mem[idx1+6:idx2].replace('_',' ')
        if 'profesori' not in name:
            member_list.append(name)
            print(name)
    return (clas,member_list)

def get_class_in_highschool():
    classes=[]
    class_list=['A','B','C','D','E']
    base_link="http://info.tm.edu.ro/alumni/2017/clasa/XII_"
    for i in class_list:
        link=base_link+i
        r = requests.get(link)
        text = r.text
        #print(text)
        soup= bs.BeautifulSoup(text,'html.parser')
        class_members_touple=get_class_members(soup,i)
        classes.append(class_members_touple)
    return classes

get_class_in_highschool()
if 'Bandi'.upper() in 'BANDI S. EUSEBIU - CATALIN':
    print('da da da')
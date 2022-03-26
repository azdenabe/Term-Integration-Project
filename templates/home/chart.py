import json
import requests
import pandas as pd
import numpy as np

def sla_total(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/sla_met/all_closed/{month}')
    j = r.json()

    raised_per_prio = j['items']
    priority = []
    data = []
    for element in raised_per_prio:
        priority.append(element['priority'])
        data.append(element['count(*)'])
    myorder = [2, 0, 3, 1]
    data = [data[i] for i in myorder]
    return data

def week_closed():
    r = requests.get('https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/closes_week/all_closed/')
    j = r.json()

    raised_per_prio = j['items']
    week = []
    number1 = []
    for element in raised_per_prio:
        week.append(element['week_number'])
        number1.append(element['count(*)'])

    week.insert(0, week.pop())
    number1.insert(0, number1.pop())
    number1[0] = number1[0]+number1[1]
    number1.pop(1)
    week.pop(0)
    return number1

def week_opened():
    r = requests.get('https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/open_week/all_raised/')
    j = r.json()

    raised_per_prio = j['items']
    week_op = []
    number1_op = []
    for element in raised_per_prio:
        week_op.append(element['week_number'])
        number1_op.append(element['count(*)'])

    week_op.insert(0, week_op.pop())
    number1_op.insert(0, number1_op.pop())
    number1_op[0] = number1_op[0]+number1_op[1]
    number1_op.pop(1)
    week_op.pop(0)
    return  number1_op

def mtbr(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/mtbr/all_closed/{month}')
    j = r.json()

    raised_per_prio = j['items']
    priority = []
    avg = []
    for element in raised_per_prio:
        priority.append(element['priority'])
        avg.append(element['mtbr'])
    myorder = [2, 0, 3, 1]
    avg = [avg[i] for i in myorder]

    return avg

def closed(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/pasta/ciao/{month}')
    j = r.json()

    raised_per_prio = j['items']
    num_close = []
    for element in raised_per_prio:
        num_close.append(element['count(*)'])
    #myorder = [2, 0, 3, 1]
    #avg = [avg[i] for i in myorder]

    return num_close


def opened(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/opened_month/all_raised/{month}')
    j = r.json()

    raised_per_prio = j['items']
    num_op = []
    for element in raised_per_prio:
        num_op.append(element['count(*)'])
    #myorder = [2, 0, 3, 1]
    #avg = [avg[i] for i in myorder]

    return num_op

def backlog(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/backlog/all_backlog/{month}')
    j = r.json()

    raised_per_prio = j['items']
    num_bl = []
    for element in raised_per_prio:
        num_bl.append(element['count(*)'])
    #myorder = [2, 0, 3, 1]
    #avg = [avg[i] for i in myorder]

    return num_bl


def week_critic_raised():
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/critical_week/all_raised/')
    j = r.json()

    raised_per_prio = j['items']
    wcr = []
    number_wcr = []
    for element in raised_per_prio:
        wcr.append(element['from_week'])


        number_wcr.append(element['count(*)'])
    wcr =(list(map(int, wcr)))
    wcr_num = pd.DataFrame(
        {'week': wcr,
         'num': number_wcr

         })
    start, end = wcr_num['week'].agg(['min', 'max'])

    wcr_num = wcr_num.set_index('week').reindex(np.arange(start-1, end+1), fill_value=0).reset_index()
    number_wcr = wcr_num['num'].to_list()
    return number_wcr



def week_critic_closed():
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/critical_week_closed/all_closed/')
    j = r.json()

    raised_per_prio = j['items']
    wcc = []
    number_wcc = []
    for element in raised_per_prio:
        wcc.append(element['from_week'])


        number_wcc.append(element['count(*)'])
    wcc =(list(map(int, wcc)))
    wcc_num = pd.DataFrame(
        {'week': wcc,
         'num': number_wcc

         })
    start, end = wcc_num['week'].agg(['min', 'max'])

    wcc_num = wcc_num.set_index('week').reindex(np.arange(start-1, end+1), fill_value=0).reset_index()
    number_wcc = wcc_num['num'].to_list()
    return number_wcc



def sla_met(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/sla_met_month/all_closed/{month}')
    j = r.json()

    raised_per_prio = j['items']
    priority = []
    data_met = []
    for element in raised_per_prio:
        priority.append(element['priority'])
        data_met.append(element['count(*)'])
    myorder = [2, 0, 3, 1]
    data_met = [data_met[i] for i in myorder]
    return data_met



def average_met(month):
    average = []
    end_index = len(sla_met(month))

    for i in range(end_index):
        average.append(sla_met(month)[i] / sla_total(month)[i])
    perc =  [i*100 for i in average]
    perc_met = [round(elem, 1) for elem in perc]
    return perc_met

def average_week():
    average = []
    end_index = len(week_critic_raised())

    for i in range(end_index):
        if week_critic_closed()[i] != 0:
            average.append(week_critic_closed()[i]/week_critic_raised()[i] )
        else:
            i = i + 1
    perc_week =  [i*100 for i in average]
    perc_week = [round(elem, 1) for elem in perc_week]
    return perc_week

def sla_not_met(month):
    met = sla_met(month)
    total = sla_total(month)
    sla_non_met = [a_i - b_i for a_i, b_i in zip(total, met)]
    return sla_non_met

def average_not_met(month):
    average = []
    end_index = len(sla_not_met(month))

    for i in range(end_index):
        average.append(sla_not_met(month)[i] / sla_total(month)[i])
    perc =  [i*100 for i in average]
    perc_not = [round(elem, 1) for elem in perc]
    return perc_not


def mtbr_met(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/mtbr_met_month/all_closed/{month}')
    j = r.json()

    raised_per_prio = j['items']
    priority = []
    avg = []
    for element in raised_per_prio:
        priority.append(element['priority'])
        avg.append(element['avg(time_to_resolve)'])
    myorder = [2, 0, 3, 1]
    avg_met = [avg[i] for i in myorder]
    avg_met = [round(elem) for elem in avg_met]

    return avg_met

def mtbr_not_met(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/mtbr_not_met_month/all_closed/{month}')
    j = r.json()

    raised_per_prio = j['items']
    priority = []
    avg = []
    for element in raised_per_prio:

        priority.append(element['priority'])
        avg.append(element['avg(time_to_resolve)'])
    myorder = [2, 0, 3, 1]
    if len(avg) == len(myorder):
        avg_not_met = [avg[i] for i in myorder]
        avg_not_met = [round(elem) for elem in avg_not_met]
    else:
        myorder = [1, 2, 0]
        avg_not_met = [avg[i] for i in myorder]
        avg_not_met = [round(elem) for elem in avg_not_met]
        avg_not_met.insert(0,0)

    return avg_not_met


def incident_mont(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/incident_month/all_raised/{month}')
    j = r.json()

    raised_per_prio = j['items']
    incident = []
    inc_mon = []
    for element in raised_per_prio:
        incident.append(element['inc_type'])
        inc_mon.append(element['count(*)'])

    return inc_mon


def month(month):
    print(sla_total(month))
    print(sla_met(month))
    print(sla_not_met(month))
    print(average_met(month))
    print(average_not_met(month))
    print(mtbr_met(month))
    print(mtbr_not_met(month))




def closed_prio(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/hello/hi/{month}')
    j = r.json()

    raised_per_prio = j['items']
    clos_prio = []
    for element in raised_per_prio:
        clos_prio.append(element['count(*)'])
    #myorder = [2, 0, 3, 1]
    #avg = [avg[i] for i in myorder]
    clos_prio.reverse()

    return clos_prio

def open_prio(month):
    r = requests.get(f'https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/merola/mamma/{month}')
    j = r.json()

    raised_per_prio = j['items']
    open_prio = []
    for element in raised_per_prio:
        open_prio.append(element['count(*)'])
    #myorder = [2, 0, 3, 1]
    #avg = [avg[i] for i in myorder]
    open_prio.reverse()

    return open_prio

print(opened(1))
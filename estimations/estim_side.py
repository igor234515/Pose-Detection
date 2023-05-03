import json
nose_etalon = 180
sup_st_etalon = 90
sup_fin_etalon = 180
def estim(file_save:str, nose_array,support_array,time):
    try:
        with open(file_save,'r') as json_file:
            json_decoded = json.load(json_file)
    except FileNotFoundError:
        print('file not found')
        json_decoded={}

    st_n,fin_n=time
    key=f'frame {st_n} : {fin_n}'
    nose=nose_array[0]
    sup_st=support_array[0]
    sup_fin=support_array[-1]
    nose_estim=max(0,nose_etalon-nose)
    sup_st_estim=max(0,sup_st-sup_st_etalon)
    sup_fin_estim=max(0,sup_fin_etalon-sup_fin)
    total=nose_estim+sup_st_estim+sup_fin_estim
    estim={'nose_estim': nose_estim,'sup_st_estim': sup_st_estim,
           'sup_fin_estim': sup_fin_estim,'total':total}
    value={'nose':nose,'sup_st':sup_st,'sup_fin':sup_fin}
    all_dict={'estimations':estim,'value':value}
    json_decoded[key]=all_dict
    with open(file_save, 'w') as json_file:
        json.dump(json_decoded, json_file)

#coding:utf-8
import json
import re
import pandas as pd

'''Excel数据处理转化成json'''

def text_split(text):
    # 连续多个空格，合并为一个
    text = re.sub(r'\s+',' ', text)
    # 去除空格
    text = re.sub(' ', '', text)
    text1 = re.split(r'。', text)

    return text1

def merge(intervals):
    """
    :param intervals: List[List[int]]
    :return: List[List[int]]
    """

    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
    return merged

def get_all_entity_position(text, entities):

    # entities为空时
    if pd.isna(entities):
        return []
    al_ent = [s for s in entities.split(',') if s != '']

    ent_posit = []
    for ent in al_ent:
        al = re.finditer(re.escape(ent), text)
        for i in al:
            positions = i.span()
            ent_posit.append([positions[0], positions[1]])
    # 若ent_posit包含两个区间以上，其中可能包含重叠的区间
    # 比如胸骨、骨、锁骨都是“转移部位”的实体，其对应位置[0,2],[1,2],[4,5],[5,7],[6,7]
    # 需要合并
    if len(ent_posit) >=2:
        ent_posit = merge(ent_posit)

    return ent_posit
def get_json(data, file_path):
    
    entity_type = ['肿瘤原发部位','原发病灶大小','转移部位']
    label_type = ["ORI","SIZ","TRA"]
    result = []
    output, label = {}, {}
    dict1 = {}
    for _, line in data.iterrows():
        yuanwen = line['原文']
        # enti
        yuanwen1 = text_split(yuanwen)
        #max_len = max(len(inst) for inst in yuanwen1)
        for t in yuanwen1:
            if t == '':
                continue
            output = {}
            label = {}
            for entity_name, lab in zip(entity_type, label_type):
                entities = line[entity_name]
                ent_pos = get_all_entity_position(t, entities)
                dict1[entity_name] = ent_pos
                label[lab] = dict1
                dict1 = {}
            output["text"] = t
            output["label"] = label
            result.append(output)



    with open(file_path,"w", encoding='utf-8') as f:
        
        for new_dic in result:
            #new_dict = json.loads(new_dic)
            json.dump(new_dic,f, ensure_ascii=False)
            f.write('\n')
        print("加载入文件完成...")

    return result

if __name__ == '__main__':
    train_data1 = pd.read_excel('./data/training_part1.xlsx')
    train_data2 = pd.read_excel('./data/training_part2.xlsx')
    test_data =  pd.read_excel('./data/test.xlsx')
    #data = pd.concat((train_data1, train_data2), axis=0, ignore_index=True)
    save_train = "./json_data/train.json"
    save_dev = "./json_data/dev.json"
    save_test = "./json_data/test.json"
    result = get_json(train_data1,save_train)
    result_dev = get_json(train_data2, save_dev)
    result_test = get_json(test_data,save_test)

    




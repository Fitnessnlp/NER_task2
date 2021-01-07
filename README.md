# Implement of ALBERT for Chinese Clinical NER Task
## 数据
>>> json_data包含json格式的病历数据，data文件夹中有原始数据

## 代码：
>> albert_model_train.py是albert + bilstm
>> albert_crf_model_train.py是albert + bilstm + crf
>> load_data.py
>> preprocess_data.py将原始数据转化成json格式

## 模型结果：
#### albert+bilstm
     >>precision    recall  f1-score   support
     ORI     0.7077    0.6126    0.6567       826
     TRA     0.6855    0.5616    0.6174       885
      SIZ     0.2787    0.3301    0.3022       103

    micro avg     0.6639    0.5717    0.6143      1814
    macro avg     0.6725    0.5717    0.6174      1814

# ALBERT for Chinese Clinical NER Task
## 说明：
* albert_zh为ALBERT提取文本特征模块，这部分代码是开源的
* 标注采用BIO系统
* utils.py是配置文件路径和模型等参数
* load_data.py将标签转为id，生成label2id.json文件
* preprocess_data.py将原始数据转化成json格式 
* 模型训练是albert_model_train.py和albert_crf_model_train.py

## 数据：
>>> data中有电子病历的标注数据和非标注数据
>>> json_data包含json格式的病历数据，data文件夹中有原始数据

 

## 模型结果：
#### albert_model
          precision    recall  f1-score   support
     ORI     0.7077    0.6126    0.6567       826
     TRA     0.6855    0.5616    0.6174       885
      SIZ     0.2787    0.3301    0.3022       103

    micro avg     0.6639    0.5717    0.6143      1814
    macro avg     0.6725    0.5717    0.6174      1814

#### albert_crf_model
          precision    recall  f1-score   support
     ORI     0.5082    0.2252    0.3121       826
     TRA     0.2217    0.0994    0.1373       885
      SIZ     0.1333    0.0194    0.0339       103

    micro avg     0.3548    0.1521    0.2130      1814
    macro avg     0.3471    0.1521    0.2110      1814

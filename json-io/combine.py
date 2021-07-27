# import json
# import os

# spoList = []
# with open("./duie(bert).json", 'r', encoding='utf8') as f:
#     for jsonObj in f:
#         spoDict = json.loads(jsonObj)
#         spoList.append(spoDict)

# print("number of object: ", len(spoList))

# print("\nprintin each json obejct")
# spotest = spoList[:3]
# print(spotest)

# print("====================")

# with open("./comb.json", "a+", encoding='utf8') as f:
#     for i in range(len(spotest)):
#         f.seek(0)
#         data = f.read(100)
#         if len(data) > 0:
#             f.write("\n")
#         spojson = json.dumps(spotest[i], ensure_ascii=False)
#         f.write(spojson)

import json
from tqdm.autonotebook import tqdm

with open("./duie(roberta).json", "r", encoding="utf8") as froberta, open("duie(pytorch).json", "r", encoding="utf8") as fpytorch, open("./duie(bert).json", "r", encoding="utf8") as fbert:
    robertaObjs = []
    pytorchObjs = []
    bertObjs = []
    for robertaObj in froberta:
        spoDict = json.loads(robertaObj)
        robertaObjs.append(spoDict)
    for pytorchObj in fpytorch:
        spoDict = json.loads(pytorchObj)
        pytorchObjs.append(spoDict)    
    for bertObj in fbert:
        spoDict = json.loads(bertObj)
        bertObjs.append(spoDict)

    res = []

    for i in tqdm(range(len(robertaObjs))):
        robertaObjs_spo_list = robertaObjs[i]["spo_list"]
        pytorchObjs_spo_list = pytorchObjs[i]["spo_list"]
        bertObjs_spo_list = bertObjs[i]["spo_list"]
        temp_res = []
        for robertaObjs_spo_list_obj in robertaObjs_spo_list:
            if robertaObjs_spo_list_obj in pytorchObjs_spo_list or robertaObjs_spo_list_obj in bertObjs_spo_list:
                temp_res.append(robertaObjs_spo_list_obj)
        
        for pytorchObjs_spo_list_obj in pytorchObjs_spo_list:
            if (pytorchObjs_spo_list_obj in robertaObjs_spo_list or pytorchObjs_spo_list_obj in bertObjs_spo_list) and pytorchObjs_spo_list_obj not in temp_res:
                temp_res.append(pytorchObjs_spo_list_obj)
        #有些句子就是不用抽取的 不要加入
        # if len(temp_res) == 0:
        #     if len(pytorchObjs_spo_list) != 0:
        #         temp_res = pytorchObjs_spo_list
        #     elif len(robertaObjs_spo_list) != 0:
        #         temp_res = robertaObjs_spo_list
        #     elif len(bertObjs_spo_list) != 0:
        #         temp_res = bertObjs_spo_list
        res.append(temp_res)
   
    for i in tqdm(range(len(robertaObjs))):
        robertaObjs[i]["spo_list"] = res[i]
    
print("======")
with open("./comb.json", "a+", encoding='utf8') as f:
    for i in range(len(robertaObjs)):
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        spojson = json.dumps(robertaObjs[i], ensure_ascii=False)
        f.write(spojson)

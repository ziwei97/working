# get files
import boto3
import os
import pandas as pd

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'BURN_ImageCollection'


table = dynamodb.Table(table_name)
# name = '103-022'

listcheck = pd.read_excel('/Users/ziweishi/Desktop/December-Truthing.xlsx',sheet_name='NeedAlgorithmMask')
rightcheck = pd.read_excel('/Users/ziweishi/Desktop/December-Truthing.xlsx',sheet_name='Sheet1')
name_list = listcheck["ImageCollectionGUID"]
right_list = rightcheck["bts"]
# print(name_list)

# collection_list_response = table.get_item(
#     Key = {
#         'Subject':name,
#         'Wound': '2'
#
#     }
# )
# collection_list = collection_list_response["Item"]["ImageCollections"]


# burn = pd.read_excel('/Users/ziweishi/Desktop/requested.xlsx', sheet_name='burn_study')
# burn_list = burn["ImgCollGUID"].tolist()

final_truth = []

# refrence = []

# check = []

# epoc_subject_id = []
# epoc_wound = []
#
for i in name_list:
    response = table.get_item(
        Key={
            'ImgCollGUID': i
        }
    )
    try:
        # refrence.append(response["Item"]["Reference"])
        # bucket.append(response["Item"]["Bucket"])
        # check.append(response["Item"]["Suffix"])
        # epoc_subject_id.append(response["Item"]["SubjectID"])
        a = response["Item"]["FinalTruth"]
        final_truth.append(a[0])
    except:
        final_truth.append("none")
    # try:
    #     epoc_wound.append(response["Item"]["Wound"])
    # except:
    #     epoc_wound.append("none")

# data_tuples = zip(epoc_wound,epoc_subject_id)
# final = pd.DataFrame(data_tuples, columns=['wound','id'])
# final.to_csv("//Users/ziweishi/Documents/epoc.csv",encoding='utf-8')


# def download_raw(raw_list):
#
#
#
#     for i in raw_list:
#
#         table = dynamodb.Table(table_name)
#
#
#         try:
#             folder_path = os.makedirs("/Users/ziweishi/Documents/check")
#
#             path = os.path.join(folder_path, i)
#             # pathlib.Path(path).parent.mkdir(exist_ok=True, parents=True)
#             s3.meta.client.download_file(name, str(i), str(path))
#         except Exception as e:
#             print(os.path.join("/Users/ziweishi/Documents/reference", str(i)))
#             print(e.args)
#

print(final_truth)


right_truth = []
for i in right_list:
    response = table.get_item(
        Key={
            'ImgCollGUID': i
        }
    )
    try:
        # refrence.append(response["Item"]["Reference"])
        # bucket.append(response["Item"]["Bucket"])
        # check.append(response["Item"]["Suffix"])
        # epoc_subject_id.append(response["Item"]["SubjectID"])
        a = response["Item"]["FinalTruth"]
        print(a)
        final_truth.append(a[0])
    except:
        final_truth.append("none")

df = pd.DataFrame(right_truth,columns=["truth"])
df.to_csv("//Users/ziweishi/Desktop/right.csv",encoding='utf-8')


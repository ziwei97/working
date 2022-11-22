import boto3
import os
import pandas as pd

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'BURN_ImageCollection'
table = dynamodb.Table(table_name)


def get_attribute(table,guid,attr):

    response = table.get_item(
        Key={
            'ImgCollGUID': guid
        }
    )
    return response["Item"][attr]





def download_raw(table,raw_list,attrs):
    fold = os.path.join("/Users/ziweishi/Documents", "new_request_raw")
    os.makedirs(fold)
    for i in raw_list:
        name = get_attribute(table,i,"Bucket")
        folder = os.path.join(fold, i)
        os.makedirs(folder)
        for j in attrs:
            try:
                attr = get_attribute(table,i,j)
                # pathlib.Path(path).parent.mkdir(exist_ok=True, parents=True)
                path = os.path.join(folder, j)
                os.makedirs(path)
                for s in attr:
                    file_name = s.split('/')[-1]
                    file_path = os.path.join(path, file_name)
                    # s3.meta.client.download_file(name, attr[0], str(path))
                    s3.Bucket(name).download_file(str(s), str(file_path))
            except Exception as e:
                print(os.path.join("/Users/ziweishi/Documents", str(i)))
                print(e.args)



attrs = ["Raw"]
list = ["051b4d32-6484-48ea-8855-1dd74136ddc0","09f94f3f-604c-404a-a504-e85188f81456","3344d0f1-055d-4e9e-8469-8d8a40b30d30"]
#
# for i in list:
#     for j in attrs:
#         try:
#             get_attribute(table,i,j)
#         except:
#             print("n")


download_raw(table,list,attrs)






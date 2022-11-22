import pandas as pd
import boto3




#
# ab = pd.read_excel("/Users/ziweishi/Desktop/abdiel.xlsx")
# co = pd.read_excel("/Users/ziweishi/Desktop/corey.xlsx")
#
# ab_id = ab["ImgCollGUID"].to_list()
# co_id = co["ImgCollGUID"].to_list()
#
# # for i in ab_id:
# #     if i not in co_id:
# #         print(i)
# #
# # for i in co_id:
# #     if i not in ab_id:
# #         print(i)
#
#
# he = pd.read_excel("/Users/ziweishi/Desktop/ImageCollection_withExcluded.xlsx",sheet_name="Sheet4")
# he_id = he["ImgGUID"].to_list()
#
# # for i in he_id:
# #     if i not in co_id:
# #         print(i)
#
# for i in he_id:
#     if i not in ab_id:
#         print(i)


# already = pd.read_excel("/Users/ziweishi/Desktop/ImageCollection_withExcluded.xlsx",sheet_name="burn_study")
# al_id = already["ImgCollGUID"].to_list()
#
# final=[]
# for i in al_id:
#     if i not in he_id:
#         final.append(i)

# for i in co_id:
#     if i not in he_id:
#         print(i)


# subjectID = []
# wound = []
# status = []
# pr = []
# se = []
# fi = []



#
# for j in final:
#     df = he[he["ImgCollGUID"]==j]
#     sid = str(df["SubjectID"].iloc[0])
#     subjectID.append(sid)
#     wo = str(df["Wound"].iloc[0])
#     wound.append(wo)
#     sta = str(df["Status"].iloc[0])
#     status.append(sta)
#     p = str(df["PrimaryDoctorTruth"].iloc[0])
#     s = str(df["SecondaryDoctorTruth"].iloc[0])
#     f = str(df["FinalTruth"].iloc[0])
#     pr.append(p)
#     se.append(s)
#     fi.append(f)
#
#
# data = zip(final,subjectID,wound,status,pr,se,fi)
# truth = pd.DataFrame(data, columns=['ImgGUID','Subject','Wound','Status','Primary','Second','Final'])
# truth.to_csv("//Users/ziweishi/Documents/truth.csv",encoding='utf-8')




alex = pd.read_excel("/Users/ziweishi/Desktop/ImgCollection_without_Truth.xlsx",sheet_name="Sheet1")

al_id = alex["ImgCollGUID"].to_list()


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BURN_Master_ImageCollections')


sub = []
wound = []

for i in al_id:
    try:
        response = table.get_item(
            Key={
                'ImgCollGUID': i
            }
        )

        sub.append(response["Item"]["SubjectID"])
        wound.append(response["Item"]["Wound"])
    except:
        sub.append("none")
        wound.append("none")

p1=[]
p2=[]

for i in range(len(al_id)):

    table = dynamodb.Table('BURN_Master_Wounds')


    try:
        response = table.get_item(
            Key={
                "Subject": sub[i],
                "Wound": wound[i]
            }
        )
        p1.append(response["Item"]["PrimaryAssigned"])
        p2.append(response["Item"]["SecondaryAssigned"])
    except:
        p1.append("none")
        p2.append("none")


for i in p2:
    print(i)
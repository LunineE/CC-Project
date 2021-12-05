import boto3
import os

s3 = boto3.client('s3')
filename = input('업로드할 파일 위치 및 이름 : ')
bucketname = input('업로드할 버킷 이름 : ')
newname = input('업로드 될 파일 이름 : ')

upload = s3.upload_file(filename, bucketname, newname)
os.system('pause')

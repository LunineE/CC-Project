import boto3

def compare_faces(bucket, source, target, region='us-east-1'):
    rekognition = boto3.client('rekognition', region)
    response = rekognition.compare_faces(
        SimilarityThreshold=0, #예제 기본 수치 80
        SourceImage={
            'S3Object': {
                'Bucket': bucket,
                'Name': source,
            }
        },

        TargetImage={
            'S3Object': {
                'Bucket': bucket,
                'Name': target,
            }
        })

    for faceMatch in response['FaceMatches']:
        similarity = round(float(faceMatch['Similarity']), 2)
        if (similarity >= 95):
            print(str(similarity) + '%')
            print('동일 인물 입니다')
        elif (similarity >= 70):
            print(str(similarity) + '%')
            print('유사 하지만 동일 인물이 아닙니다')
        else:
            print(str(similarity) + '%')
            print('다른 인물 입니다')

    return len(response['FaceMatches'])


def main():
    bucket = 'comparefacesbucket'
    source_file = 'source.png'
    target_file = 'target.png'
    face_matches = compare_faces(bucket, source_file, target_file)
    print("Face matches: " + str(face_matches))


if __name__ == "__main__":
    main()
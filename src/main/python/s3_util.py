import boto3


def push_to_s3(countries_file, hashtags_file, lang_file):
    aws_access_key_id = ''
    aws_secret_access_key = ''
    bucket = 'TwitterAnalysis'
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.create_bucket(Bucket='TwitterAnalysis')
    s3.upload_file(countries_file, bucket, countries_file)
    s3.upload_file(hashtags_file, bucket, hashtags_file)
    s3.upload_file(lang_file, bucket, lang_file)
    # Set Access to public for all pictures
    object_acl = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key).\
        ObjectAcl(bucket, countries_file)
    object_acl.put(ACL='public-read')

    object_acl = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key).\
        ObjectAcl(bucket, hashtags_file)
    object_acl.put(ACL='public-read')

    object_acl = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key).\
        ObjectAcl(bucket, lang_file)
    object_acl.put(ACL='public-read')

    return ['https://s3.amazonaws.com/' + bucket + "/" + countries_file,
            'https://s3.amazonaws.com/' + bucket + "/" + hashtags_file,
            'https://s3.amazonaws.com/' + bucket + "/" + lang_file]
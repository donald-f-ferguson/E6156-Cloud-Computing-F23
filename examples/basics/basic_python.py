import boto3

session = boto3.session.Session(profile_name='default')


def list_buckets():
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def list_instances():
    ec2 = session.resource('ec2')
    for instance in ec2.instances.all():
        print(instance)


if __name__ == "__main__":
    # list_buckets()
    list_instances()




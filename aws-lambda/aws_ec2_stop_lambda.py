#this you can run on Python 2.7 version in AWS Lambda Function

import boto3
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
# create filter for instances in running state
    filters_running = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances_running = ec2.instances.filter(Filters=filters_running)
    # create filter for instances contains in DONT_DELETE tag
    filters_exclude = [
        {
            'Name': 'tag:Name',
            'Values':['*%s*' % 'DONT_DELETE']

        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances_exclude = ec2.instances.filter(Filters=filters_exclude)

    # instantiate empty set
    RunningInstances = set(instances_running)-set(instances_exclude)
    RunningInstances_list =[]
    for instance2_del in RunningInstances:
        RunningInstances_list.append(instance2_del.id)

    ec2ins = boto3.client('ec2')
    print '---------------------------------------------------------- '
    if RunningInstances_list:
        ec2ins.stop_instances(InstanceIds=RunningInstances_list)
        print 'stopped your instances: ' + str(RunningInstances_list)
    else:
        print 'No Running Instances available to stop'
    print '---------------------------------------------------------- '
    return True

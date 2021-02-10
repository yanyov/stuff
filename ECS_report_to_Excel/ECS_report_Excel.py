import boto3
import xlsxwriter
import pprint

client = boto3.client('ecs')
ecs_clusters = client.list_clusters().get('clusterArns')

ecs_services = {}

for cluster in ecs_clusters:
    ecs_services[cluster] = client.list_services(cluster = cluster).get('serviceArns')   

data = []
for cluster, services in ecs_services.items():
    cl=cluster.split('/')[1]
    for svc in services:
        desc_serv = client.describe_services(cluster=cl, services=[svc]).get('services')
        task_definition = desc_serv[0]['deployments'][0]['taskDefinition']
        task_definition_info = client.describe_task_definition(taskDefinition = task_definition).get('taskDefinition')
        data.append({ "cluster": cl,
            "service": svc,
            "desired_count": desc_serv[0]['desiredCount'],
            "load_balancer": desc_serv[0]['loadBalancers'],
            "task_definition": task_definition,
            "cpu": task_definition_info['cpu'],
            "memory": task_definition_info['memory'],
            "region": task_definition_info['containerDefinitions'][0]['logConfiguration']['options']['awslogs-region'],
            "log_group": task_definition_info['containerDefinitions'][0]['logConfiguration']['options']['awslogs-group']
        })

workbook = xlsxwriter.Workbook('ECS_data.xlsx')
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format({'bold': True, 'font_color': 'brown'})

worksheet.write(0, 0, 'Cluster', cell_format)
worksheet.write(0, 1, 'Service', cell_format)
worksheet.write(0, 2, 'DesiredCount', cell_format)
worksheet.write(0, 3, 'LoadBalancer Target Group', cell_format)
worksheet.write(0, 4, 'Task Definition', cell_format)
worksheet.write(0, 5, 'CPU', cell_format)
worksheet.write(0, 6, 'Memory', cell_format)
worksheet.write(0, 7, 'Region', cell_format)
worksheet.write(0, 8, 'AWS Cloudwatch Log Group', cell_format)

row_num = 1

for i in data:
    print(i)
    worksheet.write(row_num, 0, i['cluster'])
    worksheet.write(row_num, 1, i['service'])
    worksheet.write(row_num, 2, i['desired_count'])
    if i['load_balancer']:
        worksheet.write(row_num, 3, str(i['load_balancer']).split('/')[1])
    else:
        worksheet.write(row_num, 3, '')
    worksheet.write(row_num, 4, i['task_definition'])
    worksheet.write(row_num, 5, i['cpu'])
    worksheet.write(row_num, 6, i['memory'])
    worksheet.write(row_num, 7, i['region'])
    worksheet.write(row_num, 8, i['log_group'])
    
    row_num += 1

workbook.close()
import boto3
import xlsxwriter

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
        data.append({ "cluster": cl,
            "service": svc,
            "desired_count": desc_serv[0]['desiredCount'],
            "load_balancer": desc_serv[0]['loadBalancers']
        })

workbook = xlsxwriter.Workbook('ECS_data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Cluster')
worksheet.write(0, 1, 'Service')
worksheet.write(0, 2, 'DesiredCount')
worksheet.write(0, 3, 'LoadBalancer Target Group')

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
    row_num += 1

workbook.close()
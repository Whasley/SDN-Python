import httplib2
import json
import sys
import logging
import requests

baseUrl = 'http://192.168.0.55:8181/restconf/operational/opendaylight-inventory:'
containerName = 'default/'
ethTypeIp = 0x800
ipTypeTcp = 0x6
ipTypeUdp = 0x11


# Wrapper function for getall
def get_all_wrapper(typestring):
    url = baseUrl + typestring
    logging.debug('url %s', url)
    headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    #'content-type': "application/json",
    'cache-control': "no-cache",
    
    }
    resp, content = h.request(url, "GET",headers=headers)

    allContent = json.loads(content)
#   allrows = allContent[attribute]
    
    print ((allContent['nodes'])['node'][0])['id']
    print ((allContent['nodes'])['node'][0])['flow-node-inventory:ip-address']
    print ((allContent['nodes'])['node'][0])['flow-node-inventory:manufacturer']
    print ((allContent['nodes'])['node'][0])['flow-node-inventory:hardware']
    print ((allContent['nodes'])['node'][0])['flow-node-inventory:table']


# Get list of switches
def get_all_nodes():

    get_all_wrapper('nodes/')    



# ---------------------------- Listando todos os Fluxos ----------------------------------------#

def get_all_flows(typestring):
    url = baseUrl + typestring
    logging.debug('url %s', url)
    headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    #'content-type': "application/json",
    'cache-control': "no-cache",    
    }

    resp, content = h.request(url, "GET", headers=headers)

    allContent = json.loads(content)

    #print(type(allContent))
    print((allContent['flow-node-inventory:table'])[0])['id']    
    #print(allContent['flow-node-inventory:table'])['flow-hash-id-map'])
    

   #print ((allContent['nodes'])['node'][0])['flow-node-inventory:ip-address']
    #print ((allContent['nodes'])['node'][0])['flow-node-inventory:manufacturer']
    #print ((allContent['nodes'])['node'][0])['flow-node-inventory:hardware']


def print_all_flows():
    #get_all_flows('nodes/node/openflow:205314561770572/table/0/')
    get_all_flows('nodes/node/openflow:205314561770572/flow-node-inventory:table/0')

# ---------------------------- Inserindo Regras ----------------------------------------#

def put_flow(): 

    url = "http://192.168.0.55:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:205314561770572/table/0/flow/TesteJSON"

    #payload = "{\n        \"flow\": [\n        {\n            \"table_id\": \"0\",\n            \"id\": \"TesteDel\",\n            \"priority\": \"3000\",\n            \"match\": {\n                \"in-port\": \"6\"\n            },\n            \"instructions\": {\n                \"instruction\": [\n                    {\n                        \"order\": 0,\n                        \"apply-actions\": {\n                            \"action\": [\n                                {\n                                    \"order\": 0,\n                                    \"output-action\": {\n                                        \"output-node-connector\": \"7\",\n                                        \"max-length\": \"65535\"\n                                    }\n                                }\n                            ]\n                        }\n                    }\n                ]\n            }\n        }\n    ]\n}"

    headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'content-type': "application/json",
    'cache-control': "no-cache",
    
    }

    payload =''' {
    "flow": [
        {
            "table_id": "0",
            "id": "TesteJSON",
            "priority": "1994",
            "match": {
                "in-port": "1"
            },
            "instructions": {
                "instruction": [
                    {
                        "order": 0,
                        "apply-actions": {
                            "action": [
                                {
                                    "order": 0,
                                    "output-action": {
                                        "output-node-connector": "2",
                                        "max-length": "65535"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
} '''

    response = requests.request("PUT", url, data=payload, headers=headers)

    #print(response.text)

    print('Regra Instalada Com Sucesso')
    

    

# ------------------------------------------------------------------------------------------#
    


#------------ TESTE

def testeGet():
    url = "http://192.168.0.55:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:205314561770572/flow-node-inventory:table/0"

    headers = {
    'authorization': "Basic YWRtaW46YWRtaW4=",
    'cache-control': "no-cache",
    'postman-token': "adacc37d-3597-4f3e-d70d-1b2c6c7d7296"
    }

    response = requests.request("GET", url, headers=headers)

    #resposta = json.loads(response)

    #print(type(response))
    resposta = response.json()
    print (type(resposta))

    print ('\n Regra 1 \n')
    
    print ('id: '+(resposta['flow-node-inventory:table'])[0]['flow'][0]['id'])
    print ("table_id: ",(resposta['flow-node-inventory:table'])[0]['flow'][0]['table_id'])
    print ('priority: ',(resposta['flow-node-inventory:table'])[0]['flow'][0]['priority'])
    print ('match: ',(resposta['flow-node-inventory:table'])[0]['flow'][0]['match'])#['in-port'])
    print ('action: ',(resposta['flow-node-inventory:table'])[0]['flow'][0]['instructions']['instruction'][0]['apply-actions']['action'][0]['output-action']['output-node-connector'])

    print ('\n Regra 2 \n')


    print ('id: '+(resposta['flow-node-inventory:table'])[0]['flow'][1]['id'])
    print ("table_id: ",(resposta['flow-node-inventory:table'])[0]['flow'][1]['table_id'])
    print ('priority: ',(resposta['flow-node-inventory:table'])[0]['flow'][1]['priority'])
    print ('match: ',(resposta['flow-node-inventory:table'])[0]['flow'][1]['match'])#['in-port'])
    print ('action: ',(resposta['flow-node-inventory:table'])[0]['flow'][1]['instructions']['instruction'][0]['apply-actions']['action'])#['output-node-connector'])

    print ('\n Regra 3 \n')


    print ('id: '+(resposta['flow-node-inventory:table'])[0]['flow'][2]['id'])
    print ("table_id: ",(resposta['flow-node-inventory:table'])[0]['flow'][2]['table_id'])
    print ('priority: ',(resposta['flow-node-inventory:table'])[0]['flow'][2]['priority'])
    print ('match: ',(resposta['flow-node-inventory:table'])[0]['flow'][2]['match'])#['in-port'])
    print ('action: ',(resposta['flow-node-inventory:table'])[0]['flow'][2]['instructions']['instruction'][0]['apply-actions']['action'])#['output-node-connector'])

    print ('\n Regra 4 \n')


    print ('id: '+(resposta['flow-node-inventory:table'])[0]['flow'][3]['id'])
    print ("table_id: ",(resposta['flow-node-inventory:table'])[0]['flow'][3]['table_id'])
    print ('priority: ',(resposta['flow-node-inventory:table'])[0]['flow'][3]['priority'])
    print ('match: ',(resposta['flow-node-inventory:table'])[0]['flow'][3]['match'])#['in-port'])
    print ('action: ',(resposta['flow-node-inventory:table'])[0]['flow'][3]['instructions']['instruction'][0]['apply-actions']['action'])#['output-node-connector'])
    

#------------ TESTE GET --------------


#----------------------------------------- Teste Delete -----------------------------------------------#


def Delete(regra):

    url = "http://192.168.0.55:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:205314561770572/table/0/flow/"+regra

    headers = {
        'authorization': "Basic YWRtaW46YWRtaW4=",
        'cache-control': "no-cache",    
    }

    response = requests.request("DELETE", url, headers=headers)

    print '\n Regra: ' + regra +' Excluida com Sucesso'



#----------------------------------------- Teste Delete -----------------------------------------------#
    



# Mais um Teste com JSON---------



def testeJson():
    teste =''' {
    "flow": [
        {
            "table_id": "0",
            "id": "Teste",
            "priority": "1000",
            "match": {
                "in-port": "4"
            },
            "instructions": {
                "instruction": [
                    {
                        "order": 0,
                        "apply-actions": {
                            "action": [
                                {
                                    "order": 0,
                                    "output-action": {
                                        "output-node-connector": "2",
                                        "max-length": "65535"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
} '''


    print (type(teste))


    content = json.loads(teste)

    print (type(content))



#--------------------------------



  
# START OF MAIN PROGRAM
# Setup logging
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')
    


 ################################################### MAIN ############################################

if __name__ == "__main__":
    
    def print_all_nodes():
        get_all_nodes()
 

    def Delete_Flow():
        option = raw_input('\nDigite o nome da Regra: ')
        Delete(option)       


    print '-----REST API LIBRARY MENU-----'
    print '1. Listar Todos os Switches'
    print '2. Inserir Fluxo Teste'
    print '3. Listar Todas as Regras'
    print '4. TEST GET FLOWS'
    print '5. Excluir uma Regra'
    print '6. Teste JSON'
    
    option = raw_input('Enter option needed:')

    if (option == '1'):
        print_all_nodes()
    elif (option == '2'):
        put_flow()
    elif (option == '3'):
        print_all_flows()
    elif (option == '4'):
        testeGet()
    elif (option == '5'):
        Delete_Flow()
    elif (option == '6'):
        testeJson()
   
   
    else:
        print 'Invalid option'

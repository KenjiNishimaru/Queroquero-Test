import json

with open("log.txt", "r") as file:
    list = {}
    for line in file:
        line = line.replace("'",'"')
        aux = json.loads(line)
        if aux["path"] not in list.keys():
            list[aux["path"]]={"path":aux["path"],"errorCount":0,"successCount":0}
        if int(aux["statusCode"]) >= 400:
            list[aux["path"]]["errorCount"]+=1
        else:
            list[aux["path"]]["successCount"]+=1
    with open("./sre-intern-test/output.json","w") as output:
        final_list = []    
        for item in list:
            final_list.append(list[item])
        json.dump(final_list,output)



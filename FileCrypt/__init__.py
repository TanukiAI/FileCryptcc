import requests, json

def userApiKey(apikey):
	"""
	Returns information about an apikey
	apikey: Your ApiKey from FileCrypt
	
	Attention: this API is limited to 10 requests for an timeframe of 1 hour.
	"""
	data={"api_key":apikey,"sub":"apikey","fn":"user"}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def userEarnings(apikey,year=None,month=None,day=None):
	"""
	Returns statistics from user income and the total available balance on the account
	apikey: Your ApiKey from FileCrypt
	year(optional): year (YYYY) (2019)
	month(optional): month (MM) (06)
	day(optional): month (DD) (13)
	"""
	data={"api_key":apikey,"sub":"earnings","fn":"user"}
	if year != None:
		data["year"] = str(year)
	if month != None:
		data["month"] = str(month)
	if day != None:
		data["day"] = str(day)
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)



def containerCreate(apikey,name,mirrors,password=None,captcha=None,allow_cnl=None,allow_dlc=None,allow_links=None,groupid=None):
	"""
	This function allows you to create an filecrypt.cc protected folder.
	apikey: Your ApiKey from FileCrypt
	name: name of your folder
	mirrors: mirrors in a tripple listed list  
		example: [[[mirror_0_link1,mirror_0_link2],[mirror_0_backup_link1,mirror_0_backup_link2]],[[mirror_1_link1,mirror_1_link2],[mirror_1_backup_link1,mirror_1_backup_link2]]]
		prettyprinted example:
        [
          [
            [
              "mirror_0_link1",
              "mirror_0_link2"
            ],
            [
              "mirror_0_backup_link1",
              "mirror_0_backup_link2"
            ]
          ],
          [
            [
              "mirror_1_link1",
              "mirror_1_link2"
            ],
            [
              "mirror_1_backup_link1",
              "mirror_1_backup_link2"
            ]
          ]
        ]
		all strings in the first and second list (where the other lists should be) will be skipped
	password(optional): password of your folder
	captcha(optional): enable captcha? Allowed Values: 0,1
	allow_cnl(optional): enable cnl? Allowed Values: 0,1
	allow_dlc(optional): enable dlc? Allowed Values: 0,1
	allow_links(optional): enable links? Allowed Values: 0,1
	groupid: group ID of your target group
	"""
	data={"api_key":apikey,"sub":"createV2","fn":"containerV2","name":name}
	
	for i in range(len(mirrors)):
		if isinstance(mirrors[i],str):
			continue
		for j in range(len(mirrors[i])):
			if isinstance(mirrors[i][j],str):
				continue
			for k in range(len(mirrors[i][j])):
				data["mirror_"+str(i+1)+"["+str(j)+"]["+str(k)+"]"] = mirrors[i][j][k]
			
	if password != None:
		data["folderpass"] = password
	if captcha != None:
		data["captcha"] = str(captcha)
	if allow_cnl != None:
		data["allow_cnl"] = str(allow_cnl)
	if allow_dlc != None:
		data["allow_dlc"] = str(allow_dlc)
	if allow_links != None:
		data["allow_links"] = str(allow_links)
	if groupid != None:
		data["group"] = str(groupid)
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def containerEdit(apikey,mirrors,container_id,name=None,password=None,captcha=None,allow_cnl=None,allow_dlc=None,allow_links=None,groupid=None):
	"""
	This function allows you to edit an filecrypt.cc protected folder.
	Once you submit mirror_1 all links are permanently removed from this folder and will be replaced with the once submitted.
	if you would like to replace just a mirror please use our info api to get informations about links inside this folder to build your request.
	For informations on statusimages please visit https://filecrypt.cc/docs/index.htm#api-General-Statusimages
	
	apikey: Your ApiKey from FileCrypt
	name(optional): name of your folder
	container_id: the container_id as string
	mirrors: same as containerCreate()
		
	password(optional): password of your folder
	captcha(optional): enable captcha? Allowed Values: 0,1
	allow_cnl(optional): enable cnl? Allowed Values: 0,1
	allow_dlc(optional): enable dlc? Allowed Values: 0,1
	allow_links(optional): enable links? Allowed Values: 0,1
	groupid: group ID of your target group
	"""
	data={"api_key":apikey,"sub":"editV2","fn":"containerV2","name":name,"container_id":container_id}
	
	for i in range(len(mirrors)):
		if isinstance(mirrors[i],str):
			continue
		for j in range(len(mirrors[i])):
			if isinstance(mirrors[i][j],str):
				continue
			for k in range(len(mirrors[i][j])):
				data["mirror_"+str(i+1)+"["+str(j)+"]["+str(k)+"]"] = mirrors[i][j][k]
			
	if name != None:
		data["name"] = name
	if password != None:
		data["folderpass"] = password
	if captcha != None:
		data["captcha"] = str(captcha)
	if allow_cnl != None:
		data["allow_cnl"] = str(allow_cnl)
	if allow_dlc != None:
		data["allow_dlc"] = str(allow_dlc)
	if allow_links != None:
		data["allow_links"] = str(allow_links)
	if groupid != None:
		data["group"] = str(groupid)
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def containerInfo(apikey,container_id):
	"""
	Returns an sorted object containing every link in your folder.
	apikey: Your ApiKey from FileCrypt
	container_id: the container_id as string
	"""
	data={"api_key":apikey,"sub":"info","fn":"containerV2","container_id":container_id}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def containerList(apikey,state=None,fav=None):
	"""
	Returns all Containers from your FileCrypt Account
	apikey: Your ApiKey from FileCrypt
	state(optional): filter by state of your folders. Allowed values: "unchecked", "ok", "uncheckable", "error", "offline", "partial"
	fav(optional): filter on favorite folders 1 = favorite, 0 = regular folder
	"""
	data={"api_key":apikey,"sub":"listV2","fn":"containerV2"}
	if state != None:
		data["state"] = state
	if fav != None:
		data["fav"] = str(fav)
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def containerMyFolder(apikey,state=None,groupid=None):
	"""
	returns a short list of your own folders filtered by state (if passed as parameter).
	Please note every Object child of the container-Node starts with a trailing _.
	apikey: Your ApiKey from FileCrypt
	state(optional): filter by state of your folders. Allowed values: "unchecked", "ok", "uncheckable", "error", "offline", "partial"
	groupid(optional): filter for specified group
	"""
	data={"api_key":apikey,"fn":"containerV2","sub":"myfolder"}
	if state != None:
		data["state"] = state
	if groupid != None:
		data["group"] = str(groupid)
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)


def containerRemove(apikey,container_id):
	"""
	*Move* folder from public to trashbin the folder will not be public available.
	apikey: Your ApiKey from FileCrypt
	container_id: the container_id as string
	"""
	data={"api_key":apikey,"fn":"containerV2","sub":"remove","container_id":container_id}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def containerStatus(apikey,container_id):
	"""
	Get status of an filecrypt.cc folder: https://filecrypt.cc/docs/index.htm#api-General-Statusimages
	apikey: Your ApiKey from FileCrypt
	container_id: the container_id as string
	"""
	data={"api_key":apikey,"fn":"containerV2","sub":"statusV2","container_id":container_id}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)


def groupAdd(apikey,name):
	"""
	Creates a new Group with the chosen Name
	apikey: Your ApiKey from FileCrypt
	name: The name of your new group
	"""
	data={"api_key":apikey,"fn":"group","sub":"add","name":name,"parent":"0"}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def groupList(apikey):
	"""
	Returns all Groups existing in your FileCrypt Account
	apikey: Your ApiKey from FileCrypt
	"""
	data={"api_key":apikey,"fn":"group","sub":"list"}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def groupMove(apikey,groupid,container_id):
	"""
	Move your filecrypt.cc containers to a specified group
	apikey: Your ApiKey from FileCrypt
	groupid: the group ID(!) you want the containers to be in
	container_id: you can input a single Container via String or input a whole list with all containers.
	"""
	data={"api_key":apikey,"fn":"group","sub":"move","group":str(groupid)}
	if isinstance(container_id,str):
		data["container_id[0]"] = container_id
	elif isinstance(container_id,list):
		for i in range(len(container_id)):
			data["container_id["+str(i)+"]"]=container_id[i]
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)

def groupRemove(apikey,groupid):
	"""
	Removes the group and moves all containers to group 0 (ungrouped)
	apikey: Your ApiKey from FileCrypt
	groupid: the group ID(!) you want to delete
	"""
	data={"api_key":apikey,"fn":"group","sub":"remove","id":str(groupid)}
	return json.loads(requests.post("https://filecrypt.cc/api.php",data=data).text)
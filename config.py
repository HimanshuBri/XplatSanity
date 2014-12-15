config = {

"PUBLISHSETTINGS_FILE" : "CollaberaInteropTest-12-8-2014-credentials.publishsettings",

#************** ACCOUNT VARIABLES *****************

"LOG_FILE" : "LOG_FILE.txt",
"LOG_FILERR" : "LOG_FILERR.txt",
"FILE_PATH" : "FILE_PATH.json",
"CERT_FILE" : "CERT_FILE.pem",
"CUSTOM_DATA_FILE" : "CustomDataFile",

#************** ACCOUNT VARIABLES *****************

"SUBSCRIPTION_ID" : "bfb5e0bf-124b-4d0c-9352-7c0a9f4d9948",
"CONFIG_KEY" : "Key",
"CONFIG_VALUE" : "Value",

#************** StaticIP VARIABLES *****************
"STATICIP_VM_NAME" : "XplatVMStatic",
"DOCKER_STATIC_VM_NAME" : "XplatDockVMStat",
"STATIC_IP_TO_CREATE" : "10.0.0.7",
"STATIC_IP_TO_SET" : "10.0.0.8",
#************** VM VARIABLES *****************
"VM_NAME" : "XplatTestVM1",
#"VM_NAME" : "OffshoreTest",
"VM_WIN_NAME" : "TestXplatWin",
"VM_VNET_NAME" : "XplatTestVNet",
"VM_VNET_LABEL" : "Xplat_vnet_img_vm",
"VM_SIZE_NAME" : "XplatTestVMSize",
"VM_COMM_NAME" : "XplatTestComm",
"VM_SSH_NAME" : "XplatTestSsh",
"VM_DOCKER_NAME" : "XplatDockerVM",
"VM_RIP_NAME" : "XplatRIPVM",
"VM_DOCKER_PORT" : "4113",
"VM_CUSTOMDATA_NAME" : "XplatCustomdata",
"LOGINUSER" : "LOGINUSER",
"LOGINPASSWORD" : "LOGINPASSWORD",

"IMAGE_NAME" :"TEstImage",
"WIN_IMAGE_NAME" :"VMImage1", #diskname is obtained from vm image list and choose the one with windows
"VM_VNET_IMAGE_NAME" :"XplatTestImage",
"VM_COMM_IMAGE_NAME" :"Some community image name", #browse http://vmdepot.msopentech.com/ select a vm anc click on deployment button
"VM_DOCKER_IMG_NAME" : "TestLinuxImage",

"USER_NAME" :"XplatTestUser",
"PASSWORD" :"Pa$$word@123" ,
"LOCATION":'"West US"',

#************** VM IMAGE VARIABLES *****************
"AFFINITY_GRP_NAME":"XplatTestAffinGrp2",
"AFFINITY_GRP_LABEL":"XplatTestGrp2",
"AFFINITY_GRP_DESC":'"Test Affinity Group2"',

#************** VM Extension VARIABLES *****************
"EXTN_PUB_NAME":"Microsoft.Compute",
"EXTN_NAME":"CustomScriptExtension",
"EXTN_VERSION":"1.1 ",
"EXTN_FILE":"foo.json",
#************** VM NETWORK VARIABLES *****************
"NETWORK_NAME":"newnet",

#************** VM IMAGE VARIABLES *****************
"VM_IMAGE_NAME" : "XplatTestImage",
"VM_IMAGE_LABEL" : "XplatTestImageLabel",
"VM_IMAGE_DESC" : '"Test Offshore Image"',
"VM_DISK_SOURCE_PATH" :"https://acsforsdk2.blob.core.windows.net/disks/ToDelete.vhd", #mediauri obtained from vm disk show diskname(diskname is obtained from vm disk list and choose the one with linux as os)
"IMAGE_BLOB_URL" : "http://acsforsdk2.blob.core.windows.net/vm-images/ToDelete",		#http://StoragecontainerUrl/vm-images/OffshoreXplatTestImage002"
"TARGET_IMG_NAME" : "XplatTestTargetImg",

#************** VM DISK IMAGE VARIABLES *****************
"VM_DISK_IMAGE_NAME" :"ToDelete",
"VM_DISK_NEW_IMAGE_NAME" :"XplatTestDiskNewImage",
"VM_DISK_LABEL" : "XplatTestDisklbl",
"VM_DISK_NEW_LABEL" : "XplatTestDiskNewlbl",
"VM_DISK_DESC" : '"Test Offshore Disk"',
"DISK_IMAGE_BLOB_URL": "https://acsforsdk2.blob.core.windows.net/disks/TestVMImage-datadisk-0-2014-11-17.vhd", 			#http://StoragecontainerUrl/disks/OffshoreXplatTestDisk"
"VM_DISK_ATTACH_BLOB_URL": "VM_DISK_ATTACH_BLOB_URL", 	#http://StoragecontainerUrl/disks/disknewupload.vhd"

#************** PIP COMMANDS ****************************
"VM_WIN_PIP" : "VMeToDelete",
"PUBLICIPNAME" : "TestIP2",
"PUBLICIPSET" : "VMPUBLICIPSET",


#************** ACL COMMANDS ****************************
"VM_WIN_ACL" : "VMeToDelete",
"ENDPOINT" : "tcp-21-23",
"REMOTESUBNET" : "23.99.18.228/31",
"ORDER" : "3",
"ACTION" : "permit",

#************** VM DISK UPLOAD VARIABLES *****************
"DISK_UPLOAD_BLOB_URL": "DISK_UPLOAD_BLOB_URL",			#http://StoragecontainerUrl/disks/OffshoreTestDiskImage002.vhd",
"DISK_UPLOAD_SOURCE_PATH" : "DISK_UPLOAD_SOURCE_PATH", 	#http://StoragecontainerUrl/vm-images/OffshoreTestImage002.vhd",
"STORAGE_ACCOUNT_KEY": "STORAGE_ACCOUNT_KEY", 			#YW55IGNhcm5hbCBwbGVhc3VyZQ==

#************** MULTIPLE ENDPOINT VALUES **************************
"ONLYPP_PUBLICPORT":"3333",

"PPANDLP_PUBLICPORT":"4444",
"PPANDLP_LOCALPORT":"4454",

"PP_LPANDLBSET_PUBLICPORT":"5555",
"PP_LPANDLBSET_LOCALPORT":"5565",
"PP_LPANDLBSET_PROTOCOL":"tcp",
"PP_LPANDLBSET_ENABLEDIRECTSERVERRETURN":"false",
"PP_LPANDLBSET_LOADBALANCERSETNAME":"LbSet1",

"PP_LP_LBSETANDPROB_PUBLICPORT":"6666",
"PP_LP_LBSETANDPROB_LOCALPORT":"6676",
"PP_LP_LBSETANDPROB_PROTOCOL":"tcp",
"PP_LP_LBSETANDPROB_ENABLEDIRECTSERVERRETURN":"false",
"PP_LP_LBSETANDPROB_LOADBALANCERSETNAME":"LbSet2",
"PP_LP_LBSETANDPROB_PROBPROTOCOL":"http",
"PP_LP_LBSETANDPROB_PROBPORT":"7777",
"PP_LP_LBSETANDPROB_PROBPATH":"/prob/listner1",

#RESERVED-IP
"RIPNAME" : "XplatTestRIP5",

#LOADBALANCER
"SUBNET" : "Subnet-1" ,
"INTERNAL_LB_NAME" : "internalLBName" ,

#************** FLAG VALUES **************************

"GLOBAL_FLAG" : "1",
"AD_Login" : "0",

# NPM FLAGS

"NPM_CLEAR_FLAG" : "0" ,
"NPM_INSTALL_FLAG" : "0" ,

# ACCOUNT FLAGS 
"AZURE_HELP_FLAG" : "0" ,
"ACCOUNT_DWNLD_FLAG" : "0" ,
"ACCOUNT_IMPRT_FLAG" : "0" ,
"ACCOUNT_LIST_FLAG" : "0" ,
"ACCOUNT_SET_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_CREATE_FLAG" : "0" ,
"ACCOUNT_AFF_GRP_SHOW_FLAG" : "0" ,
"ACCOUNT_STORAGE_LIST_FLAG" : "0" ,
"ACCOUNT_CONFIG_LIST_FLAG" : "0" ,
"ACCOUNT_CONFIG_SET_FLAG" : "0" ,
"AZURE_SERV_LIST_FLAG" : "0" ,
"AZURE_LOC_LIST_FLAG" : "0" ,
"AZURE_SERVICE_DEL_FLAG" : "0" ,
"ACCOUNT_CLEAR_FLAG" : "0" ,
"AZURE_LOGIN_FLAG" : "0",

#STATICIP FLAGS
"VM_STATICIP_CREATE_FLAG":"0",
# VM FLAGS

"VM_CREATE_FLAG" : "0" ,
"VM_VNET_CREATE_FLAG" : "0" ,
"VM_SIZE_CREATE_FLAG" : "0" ,
"VM_CUSTOMDATA_CREATE_FLAG" : "0" ,
"VM_COMM_IMG_CREATE_FLAG" : "0" ,
"VM_SSH_FLAG" : "0" ,
"VM_EXPORT_FLAG" : "0" ,
"VM_CAPTURE_FLAG" : "0" ,
"VM_CREATE_FROM_FLAG" : "0" ,
"VM_LIST_FLAG" : "0" ,
"VM__SHOW_FLAG" : "0" ,
"VM_SHUTDWN_FLAG" : "0" ,
"VM_START_FLAG" : "0" ,
"VM_RESTART_FLAG" : "0" ,
"VM_ENDPNT_CREATE_FLAG" : "0" ,
"VM_ENDPNT_CREATE_MUL_FLAG" : "0" ,
"VM_ENDPNT_SHOW_FLAG" : "0" ,
"VM_ENDPNT_LIST_FLAG" : "0" ,
"VM_ENDPNT_UPD_FLAG" : "0" ,
"VM_ENDPNT_DEL_FLAG" : "0" ,
"VM_DEL_FLAG" : "0" ,
"VM_AFFINITY_DEL_FLAG" : "0" ,
"VM_VNET_DEL_FLAG" : "0" ,
"VM_SIZE_DEL_FLAG" : "0" ,
"VM_CUSTOMDATA_DEL_FLAG" : "0" ,
"VM_COMM_DEL_FLAG" : "0" ,
"VM_SSH_DEL_FLAG" : "0" ,
"VM_RIP_CREATE_FLAG" : "0" ,
"VM_RIP_DEL_FLAG" : "0" ,

#PIP FLAGS
"PIP_VM_CREATE_FLAG" : "0",
"PIP_VM_LIST_FLAG" : "0",
"PIP_VM_REMOVE_FLAG" : "0",
"PIP_VM_SET_FLAG" : "0",
"PIP_VM_DELETE_FLAG" : "0",

#ACL FLAGS
"ACL_VM_CREATE_FLAG" : "0",
"ACL_RULE_CREATE_FLAG" : "0",
"ACL_RULE_LIST_FLAG" : "0",
"ACL_RULE_DELETE_FLAG" : "0",

# IMAGE FLAGS

"IMAGE_CREATE_FLAG" : "0" ,
"IMAGE_LIST_FLAG" : "0" ,
"IMAGE_SHOW_FLAG" : "0" ,
"IMAGE_DEL_FLAG" : "0" ,

# DISK FLAGS

"DISK_LIST_FLAG" : "0" ,
"DISK_LIST_VM_NAME_FLAG" : "0",
"DISK_CREATE_FLAG" : "0" ,
"DISK_ATTCH_FLAG" : "0" ,
"DISK_ATTCH_NEW_FLAG" : "0" ,
"DISK_DETACH_FLAG" : "0" ,
"DISK_SHOW_FLAG" : "0" ,
"DISK_UPLOAD_FLAG" : "0" ,
"NETWORK_CREATE_FLAG" : "0" ,
"NETWORK_DELETE_FLAG" : "0" ,
"DISK_DEL_FLAG" : "0" ,

#DOCKER FLAGS
"VM_DOCKER_CREATE_FLAG" : "0" ,
"VM_DOCKER_DELETE_FLAG" : "0",

#EXTENSION_FLAGS
"VM_EXTENSION_LIST_FLAG" : "0" ,
"VM_EXTENSION_GET_FLAG" : "0" ,
"VM_EXTENSION_SET_FLAG" : "0" ,

#RESERVED-IP
"RESERVED_IP_SHOW_FLAG" : "0" ,
"RESERVED_IP_CREATE_FLAG" : "0" ,
"RESERVED_IP_LIST_FLAG" : "0" ,
"RESERVED_IP_DELETE_FLAG" : "0" ,

#LOADBALANCER
"LOADBALANCER_CREATE_FLAG" : "0" ,
"LOADBALANCER_ADD_FLAG" : "0" ,
"LOADBALANCER_LIST_FLAG" : "0" ,
"LOADBALANCER_DELETE_FLAG" : "0" ,
"VM_LOADBALANCER_DEL_FLAG" : "0"

}

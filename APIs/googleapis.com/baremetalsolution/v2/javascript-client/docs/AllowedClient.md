# BareMetalSolutionApi.AllowedClient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowDev** | **Boolean** | Allow dev flag. Which controls whether to allow creation of devices. | [optional] 
**allowSuid** | **Boolean** | Allow the setuid flag. | [optional] 
**allowedClientsCidr** | **String** | The subnet of IP addresses permitted to access the share. | [optional] 
**mountPermissions** | **String** | Mount permissions. | [optional] 
**network** | **String** | The network the access point sits on. | [optional] 
**nfsPath** | **String** | Output only. The path to access NFS, in format shareIP:/InstanceID InstanceID is the generated ID instead of customer provided name. example like \&quot;10.0.0.0:/g123456789-nfs001\&quot; | [optional] [readonly] 
**noRootSquash** | **Boolean** | Disable root squashing, which is a feature of NFS. Root squash is a special mapping of the remote superuser (root) identity when using identity authentication. | [optional] 
**shareIp** | **String** | Output only. The IP address of the share on this network. Assigned automatically during provisioning based on the network&#39;s services_cidr. | [optional] [readonly] 



## Enum: MountPermissionsEnum


* `MOUNT_PERMISSIONS_UNSPECIFIED` (value: `"MOUNT_PERMISSIONS_UNSPECIFIED"`)

* `READ` (value: `"READ"`)

* `READ_WRITE` (value: `"READ_WRITE"`)





# BareMetalSolutionApi.NfsExport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowDev** | **Boolean** | Allow dev flag in NfsShare AllowedClientsRequest. | [optional] 
**allowSuid** | **Boolean** | Allow the setuid flag. | [optional] 
**cidr** | **String** | A CIDR range. | [optional] 
**machineId** | **String** | Either a single machine, identified by an ID, or a comma-separated list of machine IDs. | [optional] 
**networkId** | **String** | Network to use to publish the export. | [optional] 
**noRootSquash** | **Boolean** | Disable root squashing, which is a feature of NFS. Root squash is a special mapping of the remote superuser (root) identity when using identity authentication. | [optional] 
**permissions** | **String** | Export permissions. | [optional] 



## Enum: PermissionsEnum


* `PERMISSIONS_UNSPECIFIED` (value: `"PERMISSIONS_UNSPECIFIED"`)

* `READ_ONLY` (value: `"READ_ONLY"`)

* `READ_WRITE` (value: `"READ_WRITE"`)





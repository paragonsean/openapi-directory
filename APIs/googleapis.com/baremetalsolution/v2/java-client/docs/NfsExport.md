

# NfsExport

A NFS export entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowDev** | **Boolean** | Allow dev flag in NfsShare AllowedClientsRequest. |  [optional] |
|**allowSuid** | **Boolean** | Allow the setuid flag. |  [optional] |
|**cidr** | **String** | A CIDR range. |  [optional] |
|**machineId** | **String** | Either a single machine, identified by an ID, or a comma-separated list of machine IDs. |  [optional] |
|**networkId** | **String** | Network to use to publish the export. |  [optional] |
|**noRootSquash** | **Boolean** | Disable root squashing, which is a feature of NFS. Root squash is a special mapping of the remote superuser (root) identity when using identity authentication. |  [optional] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | Export permissions. |  [optional] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| PERMISSIONS_UNSPECIFIED | &quot;PERMISSIONS_UNSPECIFIED&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |




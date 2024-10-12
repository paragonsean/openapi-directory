

# NfsExport

A NFS export entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowDev** | **Boolean** | Allow dev. |  [optional] |
|**allowSuid** | **Boolean** | Allow the setuid flag. |  [optional] |
|**cidr** | **String** | A CIDR range. |  [optional] |
|**machineId** | **String** | Either a single machine, identified by an ID, or a comma-separated list of machine IDs. |  [optional] |
|**networkId** | **String** | Network to use to publish the export. |  [optional] |
|**noRootSquash** | **Boolean** | Disable root squashing. |  [optional] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | Export permissions. |  [optional] |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| PERMISSIONS_UNSPECIFIED | &quot;PERMISSIONS_UNSPECIFIED&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |




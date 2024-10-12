# DataBoxEdgeManagementClient.ShareProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessProtocol** | **String** | Access protocol to be used by the share. | 
**azureContainerInfo** | [**AzureContainerInfo**](AzureContainerInfo.md) |  | [optional] 
**clientAccessRights** | [**[ClientAccessRight]**](ClientAccessRight.md) | List of IP addresses and corresponding access rights on the share(required for NFS protocol). | [optional] 
**dataPolicy** | **String** | Data policy of the share. | [optional] 
**description** | **String** | Description for the share. | [optional] 
**monitoringStatus** | **String** | Current monitoring status of the share. | 
**refreshDetails** | [**RefreshDetails**](RefreshDetails.md) |  | [optional] 
**shareMappings** | [**[MountPointMap]**](MountPointMap.md) | Share mount point to the role. | [optional] [readonly] 
**shareStatus** | **String** | Current status of the share. | 
**userAccessRights** | [**[UserAccessRight]**](UserAccessRight.md) | Mapping of users and corresponding access rights on the share (required for SMB protocol). | [optional] 



## Enum: AccessProtocolEnum


* `SMB` (value: `"SMB"`)

* `NFS` (value: `"NFS"`)





## Enum: DataPolicyEnum


* `Cloud` (value: `"Cloud"`)

* `Local` (value: `"Local"`)





## Enum: MonitoringStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ShareStatusEnum


* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)





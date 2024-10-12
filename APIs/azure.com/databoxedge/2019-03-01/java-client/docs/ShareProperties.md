

# ShareProperties

The share properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessProtocol** | [**AccessProtocolEnum**](#AccessProtocolEnum) | Access protocol to be used by the share. |  |
|**azureContainerInfo** | [**AzureContainerInfo**](AzureContainerInfo.md) |  |  [optional] |
|**clientAccessRights** | [**List&lt;ClientAccessRight&gt;**](ClientAccessRight.md) | List of IP addresses and corresponding access rights on the share(required for NFS protocol). |  [optional] |
|**dataPolicy** | [**DataPolicyEnum**](#DataPolicyEnum) | Data policy of the share. |  [optional] |
|**description** | **String** | Description for the share. |  [optional] |
|**monitoringStatus** | [**MonitoringStatusEnum**](#MonitoringStatusEnum) | Current monitoring status of the share. |  |
|**refreshDetails** | [**RefreshDetails**](RefreshDetails.md) |  |  [optional] |
|**shareMappings** | [**List&lt;MountPointMap&gt;**](MountPointMap.md) | Share mount point to the role. |  [optional] [readonly] |
|**shareStatus** | [**ShareStatusEnum**](#ShareStatusEnum) | Current status of the share. |  |
|**userAccessRights** | [**List&lt;UserAccessRight&gt;**](UserAccessRight.md) | Mapping of users and corresponding access rights on the share (required for SMB protocol). |  [optional] |



## Enum: AccessProtocolEnum

| Name | Value |
|---- | -----|
| SMB | &quot;SMB&quot; |
| NFS | &quot;NFS&quot; |



## Enum: DataPolicyEnum

| Name | Value |
|---- | -----|
| CLOUD | &quot;Cloud&quot; |
| LOCAL | &quot;Local&quot; |



## Enum: MonitoringStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ShareStatusEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |




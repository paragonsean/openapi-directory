

# FileShareProperties

The File Share.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminUser** | **String** | The user/group who will have full permission in this share. Active directory email address. Example: xyz@contoso.com or Contoso\\xyz. |  |
|**dataPolicy** | [**DataPolicyEnum**](#DataPolicyEnum) | The data policy |  |
|**description** | **String** | Description for file share |  [optional] |
|**localUsedCapacityInBytes** | **Long** | The local used capacity in Bytes. |  [optional] [readonly] |
|**monitoringStatus** | [**MonitoringStatusEnum**](#MonitoringStatusEnum) | The monitoring status |  |
|**provisionedCapacityInBytes** | **Long** | The total provisioned capacity in Bytes |  |
|**shareStatus** | [**ShareStatusEnum**](#ShareStatusEnum) | The Share Status |  |
|**usedCapacityInBytes** | **Long** | The used capacity in Bytes. |  [optional] [readonly] |



## Enum: DataPolicyEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| LOCAL | &quot;Local&quot; |
| TIERED | &quot;Tiered&quot; |
| CLOUD | &quot;Cloud&quot; |



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






# ISCSIDiskProperties

The iSCSI disk properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessControlRecords** | **List&lt;String&gt;** | The access control records. |  |
|**dataPolicy** | [**DataPolicyEnum**](#DataPolicyEnum) | The data policy. |  |
|**description** | **String** | The description. |  [optional] |
|**diskStatus** | [**DiskStatusEnum**](#DiskStatusEnum) | The disk status. |  |
|**localUsedCapacityInBytes** | **Long** | The local used capacity in bytes. |  [optional] [readonly] |
|**monitoringStatus** | [**MonitoringStatusEnum**](#MonitoringStatusEnum) | The monitoring. |  |
|**provisionedCapacityInBytes** | **Long** | The provisioned capacity in bytes. |  |
|**usedCapacityInBytes** | **Long** | The used capacity in bytes. |  [optional] [readonly] |



## Enum: DataPolicyEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| LOCAL | &quot;Local&quot; |
| TIERED | &quot;Tiered&quot; |
| CLOUD | &quot;Cloud&quot; |



## Enum: DiskStatusEnum

| Name | Value |
|---- | -----|
| ONLINE | &quot;Online&quot; |
| OFFLINE | &quot;Offline&quot; |



## Enum: MonitoringStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |




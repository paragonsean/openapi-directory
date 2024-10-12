# StorSimpleManagementClient.FileShareProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminUser** | **String** | The user/group who will have full permission in this share. Active directory email address. Example: xyz@contoso.com or Contoso\\xyz. | 
**dataPolicy** | **String** | The data policy | 
**description** | **String** | Description for file share | [optional] 
**localUsedCapacityInBytes** | **Number** | The local used capacity in Bytes. | [optional] [readonly] 
**monitoringStatus** | **String** | The monitoring status | 
**provisionedCapacityInBytes** | **Number** | The total provisioned capacity in Bytes | 
**shareStatus** | **String** | The Share Status | 
**usedCapacityInBytes** | **Number** | The used capacity in Bytes. | [optional] [readonly] 



## Enum: DataPolicyEnum


* `Invalid` (value: `"Invalid"`)

* `Local` (value: `"Local"`)

* `Tiered` (value: `"Tiered"`)

* `Cloud` (value: `"Cloud"`)





## Enum: MonitoringStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ShareStatusEnum


* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)





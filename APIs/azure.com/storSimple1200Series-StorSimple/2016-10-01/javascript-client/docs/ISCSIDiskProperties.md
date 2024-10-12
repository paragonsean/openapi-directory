# StorSimpleManagementClient.ISCSIDiskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessControlRecords** | **[String]** | The access control records. | 
**dataPolicy** | **String** | The data policy. | 
**description** | **String** | The description. | [optional] 
**diskStatus** | **String** | The disk status. | 
**localUsedCapacityInBytes** | **Number** | The local used capacity in bytes. | [optional] [readonly] 
**monitoringStatus** | **String** | The monitoring. | 
**provisionedCapacityInBytes** | **Number** | The provisioned capacity in bytes. | 
**usedCapacityInBytes** | **Number** | The used capacity in bytes. | [optional] [readonly] 



## Enum: DataPolicyEnum


* `Invalid` (value: `"Invalid"`)

* `Local` (value: `"Local"`)

* `Tiered` (value: `"Tiered"`)

* `Cloud` (value: `"Cloud"`)





## Enum: DiskStatusEnum


* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)





## Enum: MonitoringStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





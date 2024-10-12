# PrivateDnsManagementClient.PrivateZoneProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxNumberOfRecordSets** | **Number** | The maximum number of record sets that can be created in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**maxNumberOfVirtualNetworkLinks** | **Number** | The maximum number of virtual networks that can be linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**maxNumberOfVirtualNetworkLinksWithRegistration** | **Number** | The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**numberOfRecordSets** | **Number** | The current number of record sets in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**numberOfVirtualNetworkLinks** | **Number** | The current number of virtual networks that are linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**numberOfVirtualNetworkLinksWithRegistration** | **Number** | The current number of virtual networks that are linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





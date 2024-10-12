# DnsManagementClient.ZoneProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxNumberOfRecordSets** | **Number** | The maximum number of record sets that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**nameServers** | **[String]** | The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**numberOfRecordSets** | **Number** | The current number of record sets in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. | [optional] [readonly] 
**registrationVirtualNetworks** | [**[SubResource]**](SubResource.md) | A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private. | [optional] 
**resolutionVirtualNetworks** | [**[SubResource]**](SubResource.md) | A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private. | [optional] 
**zoneType** | **String** | The type of this DNS zone (Public or Private). | [optional] [default to &#39;Public&#39;]



## Enum: ZoneTypeEnum


* `Public` (value: `"Public"`)

* `Private` (value: `"Private"`)





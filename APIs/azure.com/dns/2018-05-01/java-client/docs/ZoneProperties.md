

# ZoneProperties

Represents the properties of the zone.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNumberOfRecordSets** | **Long** | The maximum number of record sets that can be created in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**nameServers** | **List&lt;String&gt;** | The name servers for this DNS zone. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**numberOfRecordSets** | **Long** | The current number of record sets in this DNS zone.  This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**registrationVirtualNetworks** | [**List&lt;SubResource&gt;**](SubResource.md) | A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private. |  [optional] |
|**resolutionVirtualNetworks** | [**List&lt;SubResource&gt;**](SubResource.md) | A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private. |  [optional] |
|**zoneType** | [**ZoneTypeEnum**](#ZoneTypeEnum) | The type of this DNS zone (Public or Private). |  [optional] |



## Enum: ZoneTypeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;Public&quot; |
| PRIVATE | &quot;Private&quot; |




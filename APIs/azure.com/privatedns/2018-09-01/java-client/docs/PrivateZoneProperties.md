

# PrivateZoneProperties

Represents the properties of the Private DNS zone.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNumberOfRecordSets** | **Long** | The maximum number of record sets that can be created in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**maxNumberOfVirtualNetworkLinks** | **Long** | The maximum number of virtual networks that can be linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**maxNumberOfVirtualNetworkLinksWithRegistration** | **Long** | The maximum number of virtual networks that can be linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**numberOfRecordSets** | **Long** | The current number of record sets in this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**numberOfVirtualNetworkLinks** | **Long** | The current number of virtual networks that are linked to this Private DNS zone. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**numberOfVirtualNetworkLinksWithRegistration** | **Long** | The current number of virtual networks that are linked to this Private DNS zone with registration enabled. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. This is a read-only property and any attempt to set this value will be ignored. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |




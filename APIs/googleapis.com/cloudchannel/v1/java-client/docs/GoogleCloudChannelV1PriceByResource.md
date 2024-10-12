

# GoogleCloudChannelV1PriceByResource

Represents price by resource type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**price** | [**GoogleCloudChannelV1Price**](GoogleCloudChannelV1Price.md) |  |  [optional] |
|**pricePhases** | [**List&lt;GoogleCloudChannelV1PricePhase&gt;**](GoogleCloudChannelV1PricePhase.md) | Specifies the price by time range. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | Resource Type. Example: SEAT |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE_TYPE_UNSPECIFIED | &quot;RESOURCE_TYPE_UNSPECIFIED&quot; |
| SEAT | &quot;SEAT&quot; |
| MAU | &quot;MAU&quot; |
| GB | &quot;GB&quot; |
| LICENSED_USER | &quot;LICENSED_USER&quot; |
| MINUTES | &quot;MINUTES&quot; |
| IAAS_USAGE | &quot;IAAS_USAGE&quot; |
| SUBSCRIPTION | &quot;SUBSCRIPTION&quot; |




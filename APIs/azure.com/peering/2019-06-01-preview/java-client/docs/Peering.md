

# Peering

Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of the peering. |  |
|**location** | **String** | The location of the resource. |  |
|**properties** | [**PeeringProperties**](PeeringProperties.md) |  |  [optional] |
|**sku** | [**PeeringSku**](PeeringSku.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | The resource tags. |  [optional] |
|**id** | **String** | The ID of the resource. |  [optional] [readonly] |
|**name** | **String** | The name of the resource. |  [optional] [readonly] |
|**type** | **String** | The type of the resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| DIRECT | &quot;Direct&quot; |
| EXCHANGE | &quot;Exchange&quot; |




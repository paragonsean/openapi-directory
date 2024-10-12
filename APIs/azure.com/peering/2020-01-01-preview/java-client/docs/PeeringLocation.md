

# PeeringLocation

Peering location is where connectivity could be established to the Microsoft Cloud Edge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of peering that the peering location supports. |  [optional] |
|**properties** | [**PeeringLocationProperties**](PeeringLocationProperties.md) |  |  [optional] |
|**id** | **String** | The ID of the resource. |  [optional] [readonly] |
|**name** | **String** | The name of the resource. |  [optional] [readonly] |
|**type** | **String** | The type of the resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| DIRECT | &quot;Direct&quot; |
| EXCHANGE | &quot;Exchange&quot; |




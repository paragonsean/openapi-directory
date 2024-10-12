

# PeeringProperties

The properties that define connectivity to the Microsoft Cloud Edge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direct** | [**PeeringPropertiesDirect**](PeeringPropertiesDirect.md) |  |  [optional] |
|**exchange** | [**PeeringPropertiesExchange**](PeeringPropertiesExchange.md) |  |  [optional] |
|**peeringLocation** | **String** | The location of the peering. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |




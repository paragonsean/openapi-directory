

# ExpressRoutePortsLocationPropertiesFormat

Properties specific to ExpressRoutePorts peering location resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of peering location. |  [optional] [readonly] |
|**availableBandwidths** | [**List&lt;ExpressRoutePortsLocationBandwidths&gt;**](ExpressRoutePortsLocationBandwidths.md) | The inventory of available ExpressRoutePort bandwidths. |  [optional] |
|**contact** | **String** | Contact details of peering locations. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |




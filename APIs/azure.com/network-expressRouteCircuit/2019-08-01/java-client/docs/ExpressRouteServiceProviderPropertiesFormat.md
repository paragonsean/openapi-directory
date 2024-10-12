

# ExpressRouteServiceProviderPropertiesFormat

Properties of ExpressRouteServiceProvider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthsOffered** | [**List&lt;ExpressRouteServiceProviderBandwidthsOffered&gt;**](ExpressRouteServiceProviderBandwidthsOffered.md) | A list of bandwidths offered. |  [optional] |
|**peeringLocations** | **List&lt;String&gt;** | A list of peering locations. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |






# RouteFilterPropertiesFormat

Route Filter Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipv6Peerings** | [**List&lt;RouteFilterPropertiesFormatIpv6PeeringsInner&gt;**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit ipv6 peerings. |  [optional] |
|**peerings** | [**List&lt;RouteFilterPropertiesFormatIpv6PeeringsInner&gt;**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit peerings. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rules** | [**List&lt;RouteFilterRule&gt;**](RouteFilterRule.md) | Collection of RouteFilterRules contained within a route filter. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |




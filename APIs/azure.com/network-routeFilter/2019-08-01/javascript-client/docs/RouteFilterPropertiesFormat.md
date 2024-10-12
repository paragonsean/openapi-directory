# NetworkManagementClient.RouteFilterPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6Peerings** | [**[RouteFilterPropertiesFormatIpv6PeeringsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit ipv6 peerings. | [optional] 
**peerings** | [**[RouteFilterPropertiesFormatIpv6PeeringsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit peerings. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**rules** | [**[RouteFilterRule]**](RouteFilterRule.md) | Collection of RouteFilterRules contained within a route filter. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





# NetworkManagementClient.RouteFilterPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6Peerings** | [**[RouteFilterPropertiesFormatIpv6PeeringsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit ipv6 peerings. | [optional] 
**peerings** | [**[RouteFilterPropertiesFormatIpv6PeeringsInner]**](RouteFilterPropertiesFormatIpv6PeeringsInner.md) | A collection of references to express route circuit peerings. | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, &#39;Succeeded&#39; and &#39;Failed&#39;. | [optional] [readonly] 
**rules** | [**[RouteFilterRule]**](RouteFilterRule.md) | Collection of RouteFilterRules contained within a route filter. | [optional] 



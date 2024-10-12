# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringPropertiesIpv6PeeringConfigMicrosoftPeeringConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisedCommunities** | **[String]** | The communities of bgp peering. Specified for microsoft peering. | [optional] 
**advertisedPublicPrefixes** | **[String]** | The reference of AdvertisedPublicPrefixes. | [optional] 
**advertisedPublicPrefixesState** | **String** | The advertised public prefix state of the Peering resource. | [optional] 
**customerASN** | **Number** | The CustomerASN of the peering. | [optional] 
**legacyMode** | **Number** | The legacy mode of the peering. | [optional] 
**routingRegistryName** | **String** | The RoutingRegistryName of the configuration. | [optional] 



## Enum: AdvertisedPublicPrefixesStateEnum


* `NotConfigured` (value: `"NotConfigured"`)

* `Configuring` (value: `"Configuring"`)

* `Configured` (value: `"Configured"`)

* `ValidationNeeded` (value: `"ValidationNeeded"`)





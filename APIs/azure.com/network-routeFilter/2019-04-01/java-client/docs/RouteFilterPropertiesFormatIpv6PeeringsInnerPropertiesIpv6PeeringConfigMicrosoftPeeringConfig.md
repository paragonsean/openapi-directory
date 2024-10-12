

# RouteFilterPropertiesFormatIpv6PeeringsInnerPropertiesIpv6PeeringConfigMicrosoftPeeringConfig

Specifies the peering configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisedCommunities** | **List&lt;String&gt;** | The communities of bgp peering. Specified for microsoft peering. |  [optional] |
|**advertisedPublicPrefixes** | **List&lt;String&gt;** | The reference of AdvertisedPublicPrefixes. |  [optional] |
|**advertisedPublicPrefixesState** | [**AdvertisedPublicPrefixesStateEnum**](#AdvertisedPublicPrefixesStateEnum) | The advertised public prefix state of the Peering resource. |  [optional] |
|**customerASN** | **Integer** | The CustomerASN of the peering. |  [optional] |
|**legacyMode** | **Integer** | The legacy mode of the peering. |  [optional] |
|**routingRegistryName** | **String** | The RoutingRegistryName of the configuration. |  [optional] |



## Enum: AdvertisedPublicPrefixesStateEnum

| Name | Value |
|---- | -----|
| NOT_CONFIGURED | &quot;NotConfigured&quot; |
| CONFIGURING | &quot;Configuring&quot; |
| CONFIGURED | &quot;Configured&quot; |
| VALIDATION_NEEDED | &quot;ValidationNeeded&quot; |




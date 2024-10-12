

# ExpressRouteCircuitPeeringConfig

Specifies the peering configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisedPublicPrefixes** | **List&lt;String&gt;** | The reference of AdvertisedPublicPrefixes. |  [optional] |
|**advertisedPublicPrefixesState** | [**AdvertisedPublicPrefixesStateEnum**](#AdvertisedPublicPrefixesStateEnum) | AdvertisedPublicPrefixState of the Peering resource. Possible values are &#39;NotConfigured&#39;, &#39;Configuring&#39;, &#39;Configured&#39;, and &#39;ValidationNeeded&#39;. |  [optional] |
|**customerASN** | **Integer** | The CustomerASN of the peering. |  [optional] |
|**routingRegistryName** | **String** | The RoutingRegistryName of the configuration. |  [optional] |



## Enum: AdvertisedPublicPrefixesStateEnum

| Name | Value |
|---- | -----|
| NOT_CONFIGURED | &quot;NotConfigured&quot; |
| CONFIGURING | &quot;Configuring&quot; |
| CONFIGURED | &quot;Configured&quot; |
| VALIDATION_NEEDED | &quot;ValidationNeeded&quot; |




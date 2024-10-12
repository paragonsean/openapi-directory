

# ExpressRouteCircuitPeeringConfig

Specifies the peering config

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisedPublicPrefixes** | **List&lt;String&gt;** | Gets or sets the reference of AdvertisedPublicPrefixes |  [optional] |
|**advertisedPublicPrefixesState** | [**AdvertisedPublicPrefixesStateEnum**](#AdvertisedPublicPrefixesStateEnum) | Gets or sets AdvertisedPublicPrefixState of the Peering resource  |  [optional] |
|**customerASN** | **Integer** | Gets or Sets CustomerAsn of the peering. |  [optional] |
|**routingRegistryName** | **String** | Gets or Sets RoutingRegistryName of the config. |  [optional] |



## Enum: AdvertisedPublicPrefixesStateEnum

| Name | Value |
|---- | -----|
| NOT_CONFIGURED | &quot;NotConfigured&quot; |
| CONFIGURING | &quot;Configuring&quot; |
| CONFIGURED | &quot;Configured&quot; |
| VALIDATION_NEEDED | &quot;ValidationNeeded&quot; |




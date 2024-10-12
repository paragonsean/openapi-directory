

# ForwardingConfiguration

Describes Forwarding Route.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendPool** | [**Object**](Object.md) | Reference to another subresource. |  [optional] |
|**cacheConfiguration** | [**CacheConfiguration**](CacheConfiguration.md) |  |  [optional] |
|**customForwardingPath** | **String** | A custom path used to rewrite resource paths matched by this rule. Leave empty to use incoming path. |  [optional] |
|**forwardingProtocol** | [**ForwardingProtocolEnum**](#ForwardingProtocolEnum) | Protocol this rule will use when forwarding traffic to backends. |  [optional] |



## Enum: ForwardingProtocolEnum

| Name | Value |
|---- | -----|
| HTTP_ONLY | &quot;HttpOnly&quot; |
| HTTPS_ONLY | &quot;HttpsOnly&quot; |
| MATCH_REQUEST | &quot;MatchRequest&quot; |




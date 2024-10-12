# FrontDoorManagementClient.ForwardingConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendPool** | **Object** | Reference to another subresource. | [optional] 
**cacheConfiguration** | [**CacheConfiguration**](CacheConfiguration.md) |  | [optional] 
**customForwardingPath** | **String** | A custom path used to rewrite resource paths matched by this rule. Leave empty to use incoming path. | [optional] 
**forwardingProtocol** | **String** | Protocol this rule will use when forwarding traffic to backends. | [optional] 



## Enum: ForwardingProtocolEnum


* `HttpOnly` (value: `"HttpOnly"`)

* `HttpsOnly` (value: `"HttpsOnly"`)

* `MatchRequest` (value: `"MatchRequest"`)





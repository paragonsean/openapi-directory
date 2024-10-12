# NetworkServicesApi.ExtensionChain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | [**[ExtensionChainExtension]**](ExtensionChainExtension.md) | Required. A set of extensions to execute for the matching request. At least one extension is required. Up to 3 extensions can be defined for each extension chain for &#x60;LbTrafficExtension&#x60; resource. &#x60;LbRouteExtension&#x60; chains are limited to 1 extension per extension chain. | [optional] 
**matchCondition** | [**ExtensionChainMatchCondition**](ExtensionChainMatchCondition.md) |  | [optional] 
**name** | **String** | Required. The name for this extension chain. The name is logged as part of the HTTP request logs. The name must conform with RFC-1034, is restricted to lower-cased letters, numbers and hyphens, and can have a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number. | [optional] 



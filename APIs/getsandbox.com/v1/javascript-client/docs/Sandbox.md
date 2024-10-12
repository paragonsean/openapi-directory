# SandboxApi.Sandbox

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiDefinition** | **String** | The import source of this Sandbox. | [optional] 
**childSandboxes** | [**[Sandbox]**](Sandbox.md) | Clones of this Sandbox. | [optional] 
**configuredRoutes** | [**[ConfiguredRouteDetails]**](ConfiguredRouteDetails.md) | Extra configuration applied to some routes, delays, overrides etc. | [optional] 
**description** | **String** |  | [optional] 
**gitAccessToken** | **String** |  | [optional] 
**gitUrl** | **String** | The git clone URL. | [optional] 
**hasRepository** | **Boolean** | Whether this Sandbox has a git repository or not. | [optional] 
**id** | **String** | The ID of the Sandbox. | [optional] 
**ipWhitelist** | **[String]** | The list of IPs allowed to make requests, all allowed if omitted. | [optional] 
**name** | **String** |  | 
**parentSandbox** | [**Sandbox**](Sandbox.md) |  | [optional] 
**properties** | **{String: Object}** |  | [optional] 
**proxyStatus** | **String** | The listener status. | [optional] 
**runtimeVersion** | **String** | The library version of this Sandbox. | [optional] 
**sandboxUrl** | **String** | The request URL for this Sandbox. | [optional] 
**stackType** | **String** |  | [optional] 
**transportType** | **String** | The listener transport. | [optional] 



## Enum: ApiDefinitionEnum


* `None` (value: `"None"`)

* `Apiary` (value: `"Apiary"`)

* `Swagger_V2_Json` (value: `"Swagger_V2_Json"`)

* `RAML_V08` (value: `"RAML_V08"`)

* `WSDL` (value: `"WSDL"`)





## Enum: ProxyStatusEnum


* `STARTED` (value: `"STARTED"`)

* `STOPPED` (value: `"STOPPED"`)





## Enum: RuntimeVersionEnum


* `1` (value: `"VERSION_1"`)

* `2` (value: `"VERSION_2"`)





## Enum: StackTypeEnum


* `JavaScript` (value: `"JavaScript"`)





## Enum: TransportTypeEnum


* `HTTP` (value: `"HTTP"`)





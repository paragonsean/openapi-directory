

# Sandbox


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiDefinition** | [**ApiDefinitionEnum**](#ApiDefinitionEnum) | The import source of this Sandbox. |  [optional] |
|**childSandboxes** | [**Set&lt;Sandbox&gt;**](Sandbox.md) | Clones of this Sandbox. |  [optional] |
|**configuredRoutes** | [**Set&lt;ConfiguredRouteDetails&gt;**](ConfiguredRouteDetails.md) | Extra configuration applied to some routes, delays, overrides etc. |  [optional] |
|**description** | **String** |  |  [optional] |
|**gitAccessToken** | **String** |  |  [optional] |
|**gitUrl** | **String** | The git clone URL. |  [optional] |
|**hasRepository** | **Boolean** | Whether this Sandbox has a git repository or not. |  [optional] |
|**id** | **String** | The ID of the Sandbox. |  [optional] |
|**ipWhitelist** | **Set&lt;String&gt;** | The list of IPs allowed to make requests, all allowed if omitted. |  [optional] |
|**name** | **String** |  |  |
|**parentSandbox** | [**Sandbox**](Sandbox.md) |  |  [optional] |
|**properties** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**proxyStatus** | [**ProxyStatusEnum**](#ProxyStatusEnum) | The listener status. |  [optional] |
|**runtimeVersion** | [**RuntimeVersionEnum**](#RuntimeVersionEnum) | The library version of this Sandbox. |  [optional] |
|**sandboxUrl** | **String** | The request URL for this Sandbox. |  [optional] |
|**stackType** | [**StackTypeEnum**](#StackTypeEnum) |  |  [optional] |
|**transportType** | [**TransportTypeEnum**](#TransportTypeEnum) | The listener transport. |  [optional] |



## Enum: ApiDefinitionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| APIARY | &quot;Apiary&quot; |
| SWAGGER_V2_JSON | &quot;Swagger_V2_Json&quot; |
| RAML_V08 | &quot;RAML_V08&quot; |
| WSDL | &quot;WSDL&quot; |



## Enum: ProxyStatusEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;STARTED&quot; |
| STOPPED | &quot;STOPPED&quot; |



## Enum: RuntimeVersionEnum

| Name | Value |
|---- | -----|
| _1 | &quot;VERSION_1&quot; |
| _2 | &quot;VERSION_2&quot; |



## Enum: StackTypeEnum

| Name | Value |
|---- | -----|
| JAVA_SCRIPT | &quot;JavaScript&quot; |



## Enum: TransportTypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;HTTP&quot; |




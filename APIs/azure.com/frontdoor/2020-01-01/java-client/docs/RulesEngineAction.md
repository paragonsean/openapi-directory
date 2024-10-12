

# RulesEngineAction

One or more actions that will execute, modifying the request and/or response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestHeaderActions** | [**List&lt;HeaderAction&gt;**](HeaderAction.md) | A list of header actions to apply from the request from AFD to the origin. |  [optional] |
|**responseHeaderActions** | [**List&lt;HeaderAction&gt;**](HeaderAction.md) | A list of header actions to apply from the response from AFD to the client. |  [optional] |
|**routeConfigurationOverride** | [**RouteConfiguration**](RouteConfiguration.md) |  |  [optional] |




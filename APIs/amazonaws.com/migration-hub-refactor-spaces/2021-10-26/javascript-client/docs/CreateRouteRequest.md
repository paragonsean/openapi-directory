# AwsMigrationHubRefactorSpaces.CreateRouteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**defaultRoute** | [**CreateRouteRequestDefaultRoute**](CreateRouteRequestDefaultRoute.md) |  | [optional] 
**routeType** | **String** | The route type of the route. &lt;code&gt;DEFAULT&lt;/code&gt; indicates that all traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created. &lt;code&gt;URI_PATH&lt;/code&gt; indicates a route that is based on a URI path. | 
**serviceIdentifier** | **String** | The ID of the service in which the route is created. Traffic that matches this route is forwarded to this service. | 
**tags** | **{String: String}** | A collection of up to 50 unique tags | [optional] 
**uriPathRoute** | [**CreateRouteRequestUriPathRoute**](CreateRouteRequestUriPathRoute.md) |  | [optional] 



## Enum: RouteTypeEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `URI_PATH` (value: `"URI_PATH"`)





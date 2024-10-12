

# TlsRouteRouteRule

Specifies how to match traffic and how to route traffic when traffic is matched.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**TlsRouteRouteAction**](TlsRouteRouteAction.md) |  |  [optional] |
|**matches** | [**List&lt;TlsRouteRouteMatch&gt;**](TlsRouteRouteMatch.md) | Required. RouteMatch defines the predicate used to match requests to a given action. Multiple match types are \&quot;OR\&quot;ed for evaluation. |  [optional] |




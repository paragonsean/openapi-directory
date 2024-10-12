

# HttpRouteRouteAction

The specifications for routing traffic and applying associated policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corsPolicy** | [**HttpRouteCorsPolicy**](HttpRouteCorsPolicy.md) |  |  [optional] |
|**destinations** | [**List&lt;HttpRouteDestination&gt;**](HttpRouteDestination.md) | The destination to which traffic should be forwarded. |  [optional] |
|**directResponse** | [**HttpRouteHttpDirectResponse**](HttpRouteHttpDirectResponse.md) |  |  [optional] |
|**faultInjectionPolicy** | [**HttpRouteFaultInjectionPolicy**](HttpRouteFaultInjectionPolicy.md) |  |  [optional] |
|**idleTimeout** | **String** | Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled. |  [optional] |
|**redirect** | [**HttpRouteRedirect**](HttpRouteRedirect.md) |  |  [optional] |
|**requestHeaderModifier** | [**HttpRouteHeaderModifier**](HttpRouteHeaderModifier.md) |  |  [optional] |
|**requestMirrorPolicy** | [**HttpRouteRequestMirrorPolicy**](HttpRouteRequestMirrorPolicy.md) |  |  [optional] |
|**responseHeaderModifier** | [**HttpRouteHeaderModifier**](HttpRouteHeaderModifier.md) |  |  [optional] |
|**retryPolicy** | [**HttpRouteRetryPolicy**](HttpRouteRetryPolicy.md) |  |  [optional] |
|**statefulSessionAffinity** | [**HttpRouteStatefulSessionAffinityPolicy**](HttpRouteStatefulSessionAffinityPolicy.md) |  |  [optional] |
|**timeout** | **String** | Specifies the timeout for selected route. Timeout is computed from the time the request has been fully processed (i.e. end of stream) up until the response has been completely processed. Timeout includes all retries. |  [optional] |
|**urlRewrite** | [**HttpRouteURLRewrite**](HttpRouteURLRewrite.md) |  |  [optional] |




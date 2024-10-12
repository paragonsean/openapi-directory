

# GrpcRouteRouteAction

Specifies how to route matched traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinations** | [**List&lt;GrpcRouteDestination&gt;**](GrpcRouteDestination.md) | Optional. The destination services to which traffic should be forwarded. If multiple destinations are specified, traffic will be split between Backend Service(s) according to the weight field of these destinations. |  [optional] |
|**faultInjectionPolicy** | [**GrpcRouteFaultInjectionPolicy**](GrpcRouteFaultInjectionPolicy.md) |  |  [optional] |
|**idleTimeout** | **String** | Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled. |  [optional] |
|**retryPolicy** | [**GrpcRouteRetryPolicy**](GrpcRouteRetryPolicy.md) |  |  [optional] |
|**statefulSessionAffinity** | [**GrpcRouteStatefulSessionAffinityPolicy**](GrpcRouteStatefulSessionAffinityPolicy.md) |  |  [optional] |
|**timeout** | **String** | Optional. Specifies the timeout for selected route. Timeout is computed from the time the request has been fully processed (i.e. end of stream) up until the response has been completely processed. Timeout includes all retries. |  [optional] |




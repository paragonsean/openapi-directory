

# TlsRouteRouteAction

The specifications for routing traffic and applying associated policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinations** | [**List&lt;TlsRouteRouteDestination&gt;**](TlsRouteRouteDestination.md) | Required. The destination services to which traffic should be forwarded. At least one destination service is required. |  [optional] |
|**idleTimeout** | **String** | Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 1 hour. If set to 0s, the timeout will be disabled. |  [optional] |




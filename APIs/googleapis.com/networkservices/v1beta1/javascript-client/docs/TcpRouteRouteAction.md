# NetworkServicesApi.TcpRouteRouteAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**[TcpRouteRouteDestination]**](TcpRouteRouteDestination.md) | Optional. The destination services to which traffic should be forwarded. At least one destination service is required. Only one of route destination or original destination can be set. | [optional] 
**idleTimeout** | **String** | Optional. Specifies the idle timeout for the selected route. The idle timeout is defined as the period in which there are no bytes sent or received on either the upstream or downstream connection. If not set, the default idle timeout is 30 seconds. If set to 0s, the timeout will be disabled. | [optional] 
**originalDestination** | **Boolean** | Optional. If true, Router will use the destination IP and port of the original connection as the destination of the request. Default is false. Only one of route destinations or original destination can be set. | [optional] 



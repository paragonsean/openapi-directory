# HetznerCloudApi.LoadBalancerServiceHTTP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | **[Number]** | IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for TLS/SSL passthrough or if &#x60;protocol&#x60; is \&quot;http\&quot; | [optional] 
**cookieLifetime** | **Number** | Lifetime of the cookie used for sticky sessions | [optional] 
**cookieName** | **String** | Name of the cookie used for sticky sessions | [optional] 
**redirectHttp** | **Boolean** | Redirect HTTP requests to HTTPS. Only available if protocol is \&quot;https\&quot;. Default &#x60;false&#x60; | [optional] 
**stickySessions** | **Boolean** | Use sticky sessions. Only available if protocol is \&quot;http\&quot; or \&quot;https\&quot;. Default &#x60;false&#x60; | [optional] 



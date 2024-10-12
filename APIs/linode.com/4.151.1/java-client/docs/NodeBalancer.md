

# NodeBalancer

Linode's load balancing solution.  Can handle multiple ports, SSL termination, and any number of backends.  NodeBalancer ports are configured with NodeBalancer Configs, and each config is given one or more NodeBalancer Node that accepts traffic.  The traffic should be routed to the  NodeBalancer's ip address, the NodeBalancer will handle routing individual requests to backends. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientConnThrottle** | **Integer** | Throttle connections per second.  Set to 0 (zero) to disable throttling.  |  [optional] |
|**created** | **OffsetDateTime** | When this NodeBalancer was created.  |  [optional] [readonly] |
|**hostname** | **String** | This NodeBalancer&#39;s hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.  |  [optional] [readonly] |
|**id** | **Integer** | This NodeBalancer&#39;s unique ID.  |  [optional] [readonly] |
|**ipv4** | **String** | This NodeBalancer&#39;s public IPv4 address.  |  [optional] [readonly] |
|**ipv6** | **String** | This NodeBalancer&#39;s public IPv6 address.  |  [optional] [readonly] |
|**label** | **String** | This NodeBalancer&#39;s label. These must be unique on your Account.  |  [optional] |
|**region** | **String** | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.  |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | An array of Tags applied to this object.  Tags are for organizational purposes only.  |  [optional] |
|**transfer** | [**NodeBalancerTransfer**](NodeBalancerTransfer.md) |  |  [optional] |
|**updated** | **OffsetDateTime** | When this NodeBalancer was last updated.  |  [optional] [readonly] |




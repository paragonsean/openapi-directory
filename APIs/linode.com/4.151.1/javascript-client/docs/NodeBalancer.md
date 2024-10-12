# LinodeApi.NodeBalancer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientConnThrottle** | **Number** | Throttle connections per second.  Set to 0 (zero) to disable throttling.  | [optional] 
**created** | **Date** | When this NodeBalancer was created.  | [optional] [readonly] 
**hostname** | **String** | This NodeBalancer&#39;s hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.  | [optional] [readonly] 
**id** | **Number** | This NodeBalancer&#39;s unique ID.  | [optional] [readonly] 
**ipv4** | **String** | This NodeBalancer&#39;s public IPv4 address.  | [optional] [readonly] 
**ipv6** | **String** | This NodeBalancer&#39;s public IPv6 address.  | [optional] [readonly] 
**label** | **String** | This NodeBalancer&#39;s label. These must be unique on your Account.  | [optional] 
**region** | **String** | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.  | [optional] [readonly] 
**tags** | **[String]** | An array of Tags applied to this object.  Tags are for organizational purposes only.  | [optional] 
**transfer** | [**NodeBalancerTransfer**](NodeBalancerTransfer.md) |  | [optional] 
**updated** | **Date** | When this NodeBalancer was last updated.  | [optional] [readonly] 



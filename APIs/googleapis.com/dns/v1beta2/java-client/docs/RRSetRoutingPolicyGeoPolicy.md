

# RRSetRoutingPolicyGeoPolicy

Configures a RRSetRoutingPolicy that routes based on the geo location of the querying user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableFencing** | **Boolean** | Without fencing, if health check fails for all configured items in the current geo bucket, we failover to the next nearest geo bucket. With fencing, if health checking is enabled, as long as some targets in the current geo bucket are healthy, we return only the healthy targets. However, if all targets are unhealthy, we don&#39;t failover to the next nearest bucket; instead, we return all the items in the current bucket even when all targets are unhealthy. |  [optional] |
|**items** | [**List&lt;RRSetRoutingPolicyGeoPolicyGeoPolicyItem&gt;**](RRSetRoutingPolicyGeoPolicyGeoPolicyItem.md) | The primary geo routing configuration. If there are multiple items with the same location, an error is returned instead. |  [optional] |
|**kind** | **String** |  |  [optional] |




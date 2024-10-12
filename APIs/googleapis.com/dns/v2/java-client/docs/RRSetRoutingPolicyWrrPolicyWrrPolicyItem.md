

# RRSetRoutingPolicyWrrPolicyWrrPolicyItem

A routing block which contains the routing information for one WRR item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthCheckedTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  |  [optional] |
|**kind** | **String** |  |  [optional] |
|**rrdatas** | **List&lt;String&gt;** |  |  [optional] |
|**signatureRrdatas** | **List&lt;String&gt;** | DNSSEC generated signatures for all the rrdata within this item. Note that if health checked targets are provided for DNSSEC enabled zones, there&#39;s a restriction of 1 IP address per item. |  [optional] |
|**weight** | **Double** | The weight corresponding to this WrrPolicyItem object. When multiple WrrPolicyItem objects are configured, the probability of returning an WrrPolicyItem object&#39;s data is proportional to its weight relative to the sum of weights configured for all items. This weight must be non-negative. |  [optional] |




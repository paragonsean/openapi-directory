# CloudDnsApi.RRSetRoutingPolicyWrrPolicyWrrPolicyItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthCheckedTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem&#39;]
**rrdatas** | **[String]** |  | [optional] 
**signatureRrdatas** | **[String]** | DNSSEC generated signatures for all the rrdata within this item. Note that if health checked targets are provided for DNSSEC enabled zones, there&#39;s a restriction of 1 IP address per item. | [optional] 
**weight** | **Number** | The weight corresponding to this WrrPolicyItem object. When multiple WrrPolicyItem objects are configured, the probability of returning an WrrPolicyItem object&#39;s data is proportional to its weight relative to the sum of weights configured for all items. This weight must be non-negative. | [optional] 



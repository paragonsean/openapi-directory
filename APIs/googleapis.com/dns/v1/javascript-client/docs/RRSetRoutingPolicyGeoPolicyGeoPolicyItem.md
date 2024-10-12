# CloudDnsApi.RRSetRoutingPolicyGeoPolicyGeoPolicyItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthCheckedTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem&#39;]
**location** | **String** | The geo-location granularity is a GCP region. This location string should correspond to a GCP region. e.g. \&quot;us-east1\&quot;, \&quot;southamerica-east1\&quot;, \&quot;asia-east1\&quot;, etc. | [optional] 
**rrdatas** | **[String]** |  | [optional] 
**signatureRrdatas** | **[String]** | DNSSEC generated signatures for all the rrdata within this item. If health checked targets are provided for DNSSEC enabled zones, there&#39;s a restriction of 1 IP address per item. | [optional] 



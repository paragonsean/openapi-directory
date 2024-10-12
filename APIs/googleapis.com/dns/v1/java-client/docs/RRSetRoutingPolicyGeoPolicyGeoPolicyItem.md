

# RRSetRoutingPolicyGeoPolicyGeoPolicyItem

ResourceRecordSet data for one geo location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**healthCheckedTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  |  [optional] |
|**kind** | **String** |  |  [optional] |
|**location** | **String** | The geo-location granularity is a GCP region. This location string should correspond to a GCP region. e.g. \&quot;us-east1\&quot;, \&quot;southamerica-east1\&quot;, \&quot;asia-east1\&quot;, etc. |  [optional] |
|**rrdatas** | **List&lt;String&gt;** |  |  [optional] |
|**signatureRrdatas** | **List&lt;String&gt;** | DNSSEC generated signatures for all the rrdata within this item. If health checked targets are provided for DNSSEC enabled zones, there&#39;s a restriction of 1 IP address per item. |  [optional] |




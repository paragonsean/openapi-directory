

# PerformanceReport

The configuration data for an Ad Exchange performance report list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidRate** | **Double** | The number of bid responses with an ad. |  [optional] |
|**bidRequestRate** | **Double** | The number of bid requests sent to your bidder. |  [optional] |
|**calloutStatusRate** | **List&lt;Object&gt;** | Rate of various prefiltering statuses per match. Please refer to the callout-status-codes.txt file for different statuses. |  [optional] |
|**cookieMatcherStatusRate** | **List&lt;Object&gt;** | Average QPS for cookie matcher operations. |  [optional] |
|**creativeStatusRate** | **List&lt;Object&gt;** | Rate of ads with a given status. Please refer to the creative-status-codes.txt file for different statuses. |  [optional] |
|**filteredBidRate** | **Double** | The number of bid responses that were filtered due to a policy violation or other errors. |  [optional] |
|**hostedMatchStatusRate** | **List&lt;Object&gt;** | Average QPS for hosted match operations. |  [optional] |
|**inventoryMatchRate** | **Double** | The number of potential queries based on your pretargeting settings. |  [optional] |
|**kind** | **String** | Resource type. |  [optional] |
|**latency50thPercentile** | **Double** | The 50th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. |  [optional] |
|**latency85thPercentile** | **Double** | The 85th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. |  [optional] |
|**latency95thPercentile** | **Double** | The 95th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. |  [optional] |
|**noQuotaInRegion** | **Double** | Rate of various quota account statuses per quota check. |  [optional] |
|**outOfQuota** | **Double** | Rate of various quota account statuses per quota check. |  [optional] |
|**pixelMatchRequests** | **Double** | Average QPS for pixel match requests from clients. |  [optional] |
|**pixelMatchResponses** | **Double** | Average QPS for pixel match responses from clients. |  [optional] |
|**quotaConfiguredLimit** | **Double** | The configured quota limits for this account. |  [optional] |
|**quotaThrottledLimit** | **Double** | The throttled quota limits for this account. |  [optional] |
|**region** | **String** | The trading location of this data. |  [optional] |
|**successfulRequestRate** | **Double** | The number of properly formed bid responses received by our servers within the deadline. |  [optional] |
|**timestamp** | **String** | The unix timestamp of the starting time of this performance data. |  [optional] |
|**unsuccessfulRequestRate** | **Double** | The number of bid responses that were unsuccessful due to timeouts, incorrect formatting, etc. |  [optional] |




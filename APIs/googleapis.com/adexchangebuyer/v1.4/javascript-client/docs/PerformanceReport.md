# AdExchangeBuyerApi.PerformanceReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidRate** | **Number** | The number of bid responses with an ad. | [optional] 
**bidRequestRate** | **Number** | The number of bid requests sent to your bidder. | [optional] 
**calloutStatusRate** | **[Object]** | Rate of various prefiltering statuses per match. Please refer to the callout-status-codes.txt file for different statuses. | [optional] 
**cookieMatcherStatusRate** | **[Object]** | Average QPS for cookie matcher operations. | [optional] 
**creativeStatusRate** | **[Object]** | Rate of ads with a given status. Please refer to the creative-status-codes.txt file for different statuses. | [optional] 
**filteredBidRate** | **Number** | The number of bid responses that were filtered due to a policy violation or other errors. | [optional] 
**hostedMatchStatusRate** | **[Object]** | Average QPS for hosted match operations. | [optional] 
**inventoryMatchRate** | **Number** | The number of potential queries based on your pretargeting settings. | [optional] 
**kind** | **String** | Resource type. | [optional] [default to &#39;adexchangebuyer#performanceReport&#39;]
**latency50thPercentile** | **Number** | The 50th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. | [optional] 
**latency85thPercentile** | **Number** | The 85th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. | [optional] 
**latency95thPercentile** | **Number** | The 95th percentile round trip latency(ms) as perceived from Google servers for the duration period covered by the report. | [optional] 
**noQuotaInRegion** | **Number** | Rate of various quota account statuses per quota check. | [optional] 
**outOfQuota** | **Number** | Rate of various quota account statuses per quota check. | [optional] 
**pixelMatchRequests** | **Number** | Average QPS for pixel match requests from clients. | [optional] 
**pixelMatchResponses** | **Number** | Average QPS for pixel match responses from clients. | [optional] 
**quotaConfiguredLimit** | **Number** | The configured quota limits for this account. | [optional] 
**quotaThrottledLimit** | **Number** | The throttled quota limits for this account. | [optional] 
**region** | **String** | The trading location of this data. | [optional] 
**successfulRequestRate** | **Number** | The number of properly formed bid responses received by our servers within the deadline. | [optional] 
**timestamp** | **String** | The unix timestamp of the starting time of this performance data. | [optional] 
**unsuccessfulRequestRate** | **Number** | The number of bid responses that were unsuccessful due to timeouts, incorrect formatting, etc. | [optional] 



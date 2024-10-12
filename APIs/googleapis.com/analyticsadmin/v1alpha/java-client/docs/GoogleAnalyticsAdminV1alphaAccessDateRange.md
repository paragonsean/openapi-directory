

# GoogleAnalyticsAdminV1alphaAccessDateRange

A contiguous range of days: startDate, startDate + 1, ..., endDate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **String** | The inclusive end date for the query in the format &#x60;YYYY-MM-DD&#x60;. Cannot be before &#x60;startDate&#x60;. The format &#x60;NdaysAgo&#x60;, &#x60;yesterday&#x60;, or &#x60;today&#x60; is also accepted, and in that case, the date is inferred based on the current time in the request&#39;s time zone. |  [optional] |
|**startDate** | **String** | The inclusive start date for the query in the format &#x60;YYYY-MM-DD&#x60;. Cannot be after &#x60;endDate&#x60;. The format &#x60;NdaysAgo&#x60;, &#x60;yesterday&#x60;, or &#x60;today&#x60; is also accepted, and in that case, the date is inferred based on the current time in the request&#39;s time zone. |  [optional] |






# DateRange

A contiguous set of days: `startDate`, `startDate + 1`, ..., `endDate`. Requests are allowed up to 4 date ranges.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endDate** | **String** | The inclusive end date for the query in the format &#x60;YYYY-MM-DD&#x60;. Cannot be before &#x60;start_date&#x60;. The format &#x60;NdaysAgo&#x60;, &#x60;yesterday&#x60;, or &#x60;today&#x60; is also accepted, and in that case, the date is inferred based on the property&#39;s reporting time zone. |  [optional] |
|**name** | **String** | Assigns a name to this date range. The dimension &#x60;dateRange&#x60; is valued to this name in a report response. If set, cannot begin with &#x60;date_range_&#x60; or &#x60;RESERVED_&#x60;. If not set, date ranges are named by their zero based index in the request: &#x60;date_range_0&#x60;, &#x60;date_range_1&#x60;, etc. |  [optional] |
|**startDate** | **String** | The inclusive start date for the query in the format &#x60;YYYY-MM-DD&#x60;. Cannot be after &#x60;end_date&#x60;. The format &#x60;NdaysAgo&#x60;, &#x60;yesterday&#x60;, or &#x60;today&#x60; is also accepted, and in that case, the date is inferred based on the property&#39;s reporting time zone. |  [optional] |




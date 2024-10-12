

# DailyMetricTimeSeries

Represents a single datapoint, where each datapoint is a DailyMetric-DailySubEntityType-TimeSeries tuple.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyMetric** | [**DailyMetricEnum**](#DailyMetricEnum) | The DailyMetric that the TimeSeries represents. |  [optional] |
|**dailySubEntityType** | [**DailySubEntityType**](DailySubEntityType.md) |  |  [optional] |
|**timeSeries** | [**TimeSeries**](TimeSeries.md) |  |  [optional] |



## Enum: DailyMetricEnum

| Name | Value |
|---- | -----|
| DAILY_METRIC_UNKNOWN | &quot;DAILY_METRIC_UNKNOWN&quot; |
| BUSINESS_IMPRESSIONS_DESKTOP_MAPS | &quot;BUSINESS_IMPRESSIONS_DESKTOP_MAPS&quot; |
| BUSINESS_IMPRESSIONS_DESKTOP_SEARCH | &quot;BUSINESS_IMPRESSIONS_DESKTOP_SEARCH&quot; |
| BUSINESS_IMPRESSIONS_MOBILE_MAPS | &quot;BUSINESS_IMPRESSIONS_MOBILE_MAPS&quot; |
| BUSINESS_IMPRESSIONS_MOBILE_SEARCH | &quot;BUSINESS_IMPRESSIONS_MOBILE_SEARCH&quot; |
| BUSINESS_CONVERSATIONS | &quot;BUSINESS_CONVERSATIONS&quot; |
| BUSINESS_DIRECTION_REQUESTS | &quot;BUSINESS_DIRECTION_REQUESTS&quot; |
| CALL_CLICKS | &quot;CALL_CLICKS&quot; |
| WEBSITE_CLICKS | &quot;WEBSITE_CLICKS&quot; |
| BUSINESS_BOOKINGS | &quot;BUSINESS_BOOKINGS&quot; |
| BUSINESS_FOOD_ORDERS | &quot;BUSINESS_FOOD_ORDERS&quot; |
| BUSINESS_FOOD_MENU_CLICKS | &quot;BUSINESS_FOOD_MENU_CLICKS&quot; |




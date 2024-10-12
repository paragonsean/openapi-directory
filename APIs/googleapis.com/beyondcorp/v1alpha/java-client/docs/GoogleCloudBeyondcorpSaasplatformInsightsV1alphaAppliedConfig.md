

# GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig

The configuration that was applied to generate the result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**AggregationEnum**](#AggregationEnum) | Output only. Aggregation type applied. |  [optional] [readonly] |
|**customGrouping** | [**GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping**](GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping.md) |  |  [optional] |
|**endTime** | **String** | Output only. Ending time for the duration for which insight was pulled. |  [optional] [readonly] |
|**fieldFilter** | **String** | Output only. Filters applied. |  [optional] [readonly] |
|**group** | **String** | Output only. Group id of the grouping applied. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Starting time for the duration for which insight was pulled. |  [optional] [readonly] |



## Enum: AggregationEnum

| Name | Value |
|---- | -----|
| AGGREGATION_UNSPECIFIED | &quot;AGGREGATION_UNSPECIFIED&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| CUSTOM_DATE_RANGE | &quot;CUSTOM_DATE_RANGE&quot; |




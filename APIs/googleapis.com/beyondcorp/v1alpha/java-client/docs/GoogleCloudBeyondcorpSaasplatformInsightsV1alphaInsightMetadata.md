

# GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata

Insight filters, groupings and aggregations that can be applied for the insight. Examples: aggregations, groups, field filters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregations** | [**List&lt;AggregationsEnum&gt;**](#List&lt;AggregationsEnum&gt;) | Output only. List of aggregation types available for insight. |  [optional] [readonly] |
|**category** | **String** | Output only. Category of the insight. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Common name of the insight. |  [optional] [readonly] |
|**fields** | [**List&lt;GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField&gt;**](GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField.md) | Output only. List of fields available for insight. |  [optional] [readonly] |
|**groups** | **List&lt;String&gt;** | Output only. List of groupings available for insight. |  [optional] [readonly] |
|**subCategory** | **String** | Output only. Sub-Category of the insight. |  [optional] [readonly] |
|**type** | **String** | Output only. Type of the insight. It is metadata describing whether the insight is a metric (e.g. count) or a report (e.g. list, status). |  [optional] [readonly] |



## Enum: List&lt;AggregationsEnum&gt;

| Name | Value |
|---- | -----|
| AGGREGATION_UNSPECIFIED | &quot;AGGREGATION_UNSPECIFIED&quot; |
| HOURLY | &quot;HOURLY&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| CUSTOM_DATE_RANGE | &quot;CUSTOM_DATE_RANGE&quot; |




# BeyondCorpApi.GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | **[String]** | Output only. List of aggregation types available for insight. | [optional] [readonly] 
**category** | **String** | Output only. Category of the insight. | [optional] [readonly] 
**displayName** | **String** | Output only. Common name of the insight. | [optional] [readonly] 
**fields** | [**[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField]**](GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField.md) | Output only. List of fields available for insight. | [optional] [readonly] 
**groups** | **[String]** | Output only. List of groupings available for insight. | [optional] [readonly] 
**subCategory** | **String** | Output only. Sub-Category of the insight. | [optional] [readonly] 
**type** | **String** | Output only. Type of the insight. It is metadata describing whether the insight is a metric (e.g. count) or a report (e.g. list, status). | [optional] [readonly] 



## Enum: [AggregationsEnum]


* `AGGREGATION_UNSPECIFIED` (value: `"AGGREGATION_UNSPECIFIED"`)

* `HOURLY` (value: `"HOURLY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `CUSTOM_DATE_RANGE` (value: `"CUSTOM_DATE_RANGE"`)





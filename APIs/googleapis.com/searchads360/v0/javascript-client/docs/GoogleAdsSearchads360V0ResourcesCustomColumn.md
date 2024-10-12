# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCustomColumn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Output only. User-defined description of the custom column. | [optional] [readonly] 
**id** | **String** | Output only. ID of the custom column. | [optional] [readonly] 
**name** | **String** | Output only. User-defined name of the custom column. | [optional] [readonly] 
**queryable** | **Boolean** | Output only. True when the custom column is available to be used in the query of SearchAds360Service.Search and SearchAds360Service.SearchStream. | [optional] [readonly] 
**referencedSystemColumns** | **[String]** | Output only. The list of the referenced system columns of this custom column. For example, A custom column \&quot;sum of impressions and clicks\&quot; has referenced system columns of {\&quot;metrics.clicks\&quot;, \&quot;metrics.impressions\&quot;}. | [optional] [readonly] 
**referencesAttributes** | **Boolean** | Output only. True when the custom column is referring to one or more attributes. | [optional] [readonly] 
**referencesMetrics** | **Boolean** | Output only. True when the custom column is referring to one or more metrics. | [optional] [readonly] 
**resourceName** | **String** | Immutable. The resource name of the custom column. Custom column resource names have the form: &#x60;customers/{customer_id}/customColumns/{custom_column_id}&#x60; | [optional] 
**valueType** | **String** | Output only. The type of the result value of the custom column. | [optional] [readonly] 



## Enum: ValueTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `STRING` (value: `"STRING"`)

* `INT64` (value: `"INT64"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `BOOLEAN` (value: `"BOOLEAN"`)





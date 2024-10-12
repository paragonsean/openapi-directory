

# GoogleAdsSearchads360V0ResourcesCustomColumn

A custom column. See Search Ads 360 custom column at https://support.google.com/sa360/answer/9633916

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Output only. User-defined description of the custom column. |  [optional] [readonly] |
|**id** | **String** | Output only. ID of the custom column. |  [optional] [readonly] |
|**name** | **String** | Output only. User-defined name of the custom column. |  [optional] [readonly] |
|**queryable** | **Boolean** | Output only. True when the custom column is available to be used in the query of SearchAds360Service.Search and SearchAds360Service.SearchStream. |  [optional] [readonly] |
|**referencedSystemColumns** | **List&lt;String&gt;** | Output only. The list of the referenced system columns of this custom column. For example, A custom column \&quot;sum of impressions and clicks\&quot; has referenced system columns of {\&quot;metrics.clicks\&quot;, \&quot;metrics.impressions\&quot;}. |  [optional] [readonly] |
|**referencesAttributes** | **Boolean** | Output only. True when the custom column is referring to one or more attributes. |  [optional] [readonly] |
|**referencesMetrics** | **Boolean** | Output only. True when the custom column is referring to one or more metrics. |  [optional] [readonly] |
|**resourceName** | **String** | Immutable. The resource name of the custom column. Custom column resource names have the form: &#x60;customers/{customer_id}/customColumns/{custom_column_id}&#x60; |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | Output only. The type of the result value of the custom column. |  [optional] [readonly] |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| STRING | &quot;STRING&quot; |
| INT64 | &quot;INT64&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |




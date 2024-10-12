

# GoogleAdsSearchads360V0ResourcesConversionCustomVariable

A conversion custom variable. See \"About custom Floodlight metrics and dimensions in the new Search Ads 360\" at https://support.google.com/sa360/answer/13567857

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardinality** | [**CardinalityEnum**](#CardinalityEnum) | Output only. Cardinality of the conversion custom variable. |  [optional] [readonly] |
|**customColumnIds** | **List&lt;String&gt;** | Output only. The IDs of custom columns that use this conversion custom variable. |  [optional] [readonly] |
|**family** | [**FamilyEnum**](#FamilyEnum) | Output only. Family of the conversion custom variable. |  [optional] [readonly] |
|**floodlightConversionCustomVariableInfo** | [**GoogleAdsSearchads360V0ResourcesConversionCustomVariableFloodlightConversionCustomVariableInfo**](GoogleAdsSearchads360V0ResourcesConversionCustomVariableFloodlightConversionCustomVariableInfo.md) |  |  [optional] |
|**id** | **String** | Output only. The ID of the conversion custom variable. |  [optional] [readonly] |
|**name** | **String** | Required. The name of the conversion custom variable. Name should be unique. The maximum length of name is 100 characters. There should not be any extra spaces before and after. |  [optional] |
|**ownerCustomer** | **String** | Output only. The resource name of the customer that owns the conversion custom variable. |  [optional] [readonly] |
|**resourceName** | **String** | Immutable. The resource name of the conversion custom variable. Conversion custom variable resource names have the form: &#x60;customers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the conversion custom variable for conversion event accrual. |  [optional] |
|**tag** | **String** | Required. Immutable. The tag of the conversion custom variable. Tag should be unique and consist of a \&quot;u\&quot; character directly followed with a number less than ormequal to 100. For example: \&quot;u4\&quot;. |  [optional] |



## Enum: CardinalityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| BELOW_ALL_LIMITS | &quot;BELOW_ALL_LIMITS&quot; |
| EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT | &quot;EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT&quot; |
| APPROACHES_STATS_LIMIT | &quot;APPROACHES_STATS_LIMIT&quot; |
| EXCEEDS_STATS_LIMIT | &quot;EXCEEDS_STATS_LIMIT&quot; |



## Enum: FamilyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| STANDARD | &quot;STANDARD&quot; |
| FLOODLIGHT | &quot;FLOODLIGHT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ACTIVATION_NEEDED | &quot;ACTIVATION_NEEDED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |




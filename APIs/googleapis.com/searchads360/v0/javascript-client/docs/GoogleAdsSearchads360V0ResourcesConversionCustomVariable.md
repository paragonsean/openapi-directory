# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesConversionCustomVariable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardinality** | **String** | Output only. Cardinality of the conversion custom variable. | [optional] [readonly] 
**customColumnIds** | **[String]** | Output only. The IDs of custom columns that use this conversion custom variable. | [optional] [readonly] 
**family** | **String** | Output only. Family of the conversion custom variable. | [optional] [readonly] 
**floodlightConversionCustomVariableInfo** | [**GoogleAdsSearchads360V0ResourcesConversionCustomVariableFloodlightConversionCustomVariableInfo**](GoogleAdsSearchads360V0ResourcesConversionCustomVariableFloodlightConversionCustomVariableInfo.md) |  | [optional] 
**id** | **String** | Output only. The ID of the conversion custom variable. | [optional] [readonly] 
**name** | **String** | Required. The name of the conversion custom variable. Name should be unique. The maximum length of name is 100 characters. There should not be any extra spaces before and after. | [optional] 
**ownerCustomer** | **String** | Output only. The resource name of the customer that owns the conversion custom variable. | [optional] [readonly] 
**resourceName** | **String** | Immutable. The resource name of the conversion custom variable. Conversion custom variable resource names have the form: &#x60;customers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}&#x60; | [optional] 
**status** | **String** | The status of the conversion custom variable for conversion event accrual. | [optional] 
**tag** | **String** | Required. Immutable. The tag of the conversion custom variable. Tag should be unique and consist of a \&quot;u\&quot; character directly followed with a number less than ormequal to 100. For example: \&quot;u4\&quot;. | [optional] 



## Enum: CardinalityEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `BELOW_ALL_LIMITS` (value: `"BELOW_ALL_LIMITS"`)

* `EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT` (value: `"EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT"`)

* `APPROACHES_STATS_LIMIT` (value: `"APPROACHES_STATS_LIMIT"`)

* `EXCEEDS_STATS_LIMIT` (value: `"EXCEEDS_STATS_LIMIT"`)





## Enum: FamilyEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `STANDARD` (value: `"STANDARD"`)

* `FLOODLIGHT` (value: `"FLOODLIGHT"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ACTIVATION_NEEDED` (value: `"ACTIVATION_NEEDED"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)





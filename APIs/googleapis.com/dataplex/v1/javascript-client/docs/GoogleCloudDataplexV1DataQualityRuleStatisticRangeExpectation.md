# CloudDataplexApi.GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxValue** | **String** | Optional. The maximum column statistic value allowed for a row to pass this validation.At least one of min_value and max_value need to be provided. | [optional] 
**minValue** | **String** | Optional. The minimum column statistic value allowed for a row to pass this validation.At least one of min_value and max_value need to be provided. | [optional] 
**statistic** | **String** | Optional. The aggregate metric to evaluate. | [optional] 
**strictMaxEnabled** | **Boolean** | Optional. Whether column statistic needs to be strictly lesser than (&#39;&lt;&#39;) the maximum, or if equality is allowed.Only relevant if a max_value has been defined. Default &#x3D; false. | [optional] 
**strictMinEnabled** | **Boolean** | Optional. Whether column statistic needs to be strictly greater than (&#39;&gt;&#39;) the minimum, or if equality is allowed.Only relevant if a min_value has been defined. Default &#x3D; false. | [optional] 



## Enum: StatisticEnum


* `STATISTIC_UNDEFINED` (value: `"STATISTIC_UNDEFINED"`)

* `MEAN` (value: `"MEAN"`)

* `MIN` (value: `"MIN"`)

* `MAX` (value: `"MAX"`)





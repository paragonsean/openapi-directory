# CloudDataplexApi.GoogleCloudDataplexV1DataQualityRuleRangeExpectation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxValue** | **String** | Optional. The maximum column value allowed for a row to pass this validation. At least one of min_value and max_value need to be provided. | [optional] 
**minValue** | **String** | Optional. The minimum column value allowed for a row to pass this validation. At least one of min_value and max_value need to be provided. | [optional] 
**strictMaxEnabled** | **Boolean** | Optional. Whether each value needs to be strictly lesser than (&#39;&lt;&#39;) the maximum, or if equality is allowed.Only relevant if a max_value has been defined. Default &#x3D; false. | [optional] 
**strictMinEnabled** | **Boolean** | Optional. Whether each value needs to be strictly greater than (&#39;&gt;&#39;) the minimum, or if equality is allowed.Only relevant if a min_value has been defined. Default &#x3D; false. | [optional] 



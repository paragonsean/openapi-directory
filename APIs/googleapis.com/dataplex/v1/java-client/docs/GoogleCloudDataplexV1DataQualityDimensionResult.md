

# GoogleCloudDataplexV1DataQualityDimensionResult

DataQualityDimensionResult provides a more detailed, per-dimension view of the results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**GoogleCloudDataplexV1DataQualityDimension**](GoogleCloudDataplexV1DataQualityDimension.md) |  |  [optional] |
|**passed** | **Boolean** | Whether the dimension passed or failed. |  [optional] |
|**score** | **Float** | Output only. The dimension-level data quality score for this data scan job if and only if the &#39;dimension&#39; field is set.The score ranges between 0, 100 (up to two decimal points). |  [optional] [readonly] |




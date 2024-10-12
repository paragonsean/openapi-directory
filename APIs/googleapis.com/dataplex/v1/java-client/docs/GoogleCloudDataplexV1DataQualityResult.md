

# GoogleCloudDataplexV1DataQualityResult

The output of a DataQualityScan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | [**List&lt;GoogleCloudDataplexV1DataQualityColumnResult&gt;**](GoogleCloudDataplexV1DataQualityColumnResult.md) | Output only. A list of results at the column level.A column will have a corresponding DataQualityColumnResult if and only if there is at least one rule with the &#39;column&#39; field set to it. |  [optional] [readonly] |
|**dimensions** | [**List&lt;GoogleCloudDataplexV1DataQualityDimensionResult&gt;**](GoogleCloudDataplexV1DataQualityDimensionResult.md) | A list of results at the dimension level.A dimension will have a corresponding DataQualityDimensionResult if and only if there is at least one rule with the &#39;dimension&#39; field set to it. |  [optional] |
|**passed** | **Boolean** | Overall data quality result -- true if all rules passed. |  [optional] |
|**postScanActionsResult** | [**GoogleCloudDataplexV1DataQualityResultPostScanActionsResult**](GoogleCloudDataplexV1DataQualityResultPostScanActionsResult.md) |  |  [optional] |
|**rowCount** | **String** | The count of rows processed. |  [optional] |
|**rules** | [**List&lt;GoogleCloudDataplexV1DataQualityRuleResult&gt;**](GoogleCloudDataplexV1DataQualityRuleResult.md) | A list of all the rules in a job, and their results. |  [optional] |
|**scannedData** | [**GoogleCloudDataplexV1ScannedData**](GoogleCloudDataplexV1ScannedData.md) |  |  [optional] |
|**score** | **Float** | Output only. The overall data quality score.The score ranges between 0, 100 (up to two decimal points). |  [optional] [readonly] |




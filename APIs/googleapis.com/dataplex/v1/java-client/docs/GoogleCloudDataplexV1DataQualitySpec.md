

# GoogleCloudDataplexV1DataQualitySpec

DataQualityScan related setting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postScanActions** | [**GoogleCloudDataplexV1DataQualitySpecPostScanActions**](GoogleCloudDataplexV1DataQualitySpecPostScanActions.md) |  |  [optional] |
|**rowFilter** | **String** | Optional. A filter applied to all rows in a single DataScan job. The filter needs to be a valid SQL expression for a WHERE clause in BigQuery standard SQL syntax. Example: col1 &gt;&#x3D; 0 AND col2 &lt; 10 |  [optional] |
|**rules** | [**List&lt;GoogleCloudDataplexV1DataQualityRule&gt;**](GoogleCloudDataplexV1DataQualityRule.md) | Required. The list of rules to evaluate against a data source. At least one rule is required. |  [optional] |
|**samplingPercent** | **Float** | Optional. The percentage of the records to be selected from the dataset for DataScan. Value can range between 0.0 and 100.0 with up to 3 significant decimal digits. Sampling is not applied if sampling_percent is not specified, 0 or 100. |  [optional] |




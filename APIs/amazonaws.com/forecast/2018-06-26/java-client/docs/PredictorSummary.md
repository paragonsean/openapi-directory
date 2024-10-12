

# PredictorSummary

Provides a summary of the predictor properties that are used in the <a>ListPredictors</a> operation. To get the complete set of properties, call the <a>DescribePredictor</a> operation, and provide the listed <code>PredictorArn</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictorArn** | [**String**](String.md) |  |  [optional] |
|**predictorName** | [**String**](String.md) |  |  [optional] |
|**datasetGroupArn** | [**String**](String.md) |  |  [optional] |
|**isAutoPredictor** | [**Boolean**](Boolean.md) |  |  [optional] |
|**referencePredictorSummary** | [**PredictorSummaryReferencePredictorSummary**](PredictorSummaryReferencePredictorSummary.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |




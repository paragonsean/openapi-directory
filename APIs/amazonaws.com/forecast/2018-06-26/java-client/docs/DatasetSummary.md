

# DatasetSummary

Provides a summary of the dataset properties used in the <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasets.html\">ListDatasets</a> operation. To get the complete set of properties, call the <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDataset.html\">DescribeDataset</a> operation, and provide the <code>DatasetArn</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetArn** | [**String**](String.md) |  |  [optional] |
|**datasetName** | [**String**](String.md) |  |  [optional] |
|**datasetType** | [**DatasetType**](DatasetType.md) |  |  [optional] |
|**domain** | [**Domain**](Domain.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |




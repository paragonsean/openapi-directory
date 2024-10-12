

# DatasetDescription

<p> A description for a dataset. For more information, see <a>DescribeDataset</a>.</p> <p>The status fields <code>Status</code>, <code>StatusMessage</code>, and <code>StatusMessageCode</code> reflect the last operation on the dataset. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**DatasetStatus**](DatasetStatus.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**statusMessageCode** | [**DatasetStatusMessageCode**](DatasetStatusMessageCode.md) |  |  [optional] |
|**datasetStats** | [**DatasetDescriptionDatasetStats**](DatasetDescriptionDatasetStats.md) |  |  [optional] |




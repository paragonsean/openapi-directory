

# DatasetImportJobSummary

Provides a summary of the dataset import job properties used in the <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetImportJobs.html\">ListDatasetImportJobs</a> operation. To get the complete set of properties, call the <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetImportJob.html\">DescribeDatasetImportJob</a> operation, and provide the <code>DatasetImportJobArn</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetImportJobArn** | [**String**](String.md) |  |  [optional] |
|**datasetImportJobName** | [**String**](String.md) |  |  [optional] |
|**dataSource** | [**DatasetImportJobSummaryDataSource**](DatasetImportJobSummaryDataSource.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**importMode** | [**ImportMode**](ImportMode.md) |  |  [optional] |




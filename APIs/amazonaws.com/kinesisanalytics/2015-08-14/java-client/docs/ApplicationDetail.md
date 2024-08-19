

# ApplicationDetail

<note> <p>This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see <a href=\"/kinesisanalytics/latest/apiv2/Welcome.html\">Amazon Kinesis Data Analytics API V2 Documentation</a>.</p> </note> <p>Provides a description of the application, including the application Amazon Resource Name (ARN), status, latest version, and input and output configuration.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | [**String**](String.md) |  |  |
|**applicationDescription** | [**String**](String.md) |  |  [optional] |
|**applicationARN** | [**String**](String.md) |  |  |
|**applicationStatus** | [**ApplicationStatus**](ApplicationStatus.md) |  |  |
|**createTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdateTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**inputDescriptions** | [**List**](List.md) |  |  [optional] |
|**outputDescriptions** | [**List**](List.md) |  |  [optional] |
|**referenceDataSourceDescriptions** | [**List**](List.md) |  |  [optional] |
|**cloudWatchLoggingOptionDescriptions** | [**List**](List.md) |  |  [optional] |
|**applicationCode** | [**String**](String.md) |  |  [optional] |
|**applicationVersionId** | [**Integer**](Integer.md) |  |  |




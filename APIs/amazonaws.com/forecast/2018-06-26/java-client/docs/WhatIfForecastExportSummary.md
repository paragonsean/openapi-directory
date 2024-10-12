

# WhatIfForecastExportSummary

Provides a summary of the what-if forecast export properties used in the <a>ListWhatIfForecastExports</a> operation. To get the complete set of properties, call the <a>DescribeWhatIfForecastExport</a> operation, and provide the <code>WhatIfForecastExportArn</code> that is listed in the summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**whatIfForecastExportArn** | [**String**](String.md) |  |  [optional] |
|**whatIfForecastArns** | [**List**](List.md) |  |  [optional] |
|**whatIfForecastExportName** | [**String**](String.md) |  |  [optional] |
|**destination** | [**DescribeForecastExportJobResponseDestination**](DescribeForecastExportJobResponseDestination.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |




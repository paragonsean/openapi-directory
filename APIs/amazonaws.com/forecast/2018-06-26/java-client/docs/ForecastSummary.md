

# ForecastSummary

Provides a summary of the forecast properties used in the <a>ListForecasts</a> operation. To get the complete set of properties, call the <a>DescribeForecast</a> operation, and provide the <code>ForecastArn</code> that is listed in the summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forecastArn** | [**String**](String.md) |  |  [optional] |
|**forecastName** | [**String**](String.md) |  |  [optional] |
|**predictorArn** | [**String**](String.md) |  |  [optional] |
|**createdUsingAutoPredictor** | [**Boolean**](Boolean.md) |  |  [optional] |
|**datasetGroupArn** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModificationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |




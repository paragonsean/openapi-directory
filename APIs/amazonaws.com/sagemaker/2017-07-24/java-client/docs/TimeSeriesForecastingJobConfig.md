

# TimeSeriesForecastingJobConfig

<p>The collection of settings used by an AutoML job V2 for the time-series forecasting problem type.</p> <note> <p>The <code>TimeSeriesForecastingJobConfig</code> problem type is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featureSpecificationS3Uri** | [**String**](String.md) |  |  [optional] |
|**completionCriteria** | [**AutoMLJobCompletionCriteria**](AutoMLJobCompletionCriteria.md) |  |  [optional] |
|**forecastFrequency** | [**String**](String.md) |  |  |
|**forecastHorizon** | [**Integer**](Integer.md) |  |  |
|**forecastQuantiles** | [**List**](List.md) |  |  [optional] |
|**transformations** | [**TimeSeriesForecastingJobConfigTransformations**](TimeSeriesForecastingJobConfigTransformations.md) |  |  [optional] |
|**timeSeriesConfig** | [**TimeSeriesForecastingJobConfigTimeSeriesConfig**](TimeSeriesForecastingJobConfigTimeSeriesConfig.md) |  |  |




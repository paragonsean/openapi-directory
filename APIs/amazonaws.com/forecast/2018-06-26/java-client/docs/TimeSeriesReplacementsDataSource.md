

# TimeSeriesReplacementsDataSource

A replacement dataset is a modified version of the baseline related time series that contains only the values that you want to include in a what-if forecast. The replacement dataset must contain the forecast dimensions and item identifiers in the baseline related time series as well as at least 1 changed time series. This dataset is merged with the baseline related time series to create a transformed dataset that is used for the what-if forecast.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3Config** | [**S3Config**](S3Config.md) |  |  |
|**schema** | [**Schema**](Schema.md) |  |  |
|**format** | [**String**](String.md) |  |  [optional] |
|**timestampFormat** | [**String**](String.md) |  |  [optional] |




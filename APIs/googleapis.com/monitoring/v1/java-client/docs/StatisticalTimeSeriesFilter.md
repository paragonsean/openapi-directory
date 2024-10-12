

# StatisticalTimeSeriesFilter

A filter that ranks streams based on their statistical relation to other streams in a request. Note: This field is deprecated and completely ignored by the API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numTimeSeries** | **Integer** | How many time series to output. |  [optional] |
|**rankingMethod** | [**RankingMethodEnum**](#RankingMethodEnum) | rankingMethod is applied to a set of time series, and then the produced value for each individual time series is used to compare a given time series to others. These are methods that cannot be applied stream-by-stream, but rather require the full context of a request to evaluate time series. |  [optional] |



## Enum: RankingMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;METHOD_UNSPECIFIED&quot; |
| CLUSTER_OUTLIER | &quot;METHOD_CLUSTER_OUTLIER&quot; |




# TimeSeriesInsightsClient.InstancesSortParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | **String** | Value to use for sorting of the time series instances before being returned by search instances call. When it is set to &#39;Rank&#39;, the returned instances are sorted based on the relevance. When it is set to &#39;DisplayName&#39;, the returned results are sorted based on the display name. Display name is the name of the instance if it exists, otherwise, display name is the time series ID. Default is &#39;Rank&#39;. | [optional] 



## Enum: ByEnum


* `Rank` (value: `"Rank"`)

* `DisplayName` (value: `"DisplayName"`)







# GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket

A DeltaPresenceEstimationHistogramBucket message with the following values: min_probability: 0.1 max_probability: 0.2 frequency: 42 means that there are 42 records for which δ is in [0.1, 0.2). An important particular case is when min_probability = max_probability = 1: then, every individual who shares this quasi-identifier combination is in the dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketSize** | **String** | Number of records within these probability bounds. |  [optional] |
|**bucketValueCount** | **String** | Total number of distinct quasi-identifier tuple values in this bucket. |  [optional] |
|**bucketValues** | [**List&lt;GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues&gt;**](GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues.md) | Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20. |  [optional] |
|**maxProbability** | **Double** | Always greater than or equal to min_probability. |  [optional] |
|**minProbability** | **Double** | Between 0 and 1. |  [optional] |




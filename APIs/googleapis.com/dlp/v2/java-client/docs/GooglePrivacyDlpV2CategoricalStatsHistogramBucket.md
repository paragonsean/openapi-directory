

# GooglePrivacyDlpV2CategoricalStatsHistogramBucket

Histogram of value frequencies in the column.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketSize** | **String** | Total number of values in this bucket. |  [optional] |
|**bucketValueCount** | **String** | Total number of distinct values in this bucket. |  [optional] |
|**bucketValues** | [**List&lt;GooglePrivacyDlpV2ValueFrequency&gt;**](GooglePrivacyDlpV2ValueFrequency.md) | Sample of value frequencies in this bucket. The total number of values returned per bucket is capped at 20. |  [optional] |
|**valueFrequencyLowerBound** | **String** | Lower bound on the value frequency of the values in this bucket. |  [optional] |
|**valueFrequencyUpperBound** | **String** | Upper bound on the value frequency of the values in this bucket. |  [optional] |




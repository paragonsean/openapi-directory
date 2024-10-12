

# GooglePrivacyDlpV2KMapEstimationHistogramBucket

A KMapEstimationHistogramBucket message with the following values: min_anonymity: 3 max_anonymity: 5 frequency: 42 means that there are 42 records whose quasi-identifier values correspond to 3, 4 or 5 people in the overlying population. An important particular case is when min_anonymity = max_anonymity = 1: the frequency field then corresponds to the number of uniquely identifiable records.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketSize** | **String** | Number of records within these anonymity bounds. |  [optional] |
|**bucketValueCount** | **String** | Total number of distinct quasi-identifier tuple values in this bucket. |  [optional] |
|**bucketValues** | [**List&lt;GooglePrivacyDlpV2KMapEstimationQuasiIdValues&gt;**](GooglePrivacyDlpV2KMapEstimationQuasiIdValues.md) | Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20. |  [optional] |
|**maxAnonymity** | **String** | Always greater than or equal to min_anonymity. |  [optional] |
|**minAnonymity** | **String** | Always positive. |  [optional] |




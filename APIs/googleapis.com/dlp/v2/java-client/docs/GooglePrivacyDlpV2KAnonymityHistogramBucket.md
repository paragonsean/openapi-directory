

# GooglePrivacyDlpV2KAnonymityHistogramBucket

Histogram of k-anonymity equivalence classes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketSize** | **String** | Total number of equivalence classes in this bucket. |  [optional] |
|**bucketValueCount** | **String** | Total number of distinct equivalence classes in this bucket. |  [optional] |
|**bucketValues** | [**List&lt;GooglePrivacyDlpV2KAnonymityEquivalenceClass&gt;**](GooglePrivacyDlpV2KAnonymityEquivalenceClass.md) | Sample of equivalence classes in this bucket. The total number of classes returned per bucket is capped at 20. |  [optional] |
|**equivalenceClassSizeLowerBound** | **String** | Lower bound on the size of the equivalence classes in this bucket. |  [optional] |
|**equivalenceClassSizeUpperBound** | **String** | Upper bound on the size of the equivalence classes in this bucket. |  [optional] |




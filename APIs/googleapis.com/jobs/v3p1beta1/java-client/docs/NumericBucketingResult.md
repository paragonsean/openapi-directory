

# NumericBucketingResult

Output only. Custom numeric bucketing result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counts** | [**List&lt;BucketizedCount&gt;**](BucketizedCount.md) | Count within each bucket. Its size is the length of NumericBucketingOption.bucket_bounds plus 1. |  [optional] |
|**maxValue** | **Double** | Stores the maximum value of the numeric field. Is populated only if [NumericBucketingOption.requires_min_max] is set to true. |  [optional] |
|**minValue** | **Double** | Stores the minimum value of the numeric field. Will be populated only if [NumericBucketingOption.requires_min_max] is set to true. |  [optional] |




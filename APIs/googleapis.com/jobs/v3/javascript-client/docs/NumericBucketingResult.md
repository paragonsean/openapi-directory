# CloudTalentSolutionApi.NumericBucketingResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**[BucketizedCount]**](BucketizedCount.md) | Count within each bucket. Its size is the length of NumericBucketingOption.bucket_bounds plus 1. | [optional] 
**maxValue** | **Number** | Stores the maximum value of the numeric field. Is populated only if [NumericBucketingOption.requires_min_max] is set to true. | [optional] 
**minValue** | **Number** | Stores the minimum value of the numeric field. Will be populated only if [NumericBucketingOption.requires_min_max] is set to true. | [optional] 



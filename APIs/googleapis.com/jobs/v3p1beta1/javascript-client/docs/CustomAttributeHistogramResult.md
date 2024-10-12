# CloudTalentSolutionApi.CustomAttributeHistogramResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Stores the key of custom attribute the histogram is performed on. | [optional] 
**longValueHistogramResult** | [**NumericBucketingResult**](NumericBucketingResult.md) |  | [optional] 
**stringValueHistogramResult** | **{String: Number}** | Stores a map from the values of string custom field associated with &#x60;key&#x60; to the number of jobs with that value in this histogram result. | [optional] 



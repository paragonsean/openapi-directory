# CloudTalentSolutionApi.CustomAttributeHistogramRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Required. Specifies the custom field key to perform a histogram on. If specified without &#x60;long_value_histogram_bucketing_option&#x60;, histogram on string values of the given &#x60;key&#x60; is triggered, otherwise histogram is performed on long values. | [optional] 
**longValueHistogramBucketingOption** | [**NumericBucketingOption**](NumericBucketingOption.md) |  | [optional] 
**stringValueHistogram** | **Boolean** | Optional. If set to true, the response includes the histogram value for each key as a string. | [optional] 



# CloudTalentSolutionApi.CompensationHistogramRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketingOption** | [**NumericBucketingOption**](NumericBucketingOption.md) |  | [optional] 
**type** | **String** | Required. Type of the request, representing which field the histogramming should be performed over. A single request can only specify one histogram of each &#x60;CompensationHistogramRequestType&#x60;. | [optional] 



## Enum: TypeEnum


* `COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED` (value: `"COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED"`)

* `BASE` (value: `"BASE"`)

* `ANNUALIZED_BASE` (value: `"ANNUALIZED_BASE"`)

* `ANNUALIZED_TOTAL` (value: `"ANNUALIZED_TOTAL"`)





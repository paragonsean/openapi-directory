

# CompensationHistogramRequest

Input only. Compensation based histogram request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketingOption** | [**NumericBucketingOption**](NumericBucketingOption.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of the request, representing which field the histogramming should be performed over. A single request can only specify one histogram of each &#x60;CompensationHistogramRequestType&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED | &quot;COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED&quot; |
| BASE | &quot;BASE&quot; |
| ANNUALIZED_BASE | &quot;ANNUALIZED_BASE&quot; |
| ANNUALIZED_TOTAL | &quot;ANNUALIZED_TOTAL&quot; |






# CompensationHistogramResult

Output only. Compensation based histogram result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**result** | [**NumericBucketingResult**](NumericBucketingResult.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the request, corresponding to CompensationHistogramRequest.type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED | &quot;COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED&quot; |
| BASE | &quot;BASE&quot; |
| ANNUALIZED_BASE | &quot;ANNUALIZED_BASE&quot; |
| ANNUALIZED_TOTAL | &quot;ANNUALIZED_TOTAL&quot; |




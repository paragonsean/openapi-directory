

# ResponseBasedOriginErrorDetectionParameters

The JSON object that contains the properties to determine origin health using real requests/responses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpErrorRanges** | [**List&lt;HttpErrorRangeParameters&gt;**](HttpErrorRangeParameters.md) | The list of Http status code ranges that are considered as server errors for origin and it is marked as unhealthy. |  [optional] |
|**responseBasedDetectedErrorTypes** | [**ResponseBasedDetectedErrorTypesEnum**](#ResponseBasedDetectedErrorTypesEnum) | Type of response errors for real user requests for which origin will be deemed unhealthy |  [optional] |
|**responseBasedFailoverThresholdPercentage** | **Integer** | The percentage of failed requests in the sample where failover should trigger. |  [optional] |



## Enum: ResponseBasedDetectedErrorTypesEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| TCP_ERRORS_ONLY | &quot;TcpErrorsOnly&quot; |
| TCP_AND_HTTP_ERRORS | &quot;TcpAndHttpErrors&quot; |




# NetworkServicesApi.GrpcRouteRetryPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numRetries** | **Number** | Specifies the allowed number of retries. This number must be &gt; 0. If not specified, default to 1. | [optional] 
**retryConditions** | **[String]** | - connect-failure: Router will retry on failures connecting to Backend Services, for example due to connection timeouts. - refused-stream: Router will retry if the backend service resets the stream with a REFUSED_STREAM error code. This reset type indicates that it is safe to retry. - cancelled: Router will retry if the gRPC status code in the response header is set to cancelled - deadline-exceeded: Router will retry if the gRPC status code in the response header is set to deadline-exceeded - resource-exhausted: Router will retry if the gRPC status code in the response header is set to resource-exhausted - unavailable: Router will retry if the gRPC status code in the response header is set to unavailable | [optional] 



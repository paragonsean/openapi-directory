# VertexAiSearchForRetailApi.GoogleCloudRetailLoggingErrorLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**GoogleCloudRetailLoggingErrorContext**](GoogleCloudRetailLoggingErrorContext.md) |  | [optional] 
**importPayload** | [**GoogleCloudRetailLoggingImportErrorContext**](GoogleCloudRetailLoggingImportErrorContext.md) |  | [optional] 
**message** | **String** | A message describing the error. | [optional] 
**requestPayload** | **{String: Object}** | The API request payload, represented as a protocol buffer. Most API request types are supported. For example: \&quot;type.googleapis.com/google.cloud.retail.v2.ProductService.CreateProductRequest\&quot; \&quot;type.googleapis.com/google.cloud.retail.v2.UserEventService.WriteUserEventRequest\&quot; | [optional] 
**responsePayload** | **{String: Object}** | The API response payload, represented as a protocol buffer. This is used to log some \&quot;soft errors\&quot;, where the response is valid but we consider there are some quality issues like unjoined events. The following API responses are supported and no PII is included: \&quot;google.cloud.retail.v2.PredictionService.Predict\&quot; \&quot;google.cloud.retail.v2.UserEventService.WriteUserEvent\&quot; \&quot;google.cloud.retail.v2.UserEventService.CollectUserEvent\&quot; | [optional] 
**serviceContext** | [**GoogleCloudRetailLoggingServiceContext**](GoogleCloudRetailLoggingServiceContext.md) |  | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 



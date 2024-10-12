# DiscoveryEngineApi.GoogleCloudDiscoveryengineLoggingErrorLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**GoogleCloudDiscoveryengineLoggingErrorContext**](GoogleCloudDiscoveryengineLoggingErrorContext.md) |  | [optional] 
**importPayload** | [**GoogleCloudDiscoveryengineLoggingImportErrorContext**](GoogleCloudDiscoveryengineLoggingImportErrorContext.md) |  | [optional] 
**message** | **String** | A message describing the error. | [optional] 
**requestPayload** | **{String: Object}** | The API request payload, represented as a protocol buffer. Most API request types are supported—for example: * &#x60;type.googleapis.com/google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocumentRequest&#x60; * &#x60;type.googleapis.com/google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEventRequest&#x60; | [optional] 
**responsePayload** | **{String: Object}** | The API response payload, represented as a protocol buffer. This is used to log some \&quot;soft errors\&quot;, where the response is valid but we consider there are some quality issues like unjoined events. The following API responses are supported, and no PII is included: * &#x60;google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend&#x60; * &#x60;google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent&#x60; * &#x60;google.cloud.discoveryengine.v1alpha.UserEventService.CollectUserEvent&#x60; | [optional] 
**serviceContext** | [**GoogleCloudDiscoveryengineLoggingServiceContext**](GoogleCloudDiscoveryengineLoggingServiceContext.md) |  | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 



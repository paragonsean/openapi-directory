

# Api

This message defines attributes associated with API operations, such as a network API request. The terminology is based on the conventions used by Google APIs, Istio, and OpenAPI.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | **String** | The API operation name. For gRPC requests, it is the fully qualified API method name, such as \&quot;google.pubsub.v1.Publisher.Publish\&quot;. For OpenAPI requests, it is the &#x60;operationId&#x60;, such as \&quot;getPet\&quot;. |  [optional] |
|**protocol** | **String** | The API protocol used for sending the request, such as \&quot;http\&quot;, \&quot;https\&quot;, \&quot;grpc\&quot;, or \&quot;internal\&quot;. |  [optional] |
|**service** | **String** | The API service name. It is a logical identifier for a networked API, such as \&quot;pubsub.googleapis.com\&quot;. The naming syntax depends on the API management system being used for handling the request. |  [optional] |
|**version** | **String** | The API version associated with the API operation above, such as \&quot;v1\&quot; or \&quot;v1alpha1\&quot;. |  [optional] |




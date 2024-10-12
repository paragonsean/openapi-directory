

# GoogleCloudAiplatformV1beta1PrivateEndpoints

PrivateEndpoints proto is used to provide paths for users to send requests privately. To send request via private service access, use predict_http_uri, explain_http_uri or health_http_uri. To send request via private service connect, use service_attachment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**explainHttpUri** | **String** | Output only. Http(s) path to send explain requests. |  [optional] [readonly] |
|**healthHttpUri** | **String** | Output only. Http(s) path to send health check requests. |  [optional] [readonly] |
|**predictHttpUri** | **String** | Output only. Http(s) path to send prediction requests. |  [optional] [readonly] |
|**serviceAttachment** | **String** | Output only. The name of the service attachment resource. Populated if private service connect is enabled. |  [optional] [readonly] |




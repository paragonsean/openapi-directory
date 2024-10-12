

# GoogleCloudVideointelligenceV1p3beta1StreamingAnnotateVideoResponse

`StreamingAnnotateVideoResponse` is the only message returned to the client by `StreamingAnnotateVideo`. A series of zero or more `StreamingAnnotateVideoResponse` messages are streamed back to the client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationResults** | [**GoogleCloudVideointelligenceV1p3beta1StreamingVideoAnnotationResults**](GoogleCloudVideointelligenceV1p3beta1StreamingVideoAnnotationResults.md) |  |  [optional] |
|**annotationResultsUri** | **String** | Google Cloud Storage URI that stores annotation results of one streaming session in JSON format. It is the annotation_result_storage_directory from the request followed by &#39;/cloud_project_number-session_id&#39;. |  [optional] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |




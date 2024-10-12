

# GoogleCloudVideointelligenceV1beta2AnnotateVideoRequest

Video annotation request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**features** | [**List&lt;FeaturesEnum&gt;**](#List&lt;FeaturesEnum&gt;) | Required. Requested video annotation features. |  [optional] |
|**inputContent** | **byte[]** | The video data bytes. If unset, the input video(s) should be specified via the &#x60;input_uri&#x60;. If set, &#x60;input_uri&#x60; must be unset. |  [optional] |
|**inputUri** | **String** | Input video location. Currently, only [Cloud Storage](https://cloud.google.com/storage/) URIs are supported. URIs must be specified in the following format: &#x60;gs://bucket-id/object-id&#x60; (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/request-endpoints). To identify multiple videos, a video URI may include wildcards in the &#x60;object-id&#x60;. Supported wildcards: &#39;*&#39; to match 0 or more characters; &#39;?&#39; to match 1 character. If unset, the input video should be embedded in the request as &#x60;input_content&#x60;. If set, &#x60;input_content&#x60; must be unset. |  [optional] |
|**locationId** | **String** | Optional. Cloud region where annotation should take place. Supported cloud regions are: &#x60;us-east1&#x60;, &#x60;us-west1&#x60;, &#x60;europe-west1&#x60;, &#x60;asia-east1&#x60;. If no region is specified, the region will be determined based on video file location. |  [optional] |
|**outputUri** | **String** | Optional. Location where the output (in JSON format) should be stored. Currently, only [Cloud Storage](https://cloud.google.com/storage/) URIs are supported. These must be specified in the following format: &#x60;gs://bucket-id/object-id&#x60; (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/request-endpoints). |  [optional] |
|**videoContext** | [**GoogleCloudVideointelligenceV1beta2VideoContext**](GoogleCloudVideointelligenceV1beta2VideoContext.md) |  |  [optional] |



## Enum: List&lt;FeaturesEnum&gt;

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| LABEL_DETECTION | &quot;LABEL_DETECTION&quot; |
| SHOT_CHANGE_DETECTION | &quot;SHOT_CHANGE_DETECTION&quot; |
| EXPLICIT_CONTENT_DETECTION | &quot;EXPLICIT_CONTENT_DETECTION&quot; |
| FACE_DETECTION | &quot;FACE_DETECTION&quot; |
| SPEECH_TRANSCRIPTION | &quot;SPEECH_TRANSCRIPTION&quot; |
| TEXT_DETECTION | &quot;TEXT_DETECTION&quot; |
| OBJECT_TRACKING | &quot;OBJECT_TRACKING&quot; |
| LOGO_RECOGNITION | &quot;LOGO_RECOGNITION&quot; |
| PERSON_DETECTION | &quot;PERSON_DETECTION&quot; |




# VertexAiApi.GoogleCloudAiplatformV1beta1SchemaPredictInstanceVideoObjectTrackingPredictionInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The Google Cloud Storage location of the video on which to perform the prediction. | [optional] 
**mimeType** | **String** | The MIME type of the content of the video. Only the following are supported: video/mp4 video/avi video/quicktime | [optional] 
**timeSegmentEnd** | **String** | The end, exclusive, of the video&#39;s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with \&quot;s\&quot; appended at the end. Fractions are allowed, up to a microsecond precision, and \&quot;inf\&quot; or \&quot;Infinity\&quot; is allowed, which means the end of the video. | [optional] 
**timeSegmentStart** | **String** | The beginning, inclusive, of the video&#39;s time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with \&quot;s\&quot; appended at the end. Fractions are allowed, up to a microsecond precision. | [optional] 



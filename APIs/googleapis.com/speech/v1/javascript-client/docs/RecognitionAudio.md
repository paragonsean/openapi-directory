# CloudSpeechToTextApi.RecognitionAudio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Blob** | The audio data bytes encoded as specified in &#x60;RecognitionConfig&#x60;. Note: as with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64. | [optional] 
**uri** | **String** | URI that points to a file that contains audio data bytes as specified in &#x60;RecognitionConfig&#x60;. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: &#x60;gs://bucket_name/object_name&#x60; (other URI formats return google.rpc.Code.INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/reference-uris). | [optional] 



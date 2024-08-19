# TranscoderApi.Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | A unique key for this input. Must be specified when using advanced mapping and edit lists. | [optional] 
**preprocessingConfig** | [**PreprocessingConfig**](PreprocessingConfig.md) |  | [optional] 
**uri** | **String** | URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, &#x60;gs://bucket/inputs/file.mp4&#x60;). If empty, the value is populated from Job.input_uri. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). | [optional] 



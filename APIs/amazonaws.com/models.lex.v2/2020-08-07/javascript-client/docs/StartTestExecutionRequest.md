# AmazonLexModelBuildingV2.StartTestExecutionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**StartTestExecutionRequestTarget**](StartTestExecutionRequestTarget.md) |  | 
**apiMode** | **String** | Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Runtime API is used. Whereas, for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used. | 
**testExecutionModality** | **String** | Indicates whether audio or text is used. | [optional] 



## Enum: ApiModeEnum


* `Streaming` (value: `"Streaming"`)

* `NonStreaming` (value: `"NonStreaming"`)





## Enum: TestExecutionModalityEnum


* `Text` (value: `"Text"`)

* `Audio` (value: `"Audio"`)





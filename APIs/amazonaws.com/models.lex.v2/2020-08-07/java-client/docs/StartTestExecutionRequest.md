

# StartTestExecutionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**target** | [**StartTestExecutionRequestTarget**](StartTestExecutionRequestTarget.md) |  |  |
|**apiMode** | [**ApiModeEnum**](#ApiModeEnum) | Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Runtime API is used. Whereas, for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used. |  |
|**testExecutionModality** | [**TestExecutionModalityEnum**](#TestExecutionModalityEnum) | Indicates whether audio or text is used. |  [optional] |



## Enum: ApiModeEnum

| Name | Value |
|---- | -----|
| STREAMING | &quot;Streaming&quot; |
| NON_STREAMING | &quot;NonStreaming&quot; |



## Enum: TestExecutionModalityEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;Text&quot; |
| AUDIO | &quot;Audio&quot; |




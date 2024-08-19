

# GoogleCloudAiplatformV1FunctionResponse

The result output from a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function is used as context to the model. This should contain the result of a [FunctionCall] made based on model prediction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The name of the function to call. Matches [FunctionDeclaration.name] and [FunctionCall.name]. |  [optional] |
|**response** | **Map&lt;String, Object&gt;** | Required. The function response in JSON object format. |  [optional] |




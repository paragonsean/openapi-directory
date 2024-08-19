

# GoogleCloudAiplatformV1beta1FunctionCall

A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing the parameters and their values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **Map&lt;String, Object&gt;** | Optional. Required. The function parameters and values in JSON object format. See [FunctionDeclaration.parameters] for parameter details. |  [optional] |
|**name** | **String** | Required. The name of the function to call. Matches [FunctionDeclaration.name]. |  [optional] |




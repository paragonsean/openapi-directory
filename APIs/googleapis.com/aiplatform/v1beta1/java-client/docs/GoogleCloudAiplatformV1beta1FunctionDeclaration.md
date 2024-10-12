

# GoogleCloudAiplatformV1beta1FunctionDeclaration

Structured representation of a function declaration as defined by the [OpenAPI 3.0 specification](https://spec.openapis.org/oas/v3.0.3). Included in this declaration are the function name and parameters. This FunctionDeclaration is a representation of a block of code that can be used as a `Tool` by the model and executed by the client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. Description and purpose of the function. Model uses it to decide how and whether to call the function. |  [optional] |
|**name** | **String** | Required. The name of the function to call. Must start with a letter or an underscore. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. |  [optional] |
|**parameters** | [**GoogleCloudAiplatformV1beta1Schema**](GoogleCloudAiplatformV1beta1Schema.md) |  |  [optional] |




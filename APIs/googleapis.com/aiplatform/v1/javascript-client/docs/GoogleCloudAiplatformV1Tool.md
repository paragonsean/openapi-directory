# VertexAiApi.GoogleCloudAiplatformV1Tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functionDeclarations** | [**[GoogleCloudAiplatformV1FunctionDeclaration]**](GoogleCloudAiplatformV1FunctionDeclaration.md) | Optional. Function tool type. One or more function declarations to be passed to the model along with the current user query. Model may decide to call a subset of these functions by populating FunctionCall in the response. User should provide a FunctionResponse for each function call in the next turn. Based on the function responses, Model will generate the final response back to the user. Maximum 64 function declarations can be provided. | [optional] 



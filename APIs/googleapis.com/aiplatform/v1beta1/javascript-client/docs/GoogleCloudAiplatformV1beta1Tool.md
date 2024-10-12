# VertexAiApi.GoogleCloudAiplatformV1beta1Tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functionDeclarations** | [**[GoogleCloudAiplatformV1beta1FunctionDeclaration]**](GoogleCloudAiplatformV1beta1FunctionDeclaration.md) | Optional. Function tool type. One or more function declarations to be passed to the model along with the current user query. Model may decide to call a subset of these functions by populating FunctionCall in the response. User should provide a FunctionResponse for each function call in the next turn. Based on the function responses, Model will generate the final response back to the user. Maximum 64 function declarations can be provided. | [optional] 
**googleSearchRetrieval** | [**GoogleCloudAiplatformV1beta1GoogleSearchRetrieval**](GoogleCloudAiplatformV1beta1GoogleSearchRetrieval.md) |  | [optional] 
**retrieval** | [**GoogleCloudAiplatformV1beta1Retrieval**](GoogleCloudAiplatformV1beta1Retrieval.md) |  | [optional] 



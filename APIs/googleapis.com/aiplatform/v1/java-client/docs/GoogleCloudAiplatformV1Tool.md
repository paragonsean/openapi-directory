

# GoogleCloudAiplatformV1Tool

Tool details that the model may use to generate response. A `Tool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. A Tool object should contain exactly one type of Tool (e.g FunctionDeclaration, Retrieval or GoogleSearchRetrieval).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**functionDeclarations** | [**List&lt;GoogleCloudAiplatformV1FunctionDeclaration&gt;**](GoogleCloudAiplatformV1FunctionDeclaration.md) | Optional. Function tool type. One or more function declarations to be passed to the model along with the current user query. Model may decide to call a subset of these functions by populating FunctionCall in the response. User should provide a FunctionResponse for each function call in the next turn. Based on the function responses, Model will generate the final response back to the user. Maximum 64 function declarations can be provided. |  [optional] |




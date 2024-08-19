

# GoogleCloudAiplatformV1beta1GenerateContentRequest

Request message for [PredictionService.GenerateContent].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contents** | [**List&lt;GoogleCloudAiplatformV1beta1Content&gt;**](GoogleCloudAiplatformV1beta1Content.md) | Required. The content of the current conversation with the model. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history + latest request. |  [optional] |
|**generationConfig** | [**GoogleCloudAiplatformV1beta1GenerationConfig**](GoogleCloudAiplatformV1beta1GenerationConfig.md) |  |  [optional] |
|**safetySettings** | [**List&lt;GoogleCloudAiplatformV1beta1SafetySetting&gt;**](GoogleCloudAiplatformV1beta1SafetySetting.md) | Optional. Per request settings for blocking unsafe content. Enforced on GenerateContentResponse.candidates. |  [optional] |
|**tools** | [**List&lt;GoogleCloudAiplatformV1beta1Tool&gt;**](GoogleCloudAiplatformV1beta1Tool.md) | Optional. A list of &#x60;Tools&#x60; the model may use to generate the next response. A &#x60;Tool&#x60; is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. |  [optional] |




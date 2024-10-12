# VertexAiApi.GoogleCloudAiplatformV1ExplainResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedModelId** | **String** | ID of the Endpoint&#39;s DeployedModel that served this explanation. | [optional] 
**explanations** | [**[GoogleCloudAiplatformV1Explanation]**](GoogleCloudAiplatformV1Explanation.md) | The explanations of the Model&#39;s PredictResponse.predictions. It has the same number of elements as instances to be explained. | [optional] 
**predictions** | **[Object]** | The predictions that are the output of the predictions call. Same as PredictResponse.predictions. | [optional] 



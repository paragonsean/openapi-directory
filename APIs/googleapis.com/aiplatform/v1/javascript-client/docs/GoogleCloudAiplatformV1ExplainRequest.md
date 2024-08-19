# VertexAiApi.GoogleCloudAiplatformV1ExplainRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedModelId** | **String** | If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding Endpoint.traffic_split. | [optional] 
**explanationSpecOverride** | [**GoogleCloudAiplatformV1ExplanationSpecOverride**](GoogleCloudAiplatformV1ExplanationSpecOverride.md) |  | [optional] 
**instances** | **[Object]** | Required. The instances that are the input to the explanation call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the explanation call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint&#39;s DeployedModels&#39; Model&#39;s PredictSchemata&#39;s instance_schema_uri. | [optional] 
**parameters** | **Object** | The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint&#39;s DeployedModels&#39; Model&#39;s PredictSchemata&#39;s parameters_schema_uri. | [optional] 



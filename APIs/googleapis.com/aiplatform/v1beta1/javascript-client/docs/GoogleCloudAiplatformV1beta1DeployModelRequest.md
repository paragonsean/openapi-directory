# VertexAiApi.GoogleCloudAiplatformV1beta1DeployModelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedModel** | [**GoogleCloudAiplatformV1beta1DeployedModel**](GoogleCloudAiplatformV1beta1DeployedModel.md) |  | [optional] 
**trafficSplit** | **{String: Number}** | A map from a DeployedModel&#39;s ID to the percentage of this Endpoint&#39;s traffic that should be forwarded to that DeployedModel. If this field is non-empty, then the Endpoint&#39;s traffic_split will be overwritten with it. To refer to the ID of the just being deployed Model, a \&quot;0\&quot; should be used, and the actual ID of the new DeployedModel will be filled in its place by this method. The traffic percentage values must add up to 100. If this field is empty, then the Endpoint&#39;s traffic_split is not updated. | [optional] 



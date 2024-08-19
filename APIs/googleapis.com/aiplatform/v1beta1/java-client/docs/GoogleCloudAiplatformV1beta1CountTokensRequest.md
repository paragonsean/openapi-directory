

# GoogleCloudAiplatformV1beta1CountTokensRequest

Request message for PredictionService.CountTokens.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contents** | [**List&lt;GoogleCloudAiplatformV1beta1Content&gt;**](GoogleCloudAiplatformV1beta1Content.md) | Required. Input content. |  [optional] |
|**instances** | **List&lt;Object&gt;** | Required. The instances that are the input to token counting call. Schema is identical to the prediction schema of the underlying model. |  [optional] |
|**model** | **String** | Required. The name of the publisher model requested to serve the prediction. Format: &#x60;projects/{project}/locations/{location}/publishers/_*_/models/_*&#x60; |  [optional] |




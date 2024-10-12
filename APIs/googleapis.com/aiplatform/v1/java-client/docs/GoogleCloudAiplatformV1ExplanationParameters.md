

# GoogleCloudAiplatformV1ExplanationParameters

Parameters to configure explaining for Model's predictions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**examples** | [**GoogleCloudAiplatformV1Examples**](GoogleCloudAiplatformV1Examples.md) |  |  [optional] |
|**integratedGradientsAttribution** | [**GoogleCloudAiplatformV1IntegratedGradientsAttribution**](GoogleCloudAiplatformV1IntegratedGradientsAttribution.md) |  |  [optional] |
|**outputIndices** | **List&lt;Object&gt;** | If populated, only returns attributions that have output_index contained in output_indices. It must be an ndarray of integers, with the same shape of the output it&#39;s explaining. If not populated, returns attributions for top_k indices of outputs. If neither top_k nor output_indices is populated, returns the argmax index of the outputs. Only applicable to Models that predict multiple outputs (e,g, multi-class Models that predict multiple classes). |  [optional] |
|**sampledShapleyAttribution** | [**GoogleCloudAiplatformV1SampledShapleyAttribution**](GoogleCloudAiplatformV1SampledShapleyAttribution.md) |  |  [optional] |
|**topK** | **Integer** | If populated, returns attributions for top K indices of outputs (defaults to 1). Only applies to Models that predicts more than one outputs (e,g, multi-class Models). When set to -1, returns explanations for all outputs. |  [optional] |
|**xraiAttribution** | [**GoogleCloudAiplatformV1XraiAttribution**](GoogleCloudAiplatformV1XraiAttribution.md) |  |  [optional] |




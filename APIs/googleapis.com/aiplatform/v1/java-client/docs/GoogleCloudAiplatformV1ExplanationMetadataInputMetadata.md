

# GoogleCloudAiplatformV1ExplanationMetadataInputMetadata

Metadata of the input of a feature. Fields other than InputMetadata.input_baselines are applicable only for Models that are using Vertex AI-provided images for Tensorflow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**denseShapeTensorName** | **String** | Specifies the shape of the values of the input if the input is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. |  [optional] |
|**encodedBaselines** | **List&lt;Object&gt;** | A list of baselines for the encoded tensor. The shape of each baseline should match the shape of the encoded tensor. If a scalar is provided, Vertex AI broadcasts to the same shape as the encoded tensor. |  [optional] |
|**encodedTensorName** | **String** | Encoded tensor is a transformation of the input tensor. Must be provided if choosing Integrated Gradients attribution or XRAI attribution and the input tensor is not differentiable. An encoded tensor is generated if the input tensor is encoded by a lookup table. |  [optional] |
|**encoding** | [**EncodingEnum**](#EncodingEnum) | Defines how the feature is encoded into the input tensor. Defaults to IDENTITY. |  [optional] |
|**featureValueDomain** | [**GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain**](GoogleCloudAiplatformV1ExplanationMetadataInputMetadataFeatureValueDomain.md) |  |  [optional] |
|**groupName** | **String** | Name of the group that the input belongs to. Features with the same group name will be treated as one feature when computing attributions. Features grouped together can have different shapes in value. If provided, there will be one single attribution generated in Attribution.feature_attributions, keyed by the group name. |  [optional] |
|**indexFeatureMapping** | **List&lt;String&gt;** | A list of feature names for each index in the input tensor. Required when the input InputMetadata.encoding is BAG_OF_FEATURES, BAG_OF_FEATURES_SPARSE, INDICATOR. |  [optional] |
|**indicesTensorName** | **String** | Specifies the index of the values of the input tensor. Required when the input tensor is a sparse representation. Refer to Tensorflow documentation for more details: https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor. |  [optional] |
|**inputBaselines** | **List&lt;Object&gt;** | Baseline inputs for this feature. If no baseline is specified, Vertex AI chooses the baseline for this feature. If multiple baselines are specified, Vertex AI returns the average attributions across them in Attribution.feature_attributions. For Vertex AI-provided Tensorflow images (both 1.x and 2.x), the shape of each baseline must match the shape of the input tensor. If a scalar is provided, we broadcast to the same shape as the input tensor. For custom images, the element of the baselines must be in the same format as the feature&#39;s input in the instance[]. The schema of any single instance may be specified via Endpoint&#39;s DeployedModels&#39; Model&#39;s PredictSchemata&#39;s instance_schema_uri. |  [optional] |
|**inputTensorName** | **String** | Name of the input tensor for this feature. Required and is only applicable to Vertex AI-provided images for Tensorflow. |  [optional] |
|**modality** | **String** | Modality of the feature. Valid values are: numeric, image. Defaults to numeric. |  [optional] |
|**visualization** | [**GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization**](GoogleCloudAiplatformV1ExplanationMetadataInputMetadataVisualization.md) |  |  [optional] |



## Enum: EncodingEnum

| Name | Value |
|---- | -----|
| ENCODING_UNSPECIFIED | &quot;ENCODING_UNSPECIFIED&quot; |
| IDENTITY | &quot;IDENTITY&quot; |
| BAG_OF_FEATURES | &quot;BAG_OF_FEATURES&quot; |
| BAG_OF_FEATURES_SPARSE | &quot;BAG_OF_FEATURES_SPARSE&quot; |
| INDICATOR | &quot;INDICATOR&quot; |
| COMBINED_EMBEDDING | &quot;COMBINED_EMBEDDING&quot; |
| CONCAT_EMBEDDING | &quot;CONCAT_EMBEDDING&quot; |




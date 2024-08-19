

# GoogleCloudAiplatformV1SchemaTextPromptDatasetMetadata

The metadata of Datasets that contain Text Prompt data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidateCount** | **String** | Number of candidates. |  [optional] |
|**gcsUri** | **String** | The Google Cloud Storage URI that stores the prompt data. |  [optional] |
|**groundingConfig** | [**GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfig**](GoogleCloudAiplatformV1SchemaPredictParamsGroundingConfig.md) |  |  [optional] |
|**maxOutputTokens** | **String** | Value of the maximum number of tokens generated set when the dataset was saved. |  [optional] |
|**note** | **String** | User-created prompt note. Note size limit is 2KB. |  [optional] |
|**promptType** | **String** | Type of the prompt dataset. |  [optional] |
|**stopSequences** | **List&lt;String&gt;** | Customized stop sequences. |  [optional] |
|**temperature** | **Float** | Temperature value used for sampling set when the dataset was saved. This value is used to tune the degree of randomness. |  [optional] |
|**text** | **String** | The content of the prompt dataset. |  [optional] |
|**topK** | **String** | Top K value set when the dataset was saved. This value determines how many candidates with highest probability from the vocab would be selected for each decoding step. |  [optional] |
|**topP** | **Float** | Top P value set when the dataset was saved. Given topK tokens for decoding, top candidates will be selected until the sum of their probabilities is topP. |  [optional] |




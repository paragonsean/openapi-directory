

# TranslationModelMetadata

Model metadata that is specific to translation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseModel** | **String** | The resource name of the model to use as a baseline to train the custom model. If unset, we use the default base model provided by Google Translate. Format: &#x60;projects/{project_id}/locations/{location_id}/models/{model_id}&#x60; |  [optional] |
|**sourceLanguageCode** | **String** | Output only. Inferred from the dataset. The source languge (The BCP-47 language code) that is used for training. |  [optional] |
|**targetLanguageCode** | **String** | Output only. The target languge (The BCP-47 language code) that is used for training. |  [optional] |




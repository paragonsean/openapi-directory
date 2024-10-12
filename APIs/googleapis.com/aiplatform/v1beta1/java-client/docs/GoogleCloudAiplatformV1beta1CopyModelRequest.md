

# GoogleCloudAiplatformV1beta1CopyModelRequest

Request message for ModelService.CopyModel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  |  [optional] |
|**modelId** | **String** | Optional. Copy source_model into a new Model with this ID. The ID will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are &#x60;[a-z0-9_-]&#x60;. The first character cannot be a number or hyphen. |  [optional] |
|**parentModel** | **String** | Optional. Specify this field to copy source_model into this existing Model as a new version. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60; |  [optional] |
|**sourceModel** | **String** | Required. The resource name of the Model to copy. That Model must be in the same Project. Format: &#x60;projects/{project}/locations/{location}/models/{model}&#x60; |  [optional] |




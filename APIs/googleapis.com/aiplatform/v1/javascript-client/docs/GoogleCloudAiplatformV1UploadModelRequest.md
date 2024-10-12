# VertexAiApi.GoogleCloudAiplatformV1UploadModelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**GoogleCloudAiplatformV1Model**](GoogleCloudAiplatformV1Model.md) |  | [optional] 
**modelId** | **String** | Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are &#x60;[a-z0-9_-]&#x60;. The first character cannot be a number or hyphen. | [optional] 
**parentModel** | **String** | Optional. The resource name of the model into which to upload the version. Only specify this field when uploading a new version. | [optional] 
**serviceAccount** | **String** | Optional. The user-provided custom service account to use to do the model upload. If empty, [Vertex AI Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) will be used to access resources needed to upload the model. This account must belong to the target project where the model is uploaded to, i.e., the project specified in the &#x60;parent&#x60; field of this request and have necessary read permissions (to Google Cloud Storage, Artifact Registry, etc.). | [optional] 



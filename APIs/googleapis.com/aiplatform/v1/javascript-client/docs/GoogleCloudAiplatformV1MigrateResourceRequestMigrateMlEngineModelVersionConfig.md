# VertexAiApi.GoogleCloudAiplatformV1MigrateResourceRequestMigrateMlEngineModelVersionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **String** | Required. The ml.googleapis.com endpoint that this model version should be migrated from. Example values: * ml.googleapis.com * us-centrall-ml.googleapis.com * europe-west4-ml.googleapis.com * asia-east1-ml.googleapis.com | [optional] 
**modelDisplayName** | **String** | Required. Display name of the model in Vertex AI. System will pick a display name if unspecified. | [optional] 
**modelVersion** | **String** | Required. Full resource name of ml engine model version. Format: &#x60;projects/{project}/models/{model}/versions/{version}&#x60;. | [optional] 



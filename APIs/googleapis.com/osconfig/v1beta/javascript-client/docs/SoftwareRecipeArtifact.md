# OsConfigApi.SoftwareRecipeArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowInsecure** | **Boolean** | Defaults to false. When false, recipes are subject to validations based on the artifact type: Remote: A checksum must be specified, and only protocols with transport-layer security are permitted. GCS: An object generation number must be specified. | [optional] 
**gcs** | [**SoftwareRecipeArtifactGcs**](SoftwareRecipeArtifactGcs.md) |  | [optional] 
**id** | **String** | Required. Id of the artifact, which the installation and update steps of this recipe can reference. Artifacts in a recipe cannot have the same id. | [optional] 
**remote** | [**SoftwareRecipeArtifactRemote**](SoftwareRecipeArtifactRemote.md) |  | [optional] 



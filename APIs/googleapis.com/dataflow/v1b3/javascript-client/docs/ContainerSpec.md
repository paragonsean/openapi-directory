# DataflowApi.ContainerSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultEnvironment** | [**FlexTemplateRuntimeEnvironment**](FlexTemplateRuntimeEnvironment.md) |  | [optional] 
**image** | **String** | Name of the docker container image. E.g., gcr.io/project/some-image | [optional] 
**imageRepositoryCertPath** | **String** | Cloud Storage path to self-signed certificate of private registry. | [optional] 
**imageRepositoryPasswordSecretId** | **String** | Secret Manager secret id for password to authenticate to private registry. | [optional] 
**imageRepositoryUsernameSecretId** | **String** | Secret Manager secret id for username to authenticate to private registry. | [optional] 
**metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  | [optional] 
**sdkInfo** | [**SDKInfo**](SDKInfo.md) |  | [optional] 



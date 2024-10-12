# CloudRunAdminApi.GoogleCloudRunV2ContainerOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **[String]** | Optional. Arguments to the entrypoint. Will replace existing args for override. | [optional] 
**clearArgs** | **Boolean** | Optional. True if the intention is to clear out existing args list. | [optional] 
**env** | [**[GoogleCloudRunV2EnvVar]**](GoogleCloudRunV2EnvVar.md) | List of environment variables to set in the container. Will be merged with existing env for override. | [optional] 
**name** | **String** | The name of the container specified as a DNS_LABEL. | [optional] 



# CloudSourceRepositoriesApi.ProjectConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enablePrivateKeyCheck** | **Boolean** | Reject a Git push that contains a private key. | [optional] 
**name** | **String** | The name of the project. Values are of the form &#x60;projects/&#x60;. | [optional] 
**pubsubConfigs** | [**{String: PubsubConfig}**](PubsubConfig.md) | How this project publishes a change in the repositories through Cloud Pub/Sub. Keyed by the topic names. | [optional] 



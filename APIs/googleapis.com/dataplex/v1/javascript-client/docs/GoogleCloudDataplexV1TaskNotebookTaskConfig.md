# CloudDataplexApi.GoogleCloudDataplexV1TaskNotebookTaskConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveUris** | **[String]** | Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. | [optional] 
**fileUris** | **[String]** | Optional. Cloud Storage URIs of files to be placed in the working directory of each executor. | [optional] 
**infrastructureSpec** | [**GoogleCloudDataplexV1TaskInfrastructureSpec**](GoogleCloudDataplexV1TaskInfrastructureSpec.md) |  | [optional] 
**notebook** | **String** | Required. Path to input notebook. This can be the Cloud Storage URI of the notebook file or the path to a Notebook Content. The execution args are accessible as environment variables (TASK_key&#x3D;value). | [optional] 



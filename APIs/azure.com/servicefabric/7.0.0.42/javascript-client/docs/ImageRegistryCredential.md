# ServiceFabricClientApis.ImageRegistryCredential

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **String** | The password for the private registry. The password is required for create or update operations, however it is not returned in the get or list operations. Will be processed based on the type provided. | [optional] 
**passwordType** | [**ImageRegistryPasswordType**](ImageRegistryPasswordType.md) |  | [optional] 
**server** | **String** | Docker image registry server, without protocol such as &#x60;http&#x60; and &#x60;https&#x60;. | 
**username** | **String** | The username for the private registry. | 



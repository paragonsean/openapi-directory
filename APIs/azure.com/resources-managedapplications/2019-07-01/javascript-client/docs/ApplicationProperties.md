# ApplicationClient.ApplicationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationDefinitionId** | **String** | The fully qualified path of managed application definition Id. | [optional] 
**artifacts** | [**[ApplicationArtifact]**](ApplicationArtifact.md) | The collection of managed application artifacts. | [optional] [readonly] 
**authorizations** | [**[ApplicationAuthorization]**](ApplicationAuthorization.md) | The  read-only authorizations property that is retrieved from the application package. | [optional] [readonly] 
**billingDetails** | [**ApplicationBillingDetailsDefinition**](ApplicationBillingDetailsDefinition.md) |  | [optional] 
**createdBy** | [**ApplicationClientDetails**](ApplicationClientDetails.md) |  | [optional] 
**customerSupport** | [**ApplicationPackageContact**](ApplicationPackageContact.md) |  | [optional] 
**jitAccessPolicy** | [**ApplicationJitAccessPolicy**](ApplicationJitAccessPolicy.md) |  | [optional] 
**managedResourceGroupId** | **String** | The managed resource group Id. | [optional] 
**managementMode** | [**ApplicationManagementMode**](ApplicationManagementMode.md) |  | [optional] 
**outputs** | **Object** | Name and value pairs that define the managed application outputs. | [optional] [readonly] 
**parameters** | **Object** | Name and value pairs that define the managed application parameters. It can be a JObject or a well formed JSON string. | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**publisherTenantId** | **String** | The publisher tenant Id. | [optional] [readonly] 
**supportUrls** | [**ApplicationPackageSupportUrls**](ApplicationPackageSupportUrls.md) |  | [optional] 
**updatedBy** | [**ApplicationClientDetails**](ApplicationClientDetails.md) |  | [optional] 



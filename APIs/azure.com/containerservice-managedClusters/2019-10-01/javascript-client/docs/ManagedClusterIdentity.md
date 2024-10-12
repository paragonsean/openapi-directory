# ContainerServiceClient.ManagedClusterIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principalId** | **String** | The principal id of the system assigned identity which is used by master components. | [optional] [readonly] 
**tenantId** | **String** | The tenant id of the system assigned identity which is used by master components. | [optional] [readonly] 
**type** | **String** | The type of identity used for the managed cluster. Type &#39;SystemAssigned&#39; will use an implicitly created identity in master components and an auto-created user assigned identity in MC_ resource group in agent nodes. Type &#39;None&#39; will not use MSI for the managed cluster, service principal will be used instead. | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `None` (value: `"None"`)





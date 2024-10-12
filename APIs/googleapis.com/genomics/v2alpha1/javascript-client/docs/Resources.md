# GenomicsApi.Resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projectId** | **String** | The project ID to allocate resources in. | [optional] 
**regions** | **[String]** | The list of regions allowed for VM allocation. If set, the &#x60;zones&#x60; field must not be set. | [optional] 
**virtualMachine** | [**VirtualMachine**](VirtualMachine.md) |  | [optional] 
**zones** | **[String]** | The list of zones allowed for VM allocation. If set, the &#x60;regions&#x60; field must not be set. | [optional] 



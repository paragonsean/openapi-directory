# BareMetalSolutionApi.InstanceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientNetwork** | [**NetworkAddress**](NetworkAddress.md) |  | [optional] 
**hyperthreading** | **Boolean** | Whether the instance should be provisioned with Hyperthreading enabled. | [optional] 
**id** | **String** | A transient unique identifier to idenfity an instance within an ProvisioningConfig request. | [optional] 
**instanceType** | **String** | Instance type. | [optional] 
**location** | **String** | Location where to deploy the instance. | [optional] 
**osImage** | **String** | OS image to initialize the instance. | [optional] 
**privateNetwork** | [**NetworkAddress**](NetworkAddress.md) |  | [optional] 
**userNote** | **String** | User note field, it can be used by customers to add additional information for the BMS Ops team (b/194021617). | [optional] 



# InstanceMetadataClient.Compute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azEnvironment** | **String** | This is the name of the environment in which the VM is running. | [optional] 
**location** | **String** | This is the Azure Region in which the VM is running. | [optional] 
**name** | **String** | This is the name of the VM. | [optional] 
**offer** | **String** | This is the offer information for the VM image. This value is only present for images deployed from the Azure Image Gallery. | [optional] 
**osType** | **String** | This value indicates the type of OS the VM is running, either Linux or Windows. | [optional] 
**placementGroupId** | **String** | This is the placement group of your Virtual Machine Scale Set. | [optional] 
**plan** | [**PlanProperties**](PlanProperties.md) |  | [optional] 
**platformFaultDomain** | **String** | This is the fault domain in which the VM. | [optional] 
**platformUpdateDomain** | **String** | This is the update domain in which the VM. | [optional] 
**provider** | **String** | This is the provider of the VM. | [optional] 
**publicKeys** | [**[PublicKeysProperties]**](PublicKeysProperties.md) | This is information about the SSH certificate | [optional] 
**publisher** | **String** | This is the publisher of the VM image. | [optional] 
**resourceGroupName** | **String** | This is the resource group for the VM. | [optional] 
**sku** | **String** | This is the specific SKU for the VM image. | [optional] 
**subscriptionId** | **String** | This is the Azure subscription for the VM. | [optional] 
**tags** | **String** | This is the list of tags for your VM. | [optional] 
**version** | **String** | This is the version of the VM image. | [optional] 
**vmId** | **String** | This is the unique identifier for the VM. | [optional] 
**vmScaleSetName** | **String** | This is the resource name of the VMSS. | [optional] 
**vmSize** | **String** | This is the size of the VM. | [optional] 
**zone** | **String** | This is the availability zone of the VM. | [optional] 



# BatchService.ImageReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | **String** | For example, UbuntuServer or WindowsServer. | [optional] 
**publisher** | **String** | For example, Canonical or MicrosoftWindowsServer. | [optional] 
**sku** | **String** | For example, 18.04-LTS or 2019-Datacenter. | [optional] 
**version** | **String** | A value of &#39;latest&#39; can be specified to select the latest version of an Image. If omitted, the default is &#39;latest&#39;. | [optional] 
**virtualMachineImageId** | **String** | This property is mutually exclusive with other ImageReference properties. For Virtual Machine Image it must be in the same region and subscription as the Azure Batch account. For SIG image it must have replicas in the same region as the Azure Batch account. For information about the firewall settings for the Batch Compute Node agent to communicate with the Batch service see https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration. | [optional] 



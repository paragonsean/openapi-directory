# BatchService.VirtualMachineConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imageReference** | [**ImageReference**](ImageReference.md) |  | 
**nodeAgentSKUId** | **String** | The SKU of Batch Node Agent to be provisioned on the compute node. The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems. | 
**windowsConfiguration** | [**WindowsConfiguration**](WindowsConfiguration.md) |  | [optional] 



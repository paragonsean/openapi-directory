

# VirtualMachineConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageReference** | [**ImageReference**](ImageReference.md) |  |  [optional] |
|**nodeAgentSKUId** | **String** | The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems. You must specify a node agent SKU which matches the selected image reference. To get the list of supported node agent SKUs along with their list of verified image references, see the &#39;List supported node agent SKUs&#39; operation. |  |
|**osDisk** | [**OSDisk**](OSDisk.md) |  |  [optional] |
|**windowsConfiguration** | [**WindowsConfiguration**](WindowsConfiguration.md) |  |  [optional] |




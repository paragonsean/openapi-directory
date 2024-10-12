

# VirtualMachineConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerConfiguration** | [**ContainerConfiguration**](ContainerConfiguration.md) |  |  [optional] |
|**dataDisks** | [**List&lt;DataDisk&gt;**](DataDisk.md) | This property must be specified if the compute nodes in the pool need to have empty data disks attached to them. This cannot be updated. Each node gets its own disk (the disk is not a file share). Existing disks cannot be attached, each attached disk is empty. When the node is removed from the pool, the disk and all data associated with it is also deleted. The disk is not formatted after being attached, it must be formatted before use - for more information see https://docs.microsoft.com/en-us/azure/virtual-machines/linux/classic/attach-disk#initialize-a-new-data-disk-in-linux and https://docs.microsoft.com/en-us/azure/virtual-machines/windows/attach-disk-ps#add-an-empty-data-disk-to-a-virtual-machine. |  [optional] |
|**imageReference** | [**ImageReference**](ImageReference.md) |  |  |
|**licenseType** | **String** | This only applies to images that contain the Windows operating system, and should only be used when you hold valid on-premises licenses for the nodes which will be deployed. If omitted, no on-premises licensing discount is applied. Values are:   Windows_Server - The on-premises license is for Windows Server.  Windows_Client - The on-premises license is for Windows Client.  |  [optional] |
|**nodeAgentSKUId** | **String** | The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems. You must specify a node agent SKU which matches the selected image reference. To get the list of supported node agent SKUs along with their list of verified image references, see the &#39;List supported node agent SKUs&#39; operation. |  |
|**osDisk** | [**OSDisk**](OSDisk.md) |  |  [optional] |
|**windowsConfiguration** | [**WindowsConfiguration**](WindowsConfiguration.md) |  |  [optional] |




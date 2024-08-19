# BatchManagement.VirtualMachineConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerConfiguration** | [**ContainerConfiguration**](ContainerConfiguration.md) |  | [optional] 
**dataDisks** | [**[DataDisk]**](DataDisk.md) | This property must be specified if the compute nodes in the pool need to have empty data disks attached to them. | [optional] 
**imageReference** | [**ImageReference**](ImageReference.md) |  | 
**licenseType** | **String** | This only applies to images that contain the Windows operating system, and should only be used when you hold valid on-premises licenses for the nodes which will be deployed. If omitted, no on-premises licensing discount is applied. Values are:   Windows_Server - The on-premises license is for Windows Server.  Windows_Client - The on-premises license is for Windows Client.  | [optional] 
**nodeAgentSkuId** | **String** | The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems. You must specify a node agent SKU which matches the selected image reference. To get the list of supported node agent SKUs along with their list of verified image references, see the &#39;List supported node agent SKUs&#39; operation. | 
**windowsConfiguration** | [**WindowsConfiguration**](WindowsConfiguration.md) |  | [optional] 



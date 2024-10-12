# ComputeManagementClient.ImageStorageProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataDisks** | [**[ImageDataDisk]**](ImageDataDisk.md) | Specifies the parameters that are used to add a data disk to a virtual machine. &lt;br&gt;&lt;br&gt; For more information about disks, see [About disks and VHDs for Azure virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc&#x3D;%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). | [optional] 
**osDisk** | [**ImageOSDisk**](ImageOSDisk.md) |  | [optional] 
**zoneResilient** | **Boolean** | Specifies whether an image is zone resilient or not. Default is false. Zone resilient images can be created only in regions that provide Zone Redundant Storage (ZRS). | [optional] 



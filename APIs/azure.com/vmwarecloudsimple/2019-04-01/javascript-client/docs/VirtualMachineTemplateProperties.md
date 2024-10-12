# VMwareCloudSimple.VirtualMachineTemplateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountOfRam** | **Number** | The amount of memory | [optional] 
**controllers** | [**[VirtualDiskController]**](VirtualDiskController.md) | The list of Virtual Disk Controllers | [optional] 
**description** | **String** | The description of Virtual Machine Template | [optional] 
**disks** | [**[VirtualDisk]**](VirtualDisk.md) | The list of Virtual Disks | [optional] 
**exposeToGuestVM** | **Boolean** | Expose Guest OS or not | [optional] 
**guestOS** | **String** | The Guest OS | [optional] [readonly] 
**guestOSType** | **String** | The Guest OS types | [optional] [readonly] 
**nics** | [**[VirtualNic]**](VirtualNic.md) | The list of Virtual NICs | [optional] 
**numberOfCores** | **Number** | The number of CPU cores | [optional] 
**path** | **String** | path to folder | [optional] 
**privateCloudId** | **String** | The Private Cloud Id | 
**vSphereNetworks** | **[String]** | The list of VSphere networks | [optional] 
**vSphereTags** | **[String]** | The tags from VSphere | [optional] 
**vmwaretools** | **String** | The VMware tools version | [optional] [readonly] 



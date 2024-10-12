

# VirtualMachineTemplateProperties

Properties of virtual machine template

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountOfRam** | **Integer** | The amount of memory |  [optional] |
|**controllers** | [**List&lt;VirtualDiskController&gt;**](VirtualDiskController.md) | The list of Virtual Disk Controllers |  [optional] |
|**description** | **String** | The description of Virtual Machine Template |  [optional] |
|**disks** | [**List&lt;VirtualDisk&gt;**](VirtualDisk.md) | The list of Virtual Disks |  [optional] |
|**exposeToGuestVM** | **Boolean** | Expose Guest OS or not |  [optional] |
|**guestOS** | **String** | The Guest OS |  [optional] [readonly] |
|**guestOSType** | **String** | The Guest OS types |  [optional] [readonly] |
|**nics** | [**List&lt;VirtualNic&gt;**](VirtualNic.md) | The list of Virtual NICs |  [optional] |
|**numberOfCores** | **Integer** | The number of CPU cores |  [optional] |
|**path** | **String** | path to folder |  [optional] |
|**privateCloudId** | **String** | The Private Cloud Id |  |
|**vSphereNetworks** | **List&lt;String&gt;** | The list of VSphere networks |  [optional] |
|**vSphereTags** | **List&lt;String&gt;** | The tags from VSphere |  [optional] |
|**vmwaretools** | **String** | The VMware tools version |  [optional] [readonly] |




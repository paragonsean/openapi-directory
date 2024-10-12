# VMwareCloudSimple.VirtualMachineProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountOfRam** | **Number** | The amount of memory | 
**controllers** | [**[VirtualDiskController]**](VirtualDiskController.md) | The list of Virtual Disks&#39; Controllers | [optional] [readonly] 
**customization** | [**GuestOSCustomization**](GuestOSCustomization.md) |  | [optional] 
**disks** | [**[VirtualDisk]**](VirtualDisk.md) | The list of Virtual Disks | [optional] 
**dnsname** | **String** | The DNS name of Virtual Machine in VCenter | [optional] [readonly] 
**exposeToGuestVM** | **Boolean** | Expose Guest OS or not | [optional] 
**folder** | **String** | The path to virtual machine folder in VCenter | [optional] [readonly] 
**guestOS** | **String** | The name of Guest OS | [optional] [readonly] 
**guestOSType** | **String** | The Guest OS type | [optional] [readonly] 
**nics** | [**[VirtualNic]**](VirtualNic.md) | The list of Virtual NICs | [optional] 
**numberOfCores** | **Number** | The number of CPU cores | 
**password** | **String** | Password for login. Deprecated - use customization property | [optional] 
**privateCloudId** | **String** | Private Cloud Id | 
**provisioningState** | **String** | The provisioning status of the resource | [optional] [readonly] 
**publicIP** | **String** | The public ip of Virtual Machine | [optional] [readonly] 
**resourcePool** | [**ResourcePool**](ResourcePool.md) |  | [optional] 
**status** | **String** | The status of Virtual machine | [optional] [readonly] 
**templateId** | **String** | Virtual Machine Template Id | [optional] 
**username** | **String** | Username for login. Deprecated - use customization property | [optional] 
**vSphereNetworks** | **[String]** | The list of Virtual VSphere Networks | [optional] 
**vmId** | **String** | The internal id of Virtual Machine in VCenter | [optional] [readonly] 
**vmwaretools** | **String** | VMware tools version | [optional] [readonly] 



## Enum: GuestOSTypeEnum


* `linux` (value: `"linux"`)

* `windows` (value: `"windows"`)

* `other` (value: `"other"`)





## Enum: StatusEnum


* `running` (value: `"running"`)

* `suspended` (value: `"suspended"`)

* `poweredoff` (value: `"poweredoff"`)

* `updating` (value: `"updating"`)

* `deallocating` (value: `"deallocating"`)

* `deleting` (value: `"deleting"`)







# VirtualMachineProperties

Properties of virtual machine

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountOfRam** | **Integer** | The amount of memory |  |
|**controllers** | [**List&lt;VirtualDiskController&gt;**](VirtualDiskController.md) | The list of Virtual Disks&#39; Controllers |  [optional] [readonly] |
|**customization** | [**GuestOSCustomization**](GuestOSCustomization.md) |  |  [optional] |
|**disks** | [**List&lt;VirtualDisk&gt;**](VirtualDisk.md) | The list of Virtual Disks |  [optional] |
|**dnsname** | **String** | The DNS name of Virtual Machine in VCenter |  [optional] [readonly] |
|**exposeToGuestVM** | **Boolean** | Expose Guest OS or not |  [optional] |
|**folder** | **String** | The path to virtual machine folder in VCenter |  [optional] [readonly] |
|**guestOS** | **String** | The name of Guest OS |  [optional] [readonly] |
|**guestOSType** | [**GuestOSTypeEnum**](#GuestOSTypeEnum) | The Guest OS type |  [optional] [readonly] |
|**nics** | [**List&lt;VirtualNic&gt;**](VirtualNic.md) | The list of Virtual NICs |  [optional] |
|**numberOfCores** | **Integer** | The number of CPU cores |  |
|**password** | **String** | Password for login. Deprecated - use customization property |  [optional] |
|**privateCloudId** | **String** | Private Cloud Id |  |
|**provisioningState** | **String** | The provisioning status of the resource |  [optional] [readonly] |
|**publicIP** | **String** | The public ip of Virtual Machine |  [optional] [readonly] |
|**resourcePool** | [**ResourcePool**](ResourcePool.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of Virtual machine |  [optional] [readonly] |
|**templateId** | **String** | Virtual Machine Template Id |  [optional] |
|**username** | **String** | Username for login. Deprecated - use customization property |  [optional] |
|**vSphereNetworks** | **List&lt;String&gt;** | The list of Virtual VSphere Networks |  [optional] |
|**vmId** | **String** | The internal id of Virtual Machine in VCenter |  [optional] [readonly] |
|**vmwaretools** | **String** | VMware tools version |  [optional] [readonly] |



## Enum: GuestOSTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;linux&quot; |
| WINDOWS | &quot;windows&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| SUSPENDED | &quot;suspended&quot; |
| POWEREDOFF | &quot;poweredoff&quot; |
| UPDATING | &quot;updating&quot; |
| DEALLOCATING | &quot;deallocating&quot; |
| DELETING | &quot;deleting&quot; |




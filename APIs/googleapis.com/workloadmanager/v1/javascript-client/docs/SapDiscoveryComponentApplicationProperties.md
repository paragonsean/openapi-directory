# WorkloadManagerApi.SapDiscoveryComponentApplicationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abap** | **Boolean** | Optional. Indicates whether this is a Java or ABAP Netweaver instance. true means it is ABAP, false means it is Java. | [optional] 
**applicationType** | **String** | Required. Type of the application. Netweaver, etc. | [optional] 
**ascsUri** | **String** | Optional. Resource URI of the recognized ASCS host of the application. | [optional] 
**kernelVersion** | **String** | Optional. Kernel version for Netweaver running in the system. | [optional] 
**nfsUri** | **String** | Optional. Resource URI of the recognized shared NFS of the application. May be empty if the application server has only a single node. | [optional] 



## Enum: ApplicationTypeEnum


* `APPLICATION_TYPE_UNSPECIFIED` (value: `"APPLICATION_TYPE_UNSPECIFIED"`)

* `NETWEAVER` (value: `"NETWEAVER"`)





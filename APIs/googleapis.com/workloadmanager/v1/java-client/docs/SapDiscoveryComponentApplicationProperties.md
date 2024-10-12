

# SapDiscoveryComponentApplicationProperties

A set of properties describing an SAP Application layer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abap** | **Boolean** | Optional. Indicates whether this is a Java or ABAP Netweaver instance. true means it is ABAP, false means it is Java. |  [optional] |
|**applicationType** | [**ApplicationTypeEnum**](#ApplicationTypeEnum) | Required. Type of the application. Netweaver, etc. |  [optional] |
|**ascsUri** | **String** | Optional. Resource URI of the recognized ASCS host of the application. |  [optional] |
|**kernelVersion** | **String** | Optional. Kernel version for Netweaver running in the system. |  [optional] |
|**nfsUri** | **String** | Optional. Resource URI of the recognized shared NFS of the application. May be empty if the application server has only a single node. |  [optional] |



## Enum: ApplicationTypeEnum

| Name | Value |
|---- | -----|
| APPLICATION_TYPE_UNSPECIFIED | &quot;APPLICATION_TYPE_UNSPECIFIED&quot; |
| NETWEAVER | &quot;NETWEAVER&quot; |






# Kernel

Linux kernel object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The architecture of this Kernel. |  [optional] [readonly] |
|**built** | **OffsetDateTime** | The date on which this Kernel was built. |  [optional] [readonly] |
|**deprecated** | **Boolean** | If this Kernel is marked as deprecated, this field has a value of true; otherwise, this field is false. |  [optional] [readonly] |
|**id** | **String** | The unique ID of this Kernel. |  [optional] [readonly] |
|**kvm** | **Boolean** | If this Kernel is suitable for KVM Linodes. |  [optional] [readonly] |
|**label** | **String** | The friendly name of this Kernel. |  [optional] [readonly] |
|**pvops** | **Boolean** | If this Kernel is suitable for paravirtualized operations. |  [optional] [readonly] |
|**version** | **String** | Linux Kernel version. |  [optional] [readonly] |
|**xen** | **Boolean** | If this Kernel is suitable for Xen Linodes. |  [optional] [readonly] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| X86_64 | &quot;x86_64&quot; |
| I386 | &quot;i386&quot; |




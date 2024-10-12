

# PlatformUpdateParameters

The properties for updating the platform configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The OS architecture. |  [optional] |
|**os** | [**OsEnum**](#OsEnum) | The operating system type required for the run. |  [optional] |
|**variant** | [**VariantEnum**](#VariantEnum) | Variant of the CPU. |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| AMD64 | &quot;amd64&quot; |
| X86 | &quot;x86&quot; |
| _386 | &quot;386&quot; |
| ARM | &quot;arm&quot; |
| ARM64 | &quot;arm64&quot; |



## Enum: OsEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: VariantEnum

| Name | Value |
|---- | -----|
| V6 | &quot;v6&quot; |
| V7 | &quot;v7&quot; |
| V8 | &quot;v8&quot; |




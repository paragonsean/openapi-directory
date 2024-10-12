

# IsosGet200ResponseIsosInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | Type of cpu architecture this iso is compatible with. Null indicates no restriction on the architecture (wildcard). |  |
|**deprecated** | **String** | ISO 8601 timestamp of deprecation, null if ISO is still available. After the deprecation time it will no longer be possible to attach the ISO to Servers. |  |
|**description** | **String** | Description of the ISO |  |
|**id** | **Integer** | ID of the Resource |  |
|**name** | **String** | Unique identifier of the ISO. Only set for public ISOs |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the ISO |  |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| X86 | &quot;x86&quot; |
| ARM | &quot;arm&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| PRIVATE | &quot;private&quot; |




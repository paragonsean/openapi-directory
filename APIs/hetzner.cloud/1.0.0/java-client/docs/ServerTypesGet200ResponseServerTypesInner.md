

# ServerTypesGet200ResponseServerTypesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | Type of cpu architecture |  |
|**cores** | **BigDecimal** | Number of cpu cores a Server of this type will have |  |
|**cpuType** | [**CpuTypeEnum**](#CpuTypeEnum) | Type of cpu |  |
|**deprecated** | **Boolean** | True if Server type is deprecated |  |
|**description** | **String** | Description of the Server type |  |
|**disk** | **BigDecimal** | Disk size a Server of this type will have in GB |  |
|**id** | **BigDecimal** | ID of the Server type |  |
|**memory** | **BigDecimal** | Memory a Server of this type will have in GB |  |
|**name** | **String** | Unique identifier of the Server type |  |
|**prices** | [**List&lt;PricingGet200ResponsePricingServerTypesInnerPricesInner&gt;**](PricingGet200ResponsePricingServerTypesInnerPricesInner.md) | Prices in different Locations |  |
|**storageType** | [**StorageTypeEnum**](#StorageTypeEnum) | Type of Server boot drive. Local has higher speed. Network has better availability. |  |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| X86 | &quot;x86&quot; |
| ARM | &quot;arm&quot; |



## Enum: CpuTypeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;shared&quot; |
| DEDICATED | &quot;dedicated&quot; |



## Enum: StorageTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| NETWORK | &quot;network&quot; |




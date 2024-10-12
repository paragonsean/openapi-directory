

# ServersGet200ResponseServersInnerServerType

Type of Server - determines how much ram, disk and cpu a Server has

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cores** | **BigDecimal** | Number of cpu cores a Server of this type will have |  |
|**cpuType** | [**CpuTypeEnum**](#CpuTypeEnum) | Type of cpu |  |
|**deprecated** | **Boolean** | True if Server type is deprecated |  |
|**description** | **String** | Description of the Server type |  |
|**disk** | **BigDecimal** | Disk size a Server of this type will have in GB |  |
|**id** | **Integer** | ID of the Server type |  |
|**memory** | **BigDecimal** | Memory a Server of this type will have in GB |  |
|**name** | **String** | Unique identifier of the Server type |  |
|**prices** | [**List&lt;PricingGet200ResponsePricingServerTypesInnerPricesInner&gt;**](PricingGet200ResponsePricingServerTypesInnerPricesInner.md) | Prices in different Locations |  |
|**storageType** | [**StorageTypeEnum**](#StorageTypeEnum) | Type of Server boot drive. Local has higher speed. Network has better availability. |  |



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




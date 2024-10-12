

# EnvironmentSize

Represents a size category supported by this Lab Account (small, medium or large)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPrice** | **BigDecimal** | The pay-as-you-go dollar price per hour this size will cost. It does not include discounts and may not reflect the actual price the size will cost. This is the maximum price of all prices within this tier. |  [optional] [readonly] |
|**minMemory** | **Double** | The amount of memory available (in GB). This is the minimum amount of memory within this tier. |  [optional] [readonly] |
|**minNumberOfCores** | **Integer** | The number of cores a VM of this size has. This is the minimum number of cores within this tier. |  [optional] [readonly] |
|**name** | [**NameEnum**](#NameEnum) | The size category |  [optional] |
|**vmSizes** | [**List&lt;SizeInfo&gt;**](SizeInfo.md) | Represents a set of compute sizes that can serve this given size type |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PERFORMANCE | &quot;Performance&quot; |




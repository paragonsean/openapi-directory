# ManagedLabsClient.EnvironmentSize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPrice** | **Number** | The pay-as-you-go dollar price per hour this size will cost. It does not include discounts and may not reflect the actual price the size will cost. This is the maximum price of all prices within this tier. | [optional] [readonly] 
**minMemory** | **Number** | The amount of memory available (in GB). This is the minimum amount of memory within this tier. | [optional] [readonly] 
**minNumberOfCores** | **Number** | The number of cores a VM of this size has. This is the minimum number of cores within this tier. | [optional] [readonly] 
**name** | **String** | The size category | [optional] 
**vmSizes** | [**[SizeInfo]**](SizeInfo.md) | Represents a set of compute sizes that can serve this given size type | [optional] 



## Enum: NameEnum


* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Performance` (value: `"Performance"`)





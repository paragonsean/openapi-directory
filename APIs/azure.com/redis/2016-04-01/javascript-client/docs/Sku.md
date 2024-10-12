# RedisManagementClient.Sku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Number** | The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4). | 
**family** | **String** | The SKU family to use. Valid values: (C, P). (C &#x3D; Basic/Standard, P &#x3D; Premium). | 
**name** | **String** | The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium) | 



## Enum: FamilyEnum


* `C` (value: `"C"`)

* `P` (value: `"P"`)





## Enum: NameEnum


* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)







# NetworkMapping

Network Mapping model. Ideally it should have been possible to inherit this class from prev version in InheritedModels as long as there is no difference in structure or method signature. Since there were no base Models for certain fields and methods viz NetworkMappingProperties and Load with required return type, the class has been introduced in its entirety with references to base models to facilitate extensions in subsequent versions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**NetworkMappingProperties**](NetworkMappingProperties.md) |  |  [optional] |
|**id** | **String** | Resource Id |  [optional] [readonly] |
|**location** | **String** | Resource Location |  [optional] |
|**name** | **String** | Resource Name |  [optional] [readonly] |
|**type** | **String** | Resource Type |  [optional] [readonly] |




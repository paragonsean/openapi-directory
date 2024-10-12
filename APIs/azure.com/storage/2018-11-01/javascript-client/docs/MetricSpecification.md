# StorageManagementClient.MetricSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationType** | **String** | Aggregation type could be Average. | [optional] 
**category** | **String** | The category this metric specification belong to, could be Capacity. | [optional] 
**dimensions** | [**[Dimension]**](Dimension.md) | Dimensions of blobs, including blob type and access tier. | [optional] 
**displayDescription** | **String** | Display description of metric specification. | [optional] 
**displayName** | **String** | Display name of metric specification. | [optional] 
**fillGapWithZero** | **Boolean** | The property to decide fill gap with zero or not. | [optional] 
**name** | **String** | Name of metric specification. | [optional] 
**resourceIdDimensionNameOverride** | **String** | Account Resource Id. | [optional] 
**unit** | **String** | Unit could be Bytes or Count. | [optional] 



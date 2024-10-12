# CloudTpuApi.QueueingPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validAfterDuration** | **String** | Optional. A relative time after which resources may be created. | [optional] 
**validAfterTime** | **String** | Optional. An absolute time after which resources may be created. | [optional] 
**validInterval** | [**Interval**](Interval.md) |  | [optional] 
**validUntilDuration** | **String** | Optional. A relative time after which resources should not be created. If the request cannot be fulfilled by this time the request will be failed. | [optional] 
**validUntilTime** | **String** | Optional. An absolute time after which resources should not be created. If the request cannot be fulfilled by this time the request will be failed. | [optional] 



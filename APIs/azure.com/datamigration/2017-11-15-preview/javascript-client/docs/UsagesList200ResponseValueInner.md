# AzureDataMigrationServiceResourceProvider.UsagesList200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentValue** | **Number** | The current value of the quota. If null or missing, the current value cannot be determined in the context of the request. | [optional] 
**id** | **String** | The resource ID of the quota object | [optional] 
**limit** | **Number** | The maximum value of the quota. If null or missing, the quota has no maximum, in which case it merely tracks usage. | [optional] 
**name** | [**UsagesList200ResponseValueInnerName**](UsagesList200ResponseValueInnerName.md) |  | [optional] 
**unit** | **String** | The unit for the quota, such as Count, Bytes, BytesPerSecond, etc. | [optional] 



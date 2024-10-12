# MerakiDashboardApi.UpdateNetworkSmDevicesTagsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **String** | The ids of the devices to be modified. | [optional] 
**scope** | **String** | The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified. | [optional] 
**serials** | **String** | The serials of the devices to be modified. | [optional] 
**tags** | **String** | The tags to be added, deleted, or updated. | 
**updateAction** | **String** | One of add, delete, or update. Only devices that have been modified will be returned. | 
**wifiMacs** | **String** | The wifiMacs of the devices to be modified. | [optional] 



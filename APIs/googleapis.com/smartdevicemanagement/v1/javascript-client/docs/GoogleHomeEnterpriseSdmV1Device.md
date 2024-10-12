# SmartDeviceManagementApi.GoogleHomeEnterpriseSdmV1Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Required. The resource name of the device. For example: \&quot;enterprises/XYZ/devices/123\&quot;. | [optional] 
**parentRelations** | [**[GoogleHomeEnterpriseSdmV1ParentRelation]**](GoogleHomeEnterpriseSdmV1ParentRelation.md) | Assignee details of the device. | [optional] 
**traits** | **{String: Object}** | Output only. Device traits. | [optional] [readonly] 
**type** | **String** | Output only. Type of the device for general display purposes. For example: \&quot;THERMOSTAT\&quot;. The device type should not be used to deduce or infer functionality of the actual device it is assigned to. Instead, use the returned traits for the device. | [optional] [readonly] 



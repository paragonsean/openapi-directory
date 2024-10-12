

# GoogleHomeEnterpriseSdmV1Device

Device resource represents an instance of enterprise managed device in the property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The resource name of the device. For example: \&quot;enterprises/XYZ/devices/123\&quot;. |  [optional] |
|**parentRelations** | [**List&lt;GoogleHomeEnterpriseSdmV1ParentRelation&gt;**](GoogleHomeEnterpriseSdmV1ParentRelation.md) | Assignee details of the device. |  [optional] |
|**traits** | **Map&lt;String, Object&gt;** | Output only. Device traits. |  [optional] [readonly] |
|**type** | **String** | Output only. Type of the device for general display purposes. For example: \&quot;THERMOSTAT\&quot;. The device type should not be used to deduce or infer functionality of the actual device it is assigned to. Instead, use the returned traits for the device. |  [optional] [readonly] |




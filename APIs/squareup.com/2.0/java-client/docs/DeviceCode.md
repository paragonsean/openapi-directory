

# DeviceCode



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The unique code that can be used to login. |  [optional] |
|**createdAt** | **String** | When this DeviceCode was created. Timestamp in RFC 3339 format. |  [optional] |
|**deviceId** | **String** | The unique id of the device that used this code. Populated when the device is paired up. |  [optional] |
|**id** | **String** | The unique id for this device code. |  [optional] |
|**locationId** | **String** | The location assigned to this code. |  [optional] |
|**name** | **String** | An optional user-defined name for the device code. |  [optional] |
|**pairBy** | **String** | When this DeviceCode will expire and no longer login. Timestamp in RFC 3339 format. |  [optional] |
|**pairedAt** | **String** | When this DeviceCode was paired. Timestamp in RFC 3339 format. |  [optional] |
|**productType** | **String** | The targeting product type of the device code. |  |
|**status** | **String** | The pairing status of the device code. |  [optional] |
|**statusChangedAt** | **String** | When this DeviceCode&#39;s status was last changed. Timestamp in RFC 3339 format. |  [optional] |




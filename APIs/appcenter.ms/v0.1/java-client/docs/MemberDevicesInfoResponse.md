

# MemberDevicesInfoResponse

The information for a single distribution group member and their ios device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatarUrl** | **String** | The avatar URL of the user |  [optional] |
|**canChangePassword** | **Boolean** | User is required to send an old password in order to change the password. |  [optional] |
|**deviceName** | **String** | The device description, in the format \&quot;iPhone 7 Plus (A1784)\&quot; |  |
|**displayName** | **String** | The full name of the user. Might for example be first and last name |  [optional] |
|**email** | **String** | The email address of the user |  |
|**fullDeviceName** | **String** | A combination of the device model name and the owner name. |  [optional] |
|**id** | **UUID** | The unique id (UUID) of the user |  |
|**imei** | **String** | The device&#39;s International Mobile Equipment Identity number. Always empty or undefined at present. |  [optional] |
|**invitePending** | **Boolean** | Whether the has accepted the invite. Available when an invite is pending, and the value will be \&quot;true\&quot;. |  [optional] |
|**model** | **String** | The model identifier of the device, in the format iDeviceM,N |  |
|**name** | **String** | The unique name that is used to identify the user. |  [optional] |
|**osBuild** | **String** | The last known OS version running on the device |  |
|**osVersion** | **String** | The last known OS version running on the device |  |
|**ownerId** | **String** | The user ID of the device owner. |  [optional] |
|**registeredAt** | **String** | Timestamp of when the device was registered in ISO format. |  [optional] |
|**serial** | **String** | The device&#39;s serial number. Always empty or undefined at present. |  [optional] |
|**status** | **String** | The provisioning status of the device. |  |
|**udid** | **String** | The Unique Device IDentifier of the device |  |




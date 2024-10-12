

# MobileApplication


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**OS** | [**OSEnum**](#OSEnum) | Operating system of device. |  [optional] |
|**businessUserId** | **Long** | Business user ID |  [optional] |
|**clientID** | **String** | Client ID of user. |  [optional] |
|**deviceName** | [**DeviceNameEnum**](#DeviceNameEnum) | type of device. |  [optional] |
|**deviceOSVersion** | **String** | OS version for device. |  [optional] |
|**mobileApplicationId** | **Long** | Mobile application id for user. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of user |  [optional] |



## Enum: OSEnum

| Name | Value |
|---- | -----|
| ANDROID | &quot;Android&quot; |
| IOS | &quot;IOS&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: DeviceNameEnum

| Name | Value |
|---- | -----|
| I_PHONE | &quot;iPhone&quot; |
| ANDROID | &quot;Android&quot; |
| OTHER | &quot;Other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;LIVE&quot; |
| CLOSED | &quot;CLOSED&quot; |
| LOCKED | &quot;LOCKED&quot; |
| SMS_SENT | &quot;SMS_SENT&quot; |




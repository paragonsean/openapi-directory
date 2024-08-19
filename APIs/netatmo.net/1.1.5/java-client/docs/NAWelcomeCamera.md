

# NAWelcomeCamera


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alimStatus** | **String** | If power supply is ok (on/off) |  [optional] |
|**id** | **String** | Id of the camera |  [optional] |
|**isLocal** | **Boolean** | Only for scope access_camera. If Camera and application requesting the information are on the same IP (true/false) |  [optional] |
|**lightModeStatus** | [**LightModeStatusEnum**](#LightModeStatusEnum) | State of (flood-)light |  [optional] |
|**name** | **String** | Name of the camera |  [optional] |
|**sdStatus** | **String** | If SD card status is ok (on/off) |  [optional] |
|**status** | **String** | If camera is monitoring (on/off) |  [optional] |
|**type** | **String** | Type of the camera |  [optional] |
|**vpnUrl** | **String** | Only for scope access_camera. Address of the camera |  [optional] |



## Enum: LightModeStatusEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| AUTO | &quot;auto&quot; |




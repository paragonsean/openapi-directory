# GooglePlayGameServices.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisitionUri** | **String** | URI which shows where a user can acquire this instance. | [optional] 
**androidInstance** | [**InstanceAndroidDetails**](InstanceAndroidDetails.md) |  | [optional] 
**iosInstance** | [**InstanceIosDetails**](InstanceIosDetails.md) |  | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#instance&#x60;. | [optional] 
**name** | **String** | Localized display name. | [optional] 
**platformType** | **String** | The platform type. | [optional] 
**realtimePlay** | **Boolean** | Flag to show if this game instance supports realtime play. | [optional] 
**turnBasedPlay** | **Boolean** | Flag to show if this game instance supports turn based play. | [optional] 
**webInstance** | [**InstanceWebDetails**](InstanceWebDetails.md) |  | [optional] 



## Enum: PlatformTypeEnum


* `ANDROID` (value: `"ANDROID"`)

* `IOS` (value: `"IOS"`)

* `WEB_APP` (value: `"WEB_APP"`)





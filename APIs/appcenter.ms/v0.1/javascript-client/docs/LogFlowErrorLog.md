# AppCenterClient.LogFlowErrorLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appLaunchToffset** | **Number** | Corresponds to the number of milliseconds elapsed between the time the error occurred and the app was launched.  | [optional] 
**id** | **String** | Error identifier. | 
**sessionId** | **String** | Session ID.  | 
**device** | [**AnalyticsGenericLogFlow200ResponseLogsInnerDevice**](AnalyticsGenericLogFlow200ResponseLogsInnerDevice.md) |  | 
**installId** | **String** | Install ID.  | 
**timestamp** | **Date** | Log creation timestamp.  | 
**type** | **String** | Log type.  | 



## Enum: TypeEnum


* `event` (value: `"event"`)

* `page` (value: `"page"`)

* `start_session` (value: `"start_session"`)

* `error` (value: `"error"`)

* `start_service` (value: `"start_service"`)

* `custom_properties` (value: `"custom_properties"`)





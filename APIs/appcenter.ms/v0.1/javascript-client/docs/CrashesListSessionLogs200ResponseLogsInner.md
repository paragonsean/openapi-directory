# AppCenterClient.CrashesListSessionLogs200ResponseLogsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of the authenticated user.  | [optional] 
**authProvider** | **String** | Auth service provider.  | [optional] 
**device** | [**AnalyticsGenericLogFlow200ResponseLogsInnerDevice**](AnalyticsGenericLogFlow200ResponseLogsInnerDevice.md) |  | 
**eventId** | **String** | Event ID.  | [optional] 
**eventName** | **String** | Event name.  | [optional] 
**installId** | **String** | Install ID.  | 
**messageId** | **String** | Message ID.  | [optional] 
**properties** | **{String: String}** | event specific properties.  | [optional] 
**sessionId** | **String** | Session ID.  | [optional] 
**timestamp** | **Date** | Log creation timestamp.  | 
**type** | **String** | Log type.  | 



## Enum: TypeEnum


* `event` (value: `"event"`)

* `page` (value: `"page"`)

* `start_session` (value: `"start_session"`)

* `error` (value: `"error"`)

* `push_installation` (value: `"push_installation"`)

* `start_service` (value: `"start_service"`)

* `custom_properties` (value: `"custom_properties"`)





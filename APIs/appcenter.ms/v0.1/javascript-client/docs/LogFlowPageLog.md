# AppCenterClient.LogFlowPageLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the page.  | 
**sessionId** | **String** | Session ID.  | 
**properties** | **{String: String}** | Additional key/value pair parameters.  | [optional] 
**device** | **Object** | Device characteristics. | 
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





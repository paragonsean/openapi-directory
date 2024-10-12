# DracoonApi.LoginRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authType** | **String** | Authentication methods | [optional] 
**language** | **String** | &amp;#128679; Deprecated since v4.7.0  Language ID or ISO 639-1 code | [optional] 
**login** | **String** | &amp;#128679; Deprecated since v4.7.0  User login name | [optional] 
**password** | **String** | Password | 
**state** | **String** | For RADIUS Access-Challenge  If a &#x60;replyState&#x60; is returned, it must be included as &#x60;state&#x60; in the following request. | [optional] 
**token** | **String** | RADIUS Token | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username | [optional] 



## Enum: AuthTypeEnum


* `basic` (value: `"basic"`)

* `active_directory` (value: `"active_directory"`)

* `radius` (value: `"radius"`)





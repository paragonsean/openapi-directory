# DracoonApi.UserInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatarUuid** | **String** | &amp;#128640; Since v4.11.0  Avatar UUID | 
**displayName** | **String** | &amp;#128679; Deprecated since v4.11.0  Display name  use other fields from &#x60;UserInfo&#x60; instead to combine a display name | [optional] 
**email** | **String** | &amp;#128640; Since v4.11.0  Email  | [optional] 
**firstName** | **String** | &amp;#128640; Since v4.11.0  User first name (mandatory if &#x60;userType&#x60; is &#x60;internal&#x60;) | 
**id** | **Number** | Unique identifier for the user | 
**lastName** | **String** | &amp;#128640; Since v4.11.0  User last name (mandatory if &#x60;userType&#x60; is &#x60;internal&#x60;) | 
**title** | **String** | &amp;#128679; Deprecated since v4.18.0  Job title | [optional] 
**userName** | **String** | &amp;#128640; Since v4.13.0  Username (only returned for &#x60;internal&#x60; users) | 
**userType** | **String** | &amp;#128640; Since v4.11.0  User type:  * &#x60;internal&#x60; - ordinary DRACOON user  * &#x60;external&#x60; - external user without DRACOON account  * &#x60;system&#x60; - system user (non human &amp;#128125;)  * &#x60;deleted&#x60; - deleted DRACOON user | 



## Enum: UserTypeEnum


* `system` (value: `"system"`)

* `internal` (value: `"internal"`)

* `external` (value: `"external"`)

* `deleted` (value: `"deleted"`)





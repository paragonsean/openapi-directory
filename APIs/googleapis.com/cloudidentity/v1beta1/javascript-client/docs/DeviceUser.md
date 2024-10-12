# CloudIdentityApi.DeviceUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compromisedState** | **String** | Compromised State of the DeviceUser object | [optional] 
**createTime** | **String** | When the user first signed in to the device | [optional] 
**firstSyncTime** | **String** | Output only. Most recent time when user registered with this service. | [optional] [readonly] 
**languageCode** | **String** | Output only. Default locale used on device, in IETF BCP-47 format. | [optional] [readonly] 
**lastSyncTime** | **String** | Output only. Last time when user synced with policies. | [optional] [readonly] 
**managementState** | **String** | Output only. Management state of the user on the device. | [optional] [readonly] 
**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the DeviceUser in format: &#x60;devices/{device_id}/deviceUsers/{device_user_id}&#x60;, where &#x60;device_user_id&#x60; uniquely identifies a user&#39;s use of a device. | [optional] [readonly] 
**passwordState** | **String** | Password state of the DeviceUser object | [optional] 
**userAgent** | **String** | Output only. User agent on the device for this specific user | [optional] [readonly] 
**userEmail** | **String** | Email address of the user registered on the device. | [optional] 



## Enum: CompromisedStateEnum


* `COMPROMISED_STATE_UNSPECIFIED` (value: `"COMPROMISED_STATE_UNSPECIFIED"`)

* `COMPROMISED` (value: `"COMPROMISED"`)

* `NOT_COMPROMISED` (value: `"NOT_COMPROMISED"`)





## Enum: ManagementStateEnum


* `MANAGEMENT_STATE_UNSPECIFIED` (value: `"MANAGEMENT_STATE_UNSPECIFIED"`)

* `WIPING` (value: `"WIPING"`)

* `WIPED` (value: `"WIPED"`)

* `APPROVED` (value: `"APPROVED"`)

* `BLOCKED` (value: `"BLOCKED"`)

* `PENDING_APPROVAL` (value: `"PENDING_APPROVAL"`)

* `UNENROLLED` (value: `"UNENROLLED"`)





## Enum: PasswordStateEnum


* `STATE_UNSPECIFIED` (value: `"PASSWORD_STATE_UNSPECIFIED"`)

* `SET` (value: `"PASSWORD_SET"`)

* `NOT_SET` (value: `"PASSWORD_NOT_SET"`)





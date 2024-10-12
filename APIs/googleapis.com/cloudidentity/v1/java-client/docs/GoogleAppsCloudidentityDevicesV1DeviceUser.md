

# GoogleAppsCloudidentityDevicesV1DeviceUser

Represents a user's use of a Device in the Cloud Identity Devices API. A DeviceUser is a resource representing a user's use of a Device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compromisedState** | [**CompromisedStateEnum**](#CompromisedStateEnum) | Compromised State of the DeviceUser object |  [optional] |
|**createTime** | **String** | When the user first signed in to the device |  [optional] |
|**firstSyncTime** | **String** | Output only. Most recent time when user registered with this service. |  [optional] [readonly] |
|**languageCode** | **String** | Output only. Default locale used on device, in IETF BCP-47 format. |  [optional] [readonly] |
|**lastSyncTime** | **String** | Output only. Last time when user synced with policies. |  [optional] [readonly] |
|**managementState** | [**ManagementStateEnum**](#ManagementStateEnum) | Output only. Management state of the user on the device. |  [optional] [readonly] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the DeviceUser in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where &#x60;device_user&#x60; uniquely identifies a user&#39;s use of a device. |  [optional] [readonly] |
|**passwordState** | [**PasswordStateEnum**](#PasswordStateEnum) | Password state of the DeviceUser object |  [optional] |
|**userAgent** | **String** | Output only. User agent on the device for this specific user |  [optional] [readonly] |
|**userEmail** | **String** | Email address of the user registered on the device. |  [optional] |



## Enum: CompromisedStateEnum

| Name | Value |
|---- | -----|
| COMPROMISED_STATE_UNSPECIFIED | &quot;COMPROMISED_STATE_UNSPECIFIED&quot; |
| COMPROMISED | &quot;COMPROMISED&quot; |
| NOT_COMPROMISED | &quot;NOT_COMPROMISED&quot; |



## Enum: ManagementStateEnum

| Name | Value |
|---- | -----|
| MANAGEMENT_STATE_UNSPECIFIED | &quot;MANAGEMENT_STATE_UNSPECIFIED&quot; |
| WIPING | &quot;WIPING&quot; |
| WIPED | &quot;WIPED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| BLOCKED | &quot;BLOCKED&quot; |
| PENDING_APPROVAL | &quot;PENDING_APPROVAL&quot; |
| UNENROLLED | &quot;UNENROLLED&quot; |



## Enum: PasswordStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;PASSWORD_STATE_UNSPECIFIED&quot; |
| SET | &quot;PASSWORD_SET&quot; |
| NOT_SET | &quot;PASSWORD_NOT_SET&quot; |




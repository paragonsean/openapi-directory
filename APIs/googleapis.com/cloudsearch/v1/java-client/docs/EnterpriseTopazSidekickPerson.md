

# EnterpriseTopazSidekickPerson

Person.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityLevel** | [**AffinityLevelEnum**](#AffinityLevelEnum) | The level of affinity this person has with the requesting user. |  [optional] |
|**attendingStatus** | [**AttendingStatusEnum**](#AttendingStatusEnum) | Attendance status of the person when included in a meeting event. |  [optional] |
|**email** | **String** | Email. |  [optional] |
|**gaiaId** | **String** | Gaia id. |  [optional] |
|**isGroup** | **Boolean** | Whether the invitee is a group. |  [optional] |
|**name** | **String** | Name. |  [optional] |
|**obfuscatedGaiaId** | **String** | Obfuscated Gaia id. |  [optional] |
|**photoUrl** | **String** | Absolute URL to the profile photo of the person. |  [optional] |



## Enum: AffinityLevelEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



## Enum: AttendingStatusEnum

| Name | Value |
|---- | -----|
| AWAITING | &quot;AWAITING&quot; |
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| MAYBE | &quot;MAYBE&quot; |




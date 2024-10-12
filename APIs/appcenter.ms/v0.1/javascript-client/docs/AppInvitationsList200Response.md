# AppCenterClient.AppInvitationsList200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppsList200ResponseInner**](AppsList200ResponseInner.md) |  | 
**appCount** | **Number** | The number of apps in the group | [optional] 
**distributionGroup** | [**AppInvitationsList200ResponseDistributionGroup**](AppInvitationsList200ResponseDistributionGroup.md) |  | [optional] 
**email** | **String** | The email address of the invited user | 
**id** | **String** | The unique ID (UUID) of the invitation | 
**inviteType** | **String** | The invitation type | 
**invitedBy** | [**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md) |  | 
**isExistingUser** | **Boolean** | Indicates whether the invited user already exists | 
**permissions** | **[String]** | The permissions the user has for the app | [optional] 



## Enum: InviteTypeEnum


* `developer` (value: `"developer"`)

* `tester` (value: `"tester"`)





## Enum: [PermissionsEnum]


* `manager` (value: `"manager"`)

* `developer` (value: `"developer"`)

* `viewer` (value: `"viewer"`)

* `tester` (value: `"tester"`)





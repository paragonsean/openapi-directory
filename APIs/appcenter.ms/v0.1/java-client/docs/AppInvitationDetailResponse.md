

# AppInvitationDetailResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**app** | [**AppsList200ResponseInner**](AppsList200ResponseInner.md) |  |  |
|**appCount** | **BigDecimal** | The number of apps in the group |  [optional] |
|**distributionGroup** | [**AppInvitationsList200ResponseDistributionGroup**](AppInvitationsList200ResponseDistributionGroup.md) |  |  [optional] |
|**email** | **String** | The email address of the invited user |  |
|**id** | **UUID** | The unique ID (UUID) of the invitation |  |
|**inviteType** | [**InviteTypeEnum**](#InviteTypeEnum) | The invitation type |  |
|**invitedBy** | [**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md) |  |  |
|**isExistingUser** | **Boolean** | Indicates whether the invited user already exists |  |
|**permissions** | [**List&lt;PermissionsEnum&gt;**](#List&lt;PermissionsEnum&gt;) | The permissions the user has for the app |  [optional] |



## Enum: InviteTypeEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;developer&quot; |
| TESTER | &quot;tester&quot; |



## Enum: List&lt;PermissionsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGER | &quot;manager&quot; |
| DEVELOPER | &quot;developer&quot; |
| VIEWER | &quot;viewer&quot; |
| TESTER | &quot;tester&quot; |




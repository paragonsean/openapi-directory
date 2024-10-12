

# Membership

Represents a membership relation in Google Chat, such as whether a user or Chat app is invited to, part of, or absent from a space.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Optional. Immutable. The creation time of the membership, such as when a member joined or was invited to join a space. This field is output only, except when used to import historical memberships in import mode spaces. |  [optional] |
|**deleteTime** | **String** | Optional. Immutable. The deletion time of the membership, such as when a member left or was removed from a space. This field is output only, except when used to import historical memberships in import mode spaces. |  [optional] |
|**groupMember** | [**Group**](Group.md) |  |  [optional] |
|**member** | [**User**](User.md) |  |  [optional] |
|**name** | **String** | Resource name of the membership, assigned by the server. Format: &#x60;spaces/{space}/members/{member}&#x60; |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Optional. User&#39;s role within a Chat space, which determines their permitted actions in the space. [Developer Preview](https://developers.google.com/workspace/preview): This field can only be used as input in &#x60;UpdateMembership&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the membership. |  [optional] [readonly] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| MEMBERSHIP_ROLE_UNSPECIFIED | &quot;MEMBERSHIP_ROLE_UNSPECIFIED&quot; |
| ROLE_MEMBER | &quot;ROLE_MEMBER&quot; |
| ROLE_MANAGER | &quot;ROLE_MANAGER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| MEMBERSHIP_STATE_UNSPECIFIED | &quot;MEMBERSHIP_STATE_UNSPECIFIED&quot; |
| JOINED | &quot;JOINED&quot; |
| INVITED | &quot;INVITED&quot; |
| NOT_A_MEMBER | &quot;NOT_A_MEMBER&quot; |




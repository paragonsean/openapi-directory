# GoogleChatApi.Membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Optional. Immutable. The creation time of the membership, such as when a member joined or was invited to join a space. This field is output only, except when used to import historical memberships in import mode spaces. | [optional] 
**deleteTime** | **String** | Optional. Immutable. The deletion time of the membership, such as when a member left or was removed from a space. This field is output only, except when used to import historical memberships in import mode spaces. | [optional] 
**groupMember** | [**Group**](Group.md) |  | [optional] 
**member** | [**User**](User.md) |  | [optional] 
**name** | **String** | Resource name of the membership, assigned by the server. Format: &#x60;spaces/{space}/members/{member}&#x60; | [optional] 
**role** | **String** | Optional. User&#39;s role within a Chat space, which determines their permitted actions in the space. [Developer Preview](https://developers.google.com/workspace/preview): This field can only be used as input in &#x60;UpdateMembership&#x60;. | [optional] 
**state** | **String** | Output only. State of the membership. | [optional] [readonly] 



## Enum: RoleEnum


* `MEMBERSHIP_ROLE_UNSPECIFIED` (value: `"MEMBERSHIP_ROLE_UNSPECIFIED"`)

* `ROLE_MEMBER` (value: `"ROLE_MEMBER"`)

* `ROLE_MANAGER` (value: `"ROLE_MANAGER"`)





## Enum: StateEnum


* `MEMBERSHIP_STATE_UNSPECIFIED` (value: `"MEMBERSHIP_STATE_UNSPECIFIED"`)

* `JOINED` (value: `"JOINED"`)

* `INVITED` (value: `"INVITED"`)

* `NOT_A_MEMBER` (value: `"NOT_A_MEMBER"`)





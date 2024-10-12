# BungieNetApi.GroupsV2GroupOptionsEditAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostGuidedGamePermissionOverride** | **Number** | Minimum Member Level allowed to host guided games  Always Allowed: Founder, Acting Founder, Admin  Allowed Overrides: None, Member, Beginner  Default is Member for clans, None for groups, although this means nothing for groups. | [optional] 
**invitePermissionOverride** | **Boolean** | Minimum Member Level allowed to invite new members to group  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. | [optional] 
**joinLevel** | **Number** | Level to join a member at when accepting an invite, application, or joining an open clan  Default is Beginner. | [optional] 
**updateBannerPermissionOverride** | **Boolean** | Minimum Member Level allowed to update banner  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. | [optional] 
**updateCulturePermissionOverride** | **Boolean** | Minimum Member Level allowed to update group culture  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. | [optional] 



## Enum: HostGuidedGamePermissionOverrideEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: JoinLevelEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)





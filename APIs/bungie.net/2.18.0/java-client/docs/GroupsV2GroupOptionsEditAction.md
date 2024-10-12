

# GroupsV2GroupOptionsEditAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostGuidedGamePermissionOverride** | [**HostGuidedGamePermissionOverrideEnum**](#HostGuidedGamePermissionOverrideEnum) | Minimum Member Level allowed to host guided games  Always Allowed: Founder, Acting Founder, Admin  Allowed Overrides: None, Member, Beginner  Default is Member for clans, None for groups, although this means nothing for groups. |  [optional] |
|**invitePermissionOverride** | **Boolean** | Minimum Member Level allowed to invite new members to group  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. |  [optional] |
|**joinLevel** | [**JoinLevelEnum**](#JoinLevelEnum) | Level to join a member at when accepting an invite, application, or joining an open clan  Default is Beginner. |  [optional] |
|**updateBannerPermissionOverride** | **Boolean** | Minimum Member Level allowed to update banner  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. |  [optional] |
|**updateCulturePermissionOverride** | **Boolean** | Minimum Member Level allowed to update group culture  Always Allowed: Founder, Acting Founder  True means admins have this power, false means they don&#39;t  Default is false for clans, true for groups. |  [optional] |



## Enum: HostGuidedGamePermissionOverrideEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: JoinLevelEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |




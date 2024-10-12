

# GroupsV2GroupResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allianceStatus** | **Integer** |  |  [optional] |
|**alliedIds** | **List&lt;Long&gt;** |  |  [optional] |
|**currentUserMemberMap** | [**Map&lt;String, GroupsV2GroupMember&gt;**](GroupsV2GroupMember.md) | This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available. |  [optional] |
|**currentUserMembershipsInactiveForDestiny** | **Boolean** | A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save. |  [optional] |
|**currentUserPotentialMemberMap** | [**Map&lt;String, GroupsV2GroupPotentialMember&gt;**](GroupsV2GroupPotentialMember.md) | This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once. |  [optional] |
|**detail** | [**GroupsV2GroupV2**](GroupsV2GroupV2.md) |  |  [optional] |
|**founder** | [**GroupsV2GroupMember**](GroupsV2GroupMember.md) |  |  [optional] |
|**groupJoinInviteCount** | **Integer** |  |  [optional] |
|**parentGroup** | [**GroupsV2GroupV2**](GroupsV2GroupV2.md) |  |  [optional] |






# ADGroup

Active Directory group information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the group. |  [optional] |
|**mail** | **String** | The primary email address of the group. |  [optional] |
|**mailEnabled** | **Boolean** | Whether the group is mail-enabled. Must be false. This is because only pure security groups can be created using the Graph API. |  [optional] |
|**mailNickname** | **String** | The mail alias for the group.  |  [optional] |
|**securityEnabled** | **Boolean** | Whether the group is security-enable. |  [optional] |




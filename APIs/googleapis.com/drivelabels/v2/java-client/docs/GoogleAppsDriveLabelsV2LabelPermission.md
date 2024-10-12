

# GoogleAppsDriveLabelsV2LabelPermission

The permission that applies to a principal (user, group, audience) on a label.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audience** | **String** | Audience to grant a role to. The magic value of &#x60;audiences/default&#x60; may be used to apply the role to the default audience in the context of the organization that owns the Label. |  [optional] |
|**email** | **String** | Specifies the email address for a user or group pricinpal. Not populated for audience principals. User and Group permissions may only be inserted using email address. On update requests, if email address is specified, no principal should be specified. |  [optional] |
|**group** | **String** | Group resource name. |  [optional] |
|**name** | **String** | Resource name of this permission. |  [optional] |
|**person** | **String** | Person resource name. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The role the principal should have. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| LABEL_ROLE_UNSPECIFIED | &quot;LABEL_ROLE_UNSPECIFIED&quot; |
| READER | &quot;READER&quot; |
| APPLIER | &quot;APPLIER&quot; |
| ORGANIZER | &quot;ORGANIZER&quot; |
| EDITOR | &quot;EDITOR&quot; |




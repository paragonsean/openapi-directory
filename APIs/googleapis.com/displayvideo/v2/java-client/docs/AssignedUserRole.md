

# AssignedUserRole

A single assigned user role, which defines a user's authorized interaction with a specified partner or advertiser.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The ID of the advertiser that the assigend user role applies to. |  [optional] |
|**assignedUserRoleId** | **String** | Output only. The ID of the assigned user role. |  [optional] [readonly] |
|**partnerId** | **String** | The ID of the partner that the assigned user role applies to. |  [optional] |
|**userRole** | [**UserRoleEnum**](#UserRoleEnum) | Required. The user role to assign to a user for the entity. |  [optional] |



## Enum: UserRoleEnum

| Name | Value |
|---- | -----|
| USER_ROLE_UNSPECIFIED | &quot;USER_ROLE_UNSPECIFIED&quot; |
| ADMIN | &quot;ADMIN&quot; |
| ADMIN_PARTNER_CLIENT | &quot;ADMIN_PARTNER_CLIENT&quot; |
| STANDARD | &quot;STANDARD&quot; |
| STANDARD_PLANNER | &quot;STANDARD_PLANNER&quot; |
| STANDARD_PLANNER_LIMITED | &quot;STANDARD_PLANNER_LIMITED&quot; |
| STANDARD_PARTNER_CLIENT | &quot;STANDARD_PARTNER_CLIENT&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| REPORTING_ONLY | &quot;REPORTING_ONLY&quot; |
| LIMITED_REPORTING_ONLY | &quot;LIMITED_REPORTING_ONLY&quot; |
| CREATIVE | &quot;CREATIVE&quot; |
| CREATIVE_ADMIN | &quot;CREATIVE_ADMIN&quot; |




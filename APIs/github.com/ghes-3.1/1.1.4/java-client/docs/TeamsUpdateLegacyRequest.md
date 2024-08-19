

# TeamsUpdateLegacyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the team. |  [optional] |
|**name** | **String** | The name of the team. |  |
|**parentTeamId** | **Integer** | The ID of a team to set as the parent team. |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | **Deprecated**. The permission that new repositories will be added to the team with when none is specified. |  [optional] |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The level of privacy this team should have. Editing teams without specifying this parameter leaves &#x60;privacy&#x60; intact. The options are:   **For a non-nested team:**   \\* &#x60;secret&#x60; - only visible to organization owners and members of this team.   \\* &#x60;closed&#x60; - visible to all members of this organization.   **For a parent or child team:**   \\* &#x60;closed&#x60; - visible to all members of this organization. |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| PULL | &quot;pull&quot; |
| PUSH | &quot;push&quot; |
| ADMIN | &quot;admin&quot; |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| SECRET | &quot;secret&quot; |
| CLOSED | &quot;closed&quot; |




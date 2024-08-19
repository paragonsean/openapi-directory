# GitHubV3RestApi.TeamsCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the team. | [optional] 
**maintainers** | **[String]** | List GitHub IDs for organization members who will become team maintainers. | [optional] 
**name** | **String** | The name of the team. | 
**parentTeamId** | **Number** | The ID of a team to set as the parent team. | [optional] 
**permission** | **String** | **Deprecated**. The permission that new repositories will be added to the team with when none is specified. Can be one of:   \\* &#x60;pull&#x60; - team members can pull, but not push to or administer newly-added repositories.   \\* &#x60;push&#x60; - team members can pull and push, but not administer newly-added repositories.   \\* &#x60;admin&#x60; - team members can pull, push and administer newly-added repositories. | [optional] [default to &#39;pull&#39;]
**privacy** | **String** | The level of privacy this team should have. The options are:   **For a non-nested team:**   \\* &#x60;secret&#x60; - only visible to organization owners and members of this team.   \\* &#x60;closed&#x60; - visible to all members of this organization.   Default: &#x60;secret&#x60;   **For a parent or child team:**   \\* &#x60;closed&#x60; - visible to all members of this organization.   Default for child team: &#x60;closed&#x60; | [optional] 
**repoNames** | **[String]** | The full name (e.g., \&quot;organization-name/repository-name\&quot;) of repositories to add the team to. | [optional] 



## Enum: PermissionEnum


* `pull` (value: `"pull"`)

* `push` (value: `"push"`)

* `admin` (value: `"admin"`)





## Enum: PrivacyEnum


* `secret` (value: `"secret"`)

* `closed` (value: `"closed"`)





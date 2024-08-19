# GitHubV3RestApi.TeamsAddOrUpdateRepoPermissionsInOrgRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **String** | The permission to grant the team on this repository. Can be one of:   \\* &#x60;pull&#x60; - team members can pull, but not push to or administer this repository.   \\* &#x60;push&#x60; - team members can pull and push, but not administer this repository.   \\* &#x60;admin&#x60; - team members can pull, push and administer this repository.   \\* &#x60;maintain&#x60; - team members can manage the repository without access to sensitive or destructive actions. Recommended for project managers. Only applies to repositories owned by organizations.   \\* &#x60;triage&#x60; - team members can proactively manage issues and pull requests without write access. Recommended for contributors who triage a repository. Only applies to repositories owned by organizations.      If no permission is specified, the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this repository. | [optional] 



## Enum: PermissionEnum


* `pull` (value: `"pull"`)

* `push` (value: `"push"`)

* `admin` (value: `"admin"`)

* `maintain` (value: `"maintain"`)

* `triage` (value: `"triage"`)





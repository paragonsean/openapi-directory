# GitHubV3RestApi.TeamsAddOrUpdateRepoPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **String** | The permission to grant the team on this repository. Can be one of:   \\* &#x60;pull&#x60; - team members can pull, but not push to or administer this repository.   \\* &#x60;push&#x60; - team members can pull and push, but not administer this repository.   \\* &#x60;admin&#x60; - team members can pull, push and administer this repository.      If no permission is specified, the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this repository.   **Note**: If you pass the &#x60;hellcat-preview&#x60; media type, you can promote—but not demote—a &#x60;permission&#x60; attribute inherited through a parent team. | [optional] 



## Enum: PermissionEnum


* `pull` (value: `"pull"`)

* `push` (value: `"push"`)

* `admin` (value: `"admin"`)





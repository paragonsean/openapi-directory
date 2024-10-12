

# ReposAddCollaboratorRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | [**PermissionEnum**](#PermissionEnum) | The permission to grant the collaborator. **Only valid on organization-owned repositories.** Can be one of:   \\* &#x60;pull&#x60; - can pull, but not push to or administer this repository.   \\* &#x60;push&#x60; - can pull and push, but not administer this repository.   \\* &#x60;admin&#x60; - can pull, push and administer this repository.   \\* &#x60;maintain&#x60; - Recommended for project managers who need to manage the repository without access to sensitive or destructive actions.   \\* &#x60;triage&#x60; - Recommended for contributors who need to proactively manage issues and pull requests without write access.  \\* custom repository role name - Can assign a custom repository role if the owning organization has defined any. |  [optional] |
|**permissions** | **String** |  |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| PULL | &quot;pull&quot; |
| PUSH | &quot;push&quot; |
| ADMIN | &quot;admin&quot; |
| MAINTAIN | &quot;maintain&quot; |
| TRIAGE | &quot;triage&quot; |




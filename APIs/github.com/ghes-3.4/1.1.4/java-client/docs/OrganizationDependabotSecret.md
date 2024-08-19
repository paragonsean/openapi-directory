

# OrganizationDependabotSecret

Secrets for GitHub Dependabot for an organization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**name** | **String** | The name of the secret. |  |
|**selectedRepositoriesUrl** | **URI** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Visibility of a secret |  |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |
| SELECTED | &quot;selected&quot; |




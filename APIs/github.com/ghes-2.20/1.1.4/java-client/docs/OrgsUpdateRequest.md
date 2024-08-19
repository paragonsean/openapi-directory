

# OrgsUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingEmail** | **String** | Billing email address. This address is not publicized. |  [optional] |
|**blog** | **String** |  |  [optional] |
|**company** | **String** | The company name. |  [optional] |
|**defaultRepositoryPermission** | [**DefaultRepositoryPermissionEnum**](#DefaultRepositoryPermissionEnum) | Default permission level members have for organization repositories:   \\* &#x60;read&#x60; - can pull, but not push to or administer this repository.   \\* &#x60;write&#x60; - can pull and push, but not administer this repository.   \\* &#x60;admin&#x60; - can pull, push, and administer this repository.   \\* &#x60;none&#x60; - no permissions granted by default. |  [optional] |
|**description** | **String** | The description of the company. |  [optional] |
|**email** | **String** | The publicly visible email address. |  [optional] |
|**hasOrganizationProjects** | **Boolean** | Toggles whether an organization can use organization projects. |  [optional] |
|**hasRepositoryProjects** | **Boolean** | Toggles whether repositories that belong to the organization can use repository projects. |  [optional] |
|**location** | **String** | The location. |  [optional] |
|**membersAllowedRepositoryCreationType** | [**MembersAllowedRepositoryCreationTypeEnum**](#MembersAllowedRepositoryCreationTypeEnum) | Specifies which types of repositories non-admin organization members can create. Can be one of:   \\* &#x60;all&#x60; - all organization members can create public and private repositories.   \\* &#x60;private&#x60; - members can create private repositories. This option is only available to repositories that are part of an organization on GitHub Enterprise Cloud.   \\* &#x60;none&#x60; - only admin members can create repositories.   **Note:** This parameter is deprecated and will be removed in the future. Its return value ignores internal repositories. Using this parameter overrides values set in &#x60;members_can_create_repositories&#x60;. See the parameter deprecation notice in the operation description for details. |  [optional] |
|**membersCanCreateInternalRepositories** | **Boolean** | Toggles whether organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. Can be one of:   \\* &#x60;true&#x60; - all organization members can create internal repositories.   \\* &#x60;false&#x60; - only organization owners can create internal repositories.   Default: &#x60;true&#x60;. For more information, see \&quot;[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. |  [optional] |
|**membersCanCreatePrivateRepositories** | **Boolean** | Toggles whether organization members can create private repositories, which are visible to organization members with permission. Can be one of:   \\* &#x60;true&#x60; - all organization members can create private repositories.   \\* &#x60;false&#x60; - only organization owners can create private repositories.   Default: &#x60;true&#x60;. For more information, see \&quot;[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. |  [optional] |
|**membersCanCreatePublicRepositories** | **Boolean** | Toggles whether organization members can create public repositories, which are visible to anyone. Can be one of:   \\* &#x60;true&#x60; - all organization members can create public repositories.   \\* &#x60;false&#x60; - only organization owners can create public repositories.   Default: &#x60;true&#x60;. For more information, see \&quot;[Restricting repository creation in your organization](https://help.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. |  [optional] |
|**membersCanCreateRepositories** | **Boolean** | Toggles the ability of non-admin organization members to create repositories. Can be one of:   \\* &#x60;true&#x60; - all organization members can create repositories.   \\* &#x60;false&#x60; - only organization owners can create repositories.   Default: &#x60;true&#x60;   **Note:** A parameter can override this parameter. See &#x60;members_allowed_repository_creation_type&#x60; in this table for details. **Note:** A parameter can override this parameter. See &#x60;members_allowed_repository_creation_type&#x60; in this table for details. |  [optional] |
|**name** | **String** | The shorthand name of the company. |  [optional] |
|**twitterUsername** | **String** | The Twitter username of the company. |  [optional] |



## Enum: DefaultRepositoryPermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |
| NONE | &quot;none&quot; |



## Enum: MembersAllowedRepositoryCreationTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| PRIVATE | &quot;private&quot; |
| NONE | &quot;none&quot; |




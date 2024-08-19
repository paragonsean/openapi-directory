# GitHubV3RestApi.OrgsUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingEmail** | **String** | Billing email address. This address is not publicized. | [optional] 
**blog** | **String** |  | [optional] 
**company** | **String** | The company name. | [optional] 
**defaultRepositoryPermission** | **String** | Default permission level members have for organization repositories. | [optional] [default to &#39;read&#39;]
**description** | **String** | The description of the company. | [optional] 
**email** | **String** | The publicly visible email address. | [optional] 
**hasOrganizationProjects** | **Boolean** | Whether an organization can use organization projects. | [optional] 
**hasRepositoryProjects** | **Boolean** | Whether repositories that belong to the organization can use repository projects. | [optional] 
**location** | **String** | The location. | [optional] 
**membersAllowedRepositoryCreationType** | **String** | Specifies which types of repositories non-admin organization members can create.  **Note:** This parameter is deprecated and will be removed in the future. Its return value ignores internal repositories. Using this parameter overrides values set in &#x60;members_can_create_repositories&#x60;. See the parameter deprecation notice in the operation description for details. | [optional] 
**membersCanCreateInternalRepositories** | **Boolean** | Whether organization members can create internal repositories, which are visible to all enterprise members. You can only allow members to create internal repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**membersCanCreatePages** | **Boolean** | Whether organization members can create GitHub Pages sites. Existing published sites will not be impacted. | [optional] [default to true]
**membersCanCreatePrivateRepositories** | **Boolean** | Whether organization members can create private repositories, which are visible to organization members with permission. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**membersCanCreatePublicRepositories** | **Boolean** | Whether organization members can create public repositories, which are visible to anyone. For more information, see \&quot;[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)\&quot; in the GitHub Help documentation. | [optional] 
**membersCanCreateRepositories** | **Boolean** | Whether of non-admin organization members can create repositories. **Note:** A parameter can override this parameter. See &#x60;members_allowed_repository_creation_type&#x60; in this table for details. | [optional] [default to true]
**name** | **String** | The shorthand name of the company. | [optional] 
**twitterUsername** | **String** | The Twitter username of the company. | [optional] 



## Enum: DefaultRepositoryPermissionEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)

* `none` (value: `"none"`)





## Enum: MembersAllowedRepositoryCreationTypeEnum


* `all` (value: `"all"`)

* `private` (value: `"private"`)

* `none` (value: `"none"`)





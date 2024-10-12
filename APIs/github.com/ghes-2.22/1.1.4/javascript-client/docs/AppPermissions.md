# GitHubV3RestApi.AppPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **String** | The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**administration** | **String** | The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**checks** | **String** | The level of permission to grant the access token for checks on code. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**contentReferences** | **String** | The level of permission to grant the access token for notification of content references and creation content attachments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**contents** | **String** | The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**deployments** | **String** | The level of permission to grant the access token for deployments and deployment statuses. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**environments** | **String** | The level of permission to grant the access token for managing repository environments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**issues** | **String** | The level of permission to grant the access token for issues and related comments, assignees, labels, and milestones. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**members** | **String** | The level of permission to grant the access token for organization teams and members. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**metadata** | **String** | The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationAdministration** | **String** | The level of permission to grant the access token to manage access to an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationHooks** | **String** | The level of permission to grant the access token to manage the post-receive hooks for an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationPackages** | **String** | The level of permission to grant the access token for organization packages published to GitHub Packages. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationPlan** | **String** | The level of permission to grant the access token for viewing an organization&#39;s plan. Can be one of: &#x60;read&#x60;. | [optional] 
**organizationProjects** | **String** | The level of permission to grant the access token to manage organization projects and projects beta (where available). Can be one of: &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60;. | [optional] 
**organizationSecrets** | **String** | The level of permission to grant the access token to manage organization secrets. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationSelfHostedRunners** | **String** | The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**organizationUserBlocking** | **String** | The level of permission to grant the access token to view and manage users blocked by the organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**packages** | **String** | The level of permission to grant the access token for packages published to GitHub Packages. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**pages** | **String** | The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**pullRequests** | **String** | The level of permission to grant the access token for pull requests and related comments, assignees, labels, milestones, and merges. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**repositoryHooks** | **String** | The level of permission to grant the access token to manage the post-receive hooks for a repository. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**repositoryProjects** | **String** | The level of permission to grant the access token to manage repository projects, columns, and cards. Can be one of: &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60;. | [optional] 
**secretScanningAlerts** | **String** | The level of permission to grant the access token to view and manage secret scanning alerts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**secrets** | **String** | The level of permission to grant the access token to manage repository secrets. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**securityEvents** | **String** | The level of permission to grant the access token to view and manage security events like code scanning alerts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**singleFile** | **String** | The level of permission to grant the access token to manage just a single file. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**statuses** | **String** | The level of permission to grant the access token for commit statuses. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**teamDiscussions** | **String** | The level of permission to grant the access token to manage team discussions and related comments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. | [optional] 
**vulnerabilityAlerts** | **String** | The level of permission to grant the access token to retrieve Dependabot alerts. Can be one of: &#x60;read&#x60;. | [optional] 
**workflows** | **String** | The level of permission to grant the access token to update GitHub Actions workflow files. Can be one of: &#x60;write&#x60;. | [optional] 



## Enum: ActionsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: AdministrationEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: ChecksEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: ContentReferencesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: ContentsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: DeploymentsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: EnvironmentsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: IssuesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: MembersEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: MetadataEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationAdministrationEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationHooksEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationPackagesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationPlanEnum


* `read` (value: `"read"`)





## Enum: OrganizationProjectsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)





## Enum: OrganizationSecretsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationSelfHostedRunnersEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: OrganizationUserBlockingEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: PackagesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: PagesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: PullRequestsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: RepositoryHooksEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: RepositoryProjectsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)





## Enum: SecretScanningAlertsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: SecretsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: SecurityEventsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: SingleFileEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: StatusesEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: TeamDiscussionsEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)





## Enum: VulnerabilityAlertsEnum


* `read` (value: `"read"`)





## Enum: WorkflowsEnum


* `write` (value: `"write"`)





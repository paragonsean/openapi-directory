# GitHubV3RestApi.AppPermissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **String** | The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts. | [optional] 
**administration** | **String** | The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation. | [optional] 
**checks** | **String** | The level of permission to grant the access token for checks on code. | [optional] 
**contentReferences** | **String** | The level of permission to grant the access token for notification of content references and creation content attachments. | [optional] 
**contents** | **String** | The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges. | [optional] 
**deployments** | **String** | The level of permission to grant the access token for deployments and deployment statuses. | [optional] 
**environments** | **String** | The level of permission to grant the access token for managing repository environments. | [optional] 
**issues** | **String** | The level of permission to grant the access token for issues and related comments, assignees, labels, and milestones. | [optional] 
**members** | **String** | The level of permission to grant the access token for organization teams and members. | [optional] 
**metadata** | **String** | The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata. | [optional] 
**organizationAdministration** | **String** | The level of permission to grant the access token to manage access to an organization. | [optional] 
**organizationHooks** | **String** | The level of permission to grant the access token to manage the post-receive hooks for an organization. | [optional] 
**organizationPackages** | **String** | The level of permission to grant the access token for organization packages published to GitHub Packages. | [optional] 
**organizationPlan** | **String** | The level of permission to grant the access token for viewing an organization&#39;s plan. | [optional] 
**organizationProjects** | **String** | The level of permission to grant the access token to manage organization projects and projects beta (where available). | [optional] 
**organizationSecrets** | **String** | The level of permission to grant the access token to manage organization secrets. | [optional] 
**organizationSelfHostedRunners** | **String** | The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization. | [optional] 
**organizationUserBlocking** | **String** | The level of permission to grant the access token to view and manage users blocked by the organization. | [optional] 
**packages** | **String** | The level of permission to grant the access token for packages published to GitHub Packages. | [optional] 
**pages** | **String** | The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds. | [optional] 
**pullRequests** | **String** | The level of permission to grant the access token for pull requests and related comments, assignees, labels, milestones, and merges. | [optional] 
**repositoryHooks** | **String** | The level of permission to grant the access token to manage the post-receive hooks for a repository. | [optional] 
**repositoryProjects** | **String** | The level of permission to grant the access token to manage repository projects, columns, and cards. | [optional] 
**secretScanningAlerts** | **String** | The level of permission to grant the access token to view and manage secret scanning alerts. | [optional] 
**secrets** | **String** | The level of permission to grant the access token to manage repository secrets. | [optional] 
**securityEvents** | **String** | The level of permission to grant the access token to view and manage security events like code scanning alerts. | [optional] 
**singleFile** | **String** | The level of permission to grant the access token to manage just a single file. | [optional] 
**statuses** | **String** | The level of permission to grant the access token for commit statuses. | [optional] 
**teamDiscussions** | **String** | The level of permission to grant the access token to manage team discussions and related comments. | [optional] 
**vulnerabilityAlerts** | **String** | The level of permission to grant the access token to manage Dependabot alerts. | [optional] 
**workflows** | **String** | The level of permission to grant the access token to update GitHub Actions workflow files. | [optional] 



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

* `write` (value: `"write"`)





## Enum: WorkflowsEnum


* `write` (value: `"write"`)





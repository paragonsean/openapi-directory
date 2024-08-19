

# AppPermissions

The permissions granted to the user-to-server access token.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**ActionsEnum**](#ActionsEnum) | The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**administration** | [**AdministrationEnum**](#AdministrationEnum) | The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**checks** | [**ChecksEnum**](#ChecksEnum) | The level of permission to grant the access token for checks on code. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**contentReferences** | [**ContentReferencesEnum**](#ContentReferencesEnum) | The level of permission to grant the access token for notification of content references and creation content attachments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**contents** | [**ContentsEnum**](#ContentsEnum) | The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**deployments** | [**DeploymentsEnum**](#DeploymentsEnum) | The level of permission to grant the access token for deployments and deployment statuses. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**environments** | [**EnvironmentsEnum**](#EnvironmentsEnum) | The level of permission to grant the access token for managing repository environments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**issues** | [**IssuesEnum**](#IssuesEnum) | The level of permission to grant the access token for issues and related comments, assignees, labels, and milestones. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**members** | [**MembersEnum**](#MembersEnum) | The level of permission to grant the access token for organization teams and members. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**metadata** | [**MetadataEnum**](#MetadataEnum) | The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationAdministration** | [**OrganizationAdministrationEnum**](#OrganizationAdministrationEnum) | The level of permission to grant the access token to manage access to an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationHooks** | [**OrganizationHooksEnum**](#OrganizationHooksEnum) | The level of permission to grant the access token to manage the post-receive hooks for an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationPackages** | [**OrganizationPackagesEnum**](#OrganizationPackagesEnum) | The level of permission to grant the access token for organization packages published to GitHub Packages. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationPlan** | [**OrganizationPlanEnum**](#OrganizationPlanEnum) | The level of permission to grant the access token for viewing an organization&#39;s plan. Can be one of: &#x60;read&#x60;. |  [optional] |
|**organizationProjects** | [**OrganizationProjectsEnum**](#OrganizationProjectsEnum) | The level of permission to grant the access token to manage organization projects and projects beta (where available). Can be one of: &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60;. |  [optional] |
|**organizationSecrets** | [**OrganizationSecretsEnum**](#OrganizationSecretsEnum) | The level of permission to grant the access token to manage organization secrets. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationSelfHostedRunners** | [**OrganizationSelfHostedRunnersEnum**](#OrganizationSelfHostedRunnersEnum) | The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**organizationUserBlocking** | [**OrganizationUserBlockingEnum**](#OrganizationUserBlockingEnum) | The level of permission to grant the access token to view and manage users blocked by the organization. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**packages** | [**PackagesEnum**](#PackagesEnum) | The level of permission to grant the access token for packages published to GitHub Packages. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**pages** | [**PagesEnum**](#PagesEnum) | The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**pullRequests** | [**PullRequestsEnum**](#PullRequestsEnum) | The level of permission to grant the access token for pull requests and related comments, assignees, labels, milestones, and merges. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**repositoryHooks** | [**RepositoryHooksEnum**](#RepositoryHooksEnum) | The level of permission to grant the access token to manage the post-receive hooks for a repository. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**repositoryProjects** | [**RepositoryProjectsEnum**](#RepositoryProjectsEnum) | The level of permission to grant the access token to manage repository projects, columns, and cards. Can be one of: &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60;. |  [optional] |
|**secretScanningAlerts** | [**SecretScanningAlertsEnum**](#SecretScanningAlertsEnum) | The level of permission to grant the access token to view and manage secret scanning alerts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**secrets** | [**SecretsEnum**](#SecretsEnum) | The level of permission to grant the access token to manage repository secrets. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**securityEvents** | [**SecurityEventsEnum**](#SecurityEventsEnum) | The level of permission to grant the access token to view and manage security events like code scanning alerts. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**singleFile** | [**SingleFileEnum**](#SingleFileEnum) | The level of permission to grant the access token to manage just a single file. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**statuses** | [**StatusesEnum**](#StatusesEnum) | The level of permission to grant the access token for commit statuses. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**teamDiscussions** | [**TeamDiscussionsEnum**](#TeamDiscussionsEnum) | The level of permission to grant the access token to manage team discussions and related comments. Can be one of: &#x60;read&#x60; or &#x60;write&#x60;. |  [optional] |
|**vulnerabilityAlerts** | [**VulnerabilityAlertsEnum**](#VulnerabilityAlertsEnum) | The level of permission to grant the access token to retrieve Dependabot alerts. Can be one of: &#x60;read&#x60;. |  [optional] |
|**workflows** | [**WorkflowsEnum**](#WorkflowsEnum) | The level of permission to grant the access token to update GitHub Actions workflow files. Can be one of: &#x60;write&#x60;. |  [optional] |



## Enum: ActionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: AdministrationEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: ChecksEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: ContentReferencesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: ContentsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: DeploymentsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: EnvironmentsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: IssuesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: MembersEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: MetadataEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationAdministrationEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationHooksEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationPackagesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationPlanEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |



## Enum: OrganizationProjectsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |



## Enum: OrganizationSecretsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationSelfHostedRunnersEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: OrganizationUserBlockingEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: PackagesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: PagesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: PullRequestsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: RepositoryHooksEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: RepositoryProjectsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |



## Enum: SecretScanningAlertsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: SecretsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: SecurityEventsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: SingleFileEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: StatusesEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: TeamDiscussionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |



## Enum: VulnerabilityAlertsEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |



## Enum: WorkflowsEnum

| Name | Value |
|---- | -----|
| WRITE | &quot;write&quot; |




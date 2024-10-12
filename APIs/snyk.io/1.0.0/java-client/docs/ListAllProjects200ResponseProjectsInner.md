

# ListAllProjects200ResponseProjectsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**RetrieveASingleProject200ResponseAttributes**](RetrieveASingleProject200ResponseAttributes.md) |  |  [optional] |
|**branch** | **String** | The monitored branch (if available) |  [optional] |
|**browseUrl** | **String** | URL with project overview |  [optional] |
|**created** | **String** | The date that the project was created on |  [optional] |
|**id** | **String** | The project identifier |  [optional] |
|**imageBaseImage** | **String** | For docker projects shows the base image |  [optional] |
|**imageCluster** | **String** | For Kubernetes projects shows the origin cluster name |  [optional] |
|**imageId** | **String** | For docker projects shows the ID of the image |  [optional] |
|**imagePlatform** | **String** | For docker projects shows the platform of the image |  [optional] |
|**imageTag** | **String** | For docker projects shows the tag of the image |  [optional] |
|**importingUser** | [**RetrieveASingleProject200ResponseImportingUser**](RetrieveASingleProject200ResponseImportingUser.md) |  |  [optional] |
|**isMonitored** | **Boolean** | Describes if a project is currently monitored or it is de-activated |  [optional] |
|**issueCountsBySeverity** | [**RetrieveASingleProject200ResponseIssueCountsBySeverity**](RetrieveASingleProject200ResponseIssueCountsBySeverity.md) |  |  [optional] |
|**lastTestedDate** | **String** | The date on which the most recent test was conducted for this project |  [optional] |
|**name** | **String** |  |  [optional] |
|**origin** | **String** | The origin the project was added from |  [optional] |
|**owner** | **Object** | The user who owns the project, null if not set  {     \&quot;id\&quot;: \&quot;e713cf94-bb02-4ea0-89d9-613cce0caed2\&quot;,     \&quot;name\&quot;: \&quot;example-user@snyk.io\&quot;,     \&quot;username\&quot;: \&quot;exampleUser\&quot;,     \&quot;email\&quot;: \&quot;example-user@snyk.io\&quot; } |  [optional] |
|**readOnly** | **Boolean** | Whether the project is read-only |  [optional] |
|**remoteRepoUrl** | **String** | The project remote repository url. Only set for projects imported via the Snyk CLI tool. |  [optional] |
|**tags** | **List&lt;Object&gt;** | List of applied tags |  [optional] |
|**targetReference** | **String** | The identifier for which revision of the resource is scanned by Snyk. For example this may be a branch for SCM project, or a tag for a container image |  [optional] |
|**testFrequency** | **String** | The frequency of automated Snyk re-test. Can be &#39;daily&#39;, &#39;weekly or &#39;never&#39; |  [optional] |
|**totalDependencies** | **BigDecimal** | Number of dependencies of the project |  [optional] |
|**type** | **String** | The package manager of the project |  [optional] |




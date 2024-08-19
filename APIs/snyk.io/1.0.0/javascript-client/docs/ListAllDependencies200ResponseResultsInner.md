# SnykApi.ListAllDependencies200ResponseResultsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **[Object]** | The copyright notices for the package | [optional] 
**dependenciesWithIssues** | **[Object]** | The identifiers of dependencies with issues that are depended upon as a result of this dependency | [optional] 
**deprecatedVersions** | **[Object]** | The numbers for those versions that are marked as deprecated | [optional] 
**firstPublishedDate** | **String** | The timestamp for when the specified package was first published. | [optional] 
**id** | **String** | The identifier of the package | 
**isDeprecated** | **Boolean** | True if the latest version of the package is marked as deprecated; False otherwise. | [optional] 
**issuesCritical** | **Number** | The number of critical severity issues in this dependency | [optional] 
**issuesHigh** | **Number** | The number of high severity issues in this dependency | [optional] 
**issuesLow** | **Number** | The number of low severity issues in this dependency | [optional] 
**issuesMedium** | **Number** | The number of medium severity issues in this dependency | [optional] 
**latestVersion** | **String** | The latest version available for the specified package | [optional] 
**latestVersionPublishedDate** | **String** | The timestamp for when the latest version of the specified package was published. | [optional] 
**licenses** | [**[ListAllDependencies200ResponseResultsInnerLicensesInner]**](ListAllDependencies200ResponseResultsInnerLicensesInner.md) | The licenses of the dependency | 
**name** | **String** | The name of the package | 
**projects** | [**[ListAllDependencies200ResponseResultsInnerProjectsInner]**](ListAllDependencies200ResponseResultsInnerProjectsInner.md) | The projects which depend on the dependency | 
**type** | **String** | The package type of the dependency | 
**version** | **String** | The version of the package | 



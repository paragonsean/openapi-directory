# SnykApi.ListAllDependenciesRequestFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depStatus** | **String** | Status of the dependency. Requires reporting entitlement. Options: &#x60;deprecated&#x60; - Include only deprecated packages; &#x60;notDeprecated&#x60; - Include all packages that are not marked as deprecated; &#x60;any&#x60; - Include all packages (default) | [optional] 
**dependencies** | **Object** | The list of dependency IDs to filter the results by (i.e amdefine@1.0.1 or org.javassist:javassist@3.18.1-GA) | [optional] 
**languages** | **[Object]** | The type of languages to filter the results by | [optional] 
**licenses** | **Object** | The list of license IDs to filter the results by | [optional] 
**projects** | **Object** | The list of project IDs to filter the results by | [optional] 
**severity** | **[Object]** | The severities to filter the results by | [optional] 



# AzureDataMigrationServiceResourceProvider.ProjectsList200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | UTC Date and time when project was created | [optional] [readonly] 
**databasesInfo** | [**[ProjectsList200ResponseValueInnerPropertiesDatabasesInfoInner]**](ProjectsList200ResponseValueInnerPropertiesDatabasesInfoInner.md) | List of DatabaseInfo | [optional] 
**provisioningState** | **String** | The project&#39;s provisioning state | [optional] [readonly] 
**sourceConnectionInfo** | [**ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo**](ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo.md) |  | [optional] 
**sourcePlatform** | **String** | Source platform of the project | 
**targetConnectionInfo** | [**ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo**](ProjectsList200ResponseValueInnerPropertiesSourceConnectionInfo.md) |  | [optional] 
**targetPlatform** | **String** | Target platform of the project | 



## Enum: ProvisioningStateEnum


* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: SourcePlatformEnum


* `SQL` (value: `"SQL"`)

* `Unknown` (value: `"Unknown"`)





## Enum: TargetPlatformEnum


* `SQLDB` (value: `"SQLDB"`)

* `Unknown` (value: `"Unknown"`)





# MigrationHubStrategyRecommendations.UpdateApplicationComponentConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appType** | **String** | The type of known component. | [optional] 
**applicationComponentId** | **String** |  The ID of the application component. The ID is unique within an AWS account.  | 
**configureOnly** | **Boolean** | Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated. | [optional] 
**inclusionStatus** | **String** |  Indicates whether the application component has been included for server recommendation or not.  | [optional] 
**secretsManagerKey** | **String** |  Database credentials.  | [optional] 
**sourceCodeList** | [**[SourceCode]**](SourceCode.md) |  The list of source code configurations to update for the application component.  | [optional] 
**strategyOption** | [**UpdateApplicationComponentConfigRequestStrategyOption**](UpdateApplicationComponentConfigRequestStrategyOption.md) |  | [optional] 



## Enum: AppTypeEnum


* `DotNetFramework` (value: `"DotNetFramework"`)

* `Java` (value: `"Java"`)

* `SQLServer` (value: `"SQLServer"`)

* `IIS` (value: `"IIS"`)

* `Oracle` (value: `"Oracle"`)

* `Other` (value: `"Other"`)

* `Tomcat` (value: `"Tomcat"`)

* `JBoss` (value: `"JBoss"`)

* `Spring` (value: `"Spring"`)

* `Mongo DB` (value: `"Mongo DB"`)

* `DB2` (value: `"DB2"`)

* `Maria DB` (value: `"Maria DB"`)

* `MySQL` (value: `"MySQL"`)

* `Sybase` (value: `"Sybase"`)

* `PostgreSQLServer` (value: `"PostgreSQLServer"`)

* `Cassandra` (value: `"Cassandra"`)

* `IBM WebSphere` (value: `"IBM WebSphere"`)

* `Oracle WebLogic` (value: `"Oracle WebLogic"`)

* `Visual Basic` (value: `"Visual Basic"`)

* `Unknown` (value: `"Unknown"`)

* `DotnetCore` (value: `"DotnetCore"`)

* `Dotnet` (value: `"Dotnet"`)





## Enum: InclusionStatusEnum


* `excludeFromAssessment` (value: `"excludeFromAssessment"`)

* `includeInAssessment` (value: `"includeInAssessment"`)





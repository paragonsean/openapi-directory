

# UpdateApplicationComponentConfigRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appType** | [**AppTypeEnum**](#AppTypeEnum) | The type of known component. |  [optional] |
|**applicationComponentId** | **String** |  The ID of the application component. The ID is unique within an AWS account.  |  |
|**configureOnly** | **Boolean** | Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated. |  [optional] |
|**inclusionStatus** | [**InclusionStatusEnum**](#InclusionStatusEnum) |  Indicates whether the application component has been included for server recommendation or not.  |  [optional] |
|**secretsManagerKey** | **String** |  Database credentials.  |  [optional] |
|**sourceCodeList** | [**List&lt;SourceCode&gt;**](SourceCode.md) |  The list of source code configurations to update for the application component.  |  [optional] |
|**strategyOption** | [**UpdateApplicationComponentConfigRequestStrategyOption**](UpdateApplicationComponentConfigRequestStrategyOption.md) |  |  [optional] |



## Enum: AppTypeEnum

| Name | Value |
|---- | -----|
| DOT_NET_FRAMEWORK | &quot;DotNetFramework&quot; |
| JAVA | &quot;Java&quot; |
| SQL_SERVER | &quot;SQLServer&quot; |
| IIS | &quot;IIS&quot; |
| ORACLE | &quot;Oracle&quot; |
| OTHER | &quot;Other&quot; |
| TOMCAT | &quot;Tomcat&quot; |
| J_BOSS | &quot;JBoss&quot; |
| SPRING | &quot;Spring&quot; |
| MONGO_DB | &quot;Mongo DB&quot; |
| DB2 | &quot;DB2&quot; |
| MARIA_DB | &quot;Maria DB&quot; |
| MY_SQL | &quot;MySQL&quot; |
| SYBASE | &quot;Sybase&quot; |
| POSTGRE_SQL_SERVER | &quot;PostgreSQLServer&quot; |
| CASSANDRA | &quot;Cassandra&quot; |
| IBM_WEB_SPHERE | &quot;IBM WebSphere&quot; |
| ORACLE_WEB_LOGIC | &quot;Oracle WebLogic&quot; |
| VISUAL_BASIC | &quot;Visual Basic&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| DOTNET_CORE | &quot;DotnetCore&quot; |
| DOTNET | &quot;Dotnet&quot; |



## Enum: InclusionStatusEnum

| Name | Value |
|---- | -----|
| EXCLUDE_FROM_ASSESSMENT | &quot;excludeFromAssessment&quot; |
| INCLUDE_IN_ASSESSMENT | &quot;includeInAssessment&quot; |




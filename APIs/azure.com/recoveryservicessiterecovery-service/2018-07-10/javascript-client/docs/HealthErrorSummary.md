# SiteRecoveryManagementClient.HealthErrorSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affectedResourceCorrelationIds** | **[String]** | The list of affected resource correlation Ids. This can be used to uniquely identify the count of items affected by a specific category and severity as well as count of item affected by an specific issue. | [optional] 
**affectedResourceSubtype** | **String** | The sub type of any subcomponent within the ARM resource that this might be applicable. Value remains null if not applicable. | [optional] 
**affectedResourceType** | **String** | The type of affected ARM resource. | [optional] 
**category** | **String** | The category of the health error. | [optional] 
**severity** | **String** | Severity of error. | [optional] 
**summaryCode** | **String** | The code of the health error. | [optional] 
**summaryMessage** | **String** | The summary message of the health error. | [optional] 



## Enum: CategoryEnum


* `None` (value: `"None"`)

* `Replication` (value: `"Replication"`)

* `TestFailover` (value: `"TestFailover"`)

* `Configuration` (value: `"Configuration"`)

* `FabricInfrastructure` (value: `"FabricInfrastructure"`)

* `VersionExpiry` (value: `"VersionExpiry"`)

* `AgentAutoUpdate` (value: `"AgentAutoUpdate"`)





## Enum: SeverityEnum


* `NONE` (value: `"NONE"`)

* `Warning` (value: `"Warning"`)

* `Error` (value: `"Error"`)

* `Info` (value: `"Info"`)





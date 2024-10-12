# DataFactoryManagementClient.IntegrationRuntimeNodesGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **{String: String}** | The integration runtime capabilities dictionary | [optional] [readonly] 
**concurrentJobsLimit** | **Number** | Maximum concurrent jobs on the integration runtime node. | [optional] [readonly] 
**expiryTime** | **Date** | The time at which the integration runtime will expire in ISO8601 format. | [optional] [readonly] 
**hostServiceUri** | **String** | URI for the host machine of the integration runtime. | [optional] [readonly] 
**isActiveDispatcher** | **Boolean** | Indicates whether this node is the active dispatcher for integration runtime requests. | [optional] [readonly] 
**lastConnectTime** | **Date** | The most recent time at which the integration runtime was connected in ISO8601 format. | [optional] [readonly] 
**lastEndUpdateTime** | **Date** | The last time for the integration runtime node update end. | [optional] [readonly] 
**lastStartTime** | **Date** | The time the node last started up. | [optional] [readonly] 
**lastStartUpdateTime** | **Date** | The last time for the integration runtime node update start. | [optional] [readonly] 
**lastStopTime** | **Date** | The integration runtime node last stop time. | [optional] [readonly] 
**lastUpdateResult** | **String** | The result of the last integration runtime node update. | [optional] [readonly] 
**machineName** | **String** | Machine name of the integration runtime node. | [optional] [readonly] 
**maxConcurrentJobs** | **Number** | The maximum concurrent jobs in this integration runtime. | [optional] [readonly] 
**nodeName** | **String** | Name of the integration runtime node. | [optional] [readonly] 
**registerTime** | **Date** | The time at which the integration runtime node was registered in ISO8601 format. | [optional] [readonly] 
**status** | **String** | Status of the integration runtime node. | [optional] [readonly] 
**version** | **String** | Version of the integration runtime node. | [optional] [readonly] 
**versionStatus** | **String** | Status of the integration runtime node version. | [optional] [readonly] 



## Enum: LastUpdateResultEnum


* `None` (value: `"None"`)

* `Succeed` (value: `"Succeed"`)

* `Fail` (value: `"Fail"`)





## Enum: StatusEnum


* `NeedRegistration` (value: `"NeedRegistration"`)

* `Online` (value: `"Online"`)

* `Limited` (value: `"Limited"`)

* `Offline` (value: `"Offline"`)

* `Upgrading` (value: `"Upgrading"`)

* `Initializing` (value: `"Initializing"`)

* `InitializeFailed` (value: `"InitializeFailed"`)





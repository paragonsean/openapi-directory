

# IntegrationRuntimeNodesGet200Response

Properties of Self-hosted integration runtime node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | **Map&lt;String, String&gt;** | The integration runtime capabilities dictionary |  [optional] [readonly] |
|**concurrentJobsLimit** | **Integer** | Maximum concurrent jobs on the integration runtime node. |  [optional] [readonly] |
|**expiryTime** | **OffsetDateTime** | The time at which the integration runtime will expire in ISO8601 format. |  [optional] [readonly] |
|**hostServiceUri** | **String** | URI for the host machine of the integration runtime. |  [optional] [readonly] |
|**isActiveDispatcher** | **Boolean** | Indicates whether this node is the active dispatcher for integration runtime requests. |  [optional] [readonly] |
|**lastConnectTime** | **OffsetDateTime** | The most recent time at which the integration runtime was connected in ISO8601 format. |  [optional] [readonly] |
|**lastEndUpdateTime** | **OffsetDateTime** | The last time for the integration runtime node update end. |  [optional] [readonly] |
|**lastStartTime** | **OffsetDateTime** | The time the node last started up. |  [optional] [readonly] |
|**lastStartUpdateTime** | **OffsetDateTime** | The last time for the integration runtime node update start. |  [optional] [readonly] |
|**lastStopTime** | **OffsetDateTime** | The integration runtime node last stop time. |  [optional] [readonly] |
|**lastUpdateResult** | [**LastUpdateResultEnum**](#LastUpdateResultEnum) | The result of the last integration runtime node update. |  [optional] [readonly] |
|**machineName** | **String** | Machine name of the integration runtime node. |  [optional] [readonly] |
|**maxConcurrentJobs** | **Integer** | The maximum concurrent jobs in this integration runtime. |  [optional] [readonly] |
|**nodeName** | **String** | Name of the integration runtime node. |  [optional] [readonly] |
|**registerTime** | **OffsetDateTime** | The time at which the integration runtime node was registered in ISO8601 format. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the integration runtime node. |  [optional] [readonly] |
|**version** | **String** | Version of the integration runtime node. |  [optional] [readonly] |
|**versionStatus** | **String** | Status of the integration runtime node version. |  [optional] [readonly] |



## Enum: LastUpdateResultEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SUCCEED | &quot;Succeed&quot; |
| FAIL | &quot;Fail&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEED_REGISTRATION | &quot;NeedRegistration&quot; |
| ONLINE | &quot;Online&quot; |
| LIMITED | &quot;Limited&quot; |
| OFFLINE | &quot;Offline&quot; |
| UPGRADING | &quot;Upgrading&quot; |
| INITIALIZING | &quot;Initializing&quot; |
| INITIALIZE_FAILED | &quot;InitializeFailed&quot; |




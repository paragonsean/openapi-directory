

# MasterTargetServer

Details of a Master Target Server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentExpiryDate** | **OffsetDateTime** | Agent expiry date. |  [optional] |
|**agentVersion** | **String** | The version of the scout component on the server. |  [optional] |
|**agentVersionDetails** | [**VersionDetails**](VersionDetails.md) |  |  [optional] |
|**dataStores** | [**List&lt;DataStore&gt;**](DataStore.md) | The list of data stores in the fabric. |  [optional] |
|**diskCount** | **Integer** | Disk count of the master target. |  [optional] |
|**healthErrors** | [**List&lt;HealthError&gt;**](HealthError.md) | Health errors. |  [optional] |
|**id** | **String** | The server Id. |  [optional] |
|**ipAddress** | **String** | The IP address of the server. |  [optional] |
|**lastHeartbeat** | **OffsetDateTime** | The last heartbeat received from the server. |  [optional] |
|**marsAgentExpiryDate** | **OffsetDateTime** | MARS agent expiry date. |  [optional] |
|**marsAgentVersion** | **String** | MARS agent version. |  [optional] |
|**marsAgentVersionDetails** | [**VersionDetails**](VersionDetails.md) |  |  [optional] |
|**name** | **String** | The server name. |  [optional] |
|**osType** | **String** | The OS type of the server. |  [optional] |
|**osVersion** | **String** | OS Version of the master target. |  [optional] |
|**retentionVolumes** | [**List&lt;RetentionVolume&gt;**](RetentionVolume.md) | The retention volumes of Master target Server. |  [optional] |
|**validationErrors** | [**List&lt;HealthError&gt;**](HealthError.md) | Validation errors. |  [optional] |
|**versionStatus** | **String** | Version status |  [optional] |




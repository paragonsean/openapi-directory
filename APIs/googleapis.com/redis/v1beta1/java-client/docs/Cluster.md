

# Cluster

A cluster instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationMode** | [**AuthorizationModeEnum**](#AuthorizationModeEnum) | Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster. |  [optional] |
|**createTime** | **String** | Output only. The timestamp associated with the cluster creation request. |  [optional] [readonly] |
|**discoveryEndpoints** | [**List&lt;DiscoveryEndpoint&gt;**](DiscoveryEndpoint.md) | Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported. |  [optional] [readonly] |
|**name** | **String** | Required. Unique name of the resource in this scope including project and location using the form: &#x60;projects/{project_id}/locations/{location_id}/clusters/{cluster_id}&#x60; |  [optional] |
|**pscConfigs** | [**List&lt;PscConfig&gt;**](PscConfig.md) | Required. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported. |  [optional] |
|**pscConnections** | [**List&lt;PscConnection&gt;**](PscConnection.md) | Output only. PSC connections for discovery of the cluster topology and accessing the cluster. |  [optional] [readonly] |
|**replicaCount** | **Integer** | Optional. The number of replica nodes per shard. |  [optional] |
|**shardCount** | **Integer** | Required. Number of shards for the Redis cluster. |  [optional] |
|**sizeGb** | **Integer** | Output only. Redis memory size in GB for the entire cluster rounded up to the next integer. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED |  [optional] [readonly] |
|**stateInfo** | [**StateInfo**](StateInfo.md) |  |  [optional] |
|**transitEncryptionMode** | [**TransitEncryptionModeEnum**](#TransitEncryptionModeEnum) | Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster. |  [optional] |
|**uid** | **String** | Output only. System assigned, unique identifier for the cluster. |  [optional] [readonly] |



## Enum: AuthorizationModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUTH_MODE_UNSPECIFIED&quot; |
| IAM_AUTH | &quot;AUTH_MODE_IAM_AUTH&quot; |
| DISABLED | &quot;AUTH_MODE_DISABLED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |



## Enum: TransitEncryptionModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TRANSIT_ENCRYPTION_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;TRANSIT_ENCRYPTION_MODE_DISABLED&quot; |
| SERVER_AUTHENTICATION | &quot;TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION&quot; |




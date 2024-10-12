# GoogleCloudMemorystoreForRedisApi.Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationMode** | **String** | Optional. The authorization mode of the Redis cluster. If not provided, auth feature is disabled for the cluster. | [optional] 
**createTime** | **String** | Output only. The timestamp associated with the cluster creation request. | [optional] [readonly] 
**discoveryEndpoints** | [**[DiscoveryEndpoint]**](DiscoveryEndpoint.md) | Output only. Endpoints created on each given network, for Redis clients to connect to the cluster. Currently only one discovery endpoint is supported. | [optional] [readonly] 
**name** | **String** | Required. Unique name of the resource in this scope including project and location using the form: &#x60;projects/{project_id}/locations/{location_id}/clusters/{cluster_id}&#x60; | [optional] 
**pscConfigs** | [**[PscConfig]**](PscConfig.md) | Required. Each PscConfig configures the consumer network where IPs will be designated to the cluster for client access through Private Service Connect Automation. Currently, only one PscConfig is supported. | [optional] 
**pscConnections** | [**[PscConnection]**](PscConnection.md) | Output only. PSC connections for discovery of the cluster topology and accessing the cluster. | [optional] [readonly] 
**replicaCount** | **Number** | Optional. The number of replica nodes per shard. | [optional] 
**shardCount** | **Number** | Required. Number of shards for the Redis cluster. | [optional] 
**sizeGb** | **Number** | Output only. Redis memory size in GB for the entire cluster rounded up to the next integer. | [optional] [readonly] 
**state** | **String** | Output only. The current state of this cluster. Can be CREATING, READY, UPDATING, DELETING and SUSPENDED | [optional] [readonly] 
**stateInfo** | [**StateInfo**](StateInfo.md) |  | [optional] 
**transitEncryptionMode** | **String** | Optional. The in-transit encryption for the Redis cluster. If not provided, encryption is disabled for the cluster. | [optional] 
**uid** | **String** | Output only. System assigned, unique identifier for the cluster. | [optional] [readonly] 



## Enum: AuthorizationModeEnum


* `UNSPECIFIED` (value: `"AUTH_MODE_UNSPECIFIED"`)

* `IAM_AUTH` (value: `"AUTH_MODE_IAM_AUTH"`)

* `DISABLED` (value: `"AUTH_MODE_DISABLED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)





## Enum: TransitEncryptionModeEnum


* `UNSPECIFIED` (value: `"TRANSIT_ENCRYPTION_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"TRANSIT_ENCRYPTION_MODE_DISABLED"`)

* `SERVER_AUTHENTICATION` (value: `"TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION"`)





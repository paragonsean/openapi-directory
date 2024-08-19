# CloudMemorystoreForMemcachedApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizedNetwork** | **String** | The full name of the Google Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. If left unspecified, the &#x60;default&#x60; network will be used. | [optional] 
**createTime** | **String** | Output only. The time the instance was created. | [optional] [readonly] 
**discoveryEndpoint** | **String** | Output only. Endpoint for the Discovery API. | [optional] [readonly] 
**displayName** | **String** | User provided name for the instance, which is only used for display purposes. Cannot be more than 80 characters. | [optional] 
**instanceMessages** | [**[InstanceMessage]**](InstanceMessage.md) | List of messages that describe the current state of the Memcached instance. | [optional] 
**labels** | **{String: String}** | Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] 
**maintenancePolicy** | [**GoogleCloudMemcacheV1MaintenancePolicy**](GoogleCloudMemcacheV1MaintenancePolicy.md) |  | [optional] 
**maintenanceSchedule** | [**MaintenanceSchedule**](MaintenanceSchedule.md) |  | [optional] 
**memcacheFullVersion** | **String** | Output only. The full version of memcached server running on this instance. System automatically determines the full memcached version for an instance based on the input MemcacheVersion. The full version format will be \&quot;memcached-1.5.16\&quot;. | [optional] [readonly] 
**memcacheNodes** | [**[Node]**](Node.md) | Output only. List of Memcached nodes. Refer to Node message for more details. | [optional] [readonly] 
**memcacheVersion** | **String** | The major version of Memcached software. If not provided, latest supported version will be used. Currently the latest supported major version is &#x60;MEMCACHE_1_5&#x60;. The minor version will be automatically determined by our system based on the latest supported minor version. | [optional] 
**name** | **String** | Required. Unique name of the resource in this scope including project and location using the form: &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}&#x60; Note: Memcached instances are managed and addressed at the regional level so &#x60;location_id&#x60; here refers to a Google Cloud region; however, users may choose which zones Memcached nodes should be provisioned in within an instance. Refer to zones field for more details. | [optional] 
**nodeConfig** | [**NodeConfig**](NodeConfig.md) |  | [optional] 
**nodeCount** | **Number** | Required. Number of nodes in the Memcached instance. | [optional] 
**parameters** | [**MemcacheParameters**](MemcacheParameters.md) |  | [optional] 
**reservedIpRangeId** | **[String]** | Optional. Contains the id of allocated IP address ranges associated with the private service access connection for example, \&quot;test-default\&quot; associated with IP range 10.0.0.0/29. | [optional] 
**state** | **String** | Output only. The state of this Memcached instance. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time the instance was updated. | [optional] [readonly] 
**zones** | **[String]** | Zones in which Memcached nodes should be provisioned. Memcached nodes will be equally distributed across these zones. If not provided, the service will by default create nodes in all zones in the region for the instance. | [optional] 



## Enum: MemcacheVersionEnum


* `VERSION_UNSPECIFIED` (value: `"MEMCACHE_VERSION_UNSPECIFIED"`)

* `1_5` (value: `"MEMCACHE_1_5"`)

* `1_6_15` (value: `"MEMCACHE_1_6_15"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `PERFORMING_MAINTENANCE` (value: `"PERFORMING_MAINTENANCE"`)

* `MEMCACHE_VERSION_UPGRADING` (value: `"MEMCACHE_VERSION_UPGRADING"`)





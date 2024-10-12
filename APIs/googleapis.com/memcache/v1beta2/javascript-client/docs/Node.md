# CloudMemorystoreForMemcachedApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | Output only. Hostname or IP address of the Memcached node used by the clients to connect to the Memcached server on this node. | [optional] [readonly] 
**memcacheFullVersion** | **String** | Output only. The full version of memcached server running on this node. e.g. - memcached-1.5.16 | [optional] [readonly] 
**memcacheVersion** | **String** | Output only. Major version of memcached server running on this node, e.g. MEMCACHE_1_5 | [optional] [readonly] 
**nodeId** | **String** | Output only. Identifier of the Memcached node. The node id does not include project or location like the Memcached instance name. | [optional] [readonly] 
**parameters** | [**MemcacheParameters**](MemcacheParameters.md) |  | [optional] 
**port** | **Number** | Output only. The port number of the Memcached server on this node. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the Memcached node. | [optional] [readonly] 
**updateAvailable** | **Boolean** | Output only. Returns true if there is an update waiting to be applied | [optional] [readonly] 
**zone** | **String** | Output only. Location (GCP Zone) for the Memcached node. | [optional] [readonly] 



## Enum: MemcacheVersionEnum


* `VERSION_UNSPECIFIED` (value: `"MEMCACHE_VERSION_UNSPECIFIED"`)

* `1_5` (value: `"MEMCACHE_1_5"`)

* `1_6_15` (value: `"MEMCACHE_1_6_15"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)





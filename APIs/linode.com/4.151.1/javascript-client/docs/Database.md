# LinodeApi.Database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowList** | **[String]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  | [optional] 
**clusterSize** | **Number** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  | [optional] [default to ClusterSizeEnum.1]
**created** | **Date** | When this Managed Database was created. | [optional] [readonly] 
**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. | [optional] [default to false]
**engine** | **String** | The Managed Database engine type. | [optional] [readonly] 
**hosts** | [**DatabaseHosts**](DatabaseHosts.md) |  | [optional] 
**id** | **Number** | A unique ID that can be used to identify and reference the Managed Database. | [optional] [readonly] 
**instanceUri** | **String** | Append this to &#x60;https://api.linode.com&#x60; to run commands for the Managed Database.  | [optional] [readonly] 
**label** | **String** | A unique, user-defined string referring to the Managed Database. | [optional] 
**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. | [optional] 
**status** | **String** | The operating status of the Managed Database. | [optional] [readonly] 
**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. | [optional] 
**updated** | **Date** | When this Managed Database was last updated. | [optional] [readonly] 
**updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  | [optional] 
**version** | **String** | The Managed Database engine version. | [optional] [readonly] 



## Enum: ClusterSizeEnum


* `1` (value: `1`)

* `3` (value: `3`)





## Enum: EngineEnum


* `mongodb` (value: `"mongodb"`)

* `mysql` (value: `"mysql"`)

* `postgresql` (value: `"postgresql"`)





## Enum: StatusEnum


* `provisioning` (value: `"provisioning"`)

* `active` (value: `"active"`)

* `suspending` (value: `"suspending"`)

* `suspended` (value: `"suspended"`)

* `resuming` (value: `"resuming"`)

* `restoring` (value: `"restoring"`)

* `failed` (value: `"failed"`)

* `degraded` (value: `"degraded"`)

* `updating` (value: `"updating"`)

* `backing_up` (value: `"backing_up"`)







# Instance

An Instance is a computing unit that an end customer can connect to. It's the main unit of computing resources in AlloyDB.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 |  [optional] |
|**availabilityType** | [**AvailabilityTypeEnum**](#AvailabilityTypeEnum) | Availability type of an Instance. If empty, defaults to REGIONAL for primary instances. For read pools, availability_type is always UNSPECIFIED. Instances in the read pools are evenly distributed across available zones within the region (i.e. read pools with more than one node will have a node in at least two zones). |  [optional] |
|**clientConnectionConfig** | [**ClientConnectionConfig**](ClientConnectionConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. Create time stamp |  [optional] [readonly] |
|**databaseFlags** | **Map&lt;String, String&gt;** | Database flags. Set at instance level. * They are copied from primary instance on read instance creation. * Read instances can set new or override existing flags that are relevant for reads, e.g. for enabling columnar cache on a read instance. Flags set on read instance may or may not be present on primary. This is a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. \&quot;key\&quot;: The name of the flag. These flags are passed at instance setup time, so include both server options and system variables for Postgres. Flags are specified with underscores, not hyphens. \&quot;value\&quot;: The value of the flag. Booleans are set to **on** for true and **off** for false. This field must be omitted if the flag doesn&#39;t take a value. |  [optional] |
|**deleteTime** | **String** | Output only. Delete time stamp |  [optional] [readonly] |
|**displayName** | **String** | User-settable and human-readable display name for the Instance. |  [optional] |
|**etag** | **String** | For Resource freshness validation (https://google.aip.dev/154) |  [optional] |
|**gceZone** | **String** | The Compute Engine zone that the instance should serve from, per https://cloud.google.com/compute/docs/regions-zones This can ONLY be specified for ZONAL instances. If present for a REGIONAL instance, an error will be thrown. If this is absent for a ZONAL instance, instance is created in a random zone with available capacity. |  [optional] |
|**instanceType** | [**InstanceTypeEnum**](#InstanceTypeEnum) | Required. The type of the instance. Specified at creation time. |  [optional] |
|**ipAddress** | **String** | Output only. The IP address for the Instance. This is the connection endpoint for an end-user application. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs |  [optional] |
|**machineConfig** | [**MachineConfig**](MachineConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The name of the instance resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instance_id} where the cluster and instance ID segments should satisfy the regex expression &#x60;[a-z]([a-z0-9-]{0,61}[a-z0-9])?&#x60;, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: * projects/{project}/locations/{region}/clusters/{cluster_id} |  [optional] [readonly] |
|**networkConfig** | [**InstanceNetworkConfig**](InstanceNetworkConfig.md) |  |  [optional] |
|**nodes** | [**List&lt;Node&gt;**](Node.md) | Output only. List of available read-only VMs in this instance, including the standby for a PRIMARY instance. |  [optional] [readonly] |
|**pscInstanceConfig** | [**PscInstanceConfig**](PscInstanceConfig.md) |  |  [optional] |
|**publicIpAddress** | **String** | Output only. The public IP addresses for the Instance. This is available ONLY when enable_public_ip is set. This is the connection endpoint for an end-user application. |  [optional] [readonly] |
|**queryInsightsConfig** | [**QueryInsightsInstanceConfig**](QueryInsightsInstanceConfig.md) |  |  [optional] |
|**readPoolConfig** | [**ReadPoolConfig**](ReadPoolConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Instance does not match the user&#39;s intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current serving state of the instance. |  [optional] [readonly] |
|**uid** | **String** | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. |  [optional] [readonly] |
|**updatePolicy** | [**UpdatePolicy**](UpdatePolicy.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Update time stamp |  [optional] [readonly] |
|**writableNode** | [**Node**](Node.md) |  |  [optional] |



## Enum: AvailabilityTypeEnum

| Name | Value |
|---- | -----|
| AVAILABILITY_TYPE_UNSPECIFIED | &quot;AVAILABILITY_TYPE_UNSPECIFIED&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



## Enum: InstanceTypeEnum

| Name | Value |
|---- | -----|
| INSTANCE_TYPE_UNSPECIFIED | &quot;INSTANCE_TYPE_UNSPECIFIED&quot; |
| PRIMARY | &quot;PRIMARY&quot; |
| READ_POOL | &quot;READ_POOL&quot; |
| SECONDARY | &quot;SECONDARY&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| STOPPED | &quot;STOPPED&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| FAILED | &quot;FAILED&quot; |
| BOOTSTRAPPING | &quot;BOOTSTRAPPING&quot; |
| PROMOTING | &quot;PROMOTING&quot; |




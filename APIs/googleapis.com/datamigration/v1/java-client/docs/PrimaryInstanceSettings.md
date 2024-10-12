

# PrimaryInstanceSettings

Settings for the cluster's primary instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseFlags** | **Map&lt;String, String&gt;** | Database flags to pass to AlloyDB when DMS is creating the AlloyDB cluster and instances. See the AlloyDB documentation for how these can be used. |  [optional] |
|**id** | **String** | Required. The ID of the AlloyDB primary instance. The ID must satisfy the regex expression \&quot;[a-z0-9-]+\&quot;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels for the AlloyDB primary instance created by DMS. An object containing a list of &#39;key&#39;, &#39;value&#39; pairs. |  [optional] |
|**machineConfig** | [**MachineConfig**](MachineConfig.md) |  |  [optional] |
|**privateIp** | **String** | Output only. The private IP address for the Instance. This is the connection endpoint for an end-user application. |  [optional] [readonly] |




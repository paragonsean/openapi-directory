

# RestartNodeDescription

Describes the parameters to restart a Service Fabric node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createFabricDump** | [**CreateFabricDumpEnum**](#CreateFabricDumpEnum) | Specify True to create a dump of the fabric node process. This is case sensitive. |  [optional] |
|**nodeInstanceId** | **String** | The instance id of the target node. If instance id is specified the node is restarted only if it matches with the current instance of the node. A default value of \&quot;0\&quot; would match any instance id. The instance id can be obtained using get node query. |  |



## Enum: CreateFabricDumpEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;False&quot; |
| TRUE | &quot;True&quot; |




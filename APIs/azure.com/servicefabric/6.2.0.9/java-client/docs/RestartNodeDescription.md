

# RestartNodeDescription

Describes the parameters to restart a Service Fabric node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createFabricDump** | [**CreateFabricDumpEnum**](#CreateFabricDumpEnum) | Specify True to create a dump of the fabric node process. This is case sensitive. |  [optional] |
|**nodeInstanceId** | **String** | The instance ID of the target node. If instance ID is specified the node is restarted only if it matches with the current instance of the node. A default value of \&quot;0\&quot; would match any instance ID. The instance ID can be obtained using get node query. |  |



## Enum: CreateFabricDumpEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;False&quot; |
| TRUE | &quot;True&quot; |




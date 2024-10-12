# ServiceFabricClientApis.RestartNodeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createFabricDump** | **String** | Specify True to create a dump of the fabric node process. This is case sensitive. | [optional] [default to &#39;False&#39;]
**nodeInstanceId** | **String** | The instance id of the target node. If instance id is specified the node is restarted only if it matches with the current instance of the node. A default value of \&quot;0\&quot; would match any instance id. The instance id can be obtained using get node query. | [default to &#39;0&#39;]



## Enum: CreateFabricDumpEnum


* `False` (value: `"False"`)

* `True` (value: `"True"`)





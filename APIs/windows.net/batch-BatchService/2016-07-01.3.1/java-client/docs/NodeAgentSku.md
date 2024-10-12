

# NodeAgentSku

The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) |  |  [optional] |
|**verifiedImageReferences** | [**List&lt;ImageReference&gt;**](ImageReference.md) | This collection is not exhaustive (the node agent may be compatible with other images). |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;linux&quot; |
| WINDOWS | &quot;windows&quot; |
| UNMAPPED | &quot;unmapped&quot; |




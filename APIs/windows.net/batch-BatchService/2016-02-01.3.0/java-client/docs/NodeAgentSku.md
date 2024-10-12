

# NodeAgentSku

A node agent SKU supported by the Batch service. The Batch node agent is a program that runs on each node in the pool, and provides the command-and-control interface between the node and the Batch service. There are different implementations of the node agent, known as SKUs, for different operating systems.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The node agent SKU id. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The type of operating system compatible with the node agent SKU. |  [optional] |
|**verifiedImageReferences** | [**List&lt;ImageReference&gt;**](ImageReference.md) | The list of images verified to be compatible with this node agent SKU. This collection is not exhaustive (the node agent may be compatible with other images). |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;linux&quot; |
| WINDOWS | &quot;windows&quot; |
| UNMAPPED | &quot;unmapped&quot; |




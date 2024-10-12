

# GraphPackage

Defines the graph of modules making up the machine learning solution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**edges** | [**List&lt;GraphEdge&gt;**](GraphEdge.md) | The list of edges making up the graph. |  [optional] |
|**graphParameters** | [**Map&lt;String, GraphParameter&gt;**](GraphParameter.md) | The collection of global parameters for the graph, given as a global parameter name to GraphParameter map. Each parameter here has a 1:1 match with the global parameters values map declared at the WebServiceProperties level. |  [optional] |
|**nodes** | [**Map&lt;String, GraphNode&gt;**](GraphNode.md) | The set of nodes making up the graph, provided as a nodeId to GraphNode map |  [optional] |




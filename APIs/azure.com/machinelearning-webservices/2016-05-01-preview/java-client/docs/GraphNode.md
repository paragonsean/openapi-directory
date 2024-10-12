

# GraphNode

Specifies a node in the web service graph. The node can either be an input, output or asset node, so only one of the corresponding id properties is populated at any given time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetId** | **String** | The id of the asset represented by this node. |  [optional] |
|**inputId** | **String** | The id of the input element represented by this node. |  [optional] |
|**outputId** | **String** | The id of the output element represented by this node. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | If applicable, parameters of the node. Global graph parameters map into these, with values set at runtime. |  [optional] |






# AssetItem

Information about an asset associated with the web service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Asset&#39;s Id. |  [optional] |
|**inputPorts** | [**Map&lt;String, InputPort&gt;**](InputPort.md) | Information about the asset&#39;s input ports. |  [optional] |
|**locationInfo** | [**AssetLocation**](AssetLocation.md) |  |  |
|**metadata** | **Map&lt;String, String&gt;** | If the asset is a custom module, this holds the module&#39;s metadata. |  [optional] |
|**name** | **String** | Asset&#39;s friendly name. |  |
|**outputPorts** | [**Map&lt;String, OutputPort&gt;**](OutputPort.md) | Information about the asset&#39;s output ports. |  [optional] |
|**parameters** | [**List&lt;ModuleAssetParameter&gt;**](ModuleAssetParameter.md) | If the asset is a custom module, this holds the module&#39;s parameters. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Asset&#39;s type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MODULE | &quot;Module&quot; |
| RESOURCE | &quot;Resource&quot; |




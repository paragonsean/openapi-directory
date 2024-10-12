

# Manifest

Manifest configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dash** | [**DashConfig**](DashConfig.md) |  |  [optional] |
|**fileName** | **String** | The name of the generated file. The default is &#x60;manifest&#x60; with the extension suffix corresponding to the Manifest.type. |  [optional] |
|**muxStreams** | **List&lt;String&gt;** | Required. List of user supplied MuxStream.key values that should appear in this manifest. When Manifest.type is &#x60;HLS&#x60;, a media manifest with name MuxStream.key and &#x60;.m3u8&#x60; extension is generated for each element in this list. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of the manifest. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MANIFEST_TYPE_UNSPECIFIED | &quot;MANIFEST_TYPE_UNSPECIFIED&quot; |
| HLS | &quot;HLS&quot; |
| DASH | &quot;DASH&quot; |




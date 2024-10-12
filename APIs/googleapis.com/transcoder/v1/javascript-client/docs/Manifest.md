# TranscoderApi.Manifest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dash** | [**DashConfig**](DashConfig.md) |  | [optional] 
**fileName** | **String** | The name of the generated file. The default is &#x60;manifest&#x60; with the extension suffix corresponding to the Manifest.type. | [optional] 
**muxStreams** | **[String]** | Required. List of user supplied MuxStream.key values that should appear in this manifest. When Manifest.type is &#x60;HLS&#x60;, a media manifest with name MuxStream.key and &#x60;.m3u8&#x60; extension is generated for each element in this list. | [optional] 
**type** | **String** | Required. Type of the manifest. | [optional] 



## Enum: TypeEnum


* `MANIFEST_TYPE_UNSPECIFIED` (value: `"MANIFEST_TYPE_UNSPECIFIED"`)

* `HLS` (value: `"HLS"`)

* `DASH` (value: `"DASH"`)





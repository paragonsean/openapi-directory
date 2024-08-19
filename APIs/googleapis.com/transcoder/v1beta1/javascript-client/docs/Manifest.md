# TranscoderApi.Manifest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileName** | **String** | The name of the generated file. The default is &#x60;\&quot;manifest\&quot;&#x60; with the extension suffix corresponding to the &#x60;Manifest.type&#x60;. | [optional] 
**muxStreams** | **[String]** | Required. List of user given &#x60;MuxStream.key&#x60;s that should appear in this manifest. When &#x60;Manifest.type&#x60; is &#x60;HLS&#x60;, a media manifest with name &#x60;MuxStream.key&#x60; and &#x60;.m3u8&#x60; extension is generated for each element of the &#x60;Manifest.mux_streams&#x60;. | [optional] 
**type** | **String** | Required. Type of the manifest, can be \&quot;HLS\&quot; or \&quot;DASH\&quot;. | [optional] 



## Enum: TypeEnum


* `MANIFEST_TYPE_UNSPECIFIED` (value: `"MANIFEST_TYPE_UNSPECIFIED"`)

* `HLS` (value: `"HLS"`)

* `DASH` (value: `"DASH"`)





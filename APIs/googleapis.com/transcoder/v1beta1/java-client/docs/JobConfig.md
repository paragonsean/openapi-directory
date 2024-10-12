

# JobConfig

Job configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adBreaks** | [**List&lt;AdBreak&gt;**](AdBreak.md) | List of ad breaks. Specifies where to insert ad break tags in the output manifests. |  [optional] |
|**editList** | [**List&lt;EditAtom&gt;**](EditAtom.md) | List of &#x60;Edit atom&#x60;s. Defines the ultimate timeline of the resulting file or manifest. |  [optional] |
|**elementaryStreams** | [**List&lt;ElementaryStream&gt;**](ElementaryStream.md) | List of elementary streams. |  [optional] |
|**inputs** | [**List&lt;Input&gt;**](Input.md) | List of input assets stored in Cloud Storage. |  [optional] |
|**manifests** | [**List&lt;Manifest&gt;**](Manifest.md) | List of output manifests. |  [optional] |
|**muxStreams** | [**List&lt;MuxStream&gt;**](MuxStream.md) | List of multiplexing settings for output streams. |  [optional] |
|**output** | [**Output**](Output.md) |  |  [optional] |
|**overlays** | [**List&lt;Overlay&gt;**](Overlay.md) | List of overlays on the output video, in descending Z-order. |  [optional] |
|**pubsubDestination** | [**PubsubDestination**](PubsubDestination.md) |  |  [optional] |
|**spriteSheets** | [**List&lt;SpriteSheet&gt;**](SpriteSheet.md) | List of output sprite sheets. |  [optional] |




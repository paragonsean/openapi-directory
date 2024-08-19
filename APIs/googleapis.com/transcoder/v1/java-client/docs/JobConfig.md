

# JobConfig

Job configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adBreaks** | [**List&lt;AdBreak&gt;**](AdBreak.md) | List of ad breaks. Specifies where to insert ad break tags in the output manifests. |  [optional] |
|**editList** | [**List&lt;EditAtom&gt;**](EditAtom.md) | List of edit atoms. Defines the ultimate timeline of the resulting file or manifest. |  [optional] |
|**elementaryStreams** | [**List&lt;ElementaryStream&gt;**](ElementaryStream.md) | List of elementary streams. |  [optional] |
|**encryptions** | [**List&lt;Encryption&gt;**](Encryption.md) | List of encryption configurations for the content. Each configuration has an ID. Specify this ID in the MuxStream.encryption_id field to indicate the configuration to use for that &#x60;MuxStream&#x60; output. |  [optional] |
|**inputs** | [**List&lt;Input&gt;**](Input.md) | List of input assets stored in Cloud Storage. |  [optional] |
|**manifests** | [**List&lt;Manifest&gt;**](Manifest.md) | List of output manifests. |  [optional] |
|**muxStreams** | [**List&lt;MuxStream&gt;**](MuxStream.md) | List of multiplexing settings for output streams. |  [optional] |
|**output** | [**Output**](Output.md) |  |  [optional] |
|**overlays** | [**List&lt;Overlay&gt;**](Overlay.md) | List of overlays on the output video, in descending Z-order. |  [optional] |
|**pubsubDestination** | [**PubsubDestination**](PubsubDestination.md) |  |  [optional] |
|**spriteSheets** | [**List&lt;SpriteSheet&gt;**](SpriteSheet.md) | List of output sprite sheets. Spritesheets require at least one VideoStream in the Jobconfig. |  [optional] |




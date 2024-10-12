# TranscoderApi.JobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adBreaks** | [**[AdBreak]**](AdBreak.md) | List of ad breaks. Specifies where to insert ad break tags in the output manifests. | [optional] 
**editList** | [**[EditAtom]**](EditAtom.md) | List of &#x60;Edit atom&#x60;s. Defines the ultimate timeline of the resulting file or manifest. | [optional] 
**elementaryStreams** | [**[ElementaryStream]**](ElementaryStream.md) | List of elementary streams. | [optional] 
**inputs** | [**[Input]**](Input.md) | List of input assets stored in Cloud Storage. | [optional] 
**manifests** | [**[Manifest]**](Manifest.md) | List of output manifests. | [optional] 
**muxStreams** | [**[MuxStream]**](MuxStream.md) | List of multiplexing settings for output streams. | [optional] 
**output** | [**Output**](Output.md) |  | [optional] 
**overlays** | [**[Overlay]**](Overlay.md) | List of overlays on the output video, in descending Z-order. | [optional] 
**pubsubDestination** | [**PubsubDestination**](PubsubDestination.md) |  | [optional] 
**spriteSheets** | [**[SpriteSheet]**](SpriteSheet.md) | List of output sprite sheets. | [optional] 





# MuxStream

Multiplexing settings for output stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | The container format. The default is &#x60;mp4&#x60; Supported container formats: - &#x60;ts&#x60; - &#x60;fmp4&#x60;- the corresponding file extension is &#x60;.m4s&#x60; - &#x60;mp4&#x60; - &#x60;vtt&#x60; See also: [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats) |  [optional] |
|**elementaryStreams** | **List&lt;String&gt;** | List of ElementaryStream.key values multiplexed in this stream. |  [optional] |
|**encryptionId** | **String** | Identifier of the encryption configuration to use. If omitted, output will be unencrypted. |  [optional] |
|**fileName** | **String** | The name of the generated file. The default is MuxStream.key with the extension suffix corresponding to the MuxStream.container. Individual segments also have an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as &#x60;mux_stream0000000123.ts&#x60;. |  [optional] |
|**fmp4** | [**Fmp4Config**](Fmp4Config.md) |  |  [optional] |
|**key** | **String** | A unique key for this multiplexed stream. |  [optional] |
|**segmentSettings** | [**SegmentSettings**](SegmentSettings.md) |  |  [optional] |




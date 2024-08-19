

# MuxStream

Multiplexing settings for output stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | The container format. The default is &#x60;\&quot;mp4\&quot;&#x60; Supported container formats: - &#39;ts&#39; - &#39;fmp4&#39;- the corresponding file extension is &#x60;\&quot;.m4s\&quot;&#x60; - &#39;mp4&#39; - &#39;vtt&#39; |  [optional] |
|**elementaryStreams** | **List&lt;String&gt;** | List of &#x60;ElementaryStream.key&#x60;s multiplexed in this stream. |  [optional] |
|**encryption** | [**Encryption**](Encryption.md) |  |  [optional] |
|**fileName** | **String** | The name of the generated file. The default is &#x60;MuxStream.key&#x60; with the extension suffix corresponding to the &#x60;MuxStream.container&#x60;. Individual segments also have an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as &#x60;\&quot;mux_stream0000000123.ts\&quot;&#x60;. |  [optional] |
|**key** | **String** | A unique key for this multiplexed stream. HLS media manifests will be named &#x60;MuxStream.key&#x60; with the &#x60;\&quot;.m3u8\&quot;&#x60; extension suffix. |  [optional] |
|**segmentSettings** | [**SegmentSettings**](SegmentSettings.md) |  |  [optional] |




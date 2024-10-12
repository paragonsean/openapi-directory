

# IndexStreamTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chunkSize** | [**ChunkSizeEnum**](#ChunkSizeEnum) | &lt;strong&gt;The &lt;em&gt;chunk_size&lt;/em&gt; parameter is deprecated. To set the chunk size of a stream target, use the POST /stream_targets/[stream_target_id]/properties endpoint.&lt;/strong&gt; Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The segment duration for HLS encoding. The default is &lt;strong&gt;10&lt;/strong&gt;. |  [optional] |
|**connectionCode** | **String** | A six-character, alphanumeric string that allows Wowza Streaming Engine to send a transcoded stream to a &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; or for the Wowza GoCoder app to send an encoded stream to a &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The code can be used once and expires 24 hours after it&#39;s created. |  [optional] |
|**connectionCodeExpiresAt** | **OffsetDateTime** | The date and time that the &lt;em&gt;connection_code&lt;/em&gt; expires. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time that the stream target was created. |  [optional] |
|**hdsPlaybackUrl** | **String** | The web address that the target uses to play Adobe HDS streams. |  [optional] |
|**hlsPlaybackUrl** | **String** | Only for targets whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The web address that the target uses to play Apple HLS streams. |  [optional] |
|**id** | **String** | The unique alphanumeric string that identifies the stream target. |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. Choose a location as close as possible to your video source. |  [optional] |
|**name** | **String** | A descriptive name for the stream target. Maximum 255 characters. |  [optional] |
|**primaryUrl** | **String** | The primary ingest URL of the target. |  [optional] |
|**provider** | **String** | The CDN for the target. &lt;br /&gt;&lt;br /&gt;Required for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. Valid values for &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt;, &lt;strong&gt;akamai_rtmp&lt;/strong&gt;, &lt;strong&gt;limelight&lt;/strong&gt;, &lt;strong&gt;rtmp&lt;/strong&gt;, and &lt;strong&gt;ustream&lt;/strong&gt;. Values can be appended with **_mock** to use in the sandbox environment. &lt;br /&gt;&lt;br /&gt;Valid values for &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt; (default), &lt;strong&gt;akamai_legacy_rtmp&lt;/strong&gt;, and &lt;strong&gt;wowza&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;&lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; defaults to and must be &lt;strong&gt;wowza&lt;/strong&gt;. |  [optional] |
|**rtmpPlaybackUrl** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The web address that the target uses to play RTMP streams. |  [optional] |
|**streamName** | **String** | The name of the stream being ingested into the target. Returned for all targets except those whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and whose &lt;em&gt;source_delivery_method&lt;/em&gt; is **pull**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; is a Wowza CDN target. &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; is an ultra low latency Wowza stream target. &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; (the default) is an external, third-party destination. &lt;!--and &lt;strong&gt;FacebookStreamTarget&lt;/strong&gt; (a Facebook Live target).--&gt; |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time that the stream target was updated. |  [optional] |
|**username** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; **akamai_cupertino**. The username or ID that the target uses for RTMP authentication. |  [optional] |



## Enum: ChunkSizeEnum

| Name | Value |
|---- | -----|
| _2 | &quot;2&quot; |
| _4 | &quot;4&quot; |
| _6 | &quot;6&quot; |
| _8 | &quot;8&quot; |
| _10 | &quot;10&quot; |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| ASIA_PACIFIC_AUSTRALIA | &quot;asia_pacific_australia&quot; |
| ASIA_PACIFIC_JAPAN | &quot;asia_pacific_japan&quot; |
| ASIA_PACIFIC_SINGAPORE | &quot;asia_pacific_singapore&quot; |
| ASIA_PACIFIC_TAIWAN | &quot;asia_pacific_taiwan&quot; |
| EU_BELGIUM | &quot;eu_belgium&quot; |
| EU_GERMANY | &quot;eu_germany&quot; |
| EU_IRELAND | &quot;eu_ireland&quot; |
| SOUTH_AMERICA_BRAZIL | &quot;south_america_brazil&quot; |
| US_CENTRAL_IOWA | &quot;us_central_iowa&quot; |
| US_EAST_S_CAROLINA | &quot;us_east_s_carolina&quot; |
| US_EAST_VIRGINIA | &quot;us_east_virginia&quot; |
| US_WEST_CALIFORNIA | &quot;us_west_california&quot; |
| US_WEST_OREGON | &quot;us_west_oregon&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WOWZA_STREAM_TARGET | &quot;WowzaStreamTarget&quot; |
| ULTRA_LOW_LATENCY_STREAM_TARGET | &quot;UltraLowLatencyStreamTarget&quot; |
| CUSTOM_STREAM_TARGET | &quot;CustomStreamTarget&quot; |




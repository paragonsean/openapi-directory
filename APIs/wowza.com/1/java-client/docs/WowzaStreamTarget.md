

# WowzaStreamTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chunkSize** | [**ChunkSizeEnum**](#ChunkSizeEnum) | &lt;strong&gt;The &lt;em&gt;chunk_size&lt;/em&gt; parameter is deprecated. To set the chunk size of a stream target, use the POST /stream_targets/[stream_target_id]/properties endpoint.&lt;/strong&gt; Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The segment duration for HLS encoding. The default is &lt;strong&gt;10&lt;/strong&gt;. |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. Choose a location as close as possible to your video source. |  |
|**name** | **String** | A descriptive name for the stream target. Maximum 255 characters. |  |
|**provider** | **String** | The CDN for the target. &lt;br /&gt;&lt;br /&gt;Required for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. Valid values for &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt;, &lt;strong&gt;akamai_rtmp&lt;/strong&gt;, &lt;strong&gt;limelight&lt;/strong&gt;, &lt;strong&gt;rtmp&lt;/strong&gt;, and &lt;strong&gt;ustream&lt;/strong&gt;. Values can be appended with **_mock** to use in the sandbox environment. &lt;br /&gt;&lt;br /&gt;Valid values for &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt; (default), &lt;strong&gt;akamai_legacy_rtmp&lt;/strong&gt;, and &lt;strong&gt;wowza&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;&lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; defaults to and must be &lt;strong&gt;wowza&lt;/strong&gt;. |  [optional] |
|**type** | **String** | &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; is a Wowza CDN target. &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; is an ultra low latency Wowza stream target. &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; (the default) is an external, third-party destination. &lt;!--and &lt;strong&gt;FacebookStreamTarget&lt;/strong&gt; (a Facebook Live target).--&gt; |  [optional] |
|**useCors** | **Boolean** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. CORS, or cross-origin resource sharing, allows streams to be sent to providers such as Peer5, Viblast, and Streamroot, which implement a peer-to-peer grid delivery system. |  [optional] |
|**useHttps** | **Boolean** | &lt;strong&gt;The &lt;em&gt;use_https&lt;/em&gt; parameter is deprecated. Use the POST /stream_targets/[&lt;em&gt;stream_target_id&lt;/em&gt;]/properties endpoint and the &lt;em&gt;relative_playlists&lt;/em&gt; parameter instead.&lt;/strong&gt; |  [optional] |
|**useSecureIngest** | **Boolean** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. If &lt;strong&gt;true&lt;/strong&gt;, generates a &lt;em&gt;secure_ingest_query_param&lt;/em&gt; to securely deliver the stream from the transcoder to the provider. |  [optional] |



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




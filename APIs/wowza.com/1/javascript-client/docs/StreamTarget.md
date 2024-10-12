# WowzaStreamingCloudRestApiReferenceDocumentation.StreamTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupUrl** | **String** | The backup ingest URL for a target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; or &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. | [optional] 
**chunkSize** | **String** | &lt;strong&gt;The &lt;em&gt;chunk_size&lt;/em&gt; parameter is deprecated. To set the chunk size of a stream target, use the POST /stream_targets/[stream_target_id]/properties endpoint.&lt;/strong&gt; Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The segment duration for HLS encoding. The default is &lt;strong&gt;10&lt;/strong&gt;. | [optional] 
**connectionCode** | **String** | A six-character, alphanumeric string that allows Wowza Streaming Engine to send a transcoded stream to a &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; or for the Wowza GoCoder app to send an encoded stream to a &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The code can be used once and expires 24 hours after it&#39;s created. | [optional] 
**connectionCodeExpiresAt** | **Date** | The date and time that the &lt;em&gt;connection_code&lt;/em&gt; expires. | [optional] 
**createdAt** | **Date** | The date and time that the stream target was created. | [optional] 
**enableHls** | **Boolean** | Returned only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. Indicates whether Apple HLS playback is enabled for the stream target. | [optional] 
**enabled** | **Boolean** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. If &lt;strong&gt;true&lt;/strong&gt; (the default), the source stream is ready to be ingested. If **false**, the source stream won&#39;t be ingested by the target&#39;s origin server. | [optional] 
**hdsPlaybackUrl** | **String** | The web address that the target uses to play Adobe HDS streams. | [optional] 
**hlsPlaybackUrl** | **String** | Only for targets whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. The web address that the target uses to play Apple HLS streams. | [optional] 
**id** | **String** | The unique alphanumeric string that identifies the stream target. | [optional] 
**ingestIpWhitelist** | **[String]** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and &lt;em&gt;source_delivery_method&lt;/em&gt; is **push**. A list of IP addresses that can be used to connect to the target&#39;s origin server. | [optional] 
**location** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. Choose a location as close as possible to your video source. | [optional] 
**name** | **String** | A descriptive name for the stream target. Maximum 255 characters. | [optional] 
**password** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; **akamai_cupertino**. A &lt;em&gt;username&lt;/em&gt; must also be present. The password associated with the target username for RTMP authentication. | [optional] 
**playbackUrls** | [**HashOfPlaybackURLs**](HashOfPlaybackURLs.md) |  | [optional] 
**primaryUrl** | **String** | The primary ingest URL of the target. | [optional] 
**provider** | **String** | The CDN for the target. &lt;br /&gt;&lt;br /&gt;Required for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. Valid values for &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt;, &lt;strong&gt;akamai_rtmp&lt;/strong&gt;, &lt;strong&gt;limelight&lt;/strong&gt;, &lt;strong&gt;rtmp&lt;/strong&gt;, and &lt;strong&gt;ustream&lt;/strong&gt;. Values can be appended with **_mock** to use in the sandbox environment. &lt;br /&gt;&lt;br /&gt;Valid values for &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; are &lt;strong&gt;akamai&lt;/strong&gt;, &lt;strong&gt;akamai_cupertino&lt;/strong&gt; (default), &lt;strong&gt;akamai_legacy_rtmp&lt;/strong&gt;, and &lt;strong&gt;wowza&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;&lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; defaults to and must be &lt;strong&gt;wowza&lt;/strong&gt;. | [optional] 
**regionOverride** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and &lt;em&gt;source_delivery_method&lt;/em&gt; is **pull**. The location of the stream target&#39;s origin server. If unspecified, Wowza Streaming Cloud determines the optimal region for the origin server. | [optional] 
**rtmpPlaybackUrl** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt;. The web address that the target uses to play RTMP streams. | [optional] 
**secureIngestQueryParam** | **String** | Only for targets whose &lt;em&gt;use_secure_ingest&lt;/em&gt; is &lt;strong&gt;true&lt;/strong&gt;. The query parameter needed for secure stream delivery between the transcoder and the target. | [optional] 
**sourceDeliveryMethod** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The type of connection between the stream source and the stream target. **push** instructs the source to push the stream to the stream target. **pull** instructs the stream target to pull the stream from the source. | [optional] 
**sourceUrl** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and &lt;em&gt;source_delivery_method&lt;/em&gt; is **pull**. The URL of a source IP camera or encoder connecting to the stream target. | [optional] 
**streamName** | **String** | The name of the stream being ingested into the target. Returned for all targets except those whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; and whose &lt;em&gt;source_delivery_method&lt;/em&gt; is **pull**. | [optional] 
**type** | **String** | &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; is a Wowza CDN target. &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; is an ultra low latency Wowza stream target. &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; (the default) is an external, third-party destination. &lt;!--and &lt;strong&gt;FacebookStreamTarget&lt;/strong&gt; (a Facebook Live target).--&gt; | [optional] 
**updatedAt** | **Date** | The date and time that the stream target was updated. | [optional] 
**useCors** | **Boolean** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. CORS, or cross-origin resource sharing, allows streams to be sent to providers such as Peer5, Viblast, and Streamroot, which implement a peer-to-peer grid delivery system. | [optional] 
**useHttps** | **Boolean** | &lt;strong&gt;The &lt;em&gt;use_https&lt;/em&gt; parameter is deprecated. Use the POST /stream_targets/[&lt;em&gt;stream_target_id&lt;/em&gt;]/properties endpoint and the &lt;em&gt;relative_playlists&lt;/em&gt; parameter instead.&lt;/strong&gt; | [optional] 
**useSecureIngest** | **Boolean** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. If &lt;strong&gt;true&lt;/strong&gt;, generates a &lt;em&gt;secure_ingest_query_param&lt;/em&gt; to securely deliver the stream from the transcoder to the provider. | [optional] 
**username** | **String** | Only for targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; and &lt;em&gt;provider&lt;/em&gt; is &lt;em&gt;not&lt;/em&gt; **akamai_cupertino**. The username or ID that the target uses for RTMP authentication. | [optional] 



## Enum: ChunkSizeEnum


* `2` (value: `"2"`)

* `4` (value: `"4"`)

* `6` (value: `"6"`)

* `8` (value: `"8"`)

* `10` (value: `"10"`)





## Enum: LocationEnum


* `asia_pacific_australia` (value: `"asia_pacific_australia"`)

* `asia_pacific_japan` (value: `"asia_pacific_japan"`)

* `asia_pacific_singapore` (value: `"asia_pacific_singapore"`)

* `asia_pacific_taiwan` (value: `"asia_pacific_taiwan"`)

* `eu_belgium` (value: `"eu_belgium"`)

* `eu_germany` (value: `"eu_germany"`)

* `eu_ireland` (value: `"eu_ireland"`)

* `south_america_brazil` (value: `"south_america_brazil"`)

* `us_central_iowa` (value: `"us_central_iowa"`)

* `us_east_s_carolina` (value: `"us_east_s_carolina"`)

* `us_east_virginia` (value: `"us_east_virginia"`)

* `us_west_california` (value: `"us_west_california"`)

* `us_west_oregon` (value: `"us_west_oregon"`)





## Enum: RegionOverrideEnum


* `azure-westus` (value: `"azure-westus"`)

* `azure-eastus2` (value: `"azure-eastus2"`)

* `azure-northeurope` (value: `"azure-northeurope"`)

* `null` (value: `"null"`)





## Enum: SourceDeliveryMethodEnum


* `push` (value: `"push"`)

* `pull` (value: `"pull"`)





## Enum: TypeEnum


* `WowzaStreamTarget` (value: `"WowzaStreamTarget"`)

* `UltraLowLatencyStreamTarget` (value: `"UltraLowLatencyStreamTarget"`)

* `CustomStreamTarget` (value: `"CustomStreamTarget"`)





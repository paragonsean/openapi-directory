# MuxApi.Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspectRatio** | **String** | The aspect ratio of the asset in the form of &#x60;width:height&#x60;, for example &#x60;16:9&#x60;. | [optional] 
**createdAt** | **String** | Time the Asset was created, defined as a Unix timestamp (seconds since epoch). | [optional] 
**duration** | **Number** | The duration of the asset in seconds (max duration for a single asset is 12 hours). | [optional] 
**encodingTier** | **String** | The encoding tier informs the cost, quality, and available platform features for the asset. By default the &#x60;smart&#x60; encoding tier is used. | [optional] 
**errors** | [**AssetErrors**](AssetErrors.md) |  | [optional] 
**id** | **String** | Unique identifier for the Asset. Max 255 characters. | [optional] 
**isLive** | **Boolean** | Indicates whether the live stream that created this asset is currently &#x60;active&#x60; and not in &#x60;idle&#x60; state. This is an optional parameter added when the asset is created from a live stream. | [optional] 
**liveStreamId** | **String** | Unique identifier for the live stream. This is an optional parameter added when the asset is created from a live stream. | [optional] 
**master** | [**AssetMaster**](AssetMaster.md) |  | [optional] 
**masterAccess** | **String** |  | [optional] [default to &#39;none&#39;]
**maxResolutionTier** | **String** | Max resolution tier can be used to control the maximum &#x60;resolution_tier&#x60; your asset is encoded, stored, and streamed at. If not set, this defaults to &#x60;1080p&#x60;. | [optional] 
**maxStoredFrameRate** | **Number** | The maximum frame rate that has been stored for the asset. The asset may be delivered at lower frame rates depending on the device and bandwidth, however it cannot be delivered at a higher value than is stored. This field may return -1 if the frame rate of the input cannot be reliably determined. | [optional] 
**maxStoredResolution** | **String** | This field is deprecated. Please use &#x60;resolution_tier&#x60; instead. The maximum resolution that has been stored for the asset. The asset may be delivered at lower resolutions depending on the device and bandwidth, however it cannot be delivered at a higher value than is stored. | [optional] 
**mp4Support** | **String** |  | [optional] [default to &#39;none&#39;]
**nonStandardInputReasons** | [**AssetNonStandardInputReasons**](AssetNonStandardInputReasons.md) |  | [optional] 
**normalizeAudio** | **Boolean** | Normalize the audio track loudness level. This parameter is only applicable to on-demand (not live) assets. | [optional] [default to false]
**passthrough** | **String** | Arbitrary user-supplied metadata set for the asset. Max 255 characters. | [optional] 
**perTitleEncode** | **Boolean** |  | [optional] 
**playbackIds** | [**[PlaybackID]**](PlaybackID.md) | An array of Playback ID objects. Use these to create HLS playback URLs. See [Play your videos](https://docs.mux.com/guides/video/play-your-videos) for more details. | [optional] 
**recordingTimes** | [**[AssetRecordingTimesInner]**](AssetRecordingTimesInner.md) | An array of individual live stream recording sessions. A recording session is created on each encoder connection during the live stream. Additionally any time slate media is inserted during brief interruptions in the live stream media or times when the live streaming software disconnects, a recording session representing the slate media will be added with a \&quot;slate\&quot; type. | [optional] 
**resolutionTier** | **String** | The resolution tier that the asset was ingested at, affecting billing for ingest &amp; storage. This field also represents the highest resolution tier that the content can be delivered at, however the actual resolution may be lower depending on the device, bandwidth, and exact resolution of the uploaded asset. | [optional] 
**sourceAssetId** | **String** | Asset Identifier of the video used as the source for creating the clip. | [optional] 
**staticRenditions** | [**AssetStaticRenditions**](AssetStaticRenditions.md) |  | [optional] 
**status** | **String** | The status of the asset. | [optional] 
**test** | **Boolean** | True means this live stream is a test asset. A test asset can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test assets created. Test assets are watermarked with the Mux logo, limited to 10 seconds, and deleted after 24 hrs. | [optional] 
**tracks** | [**[Track]**](Track.md) | The individual media tracks that make up an asset. | [optional] 
**uploadId** | **String** | Unique identifier for the Direct Upload. This is an optional parameter added when the asset is created from a direct upload. | [optional] 



## Enum: EncodingTierEnum


* `smart` (value: `"smart"`)

* `baseline` (value: `"baseline"`)





## Enum: MasterAccessEnum


* `temporary` (value: `"temporary"`)

* `none` (value: `"none"`)





## Enum: MaxResolutionTierEnum


* `1080p` (value: `"1080p"`)

* `1440p` (value: `"1440p"`)

* `2160p` (value: `"2160p"`)





## Enum: MaxStoredResolutionEnum


* `Audio only` (value: `"Audio only"`)

* `SD` (value: `"SD"`)

* `HD` (value: `"HD"`)

* `FHD` (value: `"FHD"`)

* `UHD` (value: `"UHD"`)





## Enum: Mp4SupportEnum


* `standard` (value: `"standard"`)

* `none` (value: `"none"`)





## Enum: ResolutionTierEnum


* `audio-only` (value: `"audio-only"`)

* `720p` (value: `"720p"`)

* `1080p` (value: `"1080p"`)

* `1440p` (value: `"1440p"`)

* `2160p` (value: `"2160p"`)





## Enum: StatusEnum


* `preparing` (value: `"preparing"`)

* `ready` (value: `"ready"`)

* `errored` (value: `"errored"`)





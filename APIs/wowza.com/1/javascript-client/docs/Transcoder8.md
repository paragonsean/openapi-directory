# WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder8

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingMode** | **String** | The billing mode for the transcoder. The default is &lt;strong&gt;pay_as_you_go&lt;/strong&gt;. | 
**broadcastLocation** | **String** | The location where Wowza Streaming Cloud transcodes your stream. Choose a location as close as possible to your video source. | 
**bufferSize** | **Number** | The size, in milliseconds, of the incoming buffer. &lt;strong&gt;0&lt;/strong&gt; means no buffer. The default is &lt;strong&gt;4000&lt;/strong&gt; (4 seconds). | [optional] 
**closedCaptionType** | **String** | The type of closed caption data being passed from the source. The default, &lt;strong&gt;none&lt;/strong&gt;, indicates that no data is being provided. &lt;strong&gt;cea&lt;/strong&gt; indicates that a CEA closed captioning data stream is being provided. &lt;strong&gt;on_text&lt;/strong&gt; indicates that an onTextData closed captioning data stream is being provided. &lt;strong&gt;both&lt;/strong&gt; indicates that both CEA and onTextData closed captioing data streams are being provided. | [optional] 
**deliveryMethod** | **String** | The type of connection between the source encoder and the transcoder. The default, &lt;strong&gt;pull&lt;/strong&gt;, instructs the transcoder to pull the video from the source. &lt;strong&gt;push&lt;/strong&gt; instructs the source to push the stream to the transcoder. &lt;strong&gt;cdn&lt;/strong&gt; uses a stream source to deliver the stream to the transcoder. | 
**deliveryProtocols** | **[String]** | An array of playback protocols enabled for this transcoder. By default, &lt;strong&gt;rtmp&lt;/strong&gt;, &lt;strong&gt;rtsp&lt;/strong&gt;, and &lt;strong&gt;wowz&lt;/strong&gt; are returned. | [optional] 
**description** | **String** | An optional description of the transcoder. | [optional] 
**disableAuthentication** | **Boolean** | Authentication is required by default for RTMP and RTSP push connections from a video source to the transcoder. Specify &lt;strong&gt;true&lt;/strong&gt; to disable authentication with the video source. | [optional] 
**idleTimeout** | **Number** | The amount of idle time, in seconds, before the transcoder automatically shuts down. Valid values are the integers &lt;strong&gt;0&lt;/strong&gt; (never shuts down) to &lt;strong&gt;172800&lt;/strong&gt; (48 hours). The default is &lt;strong&gt;1200&lt;/strong&gt; (20 minutes). | [optional] 
**lowLatency** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, turns off the sort packet buffer and speeds the time it takes to decode and deliver video data to the player. The default is &lt;strong&gt;false&lt;/strong&gt;. | [optional] 
**name** | **String** | A descriptive name for the transcoder. Maximum 200 characters. | 
**password** | **String** | A password for authenticating an RTMP or RTSP push connection. Can contain only uppercase and lowercase letters; numbers; and the period (.), underscore (_), and hyphen (-) characters. No other special characters can be used. | [optional] 
**playMaximumConnections** | **Number** | The number of users who are allowed to connect directly to the transcoder. | [optional] 
**protocol** | **String** | The transport protocol for the source video. The default is &lt;strong&gt;rtmp&lt;/strong&gt;. | 
**recording** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, creates a recording of the transcoded output. The default is &lt;strong&gt;false&lt;/strong&gt;. | [optional] 
**sourceUrl** | **String** | For the &lt;em&gt;delivery_method&lt;/em&gt; &lt;strong&gt;pull&lt;/strong&gt;. Enter the source&#39;s web address without the preceding protocol or the trailing slash (/). | [optional] 
**streamExtension** | **String** | For the &lt;em&gt;delivery_method&lt;/em&gt; &lt;strong&gt;push&lt;/strong&gt;. Some encoders append an extension to their stream names. If the device you&#39;re using does this, enter the extension. | [optional] 
**streamSmoother** | **Boolean** | A dynamic buffer that helps stabilize streams in rough network conditions, but adds latency. Specify &lt;strong&gt;true&lt;/strong&gt; to enable stream smoothing. The default is &lt;strong&gt;false&lt;/strong&gt;. | [optional] 
**streamSourceId** | **String** | For the &lt;em&gt;delivery_method&lt;/em&gt; &lt;strong&gt;cdn&lt;/strong&gt;. The alphanumeric string that identifies the stream source that you want to use to deliver the stream to the transcoder. | [optional] 
**suppressStreamTargetStart** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, disables stream targets when the transcoder starts. If &lt;strong&gt;false&lt;/strong&gt; (the default), the targets start when the transcoder starts. | [optional] 
**transcoderType** | **String** | The type of transcoder, either &lt;strong&gt;transcoded&lt;/strong&gt; for streams that are transcoded into adaptive bitrate renditions or &lt;strong&gt;passthrough&lt;/strong&gt; for streams that aren&#39;t processed by the transcoder. The default is &lt;strong&gt;transcoded&lt;/strong&gt;. | 
**username** | **String** | A username for authenticating an RTMP or RTSP push connection. Can contain only uppercase and lowercase letters; numbers; and the period (.), underscore (_), and hyphen (-) characters. No other special characters can be used. | [optional] 
**videoFallback** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, black video plays if the video source disconnects from the transcoder. If &lt;strong&gt;false&lt;/strong&gt; (the default), a stream-not-available message appears. Works only with stream targets whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. | [optional] 
**watermark** | **Boolean** | Embeds an image into the transcoded stream for copyright protection. Specify &lt;strong&gt;true&lt;/strong&gt; to embed a watermark image. | [optional] 
**watermarkHeight** | **Number** | The height, in pixels, of the watermark image. If blank, Wowza Streaming Cloud uses the original image height. | [optional] 
**watermarkImage** | **String** | A Base64-encoded string representation of a GIF, JPEG, or PNG image that is embedded in all bitrate renditions of the stream. Watermark image files must be 2.5 MB or smaller. | [optional] 
**watermarkOpacity** | **Number** | The opacity, or percentage of transparency, of the watermark. &lt;strong&gt;0&lt;/strong&gt; is fully transparent; &lt;strong&gt;100&lt;/strong&gt; is fully opaque. | [optional] 
**watermarkPosition** | **String** | The corner of the video frame in which you want the watermark to appear. The default is &lt;strong&gt;top-left&lt;/strong&gt;. | [optional] 
**watermarkWidth** | **Number** | The width, in pixels, of the watermark image. If blank, Wowza Streaming Cloud uses the original image width. | [optional] 



## Enum: BillingModeEnum


* `pay_as_you_go` (value: `"pay_as_you_go"`)

* `twentyfour_seven` (value: `"twentyfour_seven"`)





## Enum: BroadcastLocationEnum


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





## Enum: BufferSizeEnum


* `0` (value: `0`)

* `1000` (value: `1000`)

* `2000` (value: `2000`)

* `3000` (value: `3000`)

* `4000` (value: `4000`)

* `5000` (value: `5000`)

* `6000` (value: `6000`)

* `7000` (value: `7000`)

* `8000` (value: `8000`)





## Enum: ClosedCaptionTypeEnum


* `none` (value: `"none"`)

* `cea` (value: `"cea"`)

* `on_text` (value: `"on_text"`)

* `both` (value: `"both"`)





## Enum: DeliveryMethodEnum


* `pull` (value: `"pull"`)

* `cdn` (value: `"cdn"`)

* `push` (value: `"push"`)





## Enum: PlayMaximumConnectionsEnum


* `10` (value: `10`)

* `11` (value: `11`)

* `12` (value: `12`)

* `13` (value: `13`)

* `14` (value: `14`)

* `15` (value: `15`)

* `16` (value: `16`)

* `17` (value: `17`)

* `18` (value: `18`)

* `19` (value: `19`)

* `20` (value: `20`)

* `21` (value: `21`)

* `22` (value: `22`)

* `23` (value: `23`)

* `24` (value: `24`)

* `25` (value: `25`)

* `26` (value: `26`)

* `27` (value: `27`)

* `28` (value: `28`)

* `29` (value: `29`)

* `30` (value: `30`)

* `31` (value: `31`)

* `32` (value: `32`)

* `33` (value: `33`)

* `34` (value: `34`)

* `35` (value: `35`)

* `36` (value: `36`)

* `37` (value: `37`)

* `38` (value: `38`)

* `39` (value: `39`)

* `40` (value: `40`)

* `41` (value: `41`)

* `42` (value: `42`)

* `43` (value: `43`)

* `44` (value: `44`)

* `45` (value: `45`)

* `46` (value: `46`)

* `47` (value: `47`)

* `48` (value: `48`)

* `49` (value: `49`)

* `50` (value: `50`)

* `51` (value: `51`)

* `52` (value: `52`)

* `53` (value: `53`)

* `54` (value: `54`)

* `55` (value: `55`)

* `56` (value: `56`)

* `57` (value: `57`)

* `58` (value: `58`)

* `59` (value: `59`)

* `60` (value: `60`)

* `61` (value: `61`)

* `62` (value: `62`)

* `63` (value: `63`)

* `64` (value: `64`)

* `65` (value: `65`)

* `66` (value: `66`)

* `67` (value: `67`)

* `68` (value: `68`)

* `69` (value: `69`)

* `70` (value: `70`)

* `71` (value: `71`)

* `72` (value: `72`)

* `73` (value: `73`)

* `74` (value: `74`)

* `75` (value: `75`)

* `76` (value: `76`)

* `77` (value: `77`)

* `78` (value: `78`)

* `79` (value: `79`)

* `80` (value: `80`)

* `81` (value: `81`)

* `82` (value: `82`)

* `83` (value: `83`)

* `84` (value: `84`)

* `85` (value: `85`)

* `86` (value: `86`)

* `87` (value: `87`)

* `88` (value: `88`)

* `89` (value: `89`)

* `90` (value: `90`)

* `91` (value: `91`)

* `92` (value: `92`)

* `93` (value: `93`)

* `94` (value: `94`)

* `95` (value: `95`)

* `96` (value: `96`)

* `97` (value: `97`)

* `98` (value: `98`)

* `99` (value: `99`)

* `100` (value: `100`)





## Enum: ProtocolEnum


* `rtmp` (value: `"rtmp"`)

* `rtsp` (value: `"rtsp"`)





## Enum: TranscoderTypeEnum


* `transcoded` (value: `"transcoded"`)

* `passthrough` (value: `"passthrough"`)





## Enum: WatermarkOpacityEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)

* `9` (value: `9`)

* `10` (value: `10`)

* `11` (value: `11`)

* `12` (value: `12`)

* `13` (value: `13`)

* `14` (value: `14`)

* `15` (value: `15`)

* `16` (value: `16`)

* `17` (value: `17`)

* `18` (value: `18`)

* `19` (value: `19`)

* `20` (value: `20`)

* `21` (value: `21`)

* `22` (value: `22`)

* `23` (value: `23`)

* `24` (value: `24`)

* `25` (value: `25`)

* `26` (value: `26`)

* `27` (value: `27`)

* `28` (value: `28`)

* `29` (value: `29`)

* `30` (value: `30`)

* `31` (value: `31`)

* `32` (value: `32`)

* `33` (value: `33`)

* `34` (value: `34`)

* `35` (value: `35`)

* `36` (value: `36`)

* `37` (value: `37`)

* `38` (value: `38`)

* `39` (value: `39`)

* `40` (value: `40`)

* `41` (value: `41`)

* `42` (value: `42`)

* `43` (value: `43`)

* `44` (value: `44`)

* `45` (value: `45`)

* `46` (value: `46`)

* `47` (value: `47`)

* `48` (value: `48`)

* `49` (value: `49`)

* `50` (value: `50`)

* `51` (value: `51`)

* `52` (value: `52`)

* `53` (value: `53`)

* `54` (value: `54`)

* `55` (value: `55`)

* `56` (value: `56`)

* `57` (value: `57`)

* `58` (value: `58`)

* `59` (value: `59`)

* `60` (value: `60`)

* `61` (value: `61`)

* `62` (value: `62`)

* `63` (value: `63`)

* `64` (value: `64`)

* `65` (value: `65`)

* `66` (value: `66`)

* `67` (value: `67`)

* `68` (value: `68`)

* `69` (value: `69`)

* `70` (value: `70`)

* `71` (value: `71`)

* `72` (value: `72`)

* `73` (value: `73`)

* `74` (value: `74`)

* `75` (value: `75`)

* `76` (value: `76`)

* `77` (value: `77`)

* `78` (value: `78`)

* `79` (value: `79`)

* `80` (value: `80`)

* `81` (value: `81`)

* `82` (value: `82`)

* `83` (value: `83`)

* `84` (value: `84`)

* `85` (value: `85`)

* `86` (value: `86`)

* `87` (value: `87`)

* `88` (value: `88`)

* `89` (value: `89`)

* `90` (value: `90`)

* `91` (value: `91`)

* `92` (value: `92`)

* `93` (value: `93`)

* `94` (value: `94`)

* `95` (value: `95`)

* `96` (value: `96`)

* `97` (value: `97`)

* `98` (value: `98`)

* `99` (value: `99`)

* `100` (value: `100`)





## Enum: WatermarkPositionEnum


* `top-left` (value: `"top-left"`)

* `top-right` (value: `"top-right"`)

* `bottom-left` (value: `"bottom-left"`)

* `bottom-right` (value: `"bottom-right"`)







# LiveStream7


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspectRatioHeight** | **Integer** | The height, in pixels, of the video source. Should correspond to a widescreen (16:9) or standard (4:3) aspect ratio and be divisible by 8. |  |
|**aspectRatioWidth** | **Integer** | The width, in pixels, of the video source. Should correspond to a widescreen (16:9) or standard (4:3) aspect ratio and be divisible by 8. |  |
|**closedCaptionType** | [**ClosedCaptionTypeEnum**](#ClosedCaptionTypeEnum) | The type of closed caption data being passed from the source. The default, &lt;strong&gt;none&lt;/strong&gt;, indicates that no data is being provided. &lt;strong&gt;cea&lt;/strong&gt; indicates that a CEA closed captioning data stream is being provided. &lt;strong&gt;on_text&lt;/strong&gt; indicates that an onTextData closed captioning data stream is being provided. &lt;strong&gt;both&lt;/strong&gt; indicates that both CEA and onTextData closed captioing data streams are being provided. |  [optional] |
|**deliveryMethod** | [**DeliveryMethodEnum**](#DeliveryMethodEnum) | The type of connection between the video source and the transcoder. The default, &lt;strong&gt;pull&lt;/strong&gt;, instructs the transcoder to pull the video from the source. &lt;strong&gt;push&lt;/strong&gt; instructs the source to push the stream to the transcoder. &lt;strong&gt;cdn&lt;/strong&gt; uses a stream source to deliver the stream to the transcoder. |  [optional] |
|**deliveryProtocols** | **List&lt;String&gt;** | An array of direct delivery protocols enabled for this live stream. By default, &lt;strong&gt;rtmp&lt;/strong&gt;, &lt;strong&gt;rtsp&lt;/strong&gt;, and &lt;strong&gt;wowz&lt;/strong&gt; are enabled. |  [optional] |
|**disableAuthentication** | **Boolean** | Authentication is required by default for RTMP and RTSP push connections from a video source to Wowza Streaming Cloud. Specify &lt;strong&gt;true&lt;/strong&gt; to disable authentication with the video source. |  [optional] |
|**encoder** | [**EncoderEnum**](#EncoderEnum) | The video source for the live stream. Choose the type of camera or encoder you&#39;re using to connect to the Wowza Streaming Cloud transcoder. If your specific device isn&#39;t listed, choose &lt;strong&gt;ipcamera&lt;/strong&gt;, &lt;strong&gt;other_rtmp&lt;/strong&gt;, or &lt;strong&gt;other_rtsp&lt;/strong&gt;. |  |
|**hostedPageDescription** | **String** | A description that appears on the hosted page below the player. Can&#39;t include custom HTML, JavaScript, or other tags. |  [optional] |
|**hostedPageLogoImage** | **String** | A Base64-encoded string representation of a GIF, JPEG, or PNG logo file that that appears in the upper-left corner of the hosted page. Logo file must be 2.5 MB or smaller. |  [optional] |
|**hostedPageSharingIcons** | **Boolean** | Icons that let viewers share the stream on Facebook, Google+, Twitter, and by email. The default, &lt;strong&gt;true&lt;/strong&gt;, includes sharing icons on the hosted page. Specify &lt;strong&gt;false&lt;/strong&gt; to omit sharing icons. |  [optional] |
|**hostedPageTitle** | **String** | A title for the page that appears above the player. Can&#39;t include custom HTML, JavaScript, or other tags. |  [optional] |
|**name** | **String** | A descriptive name for the live stream. Maximum 200 characters. |  |
|**password** | **String** | A password for authenticating an RTMP or RTSP push connection. Can contain only uppercase and lowercase letters; numbers; and the period (.), underscore (_), and hyphen (-) characters. No other special characters can be used. |  [optional] |
|**playerCountdown** | **Boolean** | A clock that appears in the player before the event and counts down to the start of the stream. Specify &lt;strong&gt;true&lt;/strong&gt; to display the countdown clock. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**playerCountdownAt** | **OffsetDateTime** | The date and time that the event starts, used by the countdown clock. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt;, where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. |  [optional] |
|**playerLogoImage** | **String** | A Base64-encoded string representation of a GIF, JPEG, or PNG logo file that appears partially transparent in a corner of the player throughout playback. Logo file must be 2.5 MB or smaller. |  [optional] |
|**playerLogoPosition** | [**PlayerLogoPositionEnum**](#PlayerLogoPositionEnum) | The corner of the player in which you want the player logo to appear. The default is &lt;strong&gt;top-left&lt;/strong&gt;. |  [optional] |
|**playerResponsive** | **Boolean** | A player whose size adjusts according to the device on which it&#39;s being viewed. If &lt;strong&gt;true&lt;/strong&gt;, creates a responsive player. If &lt;strong&gt;false&lt;/strong&gt;, specify a &lt;em&gt;player_width&lt;/em&gt;. |  [optional] |
|**playerType** | **String** | The player you want to use. Valid values are &lt;strong&gt;original_html5&lt;/strong&gt;, which provides HTML5 playback and falls back to Flash on older browsers, and &lt;strong&gt;wowza_player&lt;/strong&gt;, which provides HTML5 playback over Apple HLS. &lt;strong&gt;wowza_player&lt;/strong&gt; requires that &lt;strong&gt;target_delivery_protocol&lt;/strong&gt; be &lt;strong&gt;hls-https&lt;/strong&gt; and &lt;strong&gt;closed_caption_type&lt;/strong&gt; be &lt;strong&gt;none&lt;/strong&gt;. The default is &lt;strong&gt;original_html5&lt;/strong&gt;. |  [optional] |
|**playerVideoPosterImage** | **String** | A Base64-encoded string representation of a GIF, JPEG, or PNG poster image that appears in the player before the stream begins. Poster image files must be 2.5 MB or smaller. |  [optional] |
|**playerWidth** | **Integer** | The width, in pixels, of a fixed-size player. The default is &lt;strong&gt;640&lt;/strong&gt;. |  [optional] |
|**recording** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, creates a recording of the live stream. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**removeHostedPageLogoImage** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, removes the logo file from the hosted page. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**removePlayerLogoImage** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, removes the logo file from the player. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**removePlayerVideoPosterImage** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, removes the poster image. The default is &lt;strong&gt;false&lt;/strong&gt;. |  [optional] |
|**sourceUrl** | **String** | The URL of an IP camera or video encoder using an RTMP and RTSP pull connection to Wowza Streaming Cloud. Consult the camera or encoder documentation for the URL syntax. |  [optional] |
|**targetDeliveryProtocol** | [**TargetDeliveryProtocolEnum**](#TargetDeliveryProtocolEnum) | The type of stream being delivered from Wowza Streaming Cloud. The default is &lt;strong&gt;hls-https&lt;/strong&gt;. |  [optional] |
|**useStreamSource** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, uses a stream source to deliver the stream to Wowza Streaming Cloud. The default, &lt;strong&gt;false&lt;/strong&gt;, pushes directly to Wowza Streaming Cloud. |  [optional] |
|**username** | **String** | A username for authenticating an RTMP or RTSP push connection. Can contain only uppercase and lowercase letters; numbers; and the period (.), underscore (_), and hyphen (-) characters. No other special characters can be used. |  [optional] |
|**videoFallback** | **Boolean** | If &lt;strong&gt;true&lt;/strong&gt;, black video plays if the video source disconnects from the transcoder. If &lt;strong&gt;false&lt;/strong&gt; (the default), a stream-not-available message appears. Works only with HLS stream targets. |  [optional] |



## Enum: ClosedCaptionTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| CEA | &quot;cea&quot; |
| ON_TEXT | &quot;on_text&quot; |
| BOTH | &quot;both&quot; |



## Enum: DeliveryMethodEnum

| Name | Value |
|---- | -----|
| PULL | &quot;pull&quot; |
| CDN | &quot;cdn&quot; |
| PUSH | &quot;push&quot; |



## Enum: EncoderEnum

| Name | Value |
|---- | -----|
| WOWZA_STREAMING_ENGINE | &quot;wowza_streaming_engine&quot; |
| WOWZA_GOCODER | &quot;wowza_gocoder&quot; |
| MEDIA_DS | &quot;media_ds&quot; |
| AXIS | &quot;axis&quot; |
| EPIPHAN | &quot;epiphan&quot; |
| HAUPPAUGE | &quot;hauppauge&quot; |
| JVC | &quot;jvc&quot; |
| LIVE_U | &quot;live_u&quot; |
| MATROX | &quot;matrox&quot; |
| NEWTEK_TRICASTER | &quot;newtek_tricaster&quot; |
| OSPREY | &quot;osprey&quot; |
| SONY | &quot;sony&quot; |
| TELESTREAM_WIRECAST | &quot;telestream_wirecast&quot; |
| TERADEK_CUBE | &quot;teradek_cube&quot; |
| VMIX | &quot;vmix&quot; |
| X_SPLIT | &quot;x_split&quot; |
| IPCAMERA | &quot;ipcamera&quot; |
| OTHER_RTMP | &quot;other_rtmp&quot; |
| OTHER_RTSP | &quot;other_rtsp&quot; |



## Enum: PlayerLogoPositionEnum

| Name | Value |
|---- | -----|
| TOP_LEFT | &quot;top-left&quot; |
| TOP_RIGHT | &quot;top-right&quot; |
| BOTTOM_LEFT | &quot;bottom-left&quot; |
| BOTTOM_RIGHT | &quot;bottom-right&quot; |



## Enum: TargetDeliveryProtocolEnum

| Name | Value |
|---- | -----|
| HTTPS | &quot;hls-https&quot; |
| HDS | &quot;hls-hds&quot; |




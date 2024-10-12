# WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | &lt;strong&gt;chunkSize&lt;/strong&gt; defines the duration of the time-based audio and video chunks that Wowza Streaming Cloud delivers to the target. &lt;strong&gt;playSSL&lt;/strong&gt; determines whether Wowza Streaming Cloud sends the stream from the target to the player by using SSL (HTTPS). &lt;strong&gt;relativePlaylists&lt;/strong&gt; allows the viewer to watch the stream over HTTP and HTTPS, whichever protocol their browser calls. &lt;strong&gt;sendSSL&lt;/strong&gt; determines whether Wowza Streaming Cloud sends the stream from the transcoder to the target by using SSL (HTTPS). | [optional] 
**section** | **String** | The section of the stream target configuration table that contains the property. For &lt;strong&gt;chunkSize&lt;/strong&gt; and &lt;strong&gt;sendSSL&lt;/strong&gt;, use &lt;strong&gt;hls&lt;/strong&gt;. For &lt;strong&gt;playSSL&lt;/strong&gt; and &lt;strong&gt;relativePlaylists&lt;/strong&gt;, use &lt;strong&gt;playlist&lt;/strong&gt;. | [optional] 
**streamTargetId** | **String** | The unique alphanumeric string that identifies the stream target. | [optional] 
**value** | **String** | For &lt;strong&gt;chunkSize&lt;/strong&gt; use &lt;strong&gt;2&lt;/strong&gt;, &lt;strong&gt;4&lt;/strong&gt;, &lt;strong&gt;6&lt;/strong&gt;, &lt;strong&gt;8&lt;/strong&gt;, or &lt;strong&gt;10&lt;/strong&gt;. For &lt;strong&gt;playSSL&lt;/strong&gt;, &lt;strong&gt;relativePlaylists&lt;/strong&gt;, and &lt;strong&gt;sendSSL&lt;/strong&gt; use &lt;strong&gt;true&lt;/strong&gt; or &lt;strong&gt;false&lt;/strong&gt;. | [optional] 



## Enum: KeyEnum


* `chunkSize` (value: `"chunkSize"`)

* `playSSL` (value: `"playSSL"`)

* `relativePlaylists` (value: `"relativePlaylists"`)

* `sendSSL` (value: `"sendSSL"`)





## Enum: SectionEnum


* `hls` (value: `"hls"`)

* `playlist` (value: `"playlist"`)





## Enum: ValueEnum


* `2` (value: `"2"`)

* `4` (value: `"4"`)

* `6` (value: `"6"`)

* `8` (value: `"8"`)

* `10` (value: `"10"`)

* `true` (value: `"true"`)

* `false` (value: `"false"`)





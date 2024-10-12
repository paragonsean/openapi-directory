

# Property


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | [**KeyEnum**](#KeyEnum) | &lt;strong&gt;chunkSize&lt;/strong&gt; defines the duration of the time-based audio and video chunks that Wowza Streaming Cloud delivers to the target. &lt;strong&gt;playSSL&lt;/strong&gt; determines whether Wowza Streaming Cloud sends the stream from the target to the player by using SSL (HTTPS). &lt;strong&gt;relativePlaylists&lt;/strong&gt; allows the viewer to watch the stream over HTTP and HTTPS, whichever protocol their browser calls. &lt;strong&gt;sendSSL&lt;/strong&gt; determines whether Wowza Streaming Cloud sends the stream from the transcoder to the target by using SSL (HTTPS). |  |
|**section** | [**SectionEnum**](#SectionEnum) | The section of the stream target configuration table that contains the property. For &lt;strong&gt;chunkSize&lt;/strong&gt; and &lt;strong&gt;sendSSL&lt;/strong&gt;, use &lt;strong&gt;hls&lt;/strong&gt;. For &lt;strong&gt;playSSL&lt;/strong&gt; and &lt;strong&gt;relativePlaylists&lt;/strong&gt;, use &lt;strong&gt;playlist&lt;/strong&gt;. |  |
|**value** | [**ValueEnum**](#ValueEnum) | For &lt;strong&gt;chunkSize&lt;/strong&gt; use &lt;strong&gt;2&lt;/strong&gt;, &lt;strong&gt;4&lt;/strong&gt;, &lt;strong&gt;6&lt;/strong&gt;, &lt;strong&gt;8&lt;/strong&gt;, or &lt;strong&gt;10&lt;/strong&gt;. For &lt;strong&gt;playSSL&lt;/strong&gt;, &lt;strong&gt;relativePlaylists&lt;/strong&gt;, and &lt;strong&gt;sendSSL&lt;/strong&gt; use &lt;strong&gt;true&lt;/strong&gt; or &lt;strong&gt;false&lt;/strong&gt;. |  |



## Enum: KeyEnum

| Name | Value |
|---- | -----|
| CHUNK_SIZE | &quot;chunkSize&quot; |
| PLAY_SSL | &quot;playSSL&quot; |
| RELATIVE_PLAYLISTS | &quot;relativePlaylists&quot; |
| SEND_SSL | &quot;sendSSL&quot; |



## Enum: SectionEnum

| Name | Value |
|---- | -----|
| HLS | &quot;hls&quot; |
| PLAYLIST | &quot;playlist&quot; |



## Enum: ValueEnum

| Name | Value |
|---- | -----|
| _2 | &quot;2&quot; |
| _4 | &quot;4&quot; |
| _6 | &quot;6&quot; |
| _8 | &quot;8&quot; |
| _10 | &quot;10&quot; |
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |




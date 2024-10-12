

# Transcoder6


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | The state of the transcoder. |  [optional] |
|**transcodingUptimeId** | **String** | &lt;strong&gt;The &lt;em&gt;transcoding_uptime_id&lt;/em&gt; parameter is deprecated and is replaced by &lt;em&gt;uptime_id&lt;/em&gt;.&lt;/strong&gt; The unique identifier associated with a specific uptime period of a transcoder. |  [optional] |
|**uptimeId** | **String** | The unique identifier associated with a specific uptime period of a transcoder. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STARTING | &quot;starting&quot; |
| STOPPING | &quot;stopping&quot; |
| STARTED | &quot;started&quot; |
| STOPPED | &quot;stopped&quot; |
| RESETTING | &quot;resetting&quot; |




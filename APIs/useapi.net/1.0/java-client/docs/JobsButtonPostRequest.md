

# JobsButtonPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**button** | [**ButtonEnum**](#ButtonEnum) | button from buttons array of job referenced via jobid |  |
|**discord** | **String** | Optional Discord token, if provided will override discord value of referenced jobid |  [optional] |
|**jobid** | **String** | jobid of successfully completed (status set to completed) jobs/imagine or jobs/button job |  |
|**maxJobs** | **Integer** | Optional Maximum Concurrent Jobs for current Midjourney subscription |  [optional] |
|**replyRef** | **String** | Optional reference id which will be stored and returned along with this job response / result |  [optional] |
|**replyUrl** | **String** | Optional callback URL, API will call the provided replyUrl once generation completed |  [optional] |



## Enum: ButtonEnum

| Name | Value |
|---- | -----|
| U1 | &quot;U1&quot; |
| U2 | &quot;U2&quot; |
| U3 | &quot;U3&quot; |
| U4 | &quot;U4&quot; |
| V1 | &quot;V1&quot; |
| V2 | &quot;V2&quot; |
| V3 | &quot;V3&quot; |
| V4 | &quot;V4&quot; |
| u | &quot;⬅️&quot; |
| u2 | &quot;➡️&quot; |
| u3 | &quot;⬆️&quot; |
| u4 | &quot;⬇️&quot; |
| u5 | &quot;🔄&quot; |
| VARY_STRONG_ | &quot;Vary (Strong)&quot; |
| VARY_SUBTLE_ | &quot;Vary (Subtle)&quot; |
| ZOOM_OUT_1_5X | &quot;Zoom Out 1.5x&quot; |
| ZOOM_OUT_2X | &quot;Zoom Out 2x&quot; |
| MAKE_SQUARE | &quot;Make Square&quot; |
| MAKE_VARIATIONS | &quot;Make Variations&quot; |
| REMASTER | &quot;Remaster&quot; |




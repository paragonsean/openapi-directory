

# ButtonResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**button** | [**ButtonEnum**](#ButtonEnum) |  |  |
|**channel** | **String** |  |  |
|**code** | [**CodeEnum**](#CodeEnum) |  |  |
|**created** | **String** |  |  |
|**jobid** | **String** | Use returned jobid value to retrieve job status and results |  |
|**maxJobs** | **Integer** |  |  |
|**parentJobId** | **String** |  |  |
|**server** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**updated** | **String** |  |  |
|**verb** | [**VerbEnum**](#VerbEnum) |  |  |



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



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NUMBER_200 | 200 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;started&quot; |
| COMPLETED | &quot;completed&quot; |



## Enum: VerbEnum

| Name | Value |
|---- | -----|
| BUTTON | &quot;button&quot; |




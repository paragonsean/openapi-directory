

# Screenshot


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cookie** | **String** | custom cookie used (see Custom POST Data, Referer and Cookie) |  [optional] |
|**cost** | **Integer** | number of credits spent for the screenshot |  [optional] |
|**delay** | **Integer** | number of seconds to wait after page load |  [optional] |
|**details** | **Integer** | level of details about the screenshot and the page |  [optional] |
|**error** | **String** | description of the problem that occurred |  [optional] |
|**finalUrl** | **String** | URL of the screenshot (redirections can occur) |  [optional] |
|**flashDelay** | **Integer** | number of seconds to wait after page load if Flash elements are present |  [optional] |
|**height** | **Integer** | screenshot height |  [optional] |
|**id** | **Integer** | screenshot ID |  |
|**instanceId** | **Integer** | instance ID used for the screenshot |  |
|**postData** | **String** | POST data sent (see Custom POST Data, Referer and Cookie) |  [optional] |
|**priority** | **Integer** | priority given to the screenshot: high (1) to low (3) |  [optional] |
|**referer** | **String** | custom referrer used (see Custom POST Data, Referer and Cookie) |  [optional] |
|**scale** | **Double** | image scale. Always 1 for desktop browsers; mobiles may change the scale (zoom in or zoom out) to fit the page on the screen |  [optional] |
|**screenshotUrl** | **Object** | URL to download the screenshot |  [optional] |
|**script** | **String** | URL of optional javascript file executed after the page load event |  [optional] |
|**sharedUrl** | **String** | if the screenshot was shared, show the public URL |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | screenshot size requested |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status of the request: \&quot;in_queue\&quot;, \&quot;processing\&quot;, \&quot;finished\&quot;, \&quot;error\&quot;  |  |
|**url** | **String** | original URL requested |  |
|**width** | **Integer** | screenshot width |  [optional] |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| SCREEN | &quot;screen&quot; |
| PAGE | &quot;page&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_QUEUE | &quot;in_queue&quot; |
| PROCESSING | &quot;processing&quot; |
| FINISHED | &quot;finished&quot; |
| ERROR | &quot;error&quot; |




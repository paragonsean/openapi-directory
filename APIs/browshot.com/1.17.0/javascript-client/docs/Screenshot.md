# BrowshotApi.Screenshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **String** | custom cookie used (see Custom POST Data, Referer and Cookie) | [optional] 
**cost** | **Number** | number of credits spent for the screenshot | [optional] 
**delay** | **Number** | number of seconds to wait after page load | [optional] 
**details** | **Number** | level of details about the screenshot and the page | [optional] 
**error** | **String** | description of the problem that occurred | [optional] 
**finalUrl** | **String** | URL of the screenshot (redirections can occur) | [optional] 
**flashDelay** | **Number** | number of seconds to wait after page load if Flash elements are present | [optional] 
**height** | **Number** | screenshot height | [optional] 
**id** | **Number** | screenshot ID | 
**instanceId** | **Number** | instance ID used for the screenshot | 
**postData** | **String** | POST data sent (see Custom POST Data, Referer and Cookie) | [optional] 
**priority** | **Number** | priority given to the screenshot: high (1) to low (3) | [optional] 
**referer** | **String** | custom referrer used (see Custom POST Data, Referer and Cookie) | [optional] 
**scale** | **Number** | image scale. Always 1 for desktop browsers; mobiles may change the scale (zoom in or zoom out) to fit the page on the screen | [optional] 
**screenshotUrl** | **Object** | URL to download the screenshot | [optional] 
**script** | **String** | URL of optional javascript file executed after the page load event | [optional] 
**sharedUrl** | **String** | if the screenshot was shared, show the public URL | [optional] 
**size** | **String** | screenshot size requested | [optional] 
**status** | **String** | status of the request: \&quot;in_queue\&quot;, \&quot;processing\&quot;, \&quot;finished\&quot;, \&quot;error\&quot;  | 
**url** | **String** | original URL requested | 
**width** | **Number** | screenshot width | [optional] 



## Enum: SizeEnum


* `screen` (value: `"screen"`)

* `page` (value: `"page"`)





## Enum: StatusEnum


* `in_queue` (value: `"in_queue"`)

* `processing` (value: `"processing"`)

* `finished` (value: `"finished"`)

* `error` (value: `"error"`)





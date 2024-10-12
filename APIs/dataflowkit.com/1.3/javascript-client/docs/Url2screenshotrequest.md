# DataflowKitWebScraper.Url2screenshotrequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[Action]**](Action.md) | Use actions to automate manual workflows while rendering web pages. They simulate real-world human interaction with pages. | [optional] 
**clipSelector** | **String** | Captures a screenshot of specified CSS element on a web page. | [optional] 
**format** | **String** | Sets the Format of output image | [optional] [default to &#39;png&#39;]
**fullPage** | **Boolean** | takes a screenshot of a full web page. It ignores offsetX, offsety, width and height argument values. | [optional] [default to false]
**height** | **Number** | Rectangle height in device independent pixels (dip). | [optional] [default to 600]
**ignoreHTTPStatusErrCodes** | **Boolean** | The HTTP 200 OK success status response code indicates that the request has succeeded. Sometimes a server returns normal HTML content even with an erroneous Non-200 HTTP response status code. The IgnoreHTTPStatusCode option is useful when you need to force the return of HTML content. Defaults to \&quot;false.\&quot; | [optional] 
**initialCookies** | [**[InitialCookie]**](InitialCookie.md) | The \&quot;Initial Cookies\&quot; option is useful for crawling websites that require a login. The simplest solution to get an array of cookies for specific websites is to use a web browser \&quot;EditThisCookie\&quot; extension. Copy a cookie array with \&quot;EditThisCookie\&quot; and paste it into the \&quot;Initial cookie\&quot; field. | [optional] 
**offsetx** | **Number** | X offset in device independent pixels (dip). | [optional] [default to 0]
**offsety** | **Number** | Y offset in device independent pixels (dip). | [optional] [default to 0]
**output** | **String** | If set to _file_, the resulted screenshot is uploaded to Dataflow Kit Storage first. Then the link to this file is returned. Overwise, web site screenshot is returned in the response body. | [optional] [default to &#39;buffer&#39;]
**printBackground** | **Boolean** | Print background graphics in the PDF. | [optional] [default to false]
**proxy** | **String** | Specify proxy by adding [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to &#x60;country-&#x60; value to send requests through a proxy in the specified country. Use &#x60;country-any&#x60; to use random geo-targets. | [optional] 
**quality** | **Number** | Sets the Quality of output image. Compression quality from range [0..100] (jpeg only). | [optional] [default to 80]
**scale** | **Number** | Image scale factor. range [0.1 .. 3] | [optional] [default to 1]
**url** | **String** | The full URL address (including HTTP/HTTPS) of a web page that you want to capture | 
**waitDelay** | **Number** | Specify a wait delay (in seconds). This may be useful if certain elements of the web site need to be rendered after the initial page load. | [optional] [default to 0.5]
**width** | **Number** | Rectangle width in device independent pixels (dip). | [optional] [default to 800]



## Enum: FormatEnum


* `png` (value: `"png"`)

* `jpeg` (value: `"jpeg"`)





## Enum: OutputEnum


* `buffer` (value: `"buffer"`)

* `file` (value: `"file"`)





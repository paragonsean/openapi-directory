

# Url2screenshotrequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;Action&gt;**](Action.md) | Use actions to automate manual workflows while rendering web pages. They simulate real-world human interaction with pages. |  [optional] |
|**clipSelector** | **String** | Captures a screenshot of specified CSS element on a web page. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Sets the Format of output image |  [optional] |
|**fullPage** | **Boolean** | takes a screenshot of a full web page. It ignores offsetX, offsety, width and height argument values. |  [optional] |
|**height** | **Integer** | Rectangle height in device independent pixels (dip). |  [optional] |
|**ignoreHTTPStatusErrCodes** | **Boolean** | The HTTP 200 OK success status response code indicates that the request has succeeded. Sometimes a server returns normal HTML content even with an erroneous Non-200 HTTP response status code. The IgnoreHTTPStatusCode option is useful when you need to force the return of HTML content. Defaults to \&quot;false.\&quot; |  [optional] |
|**initialCookies** | [**List&lt;InitialCookie&gt;**](InitialCookie.md) | The \&quot;Initial Cookies\&quot; option is useful for crawling websites that require a login. The simplest solution to get an array of cookies for specific websites is to use a web browser \&quot;EditThisCookie\&quot; extension. Copy a cookie array with \&quot;EditThisCookie\&quot; and paste it into the \&quot;Initial cookie\&quot; field. |  [optional] |
|**offsetx** | **Integer** | X offset in device independent pixels (dip). |  [optional] |
|**offsety** | **Integer** | Y offset in device independent pixels (dip). |  [optional] |
|**output** | [**OutputEnum**](#OutputEnum) | If set to _file_, the resulted screenshot is uploaded to Dataflow Kit Storage first. Then the link to this file is returned. Overwise, web site screenshot is returned in the response body. |  [optional] |
|**printBackground** | **Boolean** | Print background graphics in the PDF. |  [optional] |
|**proxy** | **String** | Specify proxy by adding [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to &#x60;country-&#x60; value to send requests through a proxy in the specified country. Use &#x60;country-any&#x60; to use random geo-targets. |  [optional] |
|**quality** | **Integer** | Sets the Quality of output image. Compression quality from range [0..100] (jpeg only). |  [optional] |
|**scale** | **BigDecimal** | Image scale factor. range [0.1 .. 3] |  [optional] |
|**url** | **String** | The full URL address (including HTTP/HTTPS) of a web page that you want to capture |  |
|**waitDelay** | **BigDecimal** | Specify a wait delay (in seconds). This may be useful if certain elements of the web site need to be rendered after the initial page load. |  [optional] |
|**width** | **Integer** | Rectangle width in device independent pixels (dip). |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PNG | &quot;png&quot; |
| JPEG | &quot;jpeg&quot; |



## Enum: OutputEnum

| Name | Value |
|---- | -----|
| BUFFER | &quot;buffer&quot; |
| FILE | &quot;file&quot; |




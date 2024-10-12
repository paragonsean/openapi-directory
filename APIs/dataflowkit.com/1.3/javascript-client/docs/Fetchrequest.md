# DataflowKitWebScraper.Fetchrequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[Action]**](Action.md) | Use actions to automate manual workflows while rendering web pages. They simulate real-world human interaction with pages. _(Chrome fetcher type only)_ | [optional] 
**ignoreHTTPStatusErrCodes** | **Boolean** | The HTTP 200 OK success status response code indicates that the request has succeeded. Sometimes a server returns normal HTML content even with an erroneous Non-200 HTTP response status code. The IgnoreHTTPStatusCode option is useful when you need to force the return of HTML content. Defaults to \&quot;false.\&quot; | [optional] 
**initialCookies** | [**[InitialCookie]**](InitialCookie.md) | The \&quot;Initial Cookies\&quot; option is useful for crawling websites that require a login. The simplest solution to get an array of cookies for specific websites is to use a web browser \&quot;EditThisCookie\&quot; extension. Copy a cookie array with \&quot;EditThisCookie\&quot; and paste it into the \&quot;Initial cookie\&quot; field. | [optional] 
**output** | **String** | If set to _file_, the content of downloaded HTML is uploaded to Dataflow Kit Storage first. Then the link to this file is returned. Overwise, downloaded content is returned in the response body. | [optional] [default to &#39;buffer&#39;]
**proxy** | **String** | Specify proxy by adding [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to &#x60;country-&#x60; value to send requests through a proxy in the specified country. Use &#x60;country-any&#x60; to use random geo-targets. | [optional] 
**type** | **String** | If set to &#x60;base&#x60;, the Base fetcher is used for downloading web page content. Use &#x60;chrome&#x60; for fetching content with a Headless chrome browser. If omitted &#x60;base&#x60; fetcher is used by default. | 
**url** | **String** | Specify URL to download. | 
**waitDelay** | **Number** | Specify a wait delay (in seconds). This may be useful if certain elements of the web site need to be rendered after the initial page load. _(Chrome fetcher type only)_ | [optional] 



## Enum: OutputEnum


* `buffer` (value: `"buffer"`)

* `file` (value: `"file"`)





## Enum: TypeEnum


* `base` (value: `"base"`)

* `chrome` (value: `"chrome"`)





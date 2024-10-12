# DataflowKitWebScraper.Url2pdfrequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[Action]**](Action.md) | Use actions to automate manual workflows while rendering web pages. They simulate real-world human interaction with pages. | [optional] 
**ignoreHTTPStatusErrCodes** | **Boolean** | The HTTP 200 OK success status response code indicates that the request has succeeded. Sometimes a server returns normal HTML content even with an erroneous Non-200 HTTP response status code. The IgnoreHTTPStatusCode option is useful when you need to force the return of HTML content. Defaults to \&quot;false.\&quot; | [optional] 
**initialCookies** | [**[InitialCookie]**](InitialCookie.md) | The \&quot;Initial Cookies\&quot; option is useful for crawling websites that require a login. The simplest solution to get an array of cookies for specific websites is to use a web browser \&quot;EditThisCookie\&quot; extension. Copy a cookie array with \&quot;EditThisCookie\&quot; and paste it into the \&quot;Initial cookie\&quot; field. | [optional] 
**landscape** | **Boolean** | Paper orientation. Parameter landscape &#x3D; false means portrait orientation. Set landscape to true for landscape page oriantation. | [optional] [default to false]
**marginBottom** | **Number** | Bottom Margin of the PDF (in inches) | [optional] [default to 0.4]
**marginLeft** | **Number** | Left Margin of the PDF (in inches) | [optional] [default to 0.4]
**marginRight** | **Number** | Right Margin of the PDF (in inches) | [optional] [default to 0.4]
**marginTop** | **Number** | Top Margin of the PDF (in inches) | [optional] [default to 0.4]
**output** | **String** | If set to _file_, the resulted PDF is uploaded to Dataflow Kit Storage first. Then the link to this file is returned. Overwise, PDF content is returned in the response body. | [optional] [default to &#39;buffer&#39;]
**pageRanges** | **String** | Specify page ranges to convert. Defaults to the empty value, which means convert all pages. | [optional] 
**paperSize** | **String** | Page size parameter consists of the most popular page formats. | [optional] [default to &#39;A4&#39;]
**printBackground** | **Boolean** | Print background graphics in the PDF. | [optional] [default to false]
**printHeaderFooter** | **Boolean** | printHeaderFooter  parameter consists of the date, name of the web page, the page URL, and how many pages the document you are printing. | [optional] [default to false]
**proxy** | **String** | Specify proxy by adding [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to &#x60;country-&#x60; value to send requests through a proxy in the specified country. Use &#x60;country-any&#x60; to use random geo-targets. | [optional] 
**scale** | **Number** | By default, PDF document content is generated according to dimensions of the original web page content. Using the &#x60;scale&#x60; parameter, you can specify a custom zoom factor from 0.1 to 5.0 of the webpage rendering. | [optional] [default to 1]
**url** | **String** | The full URL address (including HTTP/HTTPS) of a web page that you want to save as PDF | 
**waitDelay** | **Number** | Specify a wait delay (in seconds). This may be useful if certain elements of the web site need to be rendered after the initial page load. | [optional] [default to 0.5]



## Enum: OutputEnum


* `buffer` (value: `"buffer"`)

* `file` (value: `"file"`)





## Enum: PaperSizeEnum


* `A3` (value: `"A3"`)

* `A4` (value: `"A4"`)

* `A5` (value: `"A5"`)

* `A6` (value: `"A6"`)

* `Letter` (value: `"Letter"`)

* `Legal` (value: `"Legal"`)

* `Tabloid` (value: `"Tabloid"`)





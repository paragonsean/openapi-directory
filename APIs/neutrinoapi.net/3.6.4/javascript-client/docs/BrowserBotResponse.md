# NeutrinoApi.BrowserBotResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The complete raw, decompressed and decoded page content. Usually will be either HTML, JSON or XML | 
**elements** | **[String]** | Array containing all the elements matching the supplied selector. &lt;br&gt;Each element object will contain the text content, HTML content and all current element attributes | 
**errorMessage** | **String** | Contains the error message if an error has occurred (&#39;is-error&#39; will be true) | 
**execResults** | **[String]** | If you executed any JavaScript this array holds the results as objects | 
**httpRedirectUrl** | **String** | The redirected URL if the URL responded with an HTTP redirect | 
**httpStatusCode** | **Number** | The HTTP status code the URL returned | 
**httpStatusMessage** | **String** | The HTTP status message the URL returned | 
**isError** | **Boolean** | True if an error has occurred loading the page. Check the &#39;error-message&#39; field for details | 
**isHttpOk** | **Boolean** | True if the HTTP status is OK (200) | 
**isHttpRedirect** | **Boolean** | True if the URL responded with an HTTP redirect | 
**isSecure** | **Boolean** | True if the page is secured using TLS/SSL | 
**isTimeout** | **Boolean** | True if a timeout occurred while loading the page. You can set the timeout with the request parameter &#39;timeout&#39; | 
**languageCode** | **String** | The ISO 2-letter language code of the page. Extracted from either the HTML document or via HTTP headers | 
**loadTime** | **Number** | The number of seconds taken to load the page (from initial request until DOM ready) | 
**mimeType** | **String** | The document MIME type | 
**responseHeaders** | **{String: String}** | Map containing all the HTTP response headers the URL responded with | 
**securityDetails** | **{String: String}** | Map containing details of the TLS/SSL setup | 
**serverIp** | **String** | The HTTP servers IP address | 
**title** | **String** | The document title | 
**url** | **String** | The page URL | 



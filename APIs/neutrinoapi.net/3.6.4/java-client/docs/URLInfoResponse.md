

# URLInfoResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The actual content this URL responded with. Only set if the &#39;fetch-content&#39; option was used |  |
|**contentEncoding** | **String** | The encoding format the URL uses |  |
|**contentSize** | **Integer** | The size of the URL content in bytes |  |
|**contentType** | **String** | The content-type this URL serves |  |
|**httpOk** | **Boolean** | True if this URL responded with an HTTP OK (200) status |  |
|**httpRedirect** | **Boolean** | True if this URL responded with an HTTP redirect |  |
|**httpStatus** | **Integer** | The HTTP status code this URL responded with. An HTTP status of 0 indicates a network level issue |  |
|**httpStatusMessage** | **Integer** | The HTTP status message assoicated with the status code |  |
|**isError** | **Boolean** | True if an error occurred while loading the URL. This includes network errors, TLS errors and timeouts |  |
|**isTimeout** | **Boolean** | True if a timeout occurred while loading the URL. You can set the timeout with the request parameter &#39;timeout&#39; |  |
|**languageCode** | **String** | The ISO 2-letter language code of the page. Extracted from either the HTML document or via HTTP headers |  |
|**loadTime** | **Double** | The time taken to load the URL content in seconds |  |
|**query** | **Map&lt;String, String&gt;** | A key-value map of the URL query paramaters |  |
|**real** | **Boolean** | Is this URL actually serving real content |  |
|**serverCity** | **String** | The servers IP geo-location: full city name (if detectable) |  |
|**serverCountry** | **String** | The servers IP geo-location: full country name |  |
|**serverCountryCode** | **String** | The servers IP geo-location: ISO 2-letter country code |  |
|**serverHostname** | **String** | The servers hostname (PTR record) |  |
|**serverIp** | **String** | The IP address of the server hosting this URL |  |
|**serverName** | **String** | The name of the server software hosting this URL |  |
|**serverRegion** | **String** | The servers IP geo-location: full region name (if detectable) |  |
|**title** | **String** | The document title |  |
|**url** | **String** | The fully qualified URL. This may be different to the URL requested if http-redirect is true |  |
|**urlPath** | **String** | The URL path |  |
|**urlPort** | **Integer** | The URL port |  |
|**urlProtocol** | **String** | The URL protocol, usually http or https |  |
|**valid** | **Boolean** | Is this a valid well-formed URL |  |




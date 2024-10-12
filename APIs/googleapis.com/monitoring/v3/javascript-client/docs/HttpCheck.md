# CloudMonitoringApi.HttpCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedResponseStatusCodes** | [**[ResponseStatusCode]**](ResponseStatusCode.md) | If present, the check will only pass if the HTTP response status code is in this set of status codes. If empty, the HTTP status code will only pass if the HTTP status code is 200-299. | [optional] 
**authInfo** | [**BasicAuthentication**](BasicAuthentication.md) |  | [optional] 
**body** | **Blob** | The request body associated with the HTTP POST request. If content_type is URL_ENCODED, the body passed in must be URL-encoded. Users can provide a Content-Length header via the headers field or the API will do so. If the request_method is GET and body is not empty, the API will return an error. The maximum byte size is 1 megabyte.Note: If client libraries aren&#39;t used (which performs the conversion automatically) base64 encode your body data since the field is of bytes type. | [optional] 
**contentType** | **String** | The content type header to use for the check. The following configurations result in errors: 1. Content type is specified in both the headers field and the content_type field. 2. Request method is GET and content_type is not TYPE_UNSPECIFIED 3. Request method is POST and content_type is TYPE_UNSPECIFIED. 4. Request method is POST and a \&quot;Content-Type\&quot; header is provided via headers field. The content_type field should be used instead. | [optional] 
**customContentType** | **String** | A user provided content type header to use for the check. The invalid configurations outlined in the content_type field apply to custom_content_type, as well as the following: 1. content_type is URL_ENCODED and custom_content_type is set. 2. content_type is USER_PROVIDED and custom_content_type is not set. | [optional] 
**headers** | **{String: String}** | The list of headers to send as part of the Uptime check request. If two headers have the same key and different values, they should be entered as a single header, with the value being a comma-separated list of all the desired values as described at https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31). Entering two separate headers with the same key in a Create call will cause the first to be overwritten by the second. The maximum number of headers allowed is 100. | [optional] 
**maskHeaders** | **Boolean** | Boolean specifying whether to encrypt the header information. Encryption should be specified for any headers related to authentication that you do not wish to be seen when retrieving the configuration. The server will be responsible for encrypting the headers. On Get/List calls, if mask_headers is set to true then the headers will be obscured with ******. | [optional] 
**path** | **String** | Optional (defaults to \&quot;/\&quot;). The path to the page against which to run the check. Will be combined with the host (specified within the monitored_resource) and port to construct the full URL. If the provided path does not begin with \&quot;/\&quot;, a \&quot;/\&quot; will be prepended automatically. | [optional] 
**pingConfig** | [**PingConfig**](PingConfig.md) |  | [optional] 
**port** | **Number** | Optional (defaults to 80 when use_ssl is false, and 443 when use_ssl is true). The TCP port on the HTTP server against which to run the check. Will be combined with host (specified within the monitored_resource) and path to construct the full URL. | [optional] 
**requestMethod** | **String** | The HTTP request method to use for the check. If set to METHOD_UNSPECIFIED then request_method defaults to GET. | [optional] 
**useSsl** | **Boolean** | If true, use HTTPS instead of HTTP to run the check. | [optional] 
**validateSsl** | **Boolean** | Boolean specifying whether to include SSL certificate validation as a part of the Uptime check. Only applies to checks where monitored_resource is set to uptime_url. If use_ssl is false, setting validate_ssl to true has no effect. | [optional] 



## Enum: ContentTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `URL_ENCODED` (value: `"URL_ENCODED"`)

* `USER_PROVIDED` (value: `"USER_PROVIDED"`)





## Enum: RequestMethodEnum


* `METHOD_UNSPECIFIED` (value: `"METHOD_UNSPECIFIED"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)





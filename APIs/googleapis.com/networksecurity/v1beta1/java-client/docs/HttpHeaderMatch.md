

# HttpHeaderMatch

Specification of HTTP header match attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headerName** | **String** | Required. The name of the HTTP header to match. For matching against the HTTP request&#39;s authority, use a headerMatch with the header name \&quot;:authority\&quot;. For matching a request&#39;s method, use the headerName \&quot;:method\&quot;. |  [optional] |
|**regexMatch** | **String** | Required. The value of the header must match the regular expression specified in regexMatch. For regular expression grammar, please see: en.cppreference.com/w/cpp/regex/ecmascript For matching against a port specified in the HTTP request, use a headerMatch with headerName set to Host and a regular expression that satisfies the RFC2616 Host header&#39;s port specifier. |  [optional] |




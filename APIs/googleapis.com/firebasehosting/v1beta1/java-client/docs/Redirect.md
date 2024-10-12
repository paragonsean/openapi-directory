

# Redirect

A [`Redirect`](https://firebase.google.com/docs/hosting/full-config#redirects) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**glob** | **String** | The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path. |  [optional] |
|**location** | **String** | Required. The value to put in the HTTP location header of the response. The location can contain capture group values from the pattern using a &#x60;:&#x60; prefix to identify the segment and an optional &#x60;*&#x60; to capture the rest of the URL. For example: \&quot;glob\&quot;: \&quot;/:capture*\&quot;, \&quot;statusCode\&quot;: 301, \&quot;location\&quot;: \&quot;https://example.com/foo/:capture\&quot; |  [optional] |
|**regex** | **String** | The user-supplied RE2 regular expression to match against the request URL path. |  [optional] |
|**statusCode** | **Integer** | Required. The status HTTP code to return in the response. It must be a valid 3xx status code. |  [optional] |






# Header

A [`Header`](https://firebase.google.com/docs/hosting/full-config#headers) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**glob** | **String** | The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path. |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | Required. The additional headers to add to the response. |  [optional] |
|**regex** | **String** | The user-supplied RE2 regular expression to match against the request URL path. |  [optional] |




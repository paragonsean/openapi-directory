

# BucketCorsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxAgeSeconds** | **Integer** | The value, in seconds, to return in the  Access-Control-Max-Age header used in preflight responses. |  [optional] |
|**method** | **List&lt;String&gt;** | The list of HTTP methods on which to include CORS response headers: GET, OPTIONS, POST, etc. Note, \&quot;*\&quot; is permitted in the list of methods, and means \&quot;any method\&quot;. |  [optional] |
|**origin** | **List&lt;String&gt;** | The list of Origins eligible to receive CORS response headers. Note: \&quot;*\&quot; is permitted in the list of origins, and means \&quot;any Origin\&quot;. |  [optional] |
|**responseHeader** | **List&lt;String&gt;** | The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains. |  [optional] |






# ConnectionMonitorHttpConfiguration

Describes the HTTP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | [**MethodEnum**](#MethodEnum) | The HTTP method to use. |  [optional] |
|**path** | **String** | The path component of the URI. For instance, \&quot;/dir1/dir2\&quot;. |  [optional] |
|**port** | **Integer** | The port to connect to. |  [optional] |
|**preferHTTPS** | **Boolean** | Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit. |  [optional] |
|**requestHeaders** | [**List&lt;HTTPHeader&gt;**](HTTPHeader.md) | The HTTP headers to transmit with the request. |  [optional] |
|**validStatusCodeRanges** | **List&lt;String&gt;** | HTTP status codes to consider successful. For instance, \&quot;2xx,301-304,418\&quot;. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;Get&quot; |
| POST | &quot;Post&quot; |




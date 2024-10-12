

# ProbeHttpGet

Http probe for the container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | Host IP to connect to. |  [optional] |
|**httpHeaders** | [**List&lt;ProbeHttpGetHeaders&gt;**](ProbeHttpGetHeaders.md) | Headers to set in the request. |  [optional] |
|**path** | **String** | Path to access on the HTTP request. |  [optional] |
|**port** | **Integer** | Port to access for probe. |  |
|**scheme** | [**SchemeEnum**](#SchemeEnum) | Scheme for the http probe. Can be Http or Https. |  [optional] |



## Enum: SchemeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |




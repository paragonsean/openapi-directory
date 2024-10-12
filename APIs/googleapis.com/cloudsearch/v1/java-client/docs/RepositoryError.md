

# RepositoryError

Errors when the connector is communicating to the source repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | Message that describes the error. The maximum allowable length of the message is 8192 characters. |  [optional] |
|**httpStatusCode** | **Integer** | Error codes. Matches the definition of HTTP status codes. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of error. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| NETWORK_ERROR | &quot;NETWORK_ERROR&quot; |
| DNS_ERROR | &quot;DNS_ERROR&quot; |
| CONNECTION_ERROR | &quot;CONNECTION_ERROR&quot; |
| AUTHENTICATION_ERROR | &quot;AUTHENTICATION_ERROR&quot; |
| AUTHORIZATION_ERROR | &quot;AUTHORIZATION_ERROR&quot; |
| SERVER_ERROR | &quot;SERVER_ERROR&quot; |
| QUOTA_EXCEEDED | &quot;QUOTA_EXCEEDED&quot; |
| SERVICE_UNAVAILABLE | &quot;SERVICE_UNAVAILABLE&quot; |
| CLIENT_ERROR | &quot;CLIENT_ERROR&quot; |






# NetworkConnection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localIpAddress** | **String** | Local IP address. |  [optional] |
|**localPort** | **Integer** | Local port. |  [optional] |
|**pid** | **String** | Process ID. |  [optional] |
|**processName** | **String** | Process or service name. |  [optional] |
|**protocol** | **String** | Connection protocol (e.g. TCP/UDP). |  [optional] |
|**remoteIpAddress** | **String** | Remote IP address. |  [optional] |
|**remotePort** | **Integer** | Remote port. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Network connection state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| OPENING | &quot;OPENING&quot; |
| OPEN | &quot;OPEN&quot; |
| LISTEN | &quot;LISTEN&quot; |
| CLOSING | &quot;CLOSING&quot; |
| CLOSED | &quot;CLOSED&quot; |




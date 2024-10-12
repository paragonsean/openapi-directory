

# UpdateSyslogConfig

Request model for updating syslog settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Is syslog enabled? |  [optional] |
|**host** | **String** | Syslog server (IP or FQDN) |  [optional] |
|**logIpEnabled** | **Boolean** | Determines whether user’s IP address is logged. |  [optional] |
|**port** | **Integer** | Syslog server port |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol to connect to syslog server |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;TCP&quot; |
| UDP | &quot;UDP&quot; |






# IpMapping

Database instance IP mapping

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | The IP address assigned. |  [optional] |
|**timeToRetire** | **String** | The due time for this IP to be retired in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. This field is only available when the IP is scheduled to be retired. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this IP address. A &#x60;PRIMARY&#x60; address is a public address that can accept incoming connections. A &#x60;PRIVATE&#x60; address is a private address that can accept incoming connections. An &#x60;OUTGOING&#x60; address is the source address of connections originating from the instance, if supported. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SQL_IP_ADDRESS_TYPE_UNSPECIFIED | &quot;SQL_IP_ADDRESS_TYPE_UNSPECIFIED&quot; |
| PRIMARY | &quot;PRIMARY&quot; |
| OUTGOING | &quot;OUTGOING&quot; |
| PRIVATE | &quot;PRIVATE&quot; |
| MIGRATED_1_ST_GEN | &quot;MIGRATED_1ST_GEN&quot; |




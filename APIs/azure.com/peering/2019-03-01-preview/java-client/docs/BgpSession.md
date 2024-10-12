

# BgpSession

The properties that define a BGP session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxPrefixesAdvertisedV4** | **Integer** | The maximum number of prefixes advertised over the IPv4 session. |  [optional] |
|**maxPrefixesAdvertisedV6** | **Integer** | The maximum number of prefixes advertised over the IPv6 session. |  [optional] |
|**md5AuthenticationKey** | **String** | The MD5 authentication key of the session. |  [optional] |
|**microsoftSessionIPv4Address** | **String** | The IPv4 session address on Microsoft&#39;s end. |  [optional] [readonly] |
|**microsoftSessionIPv6Address** | **String** | The IPv6 session address on Microsoft&#39;s end. |  [optional] [readonly] |
|**peerSessionIPv4Address** | **String** | The IPv4 session address on peer&#39;s end. |  [optional] |
|**peerSessionIPv6Address** | **String** | The IPv6 session address on peer&#39;s end. |  [optional] |
|**sessionPrefixV4** | **String** | The IPv4 prefix that contains both ends&#39; IPv4 addresses. |  [optional] |
|**sessionPrefixV6** | **String** | The IPv6 prefix that contains both ends&#39; IPv6 addresses. |  [optional] |
|**sessionStateV4** | [**SessionStateV4Enum**](#SessionStateV4Enum) | The state of the IPv4 session. |  [optional] [readonly] |
|**sessionStateV6** | [**SessionStateV6Enum**](#SessionStateV6Enum) | The state of the IPv6 session. |  [optional] [readonly] |



## Enum: SessionStateV4Enum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IDLE | &quot;Idle&quot; |
| CONNECT | &quot;Connect&quot; |
| ACTIVE | &quot;Active&quot; |
| OPEN_SENT | &quot;OpenSent&quot; |
| OPEN_CONFIRM | &quot;OpenConfirm&quot; |
| ESTABLISHED | &quot;Established&quot; |
| PENDING_ADD | &quot;PendingAdd&quot; |
| PENDING_UPDATE | &quot;PendingUpdate&quot; |
| PENDING_REMOVE | &quot;PendingRemove&quot; |



## Enum: SessionStateV6Enum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IDLE | &quot;Idle&quot; |
| CONNECT | &quot;Connect&quot; |
| ACTIVE | &quot;Active&quot; |
| OPEN_SENT | &quot;OpenSent&quot; |
| OPEN_CONFIRM | &quot;OpenConfirm&quot; |
| ESTABLISHED | &quot;Established&quot; |
| PENDING_ADD | &quot;PendingAdd&quot; |
| PENDING_UPDATE | &quot;PendingUpdate&quot; |
| PENDING_REMOVE | &quot;PendingRemove&quot; |




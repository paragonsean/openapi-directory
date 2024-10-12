# PeeringManagementClient.BgpSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPrefixesAdvertisedV4** | **Number** | The maximum number of prefixes advertised over the IPv4 session. | [optional] 
**maxPrefixesAdvertisedV6** | **Number** | The maximum number of prefixes advertised over the IPv6 session. | [optional] 
**md5AuthenticationKey** | **String** | The MD5 authentication key of the session. | [optional] 
**microsoftSessionIPv4Address** | **String** | The IPv4 session address on Microsoft&#39;s end. | [optional] [readonly] 
**microsoftSessionIPv6Address** | **String** | The IPv6 session address on Microsoft&#39;s end. | [optional] [readonly] 
**peerSessionIPv4Address** | **String** | The IPv4 session address on peer&#39;s end. | [optional] 
**peerSessionIPv6Address** | **String** | The IPv6 session address on peer&#39;s end. | [optional] 
**sessionPrefixV4** | **String** | The IPv4 prefix that contains both ends&#39; IPv4 addresses. | [optional] 
**sessionPrefixV6** | **String** | The IPv6 prefix that contains both ends&#39; IPv6 addresses. | [optional] 
**sessionStateV4** | **String** | The state of the IPv4 session. | [optional] [readonly] 
**sessionStateV6** | **String** | The state of the IPv6 session. | [optional] [readonly] 



## Enum: SessionStateV4Enum


* `None` (value: `"None"`)

* `Idle` (value: `"Idle"`)

* `Connect` (value: `"Connect"`)

* `Active` (value: `"Active"`)

* `OpenSent` (value: `"OpenSent"`)

* `OpenConfirm` (value: `"OpenConfirm"`)

* `Established` (value: `"Established"`)

* `PendingAdd` (value: `"PendingAdd"`)

* `PendingUpdate` (value: `"PendingUpdate"`)

* `PendingRemove` (value: `"PendingRemove"`)





## Enum: SessionStateV6Enum


* `None` (value: `"None"`)

* `Idle` (value: `"Idle"`)

* `Connect` (value: `"Connect"`)

* `Active` (value: `"Active"`)

* `OpenSent` (value: `"OpenSent"`)

* `OpenConfirm` (value: `"OpenConfirm"`)

* `Established` (value: `"Established"`)

* `PendingAdd` (value: `"PendingAdd"`)

* `PendingUpdate` (value: `"PendingUpdate"`)

* `PendingRemove` (value: `"PendingRemove"`)





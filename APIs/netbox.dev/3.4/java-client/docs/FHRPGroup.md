

# FHRPGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authKey** | **String** |  |  [optional] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**groupId** | **Integer** |  |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**ipAddresses** | [**List&lt;NestedIPAddress&gt;**](NestedIPAddress.md) |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) |  |  |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| PLAINTEXT | &quot;plaintext&quot; |
| MD5 | &quot;md5&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| VRRP2 | &quot;vrrp2&quot; |
| VRRP3 | &quot;vrrp3&quot; |
| CARP | &quot;carp&quot; |
| CLUSTERXL | &quot;clusterxl&quot; |
| HSRP | &quot;hsrp&quot; |
| GLBP | &quot;glbp&quot; |
| OTHER | &quot;other&quot; |




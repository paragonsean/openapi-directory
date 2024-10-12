

# Collector

Message describing Collector object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | Output only. Store cloud storage bucket name (which is a guid) created with this Collector. |  [optional] [readonly] |
|**clientVersion** | **String** | Output only. Client version. |  [optional] [readonly] |
|**collectionDays** | **Integer** | How many days to collect data. |  [optional] |
|**createTime** | **String** | Output only. Create time stamp. |  [optional] [readonly] |
|**description** | **String** | User specified description of the Collector. |  [optional] |
|**displayName** | **String** | User specified name of the Collector. |  [optional] |
|**eulaUri** | **String** | Uri for EULA (End User License Agreement) from customer. |  [optional] |
|**expectedAssetCount** | **String** | User specified expected asset count. |  [optional] |
|**guestOsScan** | [**GuestOsScan**](GuestOsScan.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs. |  [optional] |
|**name** | **String** | name of resource. |  [optional] |
|**serviceAccount** | **String** | Service Account email used to ingest data to this Collector. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the Collector. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Update time stamp. |  [optional] [readonly] |
|**vsphereScan** | [**VSphereScan**](VSphereScan.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;STATE_INITIALIZING&quot; |
| READY_TO_USE | &quot;STATE_READY_TO_USE&quot; |
| REGISTERED | &quot;STATE_REGISTERED&quot; |
| ACTIVE | &quot;STATE_ACTIVE&quot; |
| PAUSED | &quot;STATE_PAUSED&quot; |
| DELETING | &quot;STATE_DELETING&quot; |
| DECOMMISSIONED | &quot;STATE_DECOMMISSIONED&quot; |
| ERROR | &quot;STATE_ERROR&quot; |




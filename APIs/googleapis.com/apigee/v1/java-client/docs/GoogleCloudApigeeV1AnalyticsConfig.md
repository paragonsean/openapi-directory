

# GoogleCloudApigeeV1AnalyticsConfig

Configuration for the Analytics add-on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the Analytics add-on is enabled. |  [optional] |
|**expireTimeMillis** | **String** | Output only. Time at which the Analytics add-on expires in milliseconds since epoch. If unspecified, the add-on will never expire. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the Analytics add-on. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The latest update time. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ADDON_STATE_UNSPECIFIED | &quot;ADDON_STATE_UNSPECIFIED&quot; |
| ENABLING | &quot;ENABLING&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLING | &quot;DISABLING&quot; |
| DISABLED | &quot;DISABLED&quot; |






# GetNetworkHealthAlerts200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | Category of the alert |  [optional] |
|**id** | **String** | Alert identifier. Value can be empty |  [optional] |
|**scope** | [**GetNetworkHealthAlerts200ResponseInnerScope**](GetNetworkHealthAlerts200ResponseInnerScope.md) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of the alert |  [optional] |
|**type** | **String** | Alert type |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;error&quot; |
| INFO | &quot;info&quot; |
| WARNING | &quot;warning&quot; |




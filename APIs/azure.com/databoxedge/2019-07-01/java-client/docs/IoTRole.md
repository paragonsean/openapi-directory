

# IoTRole

Compute role.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The path ID that uniquely identifies the object. |  [optional] [readonly] |
|**name** | **String** | The object name. |  [optional] [readonly] |
|**properties** | [**IoTRoleProperties**](IoTRoleProperties.md) |  |  [optional] |
|**type** | **String** | The hierarchical type of the object. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | Role type. |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| IOT | &quot;IOT&quot; |
| ASA | &quot;ASA&quot; |
| FUNCTIONS | &quot;Functions&quot; |
| COGNITIVE | &quot;Cognitive&quot; |






# DashboardColor

Defines an encoding of data value into color space.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hex** | **String** | The hex number of the color |  |
|**id** | **String** | The unique ID of the view color. |  |
|**name** | **String** | The user-facing name of the hex color. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type is how the color is used. |  |
|**value** | **Float** | The data value mapped to this color. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MIN | &quot;min&quot; |
| MAX | &quot;max&quot; |
| THRESHOLD | &quot;threshold&quot; |
| SCALE | &quot;scale&quot; |
| TEXT | &quot;text&quot; |
| BACKGROUND | &quot;background&quot; |




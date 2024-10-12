

# LabelDescriptor

A description of a label.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable description for the label. |  [optional] |
|**key** | **String** | The key for this label. The key must meet the following criteria: Does not exceed 100 characters. Matches the following regular expression: [a-zA-Z][a-zA-Z0-9_]* The first character must be an upper- or lower-case letter. The remaining characters must be letters, digits, or underscores. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | The type of data that can be assigned to the label. |  [optional] |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;STRING&quot; |
| BOOL | &quot;BOOL&quot; |
| INT64 | &quot;INT64&quot; |






# GoogleCloudVisionV1p4beta1TextAnnotationDetectedBreak

Detected start or end of a structural component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isPrefix** | **Boolean** | True if break prepends the element. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Detected break type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| SPACE | &quot;SPACE&quot; |
| SURE_SPACE | &quot;SURE_SPACE&quot; |
| EOL_SURE_SPACE | &quot;EOL_SURE_SPACE&quot; |
| HYPHEN | &quot;HYPHEN&quot; |
| LINE_BREAK | &quot;LINE_BREAK&quot; |




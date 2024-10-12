

# TransformationRuleAction

TransformationRuleAction defines a TransformationRule action based on the JSON Patch RFC (https://www.rfc-editor.org/rfc/rfc6902)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromPath** | **String** | Optional. A string containing a JSON Pointer value that references the location in the target document to move the value from. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | Required. op specifies the operation to perform. |  [optional] |
|**path** | **String** | Optional. A string containing a JSON-Pointer value that references a location within the target document where the operation is performed. |  [optional] |
|**value** | **String** | Optional. A string that specifies the desired value in string format to use for transformation. |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| OP_UNSPECIFIED | &quot;OP_UNSPECIFIED&quot; |
| REMOVE | &quot;REMOVE&quot; |
| MOVE | &quot;MOVE&quot; |
| COPY | &quot;COPY&quot; |
| ADD | &quot;ADD&quot; |
| TEST | &quot;TEST&quot; |
| REPLACE | &quot;REPLACE&quot; |




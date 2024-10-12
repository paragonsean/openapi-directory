

# Change

This class defines the Changes on the Publish API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **String** | Json path of the source entity when using the move operation. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | Operation to apply on the entity. |  |
|**path** | **String** | Json path from the root of the document to the place where the change should be applied. |  |
|**value** | **Object** | Data to change. MUST be a valid json object. |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| ADD | &quot;add&quot; |
| REMOVE | &quot;remove&quot; |
| REPLACE | &quot;replace&quot; |
| MOVE | &quot;move&quot; |
| COPY | &quot;copy&quot; |
| TEST | &quot;test&quot; |




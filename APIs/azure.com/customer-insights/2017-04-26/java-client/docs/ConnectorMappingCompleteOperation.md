

# ConnectorMappingCompleteOperation

The complete operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionOperationType** | [**CompletionOperationTypeEnum**](#CompletionOperationTypeEnum) | The type of completion operation. |  [optional] |
|**destinationFolder** | **String** | The destination folder where files will be moved to once the import is done. |  [optional] |



## Enum: CompletionOperationTypeEnum

| Name | Value |
|---- | -----|
| DO_NOTHING | &quot;DoNothing&quot; |
| DELETE_FILE | &quot;DeleteFile&quot; |
| MOVE_FILE | &quot;MoveFile&quot; |




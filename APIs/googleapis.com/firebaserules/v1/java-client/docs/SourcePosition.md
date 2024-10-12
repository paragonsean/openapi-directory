

# SourcePosition

Position in the `Source` content including its line, column number, and an index of the `File` in the `Source` message. Used for debug purposes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **Integer** | First column on the source line associated with the source fragment. |  [optional] |
|**currentOffset** | **Integer** | Start position relative to the beginning of the file. |  [optional] |
|**endOffset** | **Integer** | End position relative to the beginning of the file. |  [optional] |
|**fileName** | **String** | Name of the &#x60;File&#x60;. |  [optional] |
|**line** | **Integer** | Line number of the source fragment. 1-based. |  [optional] |




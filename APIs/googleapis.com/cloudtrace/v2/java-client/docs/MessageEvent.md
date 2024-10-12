

# MessageEvent

An event describing a message sent/received between Spans.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compressedSizeBytes** | **String** | The number of compressed bytes sent or received. If missing, the compressed size is assumed to be the same size as the uncompressed size. |  [optional] |
|**id** | **String** | An identifier for the MessageEvent&#39;s message that can be used to match &#x60;SENT&#x60; and &#x60;RECEIVED&#x60; MessageEvents. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of MessageEvent. Indicates whether the message was sent or received. |  [optional] |
|**uncompressedSizeBytes** | **String** | The number of uncompressed bytes sent or received. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| SENT | &quot;SENT&quot; |
| RECEIVED | &quot;RECEIVED&quot; |




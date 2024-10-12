

# StructuredMessage

A rich message format, including a human readable string, a key for identifying the message, and structured data associated with the message for programmatic consumption.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageKey** | **String** | Identifier for this message type. Used by external systems to internationalize or personalize message. |  [optional] |
|**messageText** | **String** | Human-readable version of message. |  [optional] |
|**parameters** | [**List&lt;Parameter&gt;**](Parameter.md) | The structured data associated with this message. |  [optional] |




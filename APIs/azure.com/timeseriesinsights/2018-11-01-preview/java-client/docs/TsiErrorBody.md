

# TsiErrorBody

A particular API error with an error code and a message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Language-independent, human-readable string that defines a service-specific error code. This code serves as a more specific indicator for the HTTP error code specified in the response. Can be used to programmatically handle specific error cases. |  [optional] [readonly] |
|**details** | **List&lt;TsiErrorDetails&gt;** | Contains additional error information. May be null. |  [optional] [readonly] |
|**innerError** | **TsiErrorBody** |  |  [optional] |
|**message** | **String** | Human-readable, language-independent representation of the error. It is intended as an aid to developers and is not suitable for exposure to end users. |  [optional] [readonly] |
|**target** | **String** | Target of the particular error (for example, the name of the property in error). May be null. |  [optional] [readonly] |






# Status

If a `run` call succeeds but the script function (or Apps Script itself) throws an exception, the response body's error field contains this `Status` object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | The status code. For this API, this value either: - 10, indicating a &#x60;SCRIPT_TIMEOUT&#x60; error, - 3, indicating an &#x60;INVALID_ARGUMENT&#x60; error, or - 1, indicating a &#x60;CANCELLED&#x60; execution.  |  [optional] |
|**details** | **List&lt;Map&lt;String, Object&gt;&gt;** | An array that contains a single ExecutionError object that provides information about the nature of the error. |  [optional] |
|**message** | **String** | A developer-facing error message, which is in English. Any user-facing error message is localized and sent in the details field, or localized by the client. |  [optional] |




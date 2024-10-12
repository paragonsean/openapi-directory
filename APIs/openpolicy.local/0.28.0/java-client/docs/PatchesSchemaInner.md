

# PatchesSchemaInner

A JSON patch operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**op** | [**OpEnum**](#OpEnum) | JSON patch operation type |  |
|**path** | **String** | A [JSON pointer](https://tools.ietf.org/html/rfc6901) to a location within the target document where the operation is performed.  The *effective path* is this value prefixed with the API call&#39;s &#x60;path&#x60; parameter.  The server will return a *bad request* (404) response if:  - The *parent* of the effective path does not refer to an existing document - For **remove** and **replace** operations, the effective path does not refer to an existing document. |  |
|**value** | **Map&lt;String, Object&gt;** | The value to add, replace or test. |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| ADD | &quot;add&quot; |
| REMOVE | &quot;remove&quot; |
| REPLACE | &quot;replace&quot; |
| MOVE | &quot;move&quot; |
| COPY | &quot;copy&quot; |
| TEST | &quot;test&quot; |




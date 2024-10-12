

# TokenListResult

The result of a request to list tokens for a container registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | The URI that can be used to request the next list of tokens. |  [optional] |
|**value** | [**List&lt;Token&gt;**](Token.md) | The list of tokens. Since this list may be incomplete, the nextLink field should be used to request the next list of tokens. |  [optional] |






# Request

Request encapsulation for simple API version 1

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extractor** | [**ExtractorEnum**](#ExtractorEnum) | [optional] Text extractor to be used when analyzing HTML document |  [optional] |
|**id** | **String** | Unique identifier of the document, it&#39;s optional |  [optional] |
|**language** | **String** | [optional] The language of the document, auto-detection will be used if omitted |  [optional] |
|**options** | **Object** | [optional] Additional options for the internal modules (key-value pairs) |  [optional] |
|**returnTextInfo** | **Boolean** | [optional] Indicates whether to return the source text within the response object |  [optional] |
|**text** | **String** | The raw text to be analyzed, mutually exclusive with the &#39;url&#39; parameter |  [optional] |
|**url** | **String** | URL of a document to be analysed, mutually exclusive with the &#39;text&#39; parameter |  [optional] |



## Enum: ExtractorEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| ARTICLE | &quot;article&quot; |
| KEEP_EVERYTHING | &quot;keep-everything&quot; |




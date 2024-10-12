

# WriteResult

The result of applying a write.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transformResults** | [**List&lt;Value&gt;**](Value.md) | The results of applying each DocumentTransform.FieldTransform, in the same order. |  [optional] |
|**updateTime** | **String** | The last update time of the document after applying the write. Not set after a &#x60;delete&#x60;. If the write did not actually change the document, this will be the previous update_time. |  [optional] |






# ScannedClinicalDocument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** | &#x60;DELETE&#x60; operation will set this field to &#x60;true&#x60; |  [optional] [readonly] |
|**date** | **String** |  |  |
|**description** | **String** |  |  |
|**doctor** | **Integer** | ID of the doctor who owns the document |  |
|**document** | **String** | When creating, if you receive response as 201, but this field is &#x60;null&#x60;, please send a &#x60;GET&#x60; request with the created object&#39;s ID to retrieve the updated file URL |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**metatags** | **String** | Array of tags represented as string. This should be quoted--e.g. &#x60;&#39;[\&quot;a\&quot;, \&quot;b\&quot;]&#39;&#x60;--since this endpoint requires &#x60;multipart/form-data&#x60; encoding |  [optional] |
|**patient** | **Integer** | ID of the patient the document concerns |  |
|**updatedAt** | **String** |  |  [optional] [readonly] |




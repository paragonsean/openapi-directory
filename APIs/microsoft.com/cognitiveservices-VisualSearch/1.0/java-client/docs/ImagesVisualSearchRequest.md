

# ImagesVisualSearchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**knowledgeRequest** | **String** | The form data is a JSON object that identifies the image using an insights token or URL to the image. The object may also include an optional crop area that identifies an area of interest in the image. The insights token and URL are mutually exclusive – do not specify both. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only (it must not include an insights token or URL). |  [optional] |
|**image** | **File** | The form data is an image binary. The Content-Disposition header&#39;s name parameter must be set to \&quot;image\&quot;. You must specify an image binary if you do not use knowledgeRequest form data to specify the image; you may not use both forms to specify an image. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only  (it must not include an insights token or URL). |  [optional] |




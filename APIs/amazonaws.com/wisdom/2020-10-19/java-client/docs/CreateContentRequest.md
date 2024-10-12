

# CreateContentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift. |  [optional] |
|**name** | **String** | The name of the content. Each piece of content in a knowledge base must have a unique name. You can retrieve a piece of content using only its knowledge base and its name with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchContent.html\&quot;&gt;SearchContent&lt;/a&gt; API. |  |
|**overrideLinkOutUri** | **String** | The URI you want to use for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. |  [optional] |
|**title** | **String** | The title of the content. If not set, the title is equal to the name. |  [optional] |
|**uploadId** | **String** | A pointer to the uploaded asset. This value is returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\&quot;&gt;StartContentUpload&lt;/a&gt;. |  |




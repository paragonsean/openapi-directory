

# UpdateContentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **Map&lt;String, String&gt;** | A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift. |  [optional] |
|**overrideLinkOutUri** | **String** | The URI for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. To remove an existing &lt;code&gt;overrideLinkOurUri&lt;/code&gt;, exclude this argument and set &lt;code&gt;removeOverrideLinkOutUri&lt;/code&gt; to true. |  [optional] |
|**removeOverrideLinkOutUri** | **Boolean** | Unset the existing &lt;code&gt;overrideLinkOutUri&lt;/code&gt; if it exists. |  [optional] |
|**revisionId** | **String** | The &lt;code&gt;revisionId&lt;/code&gt; of the content resource to update, taken from an earlier call to &lt;code&gt;GetContent&lt;/code&gt;, &lt;code&gt;GetContentSummary&lt;/code&gt;, &lt;code&gt;SearchContent&lt;/code&gt;, or &lt;code&gt;ListContents&lt;/code&gt;. If included, this argument acts as an optimistic lock to ensure content was not modified since it was last read. If it has been modified, this API throws a &lt;code&gt;PreconditionFailedException&lt;/code&gt;. |  [optional] |
|**title** | **String** | The title of the content. |  [optional] |
|**uploadId** | **String** | A pointer to the uploaded asset. This value is returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\&quot;&gt;StartContentUpload&lt;/a&gt;.  |  [optional] |




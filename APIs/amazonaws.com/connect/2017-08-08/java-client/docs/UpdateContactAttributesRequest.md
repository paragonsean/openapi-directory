

# UpdateContactAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**initialContactId** | **String** | The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center. |  |
|**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. |  |
|**attributes** | **Map&lt;String, String&gt;** | &lt;p&gt;The Amazon Connect attributes. These attributes can be accessed in flows just like any other contact attributes.&lt;/p&gt; &lt;p&gt;You can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can include only alphanumeric, dash, and underscore characters.&lt;/p&gt; |  |




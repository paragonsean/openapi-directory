

# StartTaskContactRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. |  |
|**previousContactId** | **String** | The identifier of the previous chat, voice, or task contact.  |  [optional] |
|**contactFlowId** | **String** | &lt;p&gt;The identifier of the flow for initiating the tasks. To see the ContactFlowId in the Amazon Connect console user interface, on the navigation menu go to &lt;b&gt;Routing&lt;/b&gt;, &lt;b&gt;Contact Flows&lt;/b&gt;. Choose the flow. On the flow page, under the name of the flow, choose &lt;b&gt;Show additional flow information&lt;/b&gt;. The ContactFlowId is the last part of the ARN, shown here in bold: &lt;/p&gt; &lt;p&gt;arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/&lt;b&gt;846ec553-a005-41c0-8341-xxxxxxxxxxxx&lt;/b&gt; &lt;/p&gt; |  [optional] |
|**attributes** | **Map&lt;String, String&gt;** | &lt;p&gt;A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.&lt;/p&gt; &lt;p&gt;There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.&lt;/p&gt; |  [optional] |
|**name** | **String** | The name of a task that is shown to an agent in the Contact Control Panel (CCP). |  |
|**references** | [**Map&lt;String, Reference&gt;**](Reference.md) | A formatted URL that is shown to an agent in the Contact Control Panel (CCP). |  [optional] |
|**description** | **String** | A description of the task that is shown to an agent in the Contact Control Panel (CCP). |  [optional] |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |
|**scheduledTime** | **OffsetDateTime** | The timestamp, in Unix Epoch seconds format, at which to start running the inbound flow. The scheduled time cannot be in the past. It must be within up to 6 days in future.  |  [optional] |
|**taskTemplateId** | **String** | A unique identifier for the task template. |  [optional] |
|**quickConnectId** | **String** | The identifier for the quick connect. |  [optional] |
|**relatedContactId** | **String** | The contactId that is &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/tasks.html#linked-tasks\&quot;&gt;related&lt;/a&gt; to this contact. |  [optional] |




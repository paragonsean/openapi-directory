# AmazonConnectParticipantService.SendEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | &lt;p&gt;The content type of the request. Supported types are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;application/vnd.amazonaws.connect.event.typing&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application/vnd.amazonaws.connect.event.connection.acknowledged&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application/vnd.amazonaws.connect.event.message.delivered&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application/vnd.amazonaws.connect.event.message.read&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**content** | **String** | &lt;p&gt;The content of the event to be sent (for example, message text). For content related to message receipts, this is supported in the form of a JSON string.&lt;/p&gt; &lt;p&gt;Sample Content: \&quot;{\\\&quot;messageId\\\&quot;:\\\&quot;11111111-aaaa-bbbb-cccc-EXAMPLE01234\\\&quot;}\&quot;&lt;/p&gt; | [optional] 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 



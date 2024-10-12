

# PostTextRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sessionAttributes** | **Map&lt;String, String&gt;** | &lt;p&gt;Application-specific information passed between Amazon Lex and a client application.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs\&quot;&gt;Setting Session Attributes&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**requestAttributes** | **Map&lt;String, String&gt;** | &lt;p&gt;Request-specific information passed between Amazon Lex and a client application.&lt;/p&gt; &lt;p&gt;The namespace &lt;code&gt;x-amz-lex:&lt;/code&gt; is reserved for special attributes. Don&#39;t create any request attributes with the prefix &lt;code&gt;x-amz-lex:&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs\&quot;&gt;Setting Request Attributes&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**inputText** | **String** | The text that the user entered (Amazon Lex interprets this text). |  |
|**activeContexts** | [**List&lt;ActiveContext&gt;**](ActiveContext.md) | &lt;p&gt;A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.&lt;/p&gt; |  [optional] |




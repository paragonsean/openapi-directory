

# CreateBotVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** | Identifies a specific revision of the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot. If you specify a checksum and the &lt;code&gt;$LATEST&lt;/code&gt; version of the bot has a different checksum, a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception is returned and Amazon Lex doesn&#39;t publish a new version. If you don&#39;t specify a checksum, Amazon Lex publishes the &lt;code&gt;$LATEST&lt;/code&gt; version. |  [optional] |




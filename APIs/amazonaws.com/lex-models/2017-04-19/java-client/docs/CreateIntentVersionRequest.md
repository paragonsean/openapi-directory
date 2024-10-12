

# CreateIntentVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** | Checksum of the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent that should be used to create the new version. If you specify a checksum and the &lt;code&gt;$LATEST&lt;/code&gt; version of the intent has a different checksum, Amazon Lex returns a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception and doesn&#39;t publish a new version. If you don&#39;t specify a checksum, Amazon Lex publishes the &lt;code&gt;$LATEST&lt;/code&gt; version. |  [optional] |




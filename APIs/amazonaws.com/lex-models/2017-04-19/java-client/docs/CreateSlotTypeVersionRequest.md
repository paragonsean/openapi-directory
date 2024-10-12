

# CreateSlotTypeVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** | Checksum for the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type that you want to publish. If you specify a checksum and the &lt;code&gt;$LATEST&lt;/code&gt; version of the slot type has a different checksum, Amazon Lex returns a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception and doesn&#39;t publish the new version. If you don&#39;t specify a checksum, Amazon Lex publishes the &lt;code&gt;$LATEST&lt;/code&gt; version. |  [optional] |




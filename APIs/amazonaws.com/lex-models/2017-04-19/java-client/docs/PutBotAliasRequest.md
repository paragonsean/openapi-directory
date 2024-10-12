

# PutBotAliasRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the alias. |  [optional] |
|**botVersion** | **String** | The version of the bot. |  |
|**checksum** | **String** | &lt;p&gt;Identifies a specific revision of the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;When you create a new bot alias, leave the &lt;code&gt;checksum&lt;/code&gt; field blank. If you specify a checksum you get a &lt;code&gt;BadRequestException&lt;/code&gt; exception.&lt;/p&gt; &lt;p&gt;When you want to update a bot alias, set the &lt;code&gt;checksum&lt;/code&gt; field to the checksum of the most recent revision of the &lt;code&gt;$LATEST&lt;/code&gt; version. If you don&#39;t specify the &lt;code&gt; checksum&lt;/code&gt; field, or if the checksum does not match the &lt;code&gt;$LATEST&lt;/code&gt; version, you get a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception.&lt;/p&gt; |  [optional] |
|**conversationLogs** | [**PutBotAliasRequestConversationLogs**](PutBotAliasRequestConversationLogs.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of tags to add to the bot alias. You can only add tags when you create an alias, you can&#39;t use the &lt;code&gt;PutBotAlias&lt;/code&gt; operation to update the tags on a bot alias. To update tags, use the &lt;code&gt;TagResource&lt;/code&gt; operation. |  [optional] |




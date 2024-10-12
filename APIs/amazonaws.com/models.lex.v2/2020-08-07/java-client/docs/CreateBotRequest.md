

# CreateBotRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**botName** | **String** | The name of the bot. The bot name must be unique in the account that creates the bot. |  |
|**description** | **String** | A description of the bot. It appears in lists to help you identify a particular bot. |  [optional] |
|**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot. |  |
|**dataPrivacy** | [**CreateBotRequestDataPrivacy**](CreateBotRequestDataPrivacy.md) |  |  |
|**idleSessionTTLInSeconds** | **Integer** | &lt;p&gt;The time, in seconds, that Amazon Lex should keep information about a user&#39;s conversation with the bot. &lt;/p&gt; &lt;p&gt;A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.&lt;/p&gt; &lt;p&gt;You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.&lt;/p&gt; |  |
|**botTags** | **Map&lt;String, String&gt;** | A list of tags to add to the bot. You can only add tags when you create a bot. You can&#39;t use the &lt;code&gt;UpdateBot&lt;/code&gt; operation to update tags. To update tags, use the &lt;code&gt;TagResource&lt;/code&gt; operation. |  [optional] |
|**testBotAliasTags** | **Map&lt;String, String&gt;** | A list of tags to add to the test alias for a bot. You can only add tags when you create a bot. You can&#39;t use the &lt;code&gt;UpdateAlias&lt;/code&gt; operation to update tags. To update tags on the test alias, use the &lt;code&gt;TagResource&lt;/code&gt; operation. |  [optional] |
|**botType** | [**BotTypeEnum**](#BotTypeEnum) | The type of a bot to create. |  [optional] |
|**botMembers** | [**List&lt;BotMember&gt;**](BotMember.md) | The list of bot members in a network to be created. |  [optional] |



## Enum: BotTypeEnum

| Name | Value |
|---- | -----|
| BOT | &quot;Bot&quot; |
| BOT_NETWORK | &quot;BotNetwork&quot; |




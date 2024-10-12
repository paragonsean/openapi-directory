# AmazonLexModelBuildingV2.UpdateBotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botName** | **String** | The new name of the bot. The name must be unique in the account that creates the bot. | 
**description** | **String** | A description of the bot. | [optional] 
**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that has permissions to access the bot. | 
**dataPrivacy** | [**CreateBotRequestDataPrivacy**](CreateBotRequestDataPrivacy.md) |  | 
**idleSessionTTLInSeconds** | **Number** | &lt;p&gt;The time, in seconds, that Amazon Lex should keep information about a user&#39;s conversation with the bot.&lt;/p&gt; &lt;p&gt;A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.&lt;/p&gt; &lt;p&gt;You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.&lt;/p&gt; | 
**botType** | **String** | The type of the bot to be updated. | [optional] 
**botMembers** | [**[BotMember]**](BotMember.md) | The list of bot members in the network associated with the update action. | [optional] 



## Enum: BotTypeEnum


* `Bot` (value: `"Bot"`)

* `BotNetwork` (value: `"BotNetwork"`)





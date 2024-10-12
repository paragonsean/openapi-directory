

# PutBotRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the bot. |  [optional] |
|**intents** | [**List&lt;Intent&gt;**](Intent.md) | An array of &lt;code&gt;Intent&lt;/code&gt; objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see &lt;a&gt;how-it-works&lt;/a&gt;. |  [optional] |
|**enableModelImprovements** | **Boolean** | &lt;p&gt;Set to &lt;code&gt;true&lt;/code&gt; to enable access to natural language understanding improvements. &lt;/p&gt; &lt;p&gt;When you set the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; you can use the &lt;code&gt;nluIntentConfidenceThreshold&lt;/code&gt; parameter to configure confidence scores. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html\&quot;&gt;Confidence Scores&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can only set the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter in certain Regions. If you set the parameter to &lt;code&gt;true&lt;/code&gt;, your bot has access to accuracy improvements.&lt;/p&gt; &lt;p&gt;The Regions where you can set the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;US East (N. Virginia) (us-east-1)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;US West (Oregon) (us-west-2)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Asia Pacific (Sydney) (ap-southeast-2)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EU (Ireland) (eu-west-1)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In other Regions, the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt; by default. In these Regions setting the parameter to &lt;code&gt;false&lt;/code&gt; throws a &lt;code&gt;ValidationException&lt;/code&gt; exception.&lt;/p&gt; |  [optional] |
|**nluIntentConfidenceThreshold** | **Double** | &lt;p&gt;Determines the threshold where Amazon Lex will insert the &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt;, &lt;code&gt;AMAZON.KendraSearchIntent&lt;/code&gt;, or both when returning alternative intents in a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html\&quot;&gt;PostContent&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html\&quot;&gt;PostText&lt;/a&gt; response. &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt; and &lt;code&gt;AMAZON.KendraSearchIntent&lt;/code&gt; are only inserted if they are configured for the bot.&lt;/p&gt; &lt;p&gt;You must set the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt; to use confidence scores in the following regions.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;US East (N. Virginia) (us-east-1)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;US West (Oregon) (us-west-2)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Asia Pacific (Sydney) (ap-southeast-2)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EU (Ireland) (eu-west-1)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In other Regions, the &lt;code&gt;enableModelImprovements&lt;/code&gt; parameter is set to &lt;code&gt;true&lt;/code&gt; by default.&lt;/p&gt; &lt;p&gt;For example, suppose a bot is configured with the confidence threshold of 0.80 and the &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt;. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the &lt;code&gt;PostText&lt;/code&gt; operation would be:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;AMAZON.FallbackIntent&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentC&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**clarificationPrompt** | [**PutBotRequestClarificationPrompt**](PutBotRequestClarificationPrompt.md) |  |  [optional] |
|**abortStatement** | [**PutBotRequestAbortStatement**](PutBotRequestAbortStatement.md) |  |  [optional] |
|**idleSessionTTLInSeconds** | **Integer** | &lt;p&gt;The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.&lt;/p&gt; &lt;p&gt;A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.&lt;/p&gt; &lt;p&gt;For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn&#39;t complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.&lt;/p&gt; &lt;p&gt;If you don&#39;t include the &lt;code&gt;idleSessionTTLInSeconds&lt;/code&gt; element in a &lt;code&gt;PutBot&lt;/code&gt; operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.&lt;/p&gt; &lt;p&gt;The default is 300 seconds (5 minutes).&lt;/p&gt; |  [optional] |
|**voiceId** | **String** | The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/voicelist.html\&quot;&gt;Voices in Amazon Polly&lt;/a&gt; in the &lt;i&gt;Amazon Polly Developer Guide&lt;/i&gt;. |  [optional] |
|**checksum** | **String** | &lt;p&gt;Identifies a specific revision of the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;When you create a new bot, leave the &lt;code&gt;checksum&lt;/code&gt; field blank. If you specify a checksum you get a &lt;code&gt;BadRequestException&lt;/code&gt; exception.&lt;/p&gt; &lt;p&gt;When you want to update a bot, set the &lt;code&gt;checksum&lt;/code&gt; field to the checksum of the most recent revision of the &lt;code&gt;$LATEST&lt;/code&gt; version. If you don&#39;t specify the &lt;code&gt; checksum&lt;/code&gt; field, or if the checksum does not match the &lt;code&gt;$LATEST&lt;/code&gt; version, you get a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception.&lt;/p&gt; |  [optional] |
|**processBehavior** | [**ProcessBehaviorEnum**](#ProcessBehaviorEnum) | &lt;p&gt;If you set the &lt;code&gt;processBehavior&lt;/code&gt; element to &lt;code&gt;BUILD&lt;/code&gt;, Amazon Lex builds the bot so that it can be run. If you set the element to &lt;code&gt;SAVE&lt;/code&gt; Amazon Lex saves the bot, but doesn&#39;t build it. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify this value, the default value is &lt;code&gt;BUILD&lt;/code&gt;.&lt;/p&gt; |  [optional] |
|**locale** | [**LocaleEnum**](#LocaleEnum) | &lt;p&gt; Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot. &lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;en-US&lt;/code&gt;.&lt;/p&gt; |  |
|**childDirected** | **Boolean** | &lt;p&gt;For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children&#39;s Online Privacy Protection Act (COPPA) by specifying &lt;code&gt;true&lt;/code&gt; or &lt;code&gt;false&lt;/code&gt; in the &lt;code&gt;childDirected&lt;/code&gt; field. By specifying &lt;code&gt;true&lt;/code&gt; in the &lt;code&gt;childDirected&lt;/code&gt; field, you confirm that your use of Amazon Lex &lt;b&gt;is&lt;/b&gt; related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying &lt;code&gt;false&lt;/code&gt; in the &lt;code&gt;childDirected&lt;/code&gt; field, you confirm that your use of Amazon Lex &lt;b&gt;is not&lt;/b&gt; related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the &lt;code&gt;childDirected&lt;/code&gt; field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.&lt;/p&gt; &lt;p&gt;If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the &lt;a href&#x3D;\&quot;https://aws.amazon.com/lex/faqs#data-security\&quot;&gt;Amazon Lex FAQ.&lt;/a&gt; &lt;/p&gt; |  |
|**detectSentiment** | **Boolean** | When set to &lt;code&gt;true&lt;/code&gt; user utterances are sent to Amazon Comprehend for sentiment analysis. If you don&#39;t specify &lt;code&gt;detectSentiment&lt;/code&gt;, the default is &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**createVersion** | **Boolean** | When set to &lt;code&gt;true&lt;/code&gt; a new numbered version of the bot is created. This is the same as calling the &lt;code&gt;CreateBotVersion&lt;/code&gt; operation. If you don&#39;t specify &lt;code&gt;createVersion&lt;/code&gt;, the default is &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of tags to add to the bot. You can only add tags when you create a bot, you can&#39;t use the &lt;code&gt;PutBot&lt;/code&gt; operation to update the tags on a bot. To update tags, use the &lt;code&gt;TagResource&lt;/code&gt; operation. |  [optional] |



## Enum: ProcessBehaviorEnum

| Name | Value |
|---- | -----|
| SAVE | &quot;SAVE&quot; |
| BUILD | &quot;BUILD&quot; |



## Enum: LocaleEnum

| Name | Value |
|---- | -----|
| DE_DE | &quot;de-DE&quot; |
| EN_AU | &quot;en-AU&quot; |
| EN_GB | &quot;en-GB&quot; |
| EN_IN | &quot;en-IN&quot; |
| EN_US | &quot;en-US&quot; |
| ES_419 | &quot;es-419&quot; |
| ES_ES | &quot;es-ES&quot; |
| ES_US | &quot;es-US&quot; |
| FR_FR | &quot;fr-FR&quot; |
| FR_CA | &quot;fr-CA&quot; |
| IT_IT | &quot;it-IT&quot; |
| JA_JP | &quot;ja-JP&quot; |
| KO_KR | &quot;ko-KR&quot; |




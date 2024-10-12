# AmazonLexModelBuildingV2.CreateBotLocaleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localeId** | **String** | The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
**description** | **String** | A description of the bot locale. Use this to help identify the bot locale in lists. | [optional] 
**nluIntentConfidenceThreshold** | **Number** | &lt;p&gt;Determines the threshold where Amazon Lex will insert the &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt;, &lt;code&gt;AMAZON.KendraSearchIntent&lt;/code&gt;, or both when returning alternative intents. &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt; and &lt;code&gt;AMAZON.KendraSearchIntent&lt;/code&gt; are only inserted if they are configured for the bot.&lt;/p&gt; &lt;p&gt;For example, suppose a bot is configured with the confidence threshold of 0.80 and the &lt;code&gt;AMAZON.FallbackIntent&lt;/code&gt;. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the &lt;code&gt;RecognizeText&lt;/code&gt; operation would be:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;AMAZON.FallbackIntent&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentB&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;IntentC&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**voiceSettings** | [**UpdateBotLocaleRequestVoiceSettings**](UpdateBotLocaleRequestVoiceSettings.md) |  | [optional] 



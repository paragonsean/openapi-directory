

# CreateIntentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intentName** | **String** | The name of the intent. Intent names must be unique in the locale that contains the intent and cannot match the name of any built-in intent. |  |
|**description** | **String** | A description of the intent. Use the description to help identify the intent in lists. |  [optional] |
|**parentIntentSignature** | **String** | A unique identifier for the built-in intent to base this intent on. |  [optional] |
|**sampleUtterances** | [**List&lt;SampleUtterance&gt;**](SampleUtterance.md) | &lt;p&gt;An array of strings that a user might say to signal the intent. For example, \&quot;I want a pizza\&quot;, or \&quot;I want a {PizzaSize} pizza\&quot;. &lt;/p&gt; &lt;p&gt;In an utterance, slot names are enclosed in curly braces (\&quot;{\&quot;, \&quot;}\&quot;) to indicate where they should be displayed in the utterance shown to the user.. &lt;/p&gt; |  [optional] |
|**dialogCodeHook** | [**CreateIntentRequestDialogCodeHook**](CreateIntentRequestDialogCodeHook.md) |  |  [optional] |
|**fulfillmentCodeHook** | [**CreateIntentRequestFulfillmentCodeHook**](CreateIntentRequestFulfillmentCodeHook.md) |  |  [optional] |
|**intentConfirmationSetting** | [**CreateIntentRequestIntentConfirmationSetting**](CreateIntentRequestIntentConfirmationSetting.md) |  |  [optional] |
|**intentClosingSetting** | [**CreateIntentRequestIntentClosingSetting**](CreateIntentRequestIntentClosingSetting.md) |  |  [optional] |
|**inputContexts** | [**List&lt;InputContext&gt;**](InputContext.md) | &lt;p&gt;A list of contexts that must be active for this intent to be considered by Amazon Lex.&lt;/p&gt; &lt;p&gt;When an intent has an input context list, Amazon Lex only considers using the intent in an interaction with the user when the specified contexts are included in the active context list for the session. If the contexts are not active, then Amazon Lex will not use the intent.&lt;/p&gt; &lt;p&gt;A context can be automatically activated using the &lt;code&gt;outputContexts&lt;/code&gt; property or it can be set at runtime.&lt;/p&gt; &lt;p&gt; For example, if there are two intents with different input contexts that respond to the same utterances, only the intent with the active context will respond.&lt;/p&gt; &lt;p&gt;An intent may have up to 5 input contexts. If an intent has multiple input contexts, all of the contexts must be active to consider the intent.&lt;/p&gt; |  [optional] |
|**outputContexts** | [**List&lt;OutputContext&gt;**](OutputContext.md) | &lt;p&gt;A lists of contexts that the intent activates when it is fulfilled.&lt;/p&gt; &lt;p&gt;You can use an output context to indicate the intents that Amazon Lex should consider for the next turn of the conversation with a customer. &lt;/p&gt; &lt;p&gt;When you use the &lt;code&gt;outputContextsList&lt;/code&gt; property, all of the contexts specified in the list are activated when the intent is fulfilled. You can set up to 10 output contexts. You can also set the number of conversation turns that the context should be active, or the length of time that the context should be active.&lt;/p&gt; |  [optional] |
|**kendraConfiguration** | [**CreateIntentRequestKendraConfiguration**](CreateIntentRequestKendraConfiguration.md) |  |  [optional] |
|**initialResponseSetting** | [**CreateIntentRequestInitialResponseSetting**](CreateIntentRequestInitialResponseSetting.md) |  |  [optional] |




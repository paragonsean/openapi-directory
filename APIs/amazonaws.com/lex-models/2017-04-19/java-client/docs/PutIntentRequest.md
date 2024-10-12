

# PutIntentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the intent. |  [optional] |
|**slots** | [**List&lt;Slot&gt;**](Slot.md) | An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see &lt;a&gt;how-it-works&lt;/a&gt;.  |  [optional] |
|**sampleUtterances** | **List&lt;String&gt;** | &lt;p&gt;An array of utterances (strings) that a user might say to signal the intent. For example, \&quot;I want {PizzaSize} pizza\&quot;, \&quot;Order {Quantity} {PizzaSize} pizzas\&quot;. &lt;/p&gt; &lt;p&gt;In each utterance, a slot name is enclosed in curly braces. &lt;/p&gt; |  [optional] |
|**confirmationPrompt** | [**PutBotRequestClarificationPrompt**](PutBotRequestClarificationPrompt.md) |  |  [optional] |
|**rejectionStatement** | [**PutBotRequestAbortStatement**](PutBotRequestAbortStatement.md) |  |  [optional] |
|**followUpPrompt** | [**PutIntentRequestFollowUpPrompt**](PutIntentRequestFollowUpPrompt.md) |  |  [optional] |
|**conclusionStatement** | [**PutBotRequestAbortStatement**](PutBotRequestAbortStatement.md) |  |  [optional] |
|**dialogCodeHook** | [**PutIntentRequestDialogCodeHook**](PutIntentRequestDialogCodeHook.md) |  |  [optional] |
|**fulfillmentActivity** | [**PutIntentRequestFulfillmentActivity**](PutIntentRequestFulfillmentActivity.md) |  |  [optional] |
|**parentIntentSignature** | **String** | A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see &lt;a href&#x3D;\&quot;https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents\&quot;&gt;Standard Built-in Intents&lt;/a&gt; in the &lt;i&gt;Alexa Skills Kit&lt;/i&gt;. |  [optional] |
|**checksum** | **String** | &lt;p&gt;Identifies a specific revision of the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;When you create a new intent, leave the &lt;code&gt;checksum&lt;/code&gt; field blank. If you specify a checksum you get a &lt;code&gt;BadRequestException&lt;/code&gt; exception.&lt;/p&gt; &lt;p&gt;When you want to update a intent, set the &lt;code&gt;checksum&lt;/code&gt; field to the checksum of the most recent revision of the &lt;code&gt;$LATEST&lt;/code&gt; version. If you don&#39;t specify the &lt;code&gt; checksum&lt;/code&gt; field, or if the checksum does not match the &lt;code&gt;$LATEST&lt;/code&gt; version, you get a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception.&lt;/p&gt; |  [optional] |
|**createVersion** | **Boolean** | When set to &lt;code&gt;true&lt;/code&gt; a new numbered version of the intent is created. This is the same as calling the &lt;code&gt;CreateIntentVersion&lt;/code&gt; operation. If you do not specify &lt;code&gt;createVersion&lt;/code&gt;, the default is &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**kendraConfiguration** | [**PutIntentRequestKendraConfiguration**](PutIntentRequestKendraConfiguration.md) |  |  [optional] |
|**inputContexts** | [**List&lt;InputContext&gt;**](InputContext.md) | An array of &lt;code&gt;InputContext&lt;/code&gt; objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user. |  [optional] |
|**outputContexts** | [**List&lt;OutputContext&gt;**](OutputContext.md) | An array of &lt;code&gt;OutputContext&lt;/code&gt; objects that lists the contexts that the intent activates when the intent is fulfilled. |  [optional] |




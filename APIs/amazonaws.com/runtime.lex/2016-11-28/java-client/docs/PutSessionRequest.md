

# PutSessionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sessionAttributes** | **Map&lt;String, String&gt;** | Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application. |  [optional] |
|**dialogAction** | [**PutSessionRequestDialogAction**](PutSessionRequestDialogAction.md) |  |  [optional] |
|**recentIntentSummaryView** | [**List&lt;IntentSummary&gt;**](IntentSummary.md) | &lt;p&gt;A summary of the recent intents for the bot. You can use the intent summary view to set a checkpoint label on an intent and modify attributes of intents. You can also use it to remove or add intent summary objects to the list.&lt;/p&gt; &lt;p&gt;An intent that you modify or add to the list must make sense for the bot. For example, the intent name must be valid for the bot. You must provide valid values for:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;intentName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;slot names&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;slotToElict&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you send the &lt;code&gt;recentIntentSummaryView&lt;/code&gt; parameter in a &lt;code&gt;PutSession&lt;/code&gt; request, the contents of the new summary view replaces the old summary view. For example, if a &lt;code&gt;GetSession&lt;/code&gt; request returns three intents in the summary view and you call &lt;code&gt;PutSession&lt;/code&gt; with one intent in the summary view, the next call to &lt;code&gt;GetSession&lt;/code&gt; will only return one intent.&lt;/p&gt; |  [optional] |
|**activeContexts** | [**List&lt;ActiveContext&gt;**](ActiveContext.md) | &lt;p&gt;A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.&lt;/p&gt; |  [optional] |




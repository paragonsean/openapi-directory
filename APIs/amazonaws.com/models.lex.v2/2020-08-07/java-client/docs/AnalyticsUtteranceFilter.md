

# AnalyticsUtteranceFilter

<p>Contains fields describing a condition by which to filter the utterances. The expression may be understood as <code>name</code> <code>operator</code> <code>values</code>. For example:</p> <ul> <li> <p> <code>LocaleId EQ Book</code> – The locale is the string \"en\".</p> </li> <li> <p> <code>UtteranceText CO help</code> – The text of the utterance contains the string \"help\".</p> </li> </ul> <p>The operators that each filter supports are listed below:</p> <ul> <li> <p> <code>BotAlias</code> – <code>EQ</code>.</p> </li> <li> <p> <code>BotVersion</code> – <code>EQ</code>.</p> </li> <li> <p> <code>LocaleId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Modality</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Channel</code> – <code>EQ</code>.</p> </li> <li> <p> <code>SessionId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>OriginatingRequestId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>UtteranceState</code> – <code>EQ</code>.</p> </li> <li> <p> <code>UtteranceText</code> – <code>EQ</code>, <code>CO</code>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**AnalyticsUtteranceFilterName**](AnalyticsUtteranceFilterName.md) |  |  |
|**operator** | [**AnalyticsFilterOperator**](AnalyticsFilterOperator.md) |  |  |
|**values** | [**List**](List.md) |  |  |




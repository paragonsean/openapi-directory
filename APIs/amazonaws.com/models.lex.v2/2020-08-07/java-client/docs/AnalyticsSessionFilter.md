

# AnalyticsSessionFilter

<p>Contains fields describing a condition by which to filter the sessions. The expression may be understood as <code>name</code> <code>operator</code> <code>values</code>. For example:</p> <ul> <li> <p> <code>LocaleId EQ en</code> – The locale is \"en\".</p> </li> <li> <p> <code>Duration GT 200</code> – The duration is greater than 200 seconds.</p> </li> </ul> <p>The operators that each filter supports are listed below:</p> <ul> <li> <p> <code>BotAlias</code> – <code>EQ</code>.</p> </li> <li> <p> <code>BotVersion</code> – <code>EQ</code>.</p> </li> <li> <p> <code>LocaleId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Modality</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Channel</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Duration</code> – <code>EQ</code>, <code>GT</code>, <code>LT</code>.</p> </li> <li> <p> <code>conversationEndState</code> – <code>EQ</code>, <code>CO</code>.</p> </li> <li> <p> <code>SessionId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>OriginatingRequestId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>IntentPath</code> – <code>EQ</code>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**AnalyticsSessionFilterName**](AnalyticsSessionFilterName.md) |  |  |
|**operator** | [**AnalyticsFilterOperator**](AnalyticsFilterOperator.md) |  |  |
|**values** | [**List**](List.md) |  |  |






# AnalyticsIntentStageFilter

<p>Contains fields describing a condition by which to filter the intent stages. The expression may be understood as <code>name</code> <code>operator</code> <code>values</code>. For example:</p> <ul> <li> <p> <code>IntentName CO Book</code> – The intent name contains the string \"Book.\"</p> </li> <li> <p> <code>BotVersion EQ 2</code> – The bot version is equal to two.</p> </li> </ul> <p>The operators that each filter supports are listed below:</p> <ul> <li> <p> <code>BotAlias</code> – <code>EQ</code>.</p> </li> <li> <p> <code>BotVersion</code> – <code>EQ</code>.</p> </li> <li> <p> <code>LocaleId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Modality</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Channel</code> – <code>EQ</code>.</p> </li> <li> <p> <code>SessionId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>OriginatingRequestId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>IntentName</code> – <code>EQ</code>, <code>CO</code>.</p> </li> <li> <p> <code>IntentStageName</code> – <code>EQ</code>, <code>CO</code>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**AnalyticsIntentStageFilterName**](AnalyticsIntentStageFilterName.md) |  |  |
|**operator** | [**AnalyticsFilterOperator**](AnalyticsFilterOperator.md) |  |  |
|**values** | [**List**](List.md) |  |  |




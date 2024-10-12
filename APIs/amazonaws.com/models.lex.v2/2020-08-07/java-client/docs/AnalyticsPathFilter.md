

# AnalyticsPathFilter

<p>Contains fields describing a condition by which to filter the paths. The expression may be understood as <code>name</code> <code>operator</code> <code>values</code>. For example:</p> <ul> <li> <p> <code>LocaleId EQ en</code> – The locale is \"en\".</p> </li> <li> <p> <code>BotVersion EQ 2</code> – The bot version is equal to two.</p> </li> </ul> <p>The operators that each filter supports are listed below:</p> <ul> <li> <p> <code>BotAlias</code> – <code>EQ</code>.</p> </li> <li> <p> <code>BotVersion</code> – <code>EQ</code>.</p> </li> <li> <p> <code>LocaleId</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Modality</code> – <code>EQ</code>.</p> </li> <li> <p> <code>Channel</code> – <code>EQ</code>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**AnalyticsCommonFilterName**](AnalyticsCommonFilterName.md) |  |  |
|**operator** | [**AnalyticsFilterOperator**](AnalyticsFilterOperator.md) |  |  |
|**values** | [**List**](List.md) |  |  |




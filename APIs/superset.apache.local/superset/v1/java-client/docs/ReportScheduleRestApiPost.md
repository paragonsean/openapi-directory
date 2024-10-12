

# ReportScheduleRestApiPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** |  |  [optional] |
|**chart** | **Integer** |  |  [optional] |
|**contextMarkdown** | **String** | Markdown description |  [optional] |
|**creationMethod** | **Object** | Creation method is used to inform the frontend whether the report/alert was created in the dashboard, chart, or alerts and reports UI. |  [optional] |
|**crontab** | **String** | A CRON expression.[Crontab Guru](https://crontab.guru/) is a helpful resource that can help you craft a CRON expression. |  |
|**dashboard** | **Integer** |  |  [optional] |
|**database** | **Integer** |  |  [optional] |
|**description** | **String** | Use a nice description to give context to this Alert/Report |  [optional] |
|**gracePeriod** | **Integer** | Once an alert is triggered, how long, in seconds, before Superset nags you again. (in seconds) |  [optional] |
|**logRetention** | **Integer** | How long to keep the logs around for this report (in days) |  [optional] |
|**name** | **String** | The report schedule name. |  |
|**owners** | **List&lt;Integer&gt;** |  |  [optional] |
|**recipients** | [**List&lt;ReportRecipient&gt;**](ReportRecipient.md) |  |  [optional] |
|**reportFormat** | [**ReportFormatEnum**](#ReportFormatEnum) |  |  [optional] |
|**sql** | **String** | A SQL statement that defines whether the alert should get triggered or not. The query is expected to return either NULL or a number value. |  [optional] |
|**timezone** | **String** | A timezone string that represents the location of the timezone. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The report schedule type |  |
|**validatorConfigJson** | [**ValidatorConfigJSON**](ValidatorConfigJSON.md) |  |  [optional] |
|**validatorType** | [**ValidatorTypeEnum**](#ValidatorTypeEnum) | Determines when to trigger alert based off value from alert query. Alerts will be triggered with these validator types: - Not Null - When the return value is Not NULL, Empty, or 0 - Operator - When &#x60;sql_return_value comparison_operator threshold&#x60; is True e.g. &#x60;50 &lt;&#x3D; 75&#x60;&lt;br&gt;Supports the comparison operators &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;&#x3D;, and !&#x3D; |  [optional] |
|**workingTimeout** | **Integer** | If an alert is staled at a working state, how long until it&#39;s state is reseted to error |  [optional] |



## Enum: ReportFormatEnum

| Name | Value |
|---- | -----|
| PNG | &quot;PNG&quot; |
| CSV | &quot;CSV&quot; |
| TEXT | &quot;TEXT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ALERT | &quot;Alert&quot; |
| REPORT | &quot;Report&quot; |



## Enum: ValidatorTypeEnum

| Name | Value |
|---- | -----|
| NOT_NULL | &quot;not null&quot; |
| OPERATOR | &quot;operator&quot; |




# PublicApi.ScheduledTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cronExpression** | **String** | Cron expression of scheduled task.&lt;br /&gt;  5-digit expressions (*_/5 * * * *) are required in the following sequence:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Minute (0 - 59, also *_/5, *_/10, *_/15 and *_/30 as every 5 minutes, every 10 minutes, every quarter or every half-hour are allowed)&lt;/li&gt;&lt;li&gt;Hour (0 - 23, also * as every hour is allowed)&lt;/li&gt;&lt;li&gt;Day of the month (1 - 31, also * as every day is allowed)&lt;/li&gt;&lt;li&gt;Month (1 - 12 as January to December, also * as every month is allowed)&lt;/li&gt;&lt;li&gt;Day of the week (1 - 7 as Monday to Sunday, also * as every day is allowed)&lt;/li&gt;&lt;/ul&gt; | [optional] 
**enabled** | **Boolean** | Enabled. | [optional] 
**id** | **String** | The id of the scheduled task.&lt;br /&gt;  This value is ignored for creation of new scheduled tasks. | [optional] 
**scriptLocation** | **String** | Absolute path from this linux hosting to execute. | [optional] 



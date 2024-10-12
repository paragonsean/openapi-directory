# AmazonOpenSearchService.UpdateScheduledActionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionID** | **String** | The unique identifier of the action to reschedule. To retrieve this ID, send a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\&quot;&gt;ListScheduledActions&lt;/a&gt; request. | 
**actionType** | **String** | The type of action to reschedule. Can be one of &lt;code&gt;SERVICE_SOFTWARE_UPDATE&lt;/code&gt;, &lt;code&gt;JVM_HEAP_SIZE_TUNING&lt;/code&gt;, or &lt;code&gt;JVM_YOUNG_GEN_TUNING&lt;/code&gt;. To retrieve this value, send a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\&quot;&gt;ListScheduledActions&lt;/a&gt; request. | 
**scheduleAt** | **String** | &lt;p&gt;When to schedule the action.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NOW&lt;/code&gt; - Immediately schedules the update to happen in the current hour if there&#39;s capacity available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TIMESTAMP&lt;/code&gt; - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for &lt;code&gt;DesiredStartTime&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;OFF_PEAK_WINDOW&lt;/code&gt; - Marks the action to be picked up during an upcoming off-peak window. There&#39;s no guarantee that the change will be implemented during the next immediate window. Depending on capacity, it might happen in subsequent days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**desiredStartTime** | **Number** | The time to implement the change, in Coordinated Universal Time (UTC). Only specify this parameter if you set &lt;code&gt;ScheduleAt&lt;/code&gt; to &lt;code&gt;TIMESTAMP&lt;/code&gt;. | [optional] 



## Enum: ActionTypeEnum


* `SERVICE_SOFTWARE_UPDATE` (value: `"SERVICE_SOFTWARE_UPDATE"`)

* `JVM_HEAP_SIZE_TUNING` (value: `"JVM_HEAP_SIZE_TUNING"`)

* `JVM_YOUNG_GEN_TUNING` (value: `"JVM_YOUNG_GEN_TUNING"`)





## Enum: ScheduleAtEnum


* `NOW` (value: `"NOW"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `OFF_PEAK_WINDOW` (value: `"OFF_PEAK_WINDOW"`)





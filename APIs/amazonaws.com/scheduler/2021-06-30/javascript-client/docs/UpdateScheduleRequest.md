# AmazonEventBridgeScheduler.UpdateScheduleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionAfterCompletion** | **String** | Specifies the action that EventBridge Scheduler applies to the schedule after the schedule completes invoking the target. | [optional] 
**clientToken** | **String** |  Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency.  | [optional] 
**description** | **String** | The description you specify for the schedule. | [optional] 
**endDate** | **Date** | The date, in UTC, before which the schedule can invoke its target. Depending on the schedule&#39;s recurrence expression, invocations might stop on, or before, the &lt;code&gt;EndDate&lt;/code&gt; you specify. EventBridge Scheduler ignores &lt;code&gt;EndDate&lt;/code&gt; for one-time schedules. | [optional] 
**flexibleTimeWindow** | [**UpdateScheduleRequestFlexibleTimeWindow**](UpdateScheduleRequestFlexibleTimeWindow.md) |  | 
**groupName** | **String** | The name of the schedule group with which the schedule is associated. You must provide this value in order for EventBridge Scheduler to find the schedule you want to update. If you omit this value, EventBridge Scheduler assumes the group is associated to the default group. | [optional] 
**kmsKeyArn** | **String** | The ARN for the customer managed KMS key that that you want EventBridge Scheduler to use to encrypt and decrypt your data. | [optional] 
**scheduleExpression** | **String** | &lt;p&gt; The expression that defines when the schedule runs. The following formats are supported. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;at&lt;/code&gt; expression - &lt;code&gt;at(yyyy-mm-ddThh:mm:ss)&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;rate&lt;/code&gt; expression - &lt;code&gt;rate(value unit)&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cron&lt;/code&gt; expression - &lt;code&gt;cron(fields)&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; You can use &lt;code&gt;at&lt;/code&gt; expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use &lt;code&gt;rate&lt;/code&gt; and &lt;code&gt;cron&lt;/code&gt; expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;cron&lt;/code&gt; expression consists of six fields separated by white spaces: &lt;code&gt;(minutes hours day_of_month month day_of_week year)&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;rate&lt;/code&gt; expression consists of a &lt;i&gt;value&lt;/i&gt; as a positive integer, and a &lt;i&gt;unit&lt;/i&gt; with the following options: &lt;code&gt;minute&lt;/code&gt; | &lt;code&gt;minutes&lt;/code&gt; | &lt;code&gt;hour&lt;/code&gt; | &lt;code&gt;hours&lt;/code&gt; | &lt;code&gt;day&lt;/code&gt; | &lt;code&gt;days&lt;/code&gt; &lt;/p&gt; &lt;p&gt; For more information and examples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html\&quot;&gt;Schedule types on EventBridge Scheduler&lt;/a&gt; in the &lt;i&gt;EventBridge Scheduler User Guide&lt;/i&gt;. &lt;/p&gt; | 
**scheduleExpressionTimezone** | **String** | The timezone in which the scheduling expression is evaluated. | [optional] 
**startDate** | **Date** | The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule&#39;s recurrence expression, invocations might occur on, or after, the &lt;code&gt;StartDate&lt;/code&gt; you specify. EventBridge Scheduler ignores &lt;code&gt;StartDate&lt;/code&gt; for one-time schedules. | [optional] 
**state** | **String** | Specifies whether the schedule is enabled or disabled. | [optional] 
**target** | [**UpdateScheduleRequestTarget**](UpdateScheduleRequestTarget.md) |  | 



## Enum: ActionAfterCompletionEnum


* `NONE` (value: `"NONE"`)

* `DELETE` (value: `"DELETE"`)





## Enum: StateEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)





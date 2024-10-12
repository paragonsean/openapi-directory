# WowzaStreamingCloudRestApiReferenceDocumentation.Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | The type of action that the schedule should trigger on the transcoder. The default is &lt;strong&gt;start&lt;/strong&gt;. | [optional] 
**createdAt** | **Date** | The date and time that the schedule was created. | [optional] 
**endRepeat** | **Date** | The month, day, and year that a recurring schedule should stop running. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. | [optional] 
**id** | **String** | The unique alphanumeric string that identifies the schedule. | [optional] 
**name** | **String** | A descriptive name for the schedule. Maximum 255 characters. | [optional] 
**recurrenceData** | **String** | The day or days of the week that a recurring schedule should run. | [optional] 
**recurrenceType** | **String** | A schedule can run one time only (&lt;strong&gt;once&lt;/strong&gt;) or repeat (&lt;strong&gt;recur&lt;/strong&gt;) until a specified &lt;em&gt;end_repeat&lt;/em&gt; date. The default is &lt;strong&gt;once&lt;/strong&gt;. | [optional] 
**startRepeat** | **Date** | The month, day, and year that the recurring schedule should go into effect. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. | [optional] 
**startTranscoder** | **Date** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;start&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 
**state** | **String** | A schedule must be &lt;strong&gt;enabled&lt;/strong&gt; to run. Specify &lt;strong&gt;enabled&lt;/strong&gt; to run the schedule or &lt;strong&gt;disabled&lt;/strong&gt; to turn off the schedule so that it doesn&#39;t run. | [optional] 
**stopTranscoder** | **Date** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;stop&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 
**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder being scheduled. | [optional] 
**transcoderName** | **String** | The name of the transcoder being scheduled. | [optional] 
**updatedAt** | **Date** | The date and time that the schedule was updated. | [optional] 



## Enum: ActionTypeEnum


* `start` (value: `"start"`)

* `stop` (value: `"stop"`)

* `start_stop` (value: `"start_stop"`)





## Enum: RecurrenceDataEnum


* `sunday` (value: `"sunday"`)

* `monday` (value: `"monday"`)

* `tuesday` (value: `"tuesday"`)

* `wednesday` (value: `"wednesday"`)

* `thursday` (value: `"thursday"`)

* `friday` (value: `"friday"`)

* `saturday` (value: `"saturday"`)





## Enum: RecurrenceTypeEnum


* `once` (value: `"once"`)

* `recur` (value: `"recur"`)





## Enum: StateEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)

* `expired` (value: `"expired"`)







# Schedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | The type of action that the schedule should trigger on the transcoder. The default is &lt;strong&gt;start&lt;/strong&gt;. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time that the schedule was created. |  [optional] |
|**endRepeat** | **LocalDate** | The month, day, and year that a recurring schedule should stop running. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. |  [optional] |
|**id** | **String** | The unique alphanumeric string that identifies the schedule. |  [optional] |
|**name** | **String** | A descriptive name for the schedule. Maximum 255 characters. |  [optional] |
|**recurrenceData** | [**RecurrenceDataEnum**](#RecurrenceDataEnum) | The day or days of the week that a recurring schedule should run. |  [optional] |
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) | A schedule can run one time only (&lt;strong&gt;once&lt;/strong&gt;) or repeat (&lt;strong&gt;recur&lt;/strong&gt;) until a specified &lt;em&gt;end_repeat&lt;/em&gt; date. The default is &lt;strong&gt;once&lt;/strong&gt;. |  [optional] |
|**startRepeat** | **LocalDate** | The month, day, and year that the recurring schedule should go into effect. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. |  [optional] |
|**startTranscoder** | **OffsetDateTime** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;start&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | A schedule must be &lt;strong&gt;enabled&lt;/strong&gt; to run. Specify &lt;strong&gt;enabled&lt;/strong&gt; to run the schedule or &lt;strong&gt;disabled&lt;/strong&gt; to turn off the schedule so that it doesn&#39;t run. |  [optional] |
|**stopTranscoder** | **OffsetDateTime** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;stop&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. |  [optional] |
|**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder being scheduled. |  [optional] |
|**transcoderName** | **String** | The name of the transcoder being scheduled. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time that the schedule was updated. |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| START | &quot;start&quot; |
| STOP | &quot;stop&quot; |
| START_STOP | &quot;start_stop&quot; |



## Enum: RecurrenceDataEnum

| Name | Value |
|---- | -----|
| SUNDAY | &quot;sunday&quot; |
| MONDAY | &quot;monday&quot; |
| TUESDAY | &quot;tuesday&quot; |
| WEDNESDAY | &quot;wednesday&quot; |
| THURSDAY | &quot;thursday&quot; |
| FRIDAY | &quot;friday&quot; |
| SATURDAY | &quot;saturday&quot; |



## Enum: RecurrenceTypeEnum

| Name | Value |
|---- | -----|
| ONCE | &quot;once&quot; |
| RECUR | &quot;recur&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |
| EXPIRED | &quot;expired&quot; |






# Schedule3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | The type of action that the schedule should trigger on the transcoder. The default is &lt;strong&gt;start&lt;/strong&gt;. |  |
|**endRepeat** | **LocalDate** | The month, day, and year that a recurring schedule should stop running. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. |  [optional] |
|**name** | **String** | A descriptive name for the schedule. Maximum 255 characters. |  |
|**recurrenceData** | [**RecurrenceDataEnum**](#RecurrenceDataEnum) | The day or days of the week that a recurring schedule should run. |  [optional] |
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) | A schedule can run one time only (&lt;strong&gt;once&lt;/strong&gt;) or repeat (&lt;strong&gt;recur&lt;/strong&gt;) until a specified &lt;em&gt;end_repeat&lt;/em&gt; date. The default is &lt;strong&gt;once&lt;/strong&gt;. |  |
|**startRepeat** | **LocalDate** | The month, day, and year that the recurring schedule should go into effect. Specify &lt;strong&gt;YYYY-MM-DD&lt;/strong&gt;. |  [optional] |
|**startTranscoder** | **OffsetDateTime** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;start&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. |  [optional] |
|**stopTranscoder** | **OffsetDateTime** | The month, day, year, and time of day that the &lt;em&gt;action_type&lt;/em&gt; &lt;strong&gt;stop&lt;/strong&gt; should occur. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. |  [optional] |
|**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder being scheduled. |  |



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




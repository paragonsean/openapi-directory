

# GoogleAppsCardV1DateTimePicker

Lets users input a date, a time, or both a date and a time. For an example in Google Chat apps, see [Date time picker](https://developers.google.com/chat/ui/widgets/date-time-picker). Users can input text or use the picker to select dates and times. If users input an invalid date or time, the picker shows an error that prompts users to input the information correctly. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend):

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | The text that prompts users to input a date, a time, or a date and time. For example, if users are scheduling an appointment, use a label such as &#x60;Appointment date&#x60; or &#x60;Appointment date and time&#x60;. |  [optional] |
|**name** | **String** | The name by which the &#x60;DateTimePicker&#x60; is identified in a form input event. For details about working with form inputs, see [Receive form data](https://developers.google.com/chat/ui/read-form-data). |  [optional] |
|**onChangeAction** | [**GoogleAppsCardV1Action**](GoogleAppsCardV1Action.md) |  |  [optional] |
|**timezoneOffsetDate** | **Integer** | The number representing the time zone offset from UTC, in minutes. If set, the &#x60;value_ms_epoch&#x60; is displayed in the specified time zone. If unset, the value defaults to the user&#39;s time zone setting. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Whether the widget supports inputting a date, a time, or the date and time. |  [optional] |
|**valueMsEpoch** | **String** | The default value displayed in the widget, in milliseconds since [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time). Specify the value based on the type of picker (&#x60;DateTimePickerType&#x60;): * &#x60;DATE_AND_TIME&#x60;: a calendar date and time in UTC. For example, to represent January 1, 2023 at 12:00 PM UTC, use &#x60;1672574400000&#x60;. * &#x60;DATE_ONLY&#x60;: a calendar date at 00:00:00 UTC. For example, to represent January 1, 2023, use &#x60;1672531200000&#x60;. * &#x60;TIME_ONLY&#x60;: a time in UTC. For example, to represent 12:00 PM, use &#x60;43200000&#x60; (or &#x60;12 * 60 * 60 * 1000&#x60;). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATE_AND_TIME | &quot;DATE_AND_TIME&quot; |
| DATE_ONLY | &quot;DATE_ONLY&quot; |
| TIME_ONLY | &quot;TIME_ONLY&quot; |




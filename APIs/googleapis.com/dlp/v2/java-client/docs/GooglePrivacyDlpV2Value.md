

# GooglePrivacyDlpV2Value

Set of primitive values supported by the system. Note that for the purposes of inspection or transformation, the number of bytes considered to comprise a 'Value' is based on its representation as a UTF-8 encoded string. For example, if 'integer_value' is set to 123456789, the number of bytes would be counted as 9, even though an int64 only holds up to 8 bytes of data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**booleanValue** | **Boolean** | boolean |  [optional] |
|**dateValue** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**dayOfWeekValue** | [**DayOfWeekValueEnum**](#DayOfWeekValueEnum) | day of week |  [optional] |
|**floatValue** | **Double** | float |  [optional] |
|**integerValue** | **String** | integer |  [optional] |
|**stringValue** | **String** | string |  [optional] |
|**timeValue** | [**GoogleTypeTimeOfDay**](GoogleTypeTimeOfDay.md) |  |  [optional] |
|**timestampValue** | **String** | timestamp |  [optional] |



## Enum: DayOfWeekValueEnum

| Name | Value |
|---- | -----|
| DAY_OF_WEEK_UNSPECIFIED | &quot;DAY_OF_WEEK_UNSPECIFIED&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |






# GooglePrivacyDlpV2Condition

The field type of `value` and `field` do not need to match to be considered equal, but not all comparisons are possible. EQUAL_TO and NOT_EQUAL_TO attempt to compare even with incompatible types, but all other comparisons are invalid with incompatible types. A `value` of type: - `string` can be compared against all other types - `boolean` can only be compared against other booleans - `integer` can be compared against doubles or a string if the string value can be parsed as an integer. - `double` can be compared against integers or a string if the string can be parsed as a double. - `Timestamp` can be compared against strings in RFC 3339 date string format. - `TimeOfDay` can be compared against timestamps and strings in the format of 'HH:mm:ss'. If we fail to compare do to type mismatch, a warning will be given and the condition will evaluate to false.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Required. Operator used to compare the field or infoType to the value. |  [optional] |
|**value** | [**GooglePrivacyDlpV2Value**](GooglePrivacyDlpV2Value.md) |  |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| RELATIONAL_OPERATOR_UNSPECIFIED | &quot;RELATIONAL_OPERATOR_UNSPECIFIED&quot; |
| EQUAL_TO | &quot;EQUAL_TO&quot; |
| NOT_EQUAL_TO | &quot;NOT_EQUAL_TO&quot; |
| GREATER_THAN | &quot;GREATER_THAN&quot; |
| LESS_THAN | &quot;LESS_THAN&quot; |
| GREATER_THAN_OR_EQUALS | &quot;GREATER_THAN_OR_EQUALS&quot; |
| LESS_THAN_OR_EQUALS | &quot;LESS_THAN_OR_EQUALS&quot; |
| EXISTS | &quot;EXISTS&quot; |




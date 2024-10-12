

# ReminderTemplate

Array of reminders

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | One of &#x60;\&quot;email\&quot;&#x60;, &#x60;\&quot;sms\&quot;&#x60; or &#x60;\&quot;auto_call\&quot;&#x60; |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | One of &#x60;\&quot;email\&quot;&#x60;, &#x60;\&quot;sms\&quot;&#x60; or &#x60;\&quot;auto_call\&quot;&#x60; |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| SMS | &quot;sms&quot; |
| PHONE | &quot;phone&quot; |
| AUTO_CALL | &quot;auto_call&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MINUTES | &quot;minutes&quot; |
| HOURS | &quot;hours&quot; |
| DAYS | &quot;days&quot; |
| WEEKS | &quot;weeks&quot; |




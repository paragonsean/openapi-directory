

# ReturnPolicyOnlinePolicy

The available policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**days** | **String** | The number of days items can be returned after delivery, where one day is defined to be 24 hours after the delivery timestamp. Required for &#x60;numberOfDaysAfterDelivery&#x60; returns. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Policy type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| NUMBER_OF_DAYS_AFTER_DELIVERY | &quot;NUMBER_OF_DAYS_AFTER_DELIVERY&quot; |
| NO_RETURNS | &quot;NO_RETURNS&quot; |
| LIFETIME_RETURNS | &quot;LIFETIME_RETURNS&quot; |




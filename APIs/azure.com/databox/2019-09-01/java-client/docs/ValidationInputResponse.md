

# ValidationInputResponse

Minimum properties that should be present in each individual validation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**Error**](Error.md) |  |  [optional] |
|**validationType** | [**ValidationTypeEnum**](#ValidationTypeEnum) | Identifies the type of validation response. |  |



## Enum: ValidationTypeEnum

| Name | Value |
|---- | -----|
| VALIDATE_ADDRESS | &quot;ValidateAddress&quot; |
| VALIDATE_DATA_DESTINATION_DETAILS | &quot;ValidateDataDestinationDetails&quot; |
| VALIDATE_SUBSCRIPTION_IS_ALLOWED_TO_CREATE_JOB | &quot;ValidateSubscriptionIsAllowedToCreateJob&quot; |
| VALIDATE_PREFERENCES | &quot;ValidatePreferences&quot; |
| VALIDATE_CREATE_ORDER_LIMIT | &quot;ValidateCreateOrderLimit&quot; |
| VALIDATE_SKU_AVAILABILITY | &quot;ValidateSkuAvailability&quot; |




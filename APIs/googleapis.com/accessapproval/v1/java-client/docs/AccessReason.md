

# AccessReason


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | More detail about certain reason types. See comments for each type above. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of access justification. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CUSTOMER_INITIATED_SUPPORT | &quot;CUSTOMER_INITIATED_SUPPORT&quot; |
| GOOGLE_INITIATED_SERVICE | &quot;GOOGLE_INITIATED_SERVICE&quot; |
| GOOGLE_INITIATED_REVIEW | &quot;GOOGLE_INITIATED_REVIEW&quot; |
| THIRD_PARTY_DATA_REQUEST | &quot;THIRD_PARTY_DATA_REQUEST&quot; |
| GOOGLE_RESPONSE_TO_PRODUCTION_ALERT | &quot;GOOGLE_RESPONSE_TO_PRODUCTION_ALERT&quot; |
| CLOUD_INITIATED_ACCESS | &quot;CLOUD_INITIATED_ACCESS&quot; |




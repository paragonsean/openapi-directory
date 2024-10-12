

# InAppPurchaseAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inAppPurchaseType** | [**InAppPurchaseTypeEnum**](#InAppPurchaseTypeEnum) |  |  [optional] |
|**productId** | **String** |  |  [optional] |
|**referenceName** | **String** |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |



## Enum: InAppPurchaseTypeEnum

| Name | Value |
|---- | -----|
| AUTOMATICALLY_RENEWABLE_SUBSCRIPTION | &quot;AUTOMATICALLY_RENEWABLE_SUBSCRIPTION&quot; |
| NON_CONSUMABLE | &quot;NON_CONSUMABLE&quot; |
| CONSUMABLE | &quot;CONSUMABLE&quot; |
| NON_RENEWING_SUBSCRIPTION | &quot;NON_RENEWING_SUBSCRIPTION&quot; |
| FREE_SUBSCRIPTION | &quot;FREE_SUBSCRIPTION&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;CREATED&quot; |
| DEVELOPER_SIGNED_OFF | &quot;DEVELOPER_SIGNED_OFF&quot; |
| DEVELOPER_ACTION_NEEDED | &quot;DEVELOPER_ACTION_NEEDED&quot; |
| DELETION_IN_PROGRESS | &quot;DELETION_IN_PROGRESS&quot; |
| APPROVED | &quot;APPROVED&quot; |
| DELETED | &quot;DELETED&quot; |
| REMOVED_FROM_SALE | &quot;REMOVED_FROM_SALE&quot; |
| DEVELOPER_REMOVED_FROM_SALE | &quot;DEVELOPER_REMOVED_FROM_SALE&quot; |
| WAITING_FOR_UPLOAD | &quot;WAITING_FOR_UPLOAD&quot; |
| PROCESSING_CONTENT | &quot;PROCESSING_CONTENT&quot; |
| REPLACED | &quot;REPLACED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| WAITING_FOR_SCREENSHOT | &quot;WAITING_FOR_SCREENSHOT&quot; |
| PREPARE_FOR_SUBMISSION | &quot;PREPARE_FOR_SUBMISSION&quot; |
| MISSING_METADATA | &quot;MISSING_METADATA&quot; |
| READY_TO_SUBMIT | &quot;READY_TO_SUBMIT&quot; |
| WAITING_FOR_REVIEW | &quot;WAITING_FOR_REVIEW&quot; |
| IN_REVIEW | &quot;IN_REVIEW&quot; |
| PENDING_DEVELOPER_RELEASE | &quot;PENDING_DEVELOPER_RELEASE&quot; |




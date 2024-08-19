

# AccountHolderStoreStatusChangeNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | In case the store status has not been updated, contains fields that did not pass the validation. |  [optional] |
|**newStatus** | [**NewStatusEnum**](#NewStatusEnum) | The new status of the account holder. |  |
|**oldStatus** | [**OldStatusEnum**](#OldStatusEnum) | The former status of the account holder. |  |
|**reason** | **String** | The reason for the status change. |  [optional] |
|**store** | **String** | Alphanumeric identifier of the store. |  |
|**storeReference** | **String** | Store store reference. |  |



## Enum: NewStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLOSED | &quot;Closed&quot; |
| INACTIVE | &quot;Inactive&quot; |
| INACTIVE_WITH_MODIFICATIONS | &quot;InactiveWithModifications&quot; |
| PENDING | &quot;Pending&quot; |



## Enum: OldStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLOSED | &quot;Closed&quot; |
| INACTIVE | &quot;Inactive&quot; |
| INACTIVE_WITH_MODIFICATIONS | &quot;InactiveWithModifications&quot; |
| PENDING | &quot;Pending&quot; |




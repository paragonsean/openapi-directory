

# AccountHolderStatusChangeNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | in case the account holder has not been updated, contains account holder fields, that did not pass the validation. |  [optional] |
|**newStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The new status of the account holder. |  [optional] |
|**oldStatus** | [**AccountHolderStatus**](AccountHolderStatus.md) | The former status of the account holder. |  [optional] |
|**reason** | **String** | The reason for the status change. |  [optional] |




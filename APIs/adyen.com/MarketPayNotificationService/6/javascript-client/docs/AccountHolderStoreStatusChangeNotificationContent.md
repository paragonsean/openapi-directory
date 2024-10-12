# ClassicPlatformsNotifications.AccountHolderStoreStatusChangeNotificationContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the account holder. | 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | In case the store status has not been updated, contains fields that did not pass the validation. | [optional] 
**newStatus** | **String** | The new status of the account holder. | 
**oldStatus** | **String** | The former status of the account holder. | 
**reason** | **String** | The reason for the status change. | [optional] 
**store** | **String** | Alphanumeric identifier of the store. | 
**storeReference** | **String** | Store store reference. | 



## Enum: NewStatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `InactiveWithModifications` (value: `"InactiveWithModifications"`)

* `Pending` (value: `"Pending"`)





## Enum: OldStatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `InactiveWithModifications` (value: `"InactiveWithModifications"`)

* `Pending` (value: `"Pending"`)





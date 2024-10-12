# ClassicPlatformsNotifications.CloseAccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The account code of the account that is closed. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 
**status** | **String** | The new status of the account. &gt;Permitted values: &#x60;Active&#x60;, &#x60;Inactive&#x60;, &#x60;Suspended&#x60;, &#x60;Closed&#x60;. | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `Suspended` (value: `"Suspended"`)





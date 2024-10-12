# ClassicPlatformsNotifications.DirectDebitInitiatedNotificationContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | The code of the account. | 
**amount** | [**Amount**](Amount.md) | The amount to be debited from the funding account. | 
**debitInitiationDate** | [**LocalDate**](LocalDate.md) | The date of the debit initiation. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | Invalid fields list. | [optional] 
**merchantAccountCode** | **String** | The code of the merchant account. | 
**splits** | [**[Split]**](Split.md) | The split data for the debit request. | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) | Direct debit status. | [optional] 



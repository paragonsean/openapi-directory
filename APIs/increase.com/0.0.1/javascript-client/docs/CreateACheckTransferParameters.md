# IncreaseApi.CreateACheckTransferParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The identifier for the account that will send the transfer. | 
**addressCity** | **String** | The city of the check&#39;s destination. | 
**addressLine1** | **String** | The street address of the check&#39;s destination. | 
**addressLine2** | **String** | The second line of the address of the check&#39;s destination. | [optional] 
**addressState** | **String** | The state of the check&#39;s destination. | 
**addressZip** | **String** | The postal code of the check&#39;s destination. | 
**amount** | **Number** | The transfer amount in cents. | 
**message** | **String** | The descriptor that will be printed on the memo field on the check. | 
**note** | **String** | The descriptor that will be printed on the letter included with the check. | [optional] 
**recipientName** | **String** | The name that will be printed on the check. | 
**requireApproval** | **Boolean** | Whether the transfer requires explicit approval via the dashboard or API. | [optional] 
**returnAddress** | [**CreateACheckTransferParametersReturnAddress**](CreateACheckTransferParametersReturnAddress.md) |  | [optional] 



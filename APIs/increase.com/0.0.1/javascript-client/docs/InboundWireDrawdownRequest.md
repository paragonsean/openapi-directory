# IncreaseApi.InboundWireDrawdownRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount being requested in cents. | 
**beneficiaryAccountNumber** | **String** | The drawdown request&#39;s beneficiary&#39;s account number. | 
**beneficiaryAddressLine1** | **String** | Line 1 of the drawdown request&#39;s beneficiary&#39;s address. | 
**beneficiaryAddressLine2** | **String** | Line 2 of the drawdown request&#39;s beneficiary&#39;s address. | 
**beneficiaryAddressLine3** | **String** | Line 3 of the drawdown request&#39;s beneficiary&#39;s address. | 
**beneficiaryName** | **String** | The drawdown request&#39;s beneficiary&#39;s name. | 
**beneficiaryRoutingNumber** | **String** | The drawdown request&#39;s beneficiary&#39;s routing number. | 
**currency** | **String** | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the amount being requested. Will always be \&quot;USD\&quot;. | 
**id** | **String** | The Wire drawdown request identifier. | 
**messageToRecipient** | **String** | A message from the drawdown request&#39;s originator. | 
**originatorAccountNumber** | **String** | The drawdown request&#39;s originator&#39;s account number. | 
**originatorAddressLine1** | **String** | Line 1 of the drawdown request&#39;s originator&#39;s address. | 
**originatorAddressLine2** | **String** | Line 2 of the drawdown request&#39;s originator&#39;s address. | 
**originatorAddressLine3** | **String** | Line 3 of the drawdown request&#39;s originator&#39;s address. | 
**originatorName** | **String** | The drawdown request&#39;s originator&#39;s name. | 
**originatorRoutingNumber** | **String** | The drawdown request&#39;s originator&#39;s routing number. | 
**originatorToBeneficiaryInformationLine1** | **String** | Line 1 of the information conveyed from the originator of the message to the beneficiary. | 
**originatorToBeneficiaryInformationLine2** | **String** | Line 2 of the information conveyed from the originator of the message to the beneficiary. | 
**originatorToBeneficiaryInformationLine3** | **String** | Line 3 of the information conveyed from the originator of the message to the beneficiary. | 
**originatorToBeneficiaryInformationLine4** | **String** | Line 4 of the information conveyed from the originator of the message to the beneficiary. | 
**recipientAccountNumberId** | **String** | The Account Number from which the recipient of this request is being requested to send funds. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;inbound_wire_drawdown_request&#x60;. | 



## Enum: TypeEnum


* `inbound_wire_drawdown_request` (value: `"inbound_wire_drawdown_request"`)





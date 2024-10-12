

# CancelOrRefundRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | [**AdjustAuthorisationRequestAdditionalData**](AdjustAuthorisationRequestAdditionalData.md) |  |  [optional] |
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**mpiData** | [**ThreeDSecureData**](ThreeDSecureData.md) | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). |  [optional] |
|**originalMerchantReference** | **String** | The original merchant reference to cancel. |  [optional] |
|**originalReference** | **String** | The original pspReference of the payment to modify. This reference is returned in: * authorisation response * authorisation notification   |  |
|**reference** | **String** | Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters. |  [optional] |
|**tenderReference** | **String** | The transaction reference provided by the PED. For point-of-sale integrations only. |  [optional] |
|**uniqueTerminalId** | **String** | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. |  [optional] |




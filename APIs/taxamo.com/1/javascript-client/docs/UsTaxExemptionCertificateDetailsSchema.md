# Taxamo.UsTaxExemptionCertificateDetailsSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exemptStates** | [**[UsTaxExemptState]**](UsTaxExemptState.md) | List of states where the certificate is valid. | 
**purchaserAddress1** | **String** | Purchaser&#39;s first address line. | 
**purchaserAddress2** | **String** | Purchaser&#39;s second address line. | [optional] 
**purchaserBusinessType** | **String** | Purchaser business type. | 
**purchaserBusinessTypeOtherValue** | **String** | If business type is other, a short description must be provided. | [optional] 
**purchaserCity** | **String** | Purchaser&#39;s city. | 
**purchaserExemptionReason** | **String** | The reason for exemption reason. | 
**purchaserExemptionReasonValue** | **String** | The value of exemption reason. | 
**purchaserFirstName** | **String** | Purchaser&#39;s first name. | 
**purchaserLastName** | **String** | Purchaser&#39;s last name. | 
**purchaserState** | **String** | Purchaser&#39;s state. | 
**purchaserTaxId** | [**UsTaxId**](UsTaxId.md) |  | 
**purchaserTitle** | **String** | Purchaser&#39;s title. | [optional] 
**purchaserZip** | **String** | Purchaser&#39;s zip code. | 
**singlePurchase** | **Boolean** | Set to true if this certificate is valid for single purchase only. | [optional] 
**singlePurchaseOrderIdentifier** | **String** | Purchase/order identifier for single purchase. | [optional] 



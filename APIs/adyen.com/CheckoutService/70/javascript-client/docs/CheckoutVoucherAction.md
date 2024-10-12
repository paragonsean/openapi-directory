# AdyenCheckoutApi.CheckoutVoucherAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternativeReference** | **String** | The voucher alternative reference code. | [optional] 
**collectionInstitutionNumber** | **String** | A collection institution number (store number) for Econtext Pay-Easy ATM. | [optional] 
**downloadUrl** | **String** | The URL to download the voucher. | [optional] 
**entity** | **String** | An entity number of Multibanco. | [optional] 
**expiresAt** | **String** | The date time of the voucher expiry. | [optional] 
**initialAmount** | [**Amount**](Amount.md) | The initial amount. | [optional] 
**instructionsUrl** | **String** | The URL to the detailed instructions to make payment using the voucher. | [optional] 
**issuer** | **String** | The issuer of the voucher. | [optional] 
**maskedTelephoneNumber** | **String** | The shopper telephone number (partially masked). | [optional] 
**merchantName** | **String** | The merchant name. | [optional] 
**merchantReference** | **String** | The merchant reference. | [optional] 
**passCreationToken** | **String** | A base64 encoded signature of all properties | [optional] 
**paymentData** | **String** | Encoded payment data. | [optional] 
**paymentMethodType** | **String** | Specifies the payment method. | [optional] 
**reference** | **String** | The voucher reference code. | [optional] 
**shopperEmail** | **String** | The shopper email. | [optional] 
**shopperName** | **String** | The shopper name. | [optional] 
**surcharge** | [**Amount**](Amount.md) | The surcharge amount. | [optional] 
**totalAmount** | [**Amount**](Amount.md) | The total amount (initial plus surcharge amount). | [optional] 
**type** | **String** | **voucher** | 
**url** | **String** | Specifies the URL to redirect to. | [optional] 



## Enum: TypeEnum


* `voucher` (value: `"voucher"`)





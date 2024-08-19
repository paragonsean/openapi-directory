# IncreaseApi.CardDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardId** | **String** | The identifier for the Card for which sensitive details have been returned. | 
**expirationMonth** | **Number** | The month the card expires in M format (e.g., August is 8). | 
**expirationYear** | **Number** | The year the card expires in YYYY format (e.g., 2025). | 
**primaryAccountNumber** | **String** | The card number. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_details&#x60;. | 
**verificationCode** | **String** | The three-digit verification code for the card. It&#39;s also known as the Card Verification Code (CVC), the Card Verification Value (CVV), or the Card Identification (CID). | 



## Enum: TypeEnum


* `card_details` (value: `"card_details"`)





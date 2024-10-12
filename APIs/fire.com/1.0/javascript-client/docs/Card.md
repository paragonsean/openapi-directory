# FireFinancialServicesBusinessApi.Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **Boolean** | Whether the card is blocked or not | [optional] 
**cardId** | **Number** | card id assigned by fire.com | [optional] 
**dateCreated** | **Date** | The date-time the card was created | [optional] 
**emailAddress** | **String** | card user email address | [optional] 
**eurIcan** | **Number** | identifier for the eur fire.com account (assigned by fire.com) | [optional] 
**expiryDate** | **Date** | card expiry date | [optional] 
**firstName** | **String** | card user first name | [optional] 
**gbpIcan** | **Number** | identifier for the gbp fire.com account (assigned by fire.com) | [optional] 
**lastName** | **String** | card user last name | [optional] 
**maskedPan** | **String** | card number (masked) | [optional] 
**provider** | **String** | card provider | [optional] 
**status** | **String** | card status | [optional] 
**statusReason** | **String** | reason for card status | [optional] 
**userId** | **Number** | card user id assigned by fire.com | [optional] 



## Enum: ProviderEnum


* `MASTERCARD` (value: `"MASTERCARD"`)





## Enum: StatusEnum


* `LIVE` (value: `"LIVE"`)

* `CREATED_ACTIVE` (value: `"CREATED_ACTIVE"`)

* `CREATED_INACTIVE` (value: `"CREATED_INACTIVE"`)

* `DEACTIVATED` (value: `"DEACTIVATED"`)





## Enum: StatusReasonEnum


* `LOST_CARD` (value: `"LOST_CARD"`)

* `STOLEN_CARD` (value: `"STOLEN_CARD"`)

* `CARD_DESTROYED` (value: `"CARD_DESTROYED"`)





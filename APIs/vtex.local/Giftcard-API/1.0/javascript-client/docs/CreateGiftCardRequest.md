# GiftCardApi.CreateGiftCardRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **String** | The caption of the Giftcard. | 
**expiringDate** | **String** | It must be in the format &#x60;YYYY-MM-DDThh:mm:ss.fff&#x60;. | 
**multipleCredits** | **Boolean** | The Giftcard balance can be changed. | [optional] 
**multipleRedemptions** | **Boolean** | The Giftcard can be used to make new purchases until its value is completely used. | [optional] 
**profileId** | **String** | The client&#39;s ID. | 
**relationName** | **String** | Represents the relationship between the client and the store. | 
**restrictedToOwner** | **Boolean** | The Giftcard can only be used for a specified client&#39;s ID. | [optional] 



# ConfigurationWebhooks.Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**Authentication**](Authentication.md) | Contains the card user&#39;s password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to [3D Secure and digital wallets](https://docs.adyen.com/issuing/3d-secure-and-wallets) for more information. | [optional] 
**bin** | **String** | The bank identification number (BIN) of the card number. | [optional] 
**brand** | **String** | The brand of the physical or the virtual card. Possible values: **visa**, **mc**. | 
**brandVariant** | **String** | The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**. &gt;Reach out to your Adyen contact to get the values relevant for your integration. | 
**cardholderName** | **String** | The name of the cardholder.  Maximum length: 26 characters. | 
**configuration** | [**CardConfiguration**](CardConfiguration.md) | Settings required when creating a physical or a virtual card.   Reach out to your Adyen contact to get the values that you can send in this object. | [optional] 
**cvc** | **String** | The CVC2 value of the card. &gt; The CVC2 is not sent by default. This is only returned in the &#x60;POST&#x60; response for single-use virtual cards. | [optional] 
**deliveryContact** | [**Contact**](Contact.md) | The delivery contact (name and address) for physical card delivery. | [optional] 
**expiration** | [**Expiry**](Expiry.md) | The expiration date of the card. | [optional] 
**formFactor** | **String** | The form factor of the card. Possible values: **virtual**, **physical**. | 
**lastFour** | **String** | Last last four digits of the card number. | [optional] 
**number** | **String** | The primary account number (PAN) of the card. &gt; The PAN is masked by default and returned only for single-use virtual cards. | 
**threeDSecure** | **String** | Allocates a specific product range for either a physical or a virtual card. Possible values: **fullySupported**, **secureCorporate**. &gt;Reach out to your Adyen contact to get the values relevant for your integration. | [optional] 



## Enum: FormFactorEnum


* `physical` (value: `"physical"`)

* `unknown` (value: `"unknown"`)

* `virtual` (value: `"virtual"`)







# CreditCard

An object representing the credit card information you have on file with Linode to make Payments against your Account. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardNumber** | **String** | Your credit card number. No spaces or dashes allowed. |  |
|**cvv** | **String** | CVV (Card Verification Value) of the credit card, typically found on the back of the card.  |  |
|**expiryMonth** | **Integer** | A value from 1-12 representing the expiration month of your credit card.    * 1 &#x3D; January   * 2 &#x3D; February   * 3 &#x3D; March   * Etc.  |  |
|**expiryYear** | **Integer** | A four-digit integer representing the expiration year of your credit card.  The combination of &#x60;expiry_month&#x60; and &#x60;expiry_year&#x60; must result in a month/year combination of the current month or in the future. An expiration date set in the past is invalid.  |  |




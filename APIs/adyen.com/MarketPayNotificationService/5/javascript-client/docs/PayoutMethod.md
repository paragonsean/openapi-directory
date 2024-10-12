# ClassicPlatformsNotifications.PayoutMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchantAccount** | **String** | The [&#x60;merchantAccount&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_merchantAccount) you used in the &#x60;/payments&#x60; request when you [saved the account holder&#39;s card details](https://docs.adyen.com/marketplaces-and-platforms/classic/payouts/manual-payout/payout-to-cards#check-and-store). | 
**payoutMethodCode** | **String** | Adyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you create a payout method. Required when updating an existing payout method in an &#x60;/updateAccountHolder&#x60; request. | [optional] 
**payoutMethodReference** | **String** | Your reference for the payout method. | [optional] 
**recurringDetailReference** | **String** | The [&#x60;recurringDetailReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-recurring-recurringDetailReference)  returned in the &#x60;/payments&#x60; response when you [saved the account holder&#39;s card details](https://docs.adyen.com/marketplaces-and-platforms/classic/payouts/manual-payout/payout-to-cards#check-and-store). | 
**shopperReference** | **String** | The [&#x60;shopperReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_shopperReference) you sent in the &#x60;/payments&#x60; request when you [saved the account holder&#39;s card details](https://docs.adyen.com/marketplaces-and-platforms/classic/payouts/manual-payout/payout-to-cards#check-and-store). | 



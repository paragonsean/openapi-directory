# AdyenCheckoutApi.DonationPaymentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) | Authorised amount in the transaction. | [optional] 
**donationAccount** | **String** | The Adyen account name of your charity. We will provide you with this account name once your chosen charity has been [onboarded](https://docs.adyen.com/online-payments/donations#onboarding). | [optional] 
**id** | **String** | Your unique resource identifier. | [optional] 
**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. | [optional] 
**payment** | [**PaymentResponse**](PaymentResponse.md) | Action to be taken for completing the payment. | [optional] 
**reference** | **String** | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens (\&quot;-\&quot;). Maximum length: 80 characters. | [optional] 
**status** | **String** | The status of the donation transaction.  Possible values: * **completed** * **pending** * **refused** | [optional] 



## Enum: StatusEnum


* `completed` (value: `"completed"`)

* `pending` (value: `"pending"`)

* `refused` (value: `"refused"`)





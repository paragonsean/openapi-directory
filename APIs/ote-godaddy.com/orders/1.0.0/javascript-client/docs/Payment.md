# OpenapiJsClient.Payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Amount paid by the current payment | 
**category** | **String** | The category of payment method used at the time of purchase. Most common values are listed in the enum. | 
**paymentProfileId** | **String** | Unique identifier of the payment profile used by current payment | 
**subcategory** | **String** | The subcategory of payment method used at the time of purchase.  This field is only set for certain payment categories, such as ACH and CREDIT_CARD. Most common values are listed in the enum. | [optional] 



## Enum: CategoryEnum


* `CREDIT_CARD` (value: `"CREDIT_CARD"`)

* `PAYPAL` (value: `"PAYPAL"`)

* `ACH` (value: `"ACH"`)

* `GIFT_CARD` (value: `"GIFT_CARD"`)

* `IN_STORE_CREDIT` (value: `"IN_STORE_CREDIT"`)

* `PREPAID` (value: `"PREPAID"`)





## Enum: SubcategoryEnum


* `CHECKING_PERSONAL` (value: `"CHECKING_PERSONAL"`)

* `CHECKING_BUSINESS` (value: `"CHECKING_BUSINESS"`)

* `VISA` (value: `"VISA"`)

* `MASTER_CARD` (value: `"MASTER_CARD"`)

* `AMEX` (value: `"AMEX"`)

* `JCB` (value: `"JCB"`)

* `UNIONPAY` (value: `"UNIONPAY"`)





# AdyenCheckoutApi.CheckoutSessionInstallmentOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | **[String]** | Defines the type of installment plan. If not set, defaults to **regular**.  Possible values: * **regular** * **revolving** | [optional] 
**preselectedValue** | **Number** | Preselected number of installments offered for this payment method. | [optional] 
**values** | **[Number]** | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with &#x60;maxValue&#x60;. | [optional] 



## Enum: [PlansEnum]


* `regular` (value: `"regular"`)

* `revolving` (value: `"revolving"`)





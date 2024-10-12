

# CheckoutSessionInstallmentOption


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**plans** | [**List&lt;PlansEnum&gt;**](#List&lt;PlansEnum&gt;) | Defines the type of installment plan. If not set, defaults to **regular**.  Possible values: * **regular** * **revolving** |  [optional] |
|**preselectedValue** | **Integer** | Preselected number of installments offered for this payment method. |  [optional] |
|**values** | **List&lt;Integer&gt;** | An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with &#x60;maxValue&#x60;. |  [optional] |



## Enum: List&lt;PlansEnum&gt;

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| REVOLVING | &quot;revolving&quot; |




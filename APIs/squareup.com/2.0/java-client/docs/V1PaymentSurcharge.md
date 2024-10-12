

# V1PaymentSurcharge

V1PaymentSurcharge

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**appliedMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**name** | **String** | The name of the surcharge. |  [optional] |
|**rate** | **String** | The amount of the surcharge as a percentage. The percentage is provided as a string representing the decimal equivalent of the percentage. For example, \&quot;0.7\&quot; corresponds to a 7% surcharge. Exactly one of rate or amount_money should be set. |  [optional] |
|**surchargeId** | **String** | A Square-issued unique identifier associated with the surcharge. |  [optional] |
|**taxable** | **Boolean** | Indicates whether the surcharge is taxable. |  [optional] |
|**taxes** | [**List&lt;V1PaymentTax&gt;**](V1PaymentTax.md) | The list of taxes that should be applied to the surcharge. |  [optional] |
|**type** | **String** | Indicates the source of the surcharge. For example, if it was applied as an automatic gratuity for a large group. |  [optional] |




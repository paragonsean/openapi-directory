

# V1PaymentTax

V1PaymentTax

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**feeId** | **String** | The ID of the tax, if available. Taxes applied in older versions of Square Register might not have an ID. |  [optional] |
|**inclusionType** | **String** | Whether the tax is an ADDITIVE tax or an INCLUSIVE tax. |  [optional] |
|**name** | **String** | The merchant-defined name of the tax. |  [optional] |
|**rate** | **String** | The rate of the tax, as a string representation of a decimal number. A value of 0.07 corresponds to a rate of 7%. |  [optional] |




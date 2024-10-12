

# ModelConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Payment method, like **eftpos_australia** or **mc**. See the [possible values](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).  |  |
|**country** | **List&lt;String&gt;** | Countries, to filter different surcharge amounts for domestic or international cards. |  [optional] |
|**currencies** | [**List&lt;Currency&gt;**](Currency.md) | Currency, and surcharge percentage or amount. |  |
|**sources** | **List&lt;String&gt;** | Funding source. Possible values: * **Credit** * **Debit** |  [optional] |




# ManagementApi.Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **String** | Payment method, like **eftpos_australia** or **mc**. See the [possible values](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api).  | 
**country** | **[String]** | Countries, to filter different surcharge amounts for domestic or international cards. | [optional] 
**currencies** | [**[Currency]**](Currency.md) | Currency, and surcharge percentage or amount. | 
**sources** | **[String]** | Funding source. Possible values: * **Credit** * **Debit** | [optional] 



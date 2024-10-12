# ConfigurationWebhooks.BalanceAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderId** | **String** | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/accountHolders__resParam_id) associated with the balance account. | 
**balances** | [**[Balance]**](Balance.md) | List of balances with the amount and currency. | [optional] 
**defaultCurrencyCode** | **String** | The default three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the balance account. The default value is **EUR**. &gt; After a balance account is created, you cannot change its default currency. | [optional] 
**description** | **String** | A human-readable description of the balance account, maximum 300 characters. You can use this parameter to distinguish between multiple balance accounts under an account holder. | [optional] 
**id** | **String** | The unique identifier of the balance account. | 
**metadata** | **{String: String}** | A set of key and value pairs for general use. The keys do not have specific names and may be used for storing miscellaneous data as desired. &gt; Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. | [optional] 
**migratedAccountCode** | **String** | The unique identifier of the account of the migrated account holder in the classic integration. | [optional] 
**paymentInstruments** | [**[PaymentInstrumentReference]**](PaymentInstrumentReference.md) | List of [payment instruments](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/post/paymentInstruments) associated with the balance account. | [optional] 
**platformPaymentConfiguration** | [**PlatformPaymentConfiguration**](PlatformPaymentConfiguration.md) | Contains key-value pairs to the configure the settlement model in a balance account. | [optional] 
**reference** | **String** | Your reference for the balance account, maximum 150 characters. | [optional] 
**status** | **String** | The status of the balance account, set to **Active** by default.   | [optional] 
**timeZone** | **String** | The time zone of the balance account. For example, **Europe/Amsterdam**. Defaults to the time zone of the account holder if no time zone is set. For possible values, see the [list of time zone codes](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Closed` (value: `"Closed"`)

* `Inactive` (value: `"Inactive"`)

* `Suspended` (value: `"Suspended"`)





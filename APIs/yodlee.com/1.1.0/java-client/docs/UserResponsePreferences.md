

# UserResponsePreferences


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The currency of the user. This currency will be respected while providing the response for derived API services.&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] |
|**dateFormat** | **String** | The dateformat of the user.This attribute is just a place holder and has no impact on any other API services. |  [optional] |
|**locale** | [**LocaleEnum**](#LocaleEnum) | The locale of the user. This locale will be considered for localization features like providing the provider information in the supported locale or providing category names in the transaction related services.&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] |
|**timeZone** | **String** | The timezone of the user. This attribute is just a place holder and has no impact on any other API services. |  [optional] |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| AUD | &quot;AUD&quot; |
| BRL | &quot;BRL&quot; |
| CAD | &quot;CAD&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| HKD | &quot;HKD&quot; |
| IDR | &quot;IDR&quot; |
| INR | &quot;INR&quot; |
| JPY | &quot;JPY&quot; |
| NZD | &quot;NZD&quot; |
| SGD | &quot;SGD&quot; |
| USD | &quot;USD&quot; |
| ZAR | &quot;ZAR&quot; |
| CNY | &quot;CNY&quot; |
| VND | &quot;VND&quot; |
| MYR | &quot;MYR&quot; |
| CHF | &quot;CHF&quot; |



## Enum: LocaleEnum

| Name | Value |
|---- | -----|
| EN_US | &quot;en_US&quot; |
| EN_ES | &quot;en_ES&quot; |
| FR_CA | &quot;fr_CA&quot; |
| ZH_CN | &quot;zh_CN&quot; |




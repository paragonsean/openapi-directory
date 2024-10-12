

# PaymentAmountUpdateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The updated amount. The &#x60;currency&#x60; must match the currency used in authorisation. |  |
|**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |  [optional] |
|**merchantAccount** | **String** | The merchant account that is used to process the payment. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason for the amount update. Possible values:  * **delayedCharge**  * **noShow** |  [optional] |
|**reference** | **String** | Your reference for the amount update request. Maximum length: 80 characters. |  [optional] |
|**splits** | [**List&lt;Split&gt;**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| DELAYED_CHARGE | &quot;delayedCharge&quot; |
| NO_SHOW | &quot;noShow&quot; |




# ConfigurationWebhooks.SweepConfigurationV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty** | [**SweepCounterparty**](SweepCounterparty.md) | The destination or the source of the funds, depending on the sweep &#x60;type&#x60;.  Either a &#x60;balanceAccountId&#x60;, &#x60;transferInstrumentId&#x60;, or &#x60;merchantAccount&#x60; is required. | 
**currency** | **String** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) in uppercase. For example, **EUR**.  The sweep currency must match any of the [balances currencies](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__resParam_balances). | 
**description** | **String** | The message that will be used in the sweep transfer&#39;s description body with a maximum length of 140 characters.  If the message is longer after replacing placeholders, the message will be cut off at 140 characters. | [optional] 
**id** | **String** | The unique identifier of the sweep. | 
**reason** | **String** | The reason for disabling the sweep. | [optional] 
**schedule** | [**SweepSchedule**](SweepSchedule.md) | The schedule when the &#x60;triggerAmount&#x60; is evaluated. If the balance meets the threshold, funds are pushed out of or pulled in to the balance account. | 
**status** | **String** | The status of the sweep. If not provided, by default, this is set to **active**.  Possible values:    * **active**:  the sweep is enabled and funds will be pulled in or pushed out based on the defined configuration.    * **inactive**: the sweep is disabled and cannot be triggered.    | [optional] 
**sweepAmount** | [**Amount**](Amount.md) | The amount that must be pushed out or pulled in. You can configure either &#x60;sweepAmount&#x60; or &#x60;targetAmount&#x60;, not both. | [optional] 
**targetAmount** | [**Amount**](Amount.md) | The amount that must be available in the balance account after the sweep. You can configure either &#x60;sweepAmount&#x60; or &#x60;targetAmount&#x60;, not both. | [optional] 
**triggerAmount** | [**Amount**](Amount.md) | The threshold amount that triggers the sweep. If not provided, by default, the amount is set to zero. The &#x60;triggerAmount&#x60; is evaluated according to the specified &#x60;schedule.type&#x60;.  * For &#x60;type&#x60; **pull**, if the balance is less than or equal to the &#x60;triggerAmount&#x60;, funds are pulled in to the balance account.  * For &#x60;type&#x60; **push**, if the balance is more than or equal to the &#x60;triggerAmount&#x60;, funds are pushed out of the balance account. | [optional] 
**type** | **String** | The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set to **push**.  Possible values:   * **push**: _push out funds_ to a destination balance account or transfer instrument.   * **pull**: _pull in funds_ from a source merchant account, transfer instrument, or balance account. | [optional] [default to &#39;push&#39;]



## Enum: ReasonEnum


* `amountLimitExceeded` (value: `"amountLimitExceeded"`)

* `approved` (value: `"approved"`)

* `balanceAccountTemporarilyBlockedByTransactionRule` (value: `"balanceAccountTemporarilyBlockedByTransactionRule"`)

* `counterpartyAccountBlocked` (value: `"counterpartyAccountBlocked"`)

* `counterpartyAccountClosed` (value: `"counterpartyAccountClosed"`)

* `counterpartyAccountNotFound` (value: `"counterpartyAccountNotFound"`)

* `counterpartyAddressRequired` (value: `"counterpartyAddressRequired"`)

* `counterpartyBankTimedOut` (value: `"counterpartyBankTimedOut"`)

* `counterpartyBankUnavailable` (value: `"counterpartyBankUnavailable"`)

* `declinedByTransactionRule` (value: `"declinedByTransactionRule"`)

* `error` (value: `"error"`)

* `notEnoughBalance` (value: `"notEnoughBalance"`)

* `refusedByCounterpartyBank` (value: `"refusedByCounterpartyBank"`)

* `routeNotFound` (value: `"routeNotFound"`)

* `scaFailed` (value: `"scaFailed"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)





## Enum: TypeEnum


* `pull` (value: `"pull"`)

* `push` (value: `"push"`)





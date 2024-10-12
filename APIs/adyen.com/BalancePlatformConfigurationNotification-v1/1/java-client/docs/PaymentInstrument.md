

# PaymentInstrument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balanceAccountId** | **String** | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument. |  |
|**bankAccount** | [**PaymentInstrumentBankAccount**](PaymentInstrumentBankAccount.md) |  |  [optional] |
|**card** | [**Card**](Card.md) | Contains information about the card payment instrument. Returned when you create a payment instrument with &#x60;type&#x60; **card**. |  [optional] |
|**description** | **String** | Your description for the payment instrument, maximum 300 characters. |  [optional] |
|**id** | **String** | The unique identifier of the payment instrument. |  |
|**issuingCountryCode** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |  |
|**paymentInstrumentGroupId** | **String** | The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs. |  [optional] |
|**reference** | **String** | Your reference for the payment instrument, maximum 150 characters. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **Active** by default. However, there can be exceptions for cards based on the &#x60;card.formFactor&#x60; and the &#x60;issuingCountryCode&#x60;. For example, when issuing physical cards in the US, the default status is **Requested**.  Possible values:    * **Active**:  The payment instrument is active and can be used to make payments.    * **Requested**: The payment instrument has been requested. This state is applicable for physical cards.   * **Inactive**: The payment instrument is inactive and cannot be used to make payments.    * **Suspended**: The payment instrument is temporarily suspended and cannot be used to make payments.    * **Closed**: The payment instrument is permanently closed. This action cannot be undone.   * **Stolen**    * **Lost**    |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of payment instrument.  Possible value: **card**, **bankAccount**.  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLOSED | &quot;Closed&quot; |
| INACTIVE | &quot;Inactive&quot; |
| LOST | &quot;Lost&quot; |
| REQUESTED | &quot;Requested&quot; |
| STOLEN | &quot;Stolen&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| BLOCKED | &quot;blocked&quot; |
| DISCARDED | &quot;discarded&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT | &quot;bankAccount&quot; |
| CARD | &quot;card&quot; |




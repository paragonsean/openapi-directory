

# ContractCommitmentInfo

Describe the commitment information related to the offer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commercialCreatorUserId** | **String** | The commercial that is responsible of the creation of your account |  [optional] |
|**commercialUserId** | **String** | Your current commercial user id |  [optional] |
|**commitmentCalculatedFinishDate** | **LocalDate** | The commitment end date related to the offer |  [optional] |
|**commitmentPeriodInMonth** | **Integer** | The commitment period in month related to the offer |  [optional] |
|**contractType** | **Integer** | Internal usage: Old offer type. Your contract type |  [optional] |
|**couponOfferCode** | **String** | Your special coupon offer identifier |  [optional] |
|**currentContractId** | **String** | Your current contract id |  [optional] |
|**currentContractTerminationDate** | **LocalDate** | The current contract termination date |  [optional] |
|**currentCustomerPaymentMethod** | **PaymentMethod** |  |  [optional] |
|**fixedAndVariableClickInfo** | [**FixedAndVariableClickModelInfo**](FixedAndVariableClickModelInfo.md) |  |  [optional] |
|**isCustomerWantsToTerminateHisContract** | **Boolean** | If true, this means you want to leave us and that&#39;s sad... :&#39;-( |  [optional] |
|**isModelMustBeTransmittedInNewContract** | **Boolean** | Internal usage: Old offer type. Is the current contract model needs to be converted into a new contract type |  [optional] |
|**minBillingPeriodInMonths** | **Integer** | The minimum billing period in month authorized for this offer. |  [optional] |
|**model** | **String** | Interal usage: Old offer type. The model description |  [optional] |
|**newContractStartDate** | **OffsetDateTime** | The start date related to the offer |  [optional] |
|**offerId** | **Integer** | The offer id based on /offers. Not a free offer of course. |  [optional] |
|**offerName** | **String** | The offer Name |  [optional] |
|**paymentDelayInDays** | **Integer** | The payment delay in days related to the offer |  [optional] |
|**paymentMethodAuthorized** | **PaymentMethod** |  |  [optional] |
|**requestedPaymentMethod** | **PaymentMethod** |  |  [optional] |
|**trialPeriodFinishDate** | **LocalDate** | The trial period end date related to the offer |  [optional] |
|**trialPeriodInMonth** | **Integer** | The trial period in month related to the offer |  [optional] |
|**variableModelInfo** | [**VariableModelInfo**](VariableModelInfo.md) |  |  [optional] |




# ManagementApi.SplitConfigurationLogic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquiringFees** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with adyenFees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**additionalCommission** | [**AdditionalCommission**](AdditionalCommission.md) | Contains the logic used to calculate your user&#39;s commission, booked directly to their balance account. | [optional] 
**adyenCommission** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, interchange &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**adyenFees** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with acquiringFees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**adyenMarkup** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission &amp; interchange.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**chargeback** | **String** | Specifies the logic to apply when booking the chargeback amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. | [optional] 
**chargebackCostAllocation** | **String** | Specifies the logic to apply when allocating the chargeback costs.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** | [optional] 
**commission** | [**Commission**](Commission.md) | Contains the logic used to the calculate your platform&#39;s commission, booked to your liable balance account. | 
**interchange** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**paymentFee** | **String** | Specifies the logic to apply when booking the transaction fees. Cannot be combined with other fees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**remainder** | **String** | Specifies the logic to apply when booking the amount left over after currency conversion.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. | [optional] 
**schemeFee** | **String** | Specifies the logic to apply when booking the transaction fees. Should be combined with interchange, adyenCommission &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. | [optional] 
**splitLogicId** | **String** | Unique identifier of the split logic that is applied when the split configuration conditions are met. | [optional] [readonly] 
**surcharge** | **String** | Specifies the logic to apply when booking the surcharge amount.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount** | [optional] 
**tip** | **String** | Specifies the logic to apply when booking tips (gratuity).  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. | [optional] 



## Enum: AcquiringFeesEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: AdyenCommissionEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: AdyenFeesEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: AdyenMarkupEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: ChargebackEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)

* `deductAccordingToSplitRatio` (value: `"deductAccordingToSplitRatio"`)





## Enum: ChargebackCostAllocationEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: InterchangeEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: PaymentFeeEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: RemainderEnum


* `addToLiableAccount` (value: `"addToLiableAccount"`)

* `addToOneBalanceAccount` (value: `"addToOneBalanceAccount"`)





## Enum: SchemeFeeEnum


* `deductFromLiableAccount` (value: `"deductFromLiableAccount"`)

* `deductFromOneBalanceAccount` (value: `"deductFromOneBalanceAccount"`)





## Enum: SurchargeEnum


* `addToLiableAccount` (value: `"addToLiableAccount"`)

* `addToOneBalanceAccount` (value: `"addToOneBalanceAccount"`)





## Enum: TipEnum


* `addToLiableAccount` (value: `"addToLiableAccount"`)

* `addToOneBalanceAccount` (value: `"addToOneBalanceAccount"`)





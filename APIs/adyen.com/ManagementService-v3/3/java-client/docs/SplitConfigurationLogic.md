

# SplitConfigurationLogic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acquiringFees** | [**AcquiringFeesEnum**](#AcquiringFeesEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with adyenFees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**additionalCommission** | [**AdditionalCommission**](AdditionalCommission.md) | Contains the logic used to calculate your user&#39;s commission, booked directly to their balance account. |  [optional] |
|**adyenCommission** | [**AdyenCommissionEnum**](#AdyenCommissionEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, interchange &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**adyenFees** | [**AdyenFeesEnum**](#AdyenFeesEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with acquiringFees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**adyenMarkup** | [**AdyenMarkupEnum**](#AdyenMarkupEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission &amp; interchange.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**chargeback** | [**ChargebackEnum**](#ChargebackEnum) | Specifies the logic to apply when booking the chargeback amount.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |  [optional] |
|**chargebackCostAllocation** | [**ChargebackCostAllocationEnum**](#ChargebackCostAllocationEnum) | Specifies the logic to apply when allocating the chargeback costs.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount** |  [optional] |
|**commission** | [**Commission**](Commission.md) | Contains the logic used to the calculate your platform&#39;s commission, booked to your liable balance account. |  |
|**interchange** | [**InterchangeEnum**](#InterchangeEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with schemeFee, adyenCommission &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**paymentFee** | [**PaymentFeeEnum**](#PaymentFeeEnum) | Specifies the logic to apply when booking the transaction fees. Cannot be combined with other fees.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**remainder** | [**RemainderEnum**](#RemainderEnum) | Specifies the logic to apply when booking the amount left over after currency conversion.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |  [optional] |
|**schemeFee** | [**SchemeFeeEnum**](#SchemeFeeEnum) | Specifies the logic to apply when booking the transaction fees. Should be combined with interchange, adyenCommission &amp; adyenMarkup.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**. |  [optional] |
|**splitLogicId** | **String** | Unique identifier of the split logic that is applied when the split configuration conditions are met. |  [optional] [readonly] |
|**surcharge** | [**SurchargeEnum**](#SurchargeEnum) | Specifies the logic to apply when booking the surcharge amount.  Possible values: **addToLiableAccount**, **addToOneBalanceAccount** |  [optional] |
|**tip** | [**TipEnum**](#TipEnum) | Specifies the logic to apply when booking tips (gratuity).  Possible values: **addToLiableAccount**, **addToOneBalanceAccount**. |  [optional] |



## Enum: AcquiringFeesEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: AdyenCommissionEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: AdyenFeesEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: AdyenMarkupEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: ChargebackEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |
| DEDUCT_ACCORDING_TO_SPLIT_RATIO | &quot;deductAccordingToSplitRatio&quot; |



## Enum: ChargebackCostAllocationEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: InterchangeEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: PaymentFeeEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: RemainderEnum

| Name | Value |
|---- | -----|
| ADD_TO_LIABLE_ACCOUNT | &quot;addToLiableAccount&quot; |
| ADD_TO_ONE_BALANCE_ACCOUNT | &quot;addToOneBalanceAccount&quot; |



## Enum: SchemeFeeEnum

| Name | Value |
|---- | -----|
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



## Enum: SurchargeEnum

| Name | Value |
|---- | -----|
| ADD_TO_LIABLE_ACCOUNT | &quot;addToLiableAccount&quot; |
| ADD_TO_ONE_BALANCE_ACCOUNT | &quot;addToOneBalanceAccount&quot; |



## Enum: TipEnum

| Name | Value |
|---- | -----|
| ADD_TO_LIABLE_ACCOUNT | &quot;addToLiableAccount&quot; |
| ADD_TO_ONE_BALANCE_ACCOUNT | &quot;addToOneBalanceAccount&quot; |



